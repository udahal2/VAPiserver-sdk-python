# This file was auto-generated by Fern from our API Definition.

import typing
from ...types.create_dtmf_tool_dto import CreateDtmfToolDto
from ...types.create_end_call_tool_dto import CreateEndCallToolDto
from ...types.create_function_tool_dto import CreateFunctionToolDto
from ...types.create_ghl_tool_dto import CreateGhlToolDto
from ...types.create_make_tool_dto import CreateMakeToolDto
from ...types.create_transfer_call_tool_dto import CreateTransferCallToolDto
from ...types.create_output_tool_dto import CreateOutputToolDto

ToolsCreateRequest = typing.Union[
    CreateDtmfToolDto,
    CreateEndCallToolDto,
    CreateFunctionToolDto,
    CreateGhlToolDto,
    CreateMakeToolDto,
    CreateTransferCallToolDto,
    CreateOutputToolDto,
]
