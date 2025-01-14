# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
import datetime as dt
from ..core.request_options import RequestOptions
from .types.knowledge_bases_list_response_item import KnowledgeBasesListResponseItem
from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.knowledge_bases_create_request import KnowledgeBasesCreateRequest
from .types.knowledge_bases_create_response import KnowledgeBasesCreateResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.knowledge_bases_get_response import KnowledgeBasesGetResponse
from ..core.jsonable_encoder import jsonable_encoder
from .types.knowledge_bases_delete_response import KnowledgeBasesDeleteResponse
from .types.knowledge_bases_update_request import KnowledgeBasesUpdateRequest
from .types.knowledge_bases_update_response import KnowledgeBasesUpdateResponse
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class KnowledgeBasesClient:
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
    ) -> typing.List[KnowledgeBasesListResponseItem]:
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
        typing.List[KnowledgeBasesListResponseItem]

        """
        _response = self._client_wrapper.httpx_client.request(
            "knowledge-base",
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
                    typing.List[KnowledgeBasesListResponseItem],
                    parse_obj_as(
                        type_=typing.List[KnowledgeBasesListResponseItem],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self, *, request: KnowledgeBasesCreateRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> KnowledgeBasesCreateResponse:
        """
        Parameters
        ----------
        request : KnowledgeBasesCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KnowledgeBasesCreateResponse

        """
        _response = self._client_wrapper.httpx_client.request(
            "knowledge-base",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=KnowledgeBasesCreateRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    KnowledgeBasesCreateResponse,
                    parse_obj_as(
                        type_=KnowledgeBasesCreateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> KnowledgeBasesGetResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KnowledgeBasesGetResponse

        """
        _response = self._client_wrapper.httpx_client.request(
            f"knowledge-base/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    KnowledgeBasesGetResponse,
                    parse_obj_as(
                        type_=KnowledgeBasesGetResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> KnowledgeBasesDeleteResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KnowledgeBasesDeleteResponse

        """
        _response = self._client_wrapper.httpx_client.request(
            f"knowledge-base/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    KnowledgeBasesDeleteResponse,
                    parse_obj_as(
                        type_=KnowledgeBasesDeleteResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self, id: str, *, request: KnowledgeBasesUpdateRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> KnowledgeBasesUpdateResponse:
        """
        Parameters
        ----------
        id : str

        request : KnowledgeBasesUpdateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KnowledgeBasesUpdateResponse

        """
        _response = self._client_wrapper.httpx_client.request(
            f"knowledge-base/{jsonable_encoder(id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=KnowledgeBasesUpdateRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    KnowledgeBasesUpdateResponse,
                    parse_obj_as(
                        type_=KnowledgeBasesUpdateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncKnowledgeBasesClient:
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
    ) -> typing.List[KnowledgeBasesListResponseItem]:
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
        typing.List[KnowledgeBasesListResponseItem]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "knowledge-base",
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
                    typing.List[KnowledgeBasesListResponseItem],
                    parse_obj_as(
                        type_=typing.List[KnowledgeBasesListResponseItem],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self, *, request: KnowledgeBasesCreateRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> KnowledgeBasesCreateResponse:
        """
        Parameters
        ----------
        request : KnowledgeBasesCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KnowledgeBasesCreateResponse

        """
        _response = await self._client_wrapper.httpx_client.request(
            "knowledge-base",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=KnowledgeBasesCreateRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    KnowledgeBasesCreateResponse,
                    parse_obj_as(
                        type_=KnowledgeBasesCreateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> KnowledgeBasesGetResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KnowledgeBasesGetResponse

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"knowledge-base/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    KnowledgeBasesGetResponse,
                    parse_obj_as(
                        type_=KnowledgeBasesGetResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> KnowledgeBasesDeleteResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KnowledgeBasesDeleteResponse

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"knowledge-base/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    KnowledgeBasesDeleteResponse,
                    parse_obj_as(
                        type_=KnowledgeBasesDeleteResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self, id: str, *, request: KnowledgeBasesUpdateRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> KnowledgeBasesUpdateResponse:
        """
        Parameters
        ----------
        id : str

        request : KnowledgeBasesUpdateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KnowledgeBasesUpdateResponse

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"knowledge-base/{jsonable_encoder(id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=KnowledgeBasesUpdateRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    KnowledgeBasesUpdateResponse,
                    parse_obj_as(
                        type_=KnowledgeBasesUpdateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
