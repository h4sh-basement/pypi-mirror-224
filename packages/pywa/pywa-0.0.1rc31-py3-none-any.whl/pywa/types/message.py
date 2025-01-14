from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING, Callable, Any
from pywa.errors import WhatsAppError
from .base_update import BaseUpdate
from .others import ReplyToMessage, Reaction, Location, Contact, MessageType, User, Metadata, Order, System
from .callback import SectionList, InlineButton
from .media import Image, Video, Sticker, Document, Audio

if TYPE_CHECKING:
    from pywa.client import WhatsApp


_FIELDS_TO_OBJECTS: dict[str, Callable[[dict, WhatsApp], Any]] = {
    'text': lambda m, _client: m['body'],
    'image': Image.from_dict,
    'video': Video.from_dict,
    'sticker': Sticker.from_dict,
    'document': Document.from_dict,
    'audio': Audio.from_dict,
    'reaction': Reaction.from_dict,
    'location': Location.from_dict,
    'contacts': lambda m, _client: tuple(Contact.from_dict(c) for c in m),
    'order': Order.from_dict,
    'system': System.from_dict,
}
_MEDIA_FIELDS = ('image', 'video', 'sticker', 'document', 'audio')


@dataclass(frozen=True, slots=True)
class Message(BaseUpdate):
    """
    A message received from a user.

    - See more: https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks/components#messages-object

    Attributes:
        id: The message ID.
        metadata: The metadata of the message (to which phone number it was sent).
        type: The message type (text, image, video, etc.).
        from_user: The user who sent the message.
        timestamp: The timestamp when the message was sent.
        reply_to_message: The message to which this message is a reply to. (optional)
        forwarded: Whether the message was forwarded.
        forwarded_many_times: Whether the message was forwarded many times. (when True, ``forwarded`` will be True as well)
        text: The text of the message (if the message type is text). (optional)
        image: The image of the message (if the message type is image). (optional)
        video: The video of the message (if the message type is video). (optional)
        sticker: The sticker of the message (if the message type is sticker). (optional)
        document: The document of the message (if the message type is document). (optional)
        audio: The audio of the message (if the message type is audio). (optional)
        caption: The caption of the message (if the message type is image, video, or document). (optional)
        reaction: The reaction of the message (if the message type is reaction). (optional)
        location: The location of the message (if the message type is location). (optional)
        contacts: The contacts of the message (if the message type is contacts). (optional)
        order: The order of the message (if the message type is order). (optional)
        system: The system update (if the message type is system). (optional)
        error: The error of the message (if the message type is `unsupported`). (optional)
    """
    reply_to_message: ReplyToMessage | None
    forwarded: bool
    forwarded_many_times: bool
    text: str | None = None
    image: Image | None = None
    video: Video | None = None
    sticker: Sticker | None = None
    document: Document | None = None
    audio: Audio | None = None
    caption: str | None = None
    reaction: Reaction | None = None
    location: Location | None = None
    contacts: tuple[Contact] | None = None
    order: Order | None = None
    system: System | None = None
    error: WhatsAppError | None = None

    @property
    def message_id_to_reply(self) -> str:
        """The ID of the message to reply to."""
        return self.id if self.type != MessageType.REACTION else self.reaction.message_id

    @property
    def has_media(self) -> bool:
        """Whether the message has any media."""
        try:
            return self.media is not None
        except ValueError:
            return False

    @property
    def is_reply(self) -> bool:
        """Whether the message is a reply to another message."""
        return self.reply_to_message is not None

    @classmethod
    def from_dict(cls, client: WhatsApp, value: dict) -> Message:
        msg = value['messages'][0]
        msg_type = msg['type']
        context = msg.get('context')
        msg_obj = _FIELDS_TO_OBJECTS.get(msg_type)
        msg_content = {msg_type: msg_obj(msg[msg_type], _client=client)} if msg_obj is not None else {}
        return cls(
            _client=client,
            id=msg['id'],
            type=MessageType(msg['type']),
            **msg_content,
            from_user=User.from_dict(value['contacts'][0]),
            timestamp=datetime.fromtimestamp(int(msg['timestamp'])),
            metadata=Metadata.from_dict(value['metadata']),
            forwarded=any(context.get(key) for key in ('forwarded', 'frequently_forwarded')) if context else False,
            forwarded_many_times=context.get('frequently_forwarded', False) if context else False,
            reply_to_message=ReplyToMessage.from_dict(context),
            caption=msg[msg_type].get('caption') if msg_type in ('image', 'video', 'document') else None,
            error=WhatsAppError.from_incoming_error(msg['errors'][0]) if 'errors' in msg else None
        )

    @property
    def media(self) -> Image | Video | Sticker | Document | Audio:
        """
        The media of the message (image, video, sticker, document or audio).

        Raises:
            ValueError: If the message does not contain any media. (You can check this with ``msg.has_media``)
        """
        try:
            return next(getattr(self, media_type) for media_type in _MEDIA_FIELDS if getattr(self, media_type))
        except StopIteration:
            raise ValueError('The message does not contain any media.')

    def download_media(
            self,
            filepath: str | None = None,
            filename: str | None = None,
            in_memory: bool = False,
    ) -> str | bytes:
        """
        Download a media file from WhatsApp servers (image, video, sticker, document or audio).

        Args:
            filepath: The path where to save the file (if not provided, the current working directory will be used).
            filename: The name of the file (if not provided, it will be guessed from the URL + extension).
            in_memory: Whether to return the file as bytes instead of saving it to disk (default: False).

        Returns:
            The path of the saved file if ``in_memory`` is False, the file as bytes otherwise.

        Raises:
            ValueError: If the message does not contain any media.
        """
        return self.media.download(path=filepath, filename=filename, in_memory=in_memory)

    def copy(
            self,
            to: str,
            reply_to_message_id: str = None,
            preview_url: bool = False,
            keyboard: list[InlineButton] | SectionList | None = None,
            header: str | None = None,
            body: str | None = None,
            footer: str | None = None,
    ) -> str:
        """
        Copy incoming message to another chat
            - The WhatsApp Cloud API does not offer a `real` forward option so this is just copy the message content.

        Args:
            to: The phone ID of the WhatsApp user to copy the message to.
            reply_to_message_id:  The message ID to reply to (optional).
            preview_url: Whether to show a preview of the URL in the message (if any).
            keyboard: The buttons to send with the message (only in case of message from type ``text``, ``document``,
             ``video`` and ``image``. also, the ``SectionList`` is only available to ``text`` type)
            header: The header of the message (if keyboard is provided, optional, up to 60 characters, no markdown allowed).
            body: The body of the message (if keyboard are provided, optional, up to 1024 characters, markdown allowed).
            footer: The footer of the message (if keyboard is provided, optional, markdown has no effect).

        Returns:
            The ID of the sent message.

        Raises:
            ValueError: If the message type is ``reaction`` and no ``reply_to_message_id`` is provided, or if the message
             type is ``unsupported``.
        """
        match self.type:
            case MessageType.TEXT:
                return self._client.send_message(
                    to=to,
                    reply_to_message_id=reply_to_message_id,
                    text=self.text,
                    preview_url=preview_url,
                    keyboard=keyboard,
                    header=header,
                    footer=footer,
                )
            case MessageType.DOCUMENT:
                return self._client.send_document(
                    to=to,
                    reply_to_message_id=reply_to_message_id,
                    document=self.document.id,
                    filename=self.document.filename,
                    caption=self.caption,
                    buttons=keyboard,
                    body=body,
                    footer=footer,
                )
            case MessageType.IMAGE:
                return self._client.send_image(
                    to=to,
                    reply_to_message_id=reply_to_message_id,
                    image=self.image.id,
                    caption=self.caption,
                    buttons=keyboard,
                    body=body,
                    footer=footer,
                )
            case MessageType.VIDEO:
                return self._client.send_video(
                    to=to,
                    reply_to_message_id=reply_to_message_id,
                    video=self.video.id,
                    caption=self.caption,
                    buttons=keyboard,
                    body=body,
                    footer=footer,
                )
            case MessageType.STICKER:
                return self._client.send_sticker(
                    to=to,
                    sticker=self.sticker.id
                )
            case MessageType.LOCATION:
                return self._client.send_location(
                    to=to,
                    latitude=self.location.latitude,
                    longitude=self.location.longitude,
                    name=self.location.name,
                    address=self.location.address
                )
            case MessageType.AUDIO:
                return self._client.send_audio(
                    to=to,
                    audio=self.audio.id
                )
            case MessageType.CONTACTS:
                return self._client.send_contact(
                    to=to,
                    reply_to_message_id=reply_to_message_id,
                    contact=self.contacts
                )
            case MessageType.REACTION:
                if reply_to_message_id is None:
                    raise ValueError("You need to provide `reply_to_message_id` in order to `copy` a reaction")
                return self._client.send_reaction(
                    to=to,
                    message_id=reply_to_message_id,
                    emoji=self.reaction.emoji or ""
                )
            case MessageType.UNSUPPORTED:
                raise ValueError("MessageType.UNSUPPORTED cannot be copied!")
            case _:
                raise ValueError("Message with unknown type cannot be copied!")
