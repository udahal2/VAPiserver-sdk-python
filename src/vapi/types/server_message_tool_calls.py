# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
from .callback_step import CallbackStep
from .create_workflow_block_dto import CreateWorkflowBlockDto
from .handoff_step import HandoffStep
import typing_extensions
import typing
from .server_message_tool_calls_phone_number import ServerMessageToolCallsPhoneNumber
from ..core.serialization import FieldMetadata
import pydantic
from .server_message_tool_calls_tool_with_tool_call_list_item import ServerMessageToolCallsToolWithToolCallListItem
from .artifact import Artifact
from .create_assistant_dto import CreateAssistantDto
from .create_customer_dto import CreateCustomerDto
from .call import Call
from .tool_call import ToolCall
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.pydantic_utilities import update_forward_refs


class ServerMessageToolCalls(UniversalBaseModel):
    phone_number: typing_extensions.Annotated[
        typing.Optional[ServerMessageToolCallsPhoneNumber], FieldMetadata(alias="phoneNumber")
    ] = pydantic.Field(default=None)
    """
    This is the phone number associated with the call.
    
    This matches one of the following:
    
    - `call.phoneNumber`,
    - `call.phoneNumberId`.
    """

    type: typing.Optional[typing.Literal["tool-calls"]] = pydantic.Field(default=None)
    """
    This is the type of the message. "tool-calls" is sent to call a tool.
    """

    tool_with_tool_call_list: typing_extensions.Annotated[
        typing.List[ServerMessageToolCallsToolWithToolCallListItem], FieldMetadata(alias="toolWithToolCallList")
    ] = pydantic.Field()
    """
    This is the list of tools calls that the model is requesting along with the original tool configuration.
    """

    timestamp: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the ISO-8601 formatted timestamp of when the message was sent.
    """

    artifact: typing.Optional[Artifact] = pydantic.Field(default=None)
    """
    This is a live version of the `call.artifact`.
    
    This matches what is stored on `call.artifact` after the call.
    """

    assistant: typing.Optional[CreateAssistantDto] = pydantic.Field(default=None)
    """
    This is the assistant that is currently active. This is provided for convenience.
    
    This matches one of the following:
    
    - `call.assistant`,
    - `call.assistantId`,
    - `call.squad[n].assistant`,
    - `call.squad[n].assistantId`,
    - `call.squadId->[n].assistant`,
    - `call.squadId->[n].assistantId`.
    """

    customer: typing.Optional[CreateCustomerDto] = pydantic.Field(default=None)
    """
    This is the customer associated with the call.
    
    This matches one of the following:
    
    - `call.customer`,
    - `call.customerId`.
    """

    call: typing.Optional[Call] = pydantic.Field(default=None)
    """
    This is the call object.
    
    This matches what was returned in POST /call.
    
    Note: This might get stale during the call. To get the latest call object, especially after the call is ended, use GET /call/:id.
    """

    tool_call_list: typing_extensions.Annotated[typing.List[ToolCall], FieldMetadata(alias="toolCallList")] = (
        pydantic.Field()
    )
    """
    This is the list of tool calls that the model is requesting.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(CallbackStep, ServerMessageToolCalls=ServerMessageToolCalls)
update_forward_refs(CreateWorkflowBlockDto, ServerMessageToolCalls=ServerMessageToolCalls)
update_forward_refs(HandoffStep, ServerMessageToolCalls=ServerMessageToolCalls)
