# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..types.analytics_query import AnalyticsQuery
from ..core.request_options import RequestOptions
from ..types.analytics_query_result import AnalyticsQueryResult
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AnalyticsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, *, queries: typing.Sequence[AnalyticsQuery], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AnalyticsQueryResult]:
        """
        Parameters
        ----------
        queries : typing.Sequence[AnalyticsQuery]
            This is the list of metric queries you want to perform.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AnalyticsQueryResult]

        """
        _response = self._client_wrapper.httpx_client.request(
            "analytics",
            method="POST",
            json={
                "queries": convert_and_respect_annotation_metadata(
                    object_=queries, annotation=typing.Sequence[AnalyticsQuery], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[AnalyticsQueryResult],
                    construct_type(
                        type_=typing.List[AnalyticsQueryResult],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAnalyticsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, *, queries: typing.Sequence[AnalyticsQuery], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AnalyticsQueryResult]:
        """
        Parameters
        ----------
        queries : typing.Sequence[AnalyticsQuery]
            This is the list of metric queries you want to perform.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AnalyticsQueryResult]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "analytics",
            method="POST",
            json={
                "queries": convert_and_respect_annotation_metadata(
                    object_=queries, annotation=typing.Sequence[AnalyticsQuery], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[AnalyticsQueryResult],
                    construct_type(
                        type_=typing.List[AnalyticsQueryResult],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
