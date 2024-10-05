# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
import datetime as dt
from ..core.request_options import RequestOptions
from .types.tools_list_response_item import ToolsListResponseItem
from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.tools_create_request import ToolsCreateRequest
from .types.tools_create_response import ToolsCreateResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.tools_get_response import ToolsGetResponse
from ..core.jsonable_encoder import jsonable_encoder
from .types.tools_delete_response import ToolsDeleteResponse
from .types.update_tool_dto_messages_item import UpdateToolDtoMessagesItem
from ..types.open_ai_function import OpenAiFunction
from ..types.server import Server
from .types.tools_update_response import ToolsUpdateResponse
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ToolsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        limit: typing.Optional[float] = None,
        created_at_gt: typing.Optional[dt.datetime] = None,
        created_at_lt: typing.Optional[dt.datetime] = None,
        created_at_ge: typing.Optional[dt.datetime] = None,
        created_at_le: typing.Optional[dt.datetime] = None,
        updated_at_gt: typing.Optional[dt.datetime] = None,
        updated_at_lt: typing.Optional[dt.datetime] = None,
        updated_at_ge: typing.Optional[dt.datetime] = None,
        updated_at_le: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ToolsListResponseItem]:
        """
        Parameters
        ----------
        limit : typing.Optional[float]
            This is the maximum number of items to return. Defaults to 100.

        created_at_gt : typing.Optional[dt.datetime]
            This will return items where the createdAt is greater than the specified value.

        created_at_lt : typing.Optional[dt.datetime]
            This will return items where the createdAt is less than the specified value.

        created_at_ge : typing.Optional[dt.datetime]
            This will return items where the createdAt is greater than or equal to the specified value.

        created_at_le : typing.Optional[dt.datetime]
            This will return items where the createdAt is less than or equal to the specified value.

        updated_at_gt : typing.Optional[dt.datetime]
            This will return items where the updatedAt is greater than the specified value.

        updated_at_lt : typing.Optional[dt.datetime]
            This will return items where the updatedAt is less than the specified value.

        updated_at_ge : typing.Optional[dt.datetime]
            This will return items where the updatedAt is greater than or equal to the specified value.

        updated_at_le : typing.Optional[dt.datetime]
            This will return items where the updatedAt is less than or equal to the specified value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ToolsListResponseItem]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tool",
            method="GET",
            params={
                "limit": limit,
                "createdAtGt": serialize_datetime(created_at_gt) if created_at_gt is not None else None,
                "createdAtLt": serialize_datetime(created_at_lt) if created_at_lt is not None else None,
                "createdAtGe": serialize_datetime(created_at_ge) if created_at_ge is not None else None,
                "createdAtLe": serialize_datetime(created_at_le) if created_at_le is not None else None,
                "updatedAtGt": serialize_datetime(updated_at_gt) if updated_at_gt is not None else None,
                "updatedAtLt": serialize_datetime(updated_at_lt) if updated_at_lt is not None else None,
                "updatedAtGe": serialize_datetime(updated_at_ge) if updated_at_ge is not None else None,
                "updatedAtLe": serialize_datetime(updated_at_le) if updated_at_le is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[ToolsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[ToolsListResponseItem],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self, *, request: ToolsCreateRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> ToolsCreateResponse:
        """
        Parameters
        ----------
        request : ToolsCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolsCreateResponse

        """
        _response = self._client_wrapper.httpx_client.request(
            "tool",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=ToolsCreateRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ToolsCreateResponse,
                    parse_obj_as(
                        type_=ToolsCreateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ToolsGetResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolsGetResponse

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tool/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ToolsGetResponse,
                    parse_obj_as(
                        type_=ToolsGetResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ToolsDeleteResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolsDeleteResponse

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tool/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ToolsDeleteResponse,
                    parse_obj_as(
                        type_=ToolsDeleteResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        id: str,
        *,
        async_: typing.Optional[bool] = OMIT,
        messages: typing.Optional[typing.Sequence[UpdateToolDtoMessagesItem]] = OMIT,
        function: typing.Optional[OpenAiFunction] = OMIT,
        server: typing.Optional[Server] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolsUpdateResponse:
        """
        Parameters
        ----------
        id : str

        async_ : typing.Optional[bool]
            This determines if the tool is async.

            If async, the assistant will move forward without waiting for your server to respond. This is useful if you just want to trigger something on your server.

            If sync, the assistant will wait for your server to respond. This is useful if want assistant to respond with the result from your server.

            Defaults to synchronous (`false`).

        messages : typing.Optional[typing.Sequence[UpdateToolDtoMessagesItem]]
            These are the messages that will be spoken to the user as the tool is running.

            For some tools, this is auto-filled based on special fields like `tool.destinations`. For others like the function tool, these can be custom configured.

        function : typing.Optional[OpenAiFunction]
            This is the function definition of the tool.

            For `endCall`, `transferCall`, and `dtmf` tools, this is auto-filled based on tool-specific fields like `tool.destinations`. But, even in those cases, you can provide a custom function definition for advanced use cases.

            An example of an advanced use case is if you want to customize the message that's spoken for `endCall` tool. You can specify a function where it returns an argument "reason". Then, in `messages` array, you can have many "request-complete" messages. One of these messages will be triggered if the `messages[].conditions` matches the "reason" argument.

        server : typing.Optional[Server]
            This is the server that will be hit when this tool is requested by the model.

            All requests will be sent with the call object among other things. You can find more details in the Server URL documentation.

            This overrides the serverUrl set on the org and the phoneNumber. Order of precedence: highest tool.server.url, then assistant.serverUrl, then phoneNumber.serverUrl, then org.serverUrl.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolsUpdateResponse

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tool/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "async": async_,
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[UpdateToolDtoMessagesItem], direction="write"
                ),
                "function": convert_and_respect_annotation_metadata(
                    object_=function, annotation=OpenAiFunction, direction="write"
                ),
                "server": convert_and_respect_annotation_metadata(object_=server, annotation=Server, direction="write"),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ToolsUpdateResponse,
                    parse_obj_as(
                        type_=ToolsUpdateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncToolsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        limit: typing.Optional[float] = None,
        created_at_gt: typing.Optional[dt.datetime] = None,
        created_at_lt: typing.Optional[dt.datetime] = None,
        created_at_ge: typing.Optional[dt.datetime] = None,
        created_at_le: typing.Optional[dt.datetime] = None,
        updated_at_gt: typing.Optional[dt.datetime] = None,
        updated_at_lt: typing.Optional[dt.datetime] = None,
        updated_at_ge: typing.Optional[dt.datetime] = None,
        updated_at_le: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ToolsListResponseItem]:
        """
        Parameters
        ----------
        limit : typing.Optional[float]
            This is the maximum number of items to return. Defaults to 100.

        created_at_gt : typing.Optional[dt.datetime]
            This will return items where the createdAt is greater than the specified value.

        created_at_lt : typing.Optional[dt.datetime]
            This will return items where the createdAt is less than the specified value.

        created_at_ge : typing.Optional[dt.datetime]
            This will return items where the createdAt is greater than or equal to the specified value.

        created_at_le : typing.Optional[dt.datetime]
            This will return items where the createdAt is less than or equal to the specified value.

        updated_at_gt : typing.Optional[dt.datetime]
            This will return items where the updatedAt is greater than the specified value.

        updated_at_lt : typing.Optional[dt.datetime]
            This will return items where the updatedAt is less than the specified value.

        updated_at_ge : typing.Optional[dt.datetime]
            This will return items where the updatedAt is greater than or equal to the specified value.

        updated_at_le : typing.Optional[dt.datetime]
            This will return items where the updatedAt is less than or equal to the specified value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ToolsListResponseItem]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tool",
            method="GET",
            params={
                "limit": limit,
                "createdAtGt": serialize_datetime(created_at_gt) if created_at_gt is not None else None,
                "createdAtLt": serialize_datetime(created_at_lt) if created_at_lt is not None else None,
                "createdAtGe": serialize_datetime(created_at_ge) if created_at_ge is not None else None,
                "createdAtLe": serialize_datetime(created_at_le) if created_at_le is not None else None,
                "updatedAtGt": serialize_datetime(updated_at_gt) if updated_at_gt is not None else None,
                "updatedAtLt": serialize_datetime(updated_at_lt) if updated_at_lt is not None else None,
                "updatedAtGe": serialize_datetime(updated_at_ge) if updated_at_ge is not None else None,
                "updatedAtLe": serialize_datetime(updated_at_le) if updated_at_le is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[ToolsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[ToolsListResponseItem],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self, *, request: ToolsCreateRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> ToolsCreateResponse:
        """
        Parameters
        ----------
        request : ToolsCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolsCreateResponse

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tool",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=ToolsCreateRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ToolsCreateResponse,
                    parse_obj_as(
                        type_=ToolsCreateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ToolsGetResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolsGetResponse

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tool/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ToolsGetResponse,
                    parse_obj_as(
                        type_=ToolsGetResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ToolsDeleteResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolsDeleteResponse

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tool/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ToolsDeleteResponse,
                    parse_obj_as(
                        type_=ToolsDeleteResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        id: str,
        *,
        async_: typing.Optional[bool] = OMIT,
        messages: typing.Optional[typing.Sequence[UpdateToolDtoMessagesItem]] = OMIT,
        function: typing.Optional[OpenAiFunction] = OMIT,
        server: typing.Optional[Server] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolsUpdateResponse:
        """
        Parameters
        ----------
        id : str

        async_ : typing.Optional[bool]
            This determines if the tool is async.

            If async, the assistant will move forward without waiting for your server to respond. This is useful if you just want to trigger something on your server.

            If sync, the assistant will wait for your server to respond. This is useful if want assistant to respond with the result from your server.

            Defaults to synchronous (`false`).

        messages : typing.Optional[typing.Sequence[UpdateToolDtoMessagesItem]]
            These are the messages that will be spoken to the user as the tool is running.

            For some tools, this is auto-filled based on special fields like `tool.destinations`. For others like the function tool, these can be custom configured.

        function : typing.Optional[OpenAiFunction]
            This is the function definition of the tool.

            For `endCall`, `transferCall`, and `dtmf` tools, this is auto-filled based on tool-specific fields like `tool.destinations`. But, even in those cases, you can provide a custom function definition for advanced use cases.

            An example of an advanced use case is if you want to customize the message that's spoken for `endCall` tool. You can specify a function where it returns an argument "reason". Then, in `messages` array, you can have many "request-complete" messages. One of these messages will be triggered if the `messages[].conditions` matches the "reason" argument.

        server : typing.Optional[Server]
            This is the server that will be hit when this tool is requested by the model.

            All requests will be sent with the call object among other things. You can find more details in the Server URL documentation.

            This overrides the serverUrl set on the org and the phoneNumber. Order of precedence: highest tool.server.url, then assistant.serverUrl, then phoneNumber.serverUrl, then org.serverUrl.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolsUpdateResponse

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tool/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "async": async_,
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[UpdateToolDtoMessagesItem], direction="write"
                ),
                "function": convert_and_respect_annotation_metadata(
                    object_=function, annotation=OpenAiFunction, direction="write"
                ),
                "server": convert_and_respect_annotation_metadata(object_=server, annotation=Server, direction="write"),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ToolsUpdateResponse,
                    parse_obj_as(
                        type_=ToolsUpdateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
