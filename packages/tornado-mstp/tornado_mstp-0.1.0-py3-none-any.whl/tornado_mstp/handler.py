import json
from typing import Union, Optional, Awaitable

from tornado.websocket import WebSocketHandler

from .schema import (
    PackageType,
    ServerInfo,
    LoginInfo,
    Reconnect,
    MessageHeader,
    MessageReceiver,
    Segment,
    ContentType,
    Ack,
    ClientEndConnection
)


class MstpSocketHandler(WebSocketHandler):
    """An MSTP base class for WebSocket handler.

    Class attributes ``automatic_closing_time`` and ``ver`` needs to be set when
    creating handler from this base class.
    """
    automatic_closing_time: Optional[int] = 10
    ver: Optional[str] = "0.1"

    async def open(
        self,
        *args: str,
        **kwargs: str
    ) -> Optional[Awaitable[None]]:
        self.set_nodelay(True)  # disable Nagle algorithm to make packet transferred immediately

        await self._send_server_info()
        return

    async def on_message(
        self,
        message: Union[str, bytes]
    ) -> Optional[Awaitable[None]]:
        try:
            ws_msg = json.loads(message)
        except json.JSONDecodeError as e:
            print(e)  # TODO: log
            await self.write_message(
                "Invalid ws message type, only JSON is supported.")
            return
        else:
            if not isinstance(ws_msg, dict):
                await self.write_message("Invalid ws message body.")
                return

        package_type = ws_msg.get("package_type")
        match package_type:
            case PackageType.LOGIN_INFO:
                login_info = LoginInfo(**ws_msg)
                await self.handle_login(secret=login_info.secret)
            case PackageType.RECONNECT:
                reconnect = Reconnect(**ws_msg)
                await self.handle_reconnect(session_id=reconnect.session_id)
            case PackageType.MESSAGE_HEADER:
                message_header = MessageHeader(**ws_msg)
                await self.handle_message_header(
                    package_id=message_header.package_id,
                    message_index=message_header.message_index,
                    receiver=message_header.receiver
                )
            case PackageType.SEGMENT:
                segment = Segment(**ws_msg)
                await self.handle_segment(
                    package_id=segment.package_id,
                    message_index=segment.message_index,
                    segment_index=segment.segment_index,
                    is_end=segment.is_end,
                    content_type=segment.content_type,
                    content=segment.content
                )
            case PackageType.ACK:
                ack = Ack(**ws_msg)
                await self.handle_ack(package_id=ack.package_id)
            case PackageType.CLIENT_END_CONNECTION:
                client_end_connection = ClientEndConnection(**ws_msg)
                await self.handle_client_end_connection(
                    reason=client_end_connection.reason
                )
            case _:
                await self.write_message("Unsupported `package_type`")
        return

    async def _send_server_info(self):
        await self.write_message(
            ServerInfo(
                automatic_closing_time=self.automatic_closing_time,
                ver=self.ver
            ).model_dump_json(exclude_none=True)
        )

    async def handle_login(self, *, secret: Optional[str] = None) -> None:
        """**needs implementation**
        A callback function called when server receives an MSTP package of
        `tornado_mstp.schema.PackageType.LOGIN` from the client.

        :param secret: a pre-defined 32-chars
        """
        raise NotImplementedError

    async def handle_reconnect(
        self,
        *,
        session_id: Optional[str] = None
    ) -> None:
        """**needs implementation**
        A callback function called when server receives an MSTP package of
        `tornado_mstp.schema.PackageType.RECONNECT` from the client.

        :param session_id: a random 32-chars sequence originate by server to
            indicate this session
        """
        raise NotImplementedError

    async def handle_message_header(
        self,
        *,
        package_id: Optional[str] = None,
        message_index: Optional[int] = None,
        receiver: Optional[MessageReceiver] = None
    ) -> None:
        """**needs implementation**
        A callback function called when server receives an MSTP package of
        `tornado_mstp.schema.PackageType.MESSAGE_HEADER` from the client.

        :param package_id: a random 16-chars sequence indicate this package
        :param message_index: indicate the index of this message
        :param receiver: agent/user
        """
        raise NotImplementedError

    async def handle_segment(
        self,
        package_id: Optional[str] = None,
        message_index: Optional[int] = None,
        segment_index: Optional[int] = None,
        is_end: Optional[bool] = None,
        content_type: Optional[ContentType] = None,
        content: Optional[str] = None
    ) -> None:
        """**needs implementation**
        A callback function called when server receives an MSTP package of
        `tornado_mstp.schema.PackageType.SEGMENT` from the client.

        :param package_id: a random 16-chars sequence indicate this package
        :param message_index: indicate the index of this message
        :param segment_index: indicate the order of this segment in the current
            message
        :param is_end: indicate if this segment is the end of the current message
        :param content_type: segment content_type, see
            `tornado_mstp.schema.ContentType`
        :param content: text, http address for image audio video and web
        """
        raise NotImplementedError

    async def handle_ack(self, *, package_id: Optional[str] = None) -> None:
        """**needs implementation**
        A callback function called when server receives an MSTP package of
        `tornado_mstp.schema.PackageType.ACK` from the client.

        :param package_id: the package id that should be acked
        """
        raise NotImplementedError

    async def handle_client_end_connection(
        self,
        *,
        reason: Optional[str] = None
    ) -> None:
        """**needs implementation**
        A callback function called when server receives an MSTP package of
        `tornado_mstp.schema.PackageType.CLIENT_END_CONNECTION` from the client.

        :param reason: reason of ending connection by client
        """
        raise NotImplementedError
