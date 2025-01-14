# coding: utf-8

"""
    Empire - Platform API

    OpenAPI specification for the Platform REST API of Empire  **System Time:** Europe/Amsterdam  **General data formats:**   * _capacity values_ => kW (integers)   * _dates and local times_ => System Time   * _currencies_ => EUR   # noqa: E501

    The version of the OpenAPI document: 0.176.9
    Contact: britned.info@britned.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from datetime import datetime

from pydantic import Field, StrictStr, conint, conlist

from typing import List, Optional

from empire_platform_api_public_client.models.aggregated_allocated_auction import AggregatedAllocatedAuction
from empire_platform_api_public_client.models.allocated_auction_batch import AllocatedAuctionBatch
from empire_platform_api_public_client.models.allocated_auction_sort_by import AllocatedAuctionSortBy
from empire_platform_api_public_client.models.auction_product_type import AuctionProductType
from empire_platform_api_public_client.models.auction_timescale import AuctionTimescale
from empire_platform_api_public_client.models.border_direction import BorderDirection

from empire_platform_api_public_client.api_client import ApiClient
from empire_platform_api_public_client.api_response import ApiResponse
from empire_platform_api_public_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PublicAllocatedAuctionApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_public_aggregated_allocated_auctions(self, border_direction : Optional[BorderDirection] = None, timescale : Optional[AuctionTimescale] = None, product_types : Optional[conlist(AuctionProductType)] = None, delivery_period_start : Optional[datetime] = None, delivery_period_end : Optional[datetime] = None, **kwargs) -> List[AggregatedAllocatedAuction]:  # noqa: E501
        """get_public_aggregated_allocated_auctions  # noqa: E501

        Fetch a filterable list of Aggregated Allocated Auctions   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_public_aggregated_allocated_auctions(border_direction, timescale, product_types, delivery_period_start, delivery_period_end, async_req=True)
        >>> result = thread.get()

        :param border_direction:
        :type border_direction: BorderDirection
        :param timescale:
        :type timescale: AuctionTimescale
        :param product_types:
        :type product_types: List[AuctionProductType]
        :param delivery_period_start:
        :type delivery_period_start: datetime
        :param delivery_period_end:
        :type delivery_period_end: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[AggregatedAllocatedAuction]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_public_aggregated_allocated_auctions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_public_aggregated_allocated_auctions_with_http_info(border_direction, timescale, product_types, delivery_period_start, delivery_period_end, **kwargs)  # noqa: E501

    @validate_arguments
    def get_public_aggregated_allocated_auctions_with_http_info(self, border_direction : Optional[BorderDirection] = None, timescale : Optional[AuctionTimescale] = None, product_types : Optional[conlist(AuctionProductType)] = None, delivery_period_start : Optional[datetime] = None, delivery_period_end : Optional[datetime] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_public_aggregated_allocated_auctions  # noqa: E501

        Fetch a filterable list of Aggregated Allocated Auctions   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_public_aggregated_allocated_auctions_with_http_info(border_direction, timescale, product_types, delivery_period_start, delivery_period_end, async_req=True)
        >>> result = thread.get()

        :param border_direction:
        :type border_direction: BorderDirection
        :param timescale:
        :type timescale: AuctionTimescale
        :param product_types:
        :type product_types: List[AuctionProductType]
        :param delivery_period_start:
        :type delivery_period_start: datetime
        :param delivery_period_end:
        :type delivery_period_end: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[AggregatedAllocatedAuction], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'border_direction',
            'timescale',
            'product_types',
            'delivery_period_start',
            'delivery_period_end'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_public_aggregated_allocated_auctions" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('border_direction') is not None:  # noqa: E501
            _query_params.append(('borderDirection', _params['border_direction'].value))

        if _params.get('timescale') is not None:  # noqa: E501
            _query_params.append(('timescale', _params['timescale'].value))

        if _params.get('product_types') is not None:  # noqa: E501
            _query_params.append(('productTypes', _params['product_types']))
            _collection_formats['productTypes'] = 'multi'

        if _params.get('delivery_period_start') is not None:  # noqa: E501
            if isinstance(_params['delivery_period_start'], datetime):
                _query_params.append(('deliveryPeriodStart', _params['delivery_period_start'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('deliveryPeriodStart', _params['delivery_period_start']))

        if _params.get('delivery_period_end') is not None:  # noqa: E501
            if isinstance(_params['delivery_period_end'], datetime):
                _query_params.append(('deliveryPeriodEnd', _params['delivery_period_end'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('deliveryPeriodEnd', _params['delivery_period_end']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "List[AggregatedAllocatedAuction]",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '422': "ErrorResponse",
        }

        return self.api_client.call_api(
            '/v1/public/allocated-auctions/aggregated', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_public_allocated_auctions(self, limit : Annotated[conint(strict=True, le=100, ge=1), Field(..., description="Number of records to return on a page")], offset : Annotated[conint(strict=True, ge=0), Field(..., description="Offset in the list of records to return")], sort_by : AllocatedAuctionSortBy, border_direction : Optional[BorderDirection] = None, timescale : Optional[AuctionTimescale] = None, product_types : Optional[conlist(AuctionProductType)] = None, delivery_period_start : Optional[datetime] = None, delivery_period_end : Optional[datetime] = None, query : Optional[StrictStr] = None, **kwargs) -> AllocatedAuctionBatch:  # noqa: E501
        """get_public_allocated_auctions  # noqa: E501

        Fetch a paginated, sortable, filterable list of Allocated Auctions   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_public_allocated_auctions(limit, offset, sort_by, border_direction, timescale, product_types, delivery_period_start, delivery_period_end, query, async_req=True)
        >>> result = thread.get()

        :param limit: Number of records to return on a page (required)
        :type limit: int
        :param offset: Offset in the list of records to return (required)
        :type offset: int
        :param sort_by: (required)
        :type sort_by: AllocatedAuctionSortBy
        :param border_direction:
        :type border_direction: BorderDirection
        :param timescale:
        :type timescale: AuctionTimescale
        :param product_types:
        :type product_types: List[AuctionProductType]
        :param delivery_period_start:
        :type delivery_period_start: datetime
        :param delivery_period_end:
        :type delivery_period_end: datetime
        :param query:
        :type query: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AllocatedAuctionBatch
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_public_allocated_auctions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_public_allocated_auctions_with_http_info(limit, offset, sort_by, border_direction, timescale, product_types, delivery_period_start, delivery_period_end, query, **kwargs)  # noqa: E501

    @validate_arguments
    def get_public_allocated_auctions_with_http_info(self, limit : Annotated[conint(strict=True, le=100, ge=1), Field(..., description="Number of records to return on a page")], offset : Annotated[conint(strict=True, ge=0), Field(..., description="Offset in the list of records to return")], sort_by : AllocatedAuctionSortBy, border_direction : Optional[BorderDirection] = None, timescale : Optional[AuctionTimescale] = None, product_types : Optional[conlist(AuctionProductType)] = None, delivery_period_start : Optional[datetime] = None, delivery_period_end : Optional[datetime] = None, query : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_public_allocated_auctions  # noqa: E501

        Fetch a paginated, sortable, filterable list of Allocated Auctions   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_public_allocated_auctions_with_http_info(limit, offset, sort_by, border_direction, timescale, product_types, delivery_period_start, delivery_period_end, query, async_req=True)
        >>> result = thread.get()

        :param limit: Number of records to return on a page (required)
        :type limit: int
        :param offset: Offset in the list of records to return (required)
        :type offset: int
        :param sort_by: (required)
        :type sort_by: AllocatedAuctionSortBy
        :param border_direction:
        :type border_direction: BorderDirection
        :param timescale:
        :type timescale: AuctionTimescale
        :param product_types:
        :type product_types: List[AuctionProductType]
        :param delivery_period_start:
        :type delivery_period_start: datetime
        :param delivery_period_end:
        :type delivery_period_end: datetime
        :param query:
        :type query: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AllocatedAuctionBatch, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'limit',
            'offset',
            'sort_by',
            'border_direction',
            'timescale',
            'product_types',
            'delivery_period_start',
            'delivery_period_end',
            'query'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_public_allocated_auctions" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        if _params.get('sort_by') is not None:  # noqa: E501
            _query_params.append(('sortBy', _params['sort_by'].value))

        if _params.get('border_direction') is not None:  # noqa: E501
            _query_params.append(('borderDirection', _params['border_direction'].value))

        if _params.get('timescale') is not None:  # noqa: E501
            _query_params.append(('timescale', _params['timescale'].value))

        if _params.get('product_types') is not None:  # noqa: E501
            _query_params.append(('productTypes', _params['product_types']))
            _collection_formats['productTypes'] = 'multi'

        if _params.get('delivery_period_start') is not None:  # noqa: E501
            if isinstance(_params['delivery_period_start'], datetime):
                _query_params.append(('deliveryPeriodStart', _params['delivery_period_start'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('deliveryPeriodStart', _params['delivery_period_start']))

        if _params.get('delivery_period_end') is not None:  # noqa: E501
            if isinstance(_params['delivery_period_end'], datetime):
                _query_params.append(('deliveryPeriodEnd', _params['delivery_period_end'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('deliveryPeriodEnd', _params['delivery_period_end']))

        if _params.get('query') is not None:  # noqa: E501
            _query_params.append(('query', _params['query']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "AllocatedAuctionBatch",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '422': "ErrorResponse",
        }

        return self.api_client.call_api(
            '/v1/public/allocated-auctions', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
