# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
import datetime as dt
from ..core.request_options import RequestOptions
from .types.phone_numbers_list_response_item import PhoneNumbersListResponseItem
from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.phone_numbers_create_request import PhoneNumbersCreateRequest
from .types.phone_numbers_create_response import PhoneNumbersCreateResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.phone_numbers_get_response import PhoneNumbersGetResponse
from ..core.jsonable_encoder import jsonable_encoder
from .types.phone_numbers_delete_response import PhoneNumbersDeleteResponse
from .types.update_phone_number_dto_fallback_destination import UpdatePhoneNumberDtoFallbackDestination
from .types.phone_numbers_update_response import PhoneNumbersUpdateResponse
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PhoneNumbersClient:
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
    ) -> typing.List[PhoneNumbersListResponseItem]:
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
        typing.List[PhoneNumbersListResponseItem]


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.phone_numbers.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "phone-number",
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
                    typing.List[PhoneNumbersListResponseItem],
                    parse_obj_as(
                        type_=typing.List[PhoneNumbersListResponseItem],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self, *, request: PhoneNumbersCreateRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PhoneNumbersCreateResponse:
        """
        Parameters
        ----------
        request : PhoneNumbersCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumbersCreateResponse


        Examples
        --------
        from vapi import CreateByoPhoneNumberDto, Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.phone_numbers.create(
            request=CreateByoPhoneNumberDto(
                credential_id="credentialId",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "phone-number",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PhoneNumbersCreateRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PhoneNumbersCreateResponse,
                    parse_obj_as(
                        type_=PhoneNumbersCreateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> PhoneNumbersGetResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumbersGetResponse


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.phone_numbers.get(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"phone-number/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PhoneNumbersGetResponse,
                    parse_obj_as(
                        type_=PhoneNumbersGetResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> PhoneNumbersDeleteResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumbersDeleteResponse


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.phone_numbers.delete(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"phone-number/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PhoneNumbersDeleteResponse,
                    parse_obj_as(
                        type_=PhoneNumbersDeleteResponse,  # type: ignore
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
        fallback_destination: typing.Optional[UpdatePhoneNumberDtoFallbackDestination] = OMIT,
        name: typing.Optional[str] = OMIT,
        assistant_id: typing.Optional[str] = OMIT,
        squad_id: typing.Optional[str] = OMIT,
        server_url: typing.Optional[str] = OMIT,
        server_url_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PhoneNumbersUpdateResponse:
        """
        Parameters
        ----------
        id : str

        fallback_destination : typing.Optional[UpdatePhoneNumberDtoFallbackDestination]
            This is the fallback destination an inbound call will be transferred to if:
            1. `assistantId` is not set
            2. `squadId` is not set
            3. and, `assistant-request` message to the `serverUrl` fails

            If this is not set and above conditions are met, the inbound call is hung up with an error message.

        name : typing.Optional[str]
            This is the name of the phone number. This is just for your own reference.

        assistant_id : typing.Optional[str]
            This is the assistant that will be used for incoming calls to this phone number.

            If neither `assistantId` nor `squadId` is set, `assistant-request` will be sent to your Server URL. Check `ServerMessage` and `ServerMessageResponse` for the shape of the message and response that is expected.

        squad_id : typing.Optional[str]
            This is the squad that will be used for incoming calls to this phone number.

            If neither `assistantId` nor `squadId` is set, `assistant-request` will be sent to your Server URL. Check `ServerMessage` and `ServerMessageResponse` for the shape of the message and response that is expected.

        server_url : typing.Optional[str]
            This is the server URL where messages will be sent for calls on this number. This includes the `assistant-request` message.

            You can see the shape of the messages sent in `ServerMessage`.

            This overrides the `org.serverUrl`. Order of precedence: tool.server.url > assistant.serverUrl > phoneNumber.serverUrl > org.serverUrl.

        server_url_secret : typing.Optional[str]
            This is the secret Vapi will send with every message to your server. It's sent as a header called x-vapi-secret.

            Same precedence logic as serverUrl.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumbersUpdateResponse


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.phone_numbers.update(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"phone-number/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "fallbackDestination": convert_and_respect_annotation_metadata(
                    object_=fallback_destination, annotation=UpdatePhoneNumberDtoFallbackDestination, direction="write"
                ),
                "name": name,
                "assistantId": assistant_id,
                "squadId": squad_id,
                "serverUrl": server_url,
                "serverUrlSecret": server_url_secret,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PhoneNumbersUpdateResponse,
                    parse_obj_as(
                        type_=PhoneNumbersUpdateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPhoneNumbersClient:
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
    ) -> typing.List[PhoneNumbersListResponseItem]:
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
        typing.List[PhoneNumbersListResponseItem]


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.phone_numbers.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "phone-number",
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
                    typing.List[PhoneNumbersListResponseItem],
                    parse_obj_as(
                        type_=typing.List[PhoneNumbersListResponseItem],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self, *, request: PhoneNumbersCreateRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PhoneNumbersCreateResponse:
        """
        Parameters
        ----------
        request : PhoneNumbersCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumbersCreateResponse


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi, CreateByoPhoneNumberDto

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.phone_numbers.create(
                request=CreateByoPhoneNumberDto(
                    credential_id="credentialId",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "phone-number",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PhoneNumbersCreateRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PhoneNumbersCreateResponse,
                    parse_obj_as(
                        type_=PhoneNumbersCreateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> PhoneNumbersGetResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumbersGetResponse


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.phone_numbers.get(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"phone-number/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PhoneNumbersGetResponse,
                    parse_obj_as(
                        type_=PhoneNumbersGetResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PhoneNumbersDeleteResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumbersDeleteResponse


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.phone_numbers.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"phone-number/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PhoneNumbersDeleteResponse,
                    parse_obj_as(
                        type_=PhoneNumbersDeleteResponse,  # type: ignore
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
        fallback_destination: typing.Optional[UpdatePhoneNumberDtoFallbackDestination] = OMIT,
        name: typing.Optional[str] = OMIT,
        assistant_id: typing.Optional[str] = OMIT,
        squad_id: typing.Optional[str] = OMIT,
        server_url: typing.Optional[str] = OMIT,
        server_url_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PhoneNumbersUpdateResponse:
        """
        Parameters
        ----------
        id : str

        fallback_destination : typing.Optional[UpdatePhoneNumberDtoFallbackDestination]
            This is the fallback destination an inbound call will be transferred to if:
            1. `assistantId` is not set
            2. `squadId` is not set
            3. and, `assistant-request` message to the `serverUrl` fails

            If this is not set and above conditions are met, the inbound call is hung up with an error message.

        name : typing.Optional[str]
            This is the name of the phone number. This is just for your own reference.

        assistant_id : typing.Optional[str]
            This is the assistant that will be used for incoming calls to this phone number.

            If neither `assistantId` nor `squadId` is set, `assistant-request` will be sent to your Server URL. Check `ServerMessage` and `ServerMessageResponse` for the shape of the message and response that is expected.

        squad_id : typing.Optional[str]
            This is the squad that will be used for incoming calls to this phone number.

            If neither `assistantId` nor `squadId` is set, `assistant-request` will be sent to your Server URL. Check `ServerMessage` and `ServerMessageResponse` for the shape of the message and response that is expected.

        server_url : typing.Optional[str]
            This is the server URL where messages will be sent for calls on this number. This includes the `assistant-request` message.

            You can see the shape of the messages sent in `ServerMessage`.

            This overrides the `org.serverUrl`. Order of precedence: tool.server.url > assistant.serverUrl > phoneNumber.serverUrl > org.serverUrl.

        server_url_secret : typing.Optional[str]
            This is the secret Vapi will send with every message to your server. It's sent as a header called x-vapi-secret.

            Same precedence logic as serverUrl.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumbersUpdateResponse


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.phone_numbers.update(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"phone-number/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "fallbackDestination": convert_and_respect_annotation_metadata(
                    object_=fallback_destination, annotation=UpdatePhoneNumberDtoFallbackDestination, direction="write"
                ),
                "name": name,
                "assistantId": assistant_id,
                "squadId": squad_id,
                "serverUrl": server_url,
                "serverUrlSecret": server_url_secret,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PhoneNumbersUpdateResponse,
                    parse_obj_as(
                        type_=PhoneNumbersUpdateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
