# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .vonage_phone_number_fallback_destination import VonagePhoneNumberFallbackDestination
from ..core.serialization import FieldMetadata
import pydantic
import datetime as dt
from .server import Server
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class VonagePhoneNumber(UniversalBaseModel):
    fallback_destination: typing_extensions.Annotated[
        typing.Optional[VonagePhoneNumberFallbackDestination], FieldMetadata(alias="fallbackDestination")
    ] = pydantic.Field(default=None)
    """
    This is the fallback destination an inbound call will be transferred to if:
    1. `assistantId` is not set
    2. `squadId` is not set
    3. and, `assistant-request` message to the `serverUrl` fails
    
    If this is not set and above conditions are met, the inbound call is hung up with an error message.
    """

    provider: typing.Literal["vonage"] = "vonage"
    id: str = pydantic.Field()
    """
    This is the unique identifier for the phone number.
    """

    org_id: typing_extensions.Annotated[str, FieldMetadata(alias="orgId")] = pydantic.Field()
    """
    This is the unique identifier for the org that this phone number belongs to.
    """

    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the phone number was created.
    """

    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the phone number was last updated.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of the phone number. This is just for your own reference.
    """

    assistant_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="assistantId")] = (
        pydantic.Field(default=None)
    )
    """
    This is the assistant that will be used for incoming calls to this phone number.
    
    If neither `assistantId` nor `squadId` is set, `assistant-request` will be sent to your Server URL. Check `ServerMessage` and `ServerMessageResponse` for the shape of the message and response that is expected.
    """

    squad_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="squadId")] = pydantic.Field(
        default=None
    )
    """
    This is the squad that will be used for incoming calls to this phone number.
    
    If neither `assistantId` nor `squadId` is set, `assistant-request` will be sent to your Server URL. Check `ServerMessage` and `ServerMessageResponse` for the shape of the message and response that is expected.
    """

    server: typing.Optional[Server] = pydantic.Field(default=None)
    """
    This is where Vapi will send webhooks. You can find all webhooks available along with their shape in ServerMessage schema.
    
    The order of precedence is:
    
    1. assistant.server
    2. phoneNumber.server
    3. org.server
    """

    number: str = pydantic.Field()
    """
    These are the digits of the phone number you own on your Vonage.
    """

    credential_id: typing_extensions.Annotated[str, FieldMetadata(alias="credentialId")] = pydantic.Field()
    """
    This is the credential that is used to make outgoing calls, and do operations like call transfer and hang up.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
