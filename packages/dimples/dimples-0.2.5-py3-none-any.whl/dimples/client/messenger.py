# -*- coding: utf-8 -*-
# ==============================================================================
# MIT License
#
# Copyright (c) 2019 Albert Moky
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==============================================================================

"""
    Messenger for client
    ~~~~~~~~~~~~~~~~~~~~

    Transform and send message
"""

from typing import Optional, List, Dict

from dimples import EntityType, ID, EVERYONE
from dimples import Station
from dimples import Envelope, InstantMessage, ReliableMessage
from dimples import ContentType, MetaCommand, DocumentCommand, ReceiptCommand

from ..utils import QueryFrequencyChecker
from ..common import HandshakeCommand, ReportCommand, LoginCommand
from ..common import CommonMessenger

from .network import ClientSession

from .group import GroupManager


class ClientMessenger(CommonMessenger):

    @property
    def session(self) -> ClientSession:
        sess = super().session
        assert isinstance(sess, ClientSession), 'session error: %s' % sess
        return sess

    def handshake(self, session_key: Optional[str]):
        """ send handshake command to current station """
        session = self.session
        station = session.station
        srv_id = station.identifier
        if session_key is None:
            # first handshake
            facebook = self.facebook
            user = facebook.current_user
            assert user is not None, 'current user not found'
            env = Envelope.create(sender=user.identifier, receiver=srv_id)
            cmd = HandshakeCommand.start()
            # send first handshake command as broadcast message
            cmd.group = Station.EVERY
            # create instant message with meta & visa
            i_msg = InstantMessage.create(head=env, body=cmd)
            i_msg['meta'] = user.meta.dictionary
            i_msg['visa'] = user.visa.dictionary
            self.send_instant_message(msg=i_msg, priority=-1)
        else:
            # handshake again
            cmd = HandshakeCommand.restart(session=session_key)
            self.send_content(sender=None, receiver=srv_id, content=cmd, priority=-1)

    # Override
    def handshake_success(self):
        # broadcast current documents after handshake success
        self.broadcast_document()

    # Override
    def suspend_reliable_message(self, msg: ReliableMessage, error: Dict):
        self.warning(msg='suspend message: %s -> %s, %s' % (msg.sender, msg.receiver, error))
        msg['error'] = error

    # Override
    def suspend_instant_message(self, msg: InstantMessage, error: Dict):
        self.warning(msg='suspend message: %s -> %s, %s' % (msg.sender, msg.receiver, error))
        msg['error'] = error

    def broadcast_login(self, sender: ID, user_agent: str):
        """ send login command to keep roaming """
        # get current station
        station = self.session.station
        assert sender.type != EntityType.STATION, 'station (%s) cannot login: %s' % (sender, station)
        # create login command
        command = LoginCommand(identifier=sender)
        command.agent = user_agent
        command.station = station
        # broadcast to everyone@everywhere
        self.send_content(sender=sender, receiver=EVERYONE, content=command, priority=1)

    def report_online(self, sender: ID = None):
        """ send report command to keep user online """
        command = ReportCommand(title=ReportCommand.ONLINE)
        self.send_content(sender=sender, receiver=Station.ANY, content=command, priority=1)

    def report_offline(self, sender: ID = None):
        """ Send report command to let user offline """
        command = ReportCommand(title=ReportCommand.OFFLINE)
        self.send_content(sender=sender, receiver=Station.ANY, content=command, priority=1)

    def broadcast_document(self, updated: bool = False):
        """ broadcast meta & visa document to all stations """
        facebook = self.facebook
        user = facebook.current_user
        assert user is not None, 'current user not found'
        current = user.identifier
        meta = user.meta
        visa = user.visa
        assert visa is not None, 'visa not found: %s' % user
        command = DocumentCommand.response(identifier=current, meta=meta, document=visa)
        # send to all contacts
        contacts = facebook.contacts(identifier=current)
        for item in contacts:
            self.send_visa(sender=current, receiver=item, content=command, force=updated)
        # broadcast to everyone@everywhere
        self.send_visa(sender=current, receiver=EVERYONE, content=command, force=updated)

    def send_visa(self, sender: Optional[ID], receiver: ID, content: DocumentCommand, force: bool = False):
        checker = QueryFrequencyChecker()
        if checker.document_response_expired(identifier=receiver, force=force):
            self.info(msg='push visa to: %s' % receiver)
            self.send_content(sender=sender, receiver=receiver, content=content, priority=1)
        else:
            # response not expired yet
            self.debug(msg='document response not expired yet: %s' % receiver)

    # Override
    def query_meta(self, identifier: ID) -> bool:
        checker = QueryFrequencyChecker()
        if not checker.meta_query_expired(identifier=identifier):
            # query not expired yet
            self.debug(msg='meta query not expired yet: %s' % identifier)
            return False
        self.info(msg='querying meta: %s from any station' % identifier)
        command = MetaCommand.query(identifier=identifier)
        self.send_content(sender=None, receiver=Station.ANY, content=command, priority=1)
        return True

    # Override
    def query_document(self, identifier: ID) -> bool:
        checker = QueryFrequencyChecker()
        if not checker.document_query_expired(identifier=identifier):
            # query not expired yet
            self.debug(msg='document query not expired yet: %s' % identifier)
            return False
        self.info(msg='querying document: %s from any station' % identifier)
        command = DocumentCommand.query(identifier=identifier)
        self.send_content(sender=None, receiver=Station.ANY, content=command, priority=1)
        return True

    # Override
    def query_members(self, identifier: ID) -> bool:
        checker = QueryFrequencyChecker()
        if not checker.members_query_expired(identifier=identifier):
            # query not expired yet
            self.debug(msg='members query not expired yet: %s' % identifier)
            return False
        self.info(msg='querying members: %s from any station' % identifier)
        man = GroupManager()
        assistants = man.assistants(identifier=identifier)
        if assistants is None or len(assistants) == 0:
            self.error(msg='group assistants not found: %s' % identifier)
            return False
        # querying members from bot
        command = DocumentCommand.query(identifier=identifier)
        for bot in assistants:
            self.send_content(sender=None, receiver=bot, content=command, priority=1)
        return True

    # Override
    def process_reliable_message(self, msg: ReliableMessage) -> List[ReliableMessage]:
        # call super
        responses = super().process_reliable_message(msg=msg)
        if len(responses) == 0 and self._needs_receipt(msg=msg):
            current_user = self.facebook.current_user
            res = ReceiptCommand.create(text='Message received.', msg=msg)
            env = Envelope.create(sender=current_user.identifier, receiver=msg.sender)
            i_msg = InstantMessage.create(head=env, body=res)
            s_msg = self.encrypt_message(msg=i_msg)
            assert s_msg is not None, 'failed to encrypt message: %s -> %s' % (current_user, msg.sender)
            r_msg = self.sign_message(msg=s_msg)
            assert r_msg is not None, 'failed to sign message: %s -> %s' % (current_user, msg.sender)
            responses = [r_msg]
        return responses

    # noinspection PyMethodMayBeStatic
    def _needs_receipt(self, msg: ReliableMessage) -> bool:
        if msg.type == ContentType.COMMAND:
            # filter for looping message (receipt for receipt)
            return False
        sender = msg.sender
        # receiver = msg.receiver
        # if sender.type == EntityType.STATION or sender.type == EntityType.BOT:
        #     if receiver.type == EntityType.STATION or receiver.type == EntityType.BOT:
        #         # message between bots
        #         return False
        if sender.type != EntityType.USER:  # and receiver.type != EntityType.USER:
            # message between bots
            return False
        # current_user = self.facebook.current_user
        # if receiver != current_user.identifier:
        #     # forward message
        #     return True
        # TODO: other condition?
        return True
