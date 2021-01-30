"""
    OBADA Client Helper API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: techops@obada.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.base_response import BaseResponse
from openapi_client.model.block_chain_obit_response import BlockChainObitResponse
from openapi_client.model.client_obit_response import ClientObitResponse
from openapi_client.model.local_obit import LocalObit
from openapi_client.model.obit_definition_response import ObitDefinitionResponse
from openapi_client.model.obit_did import ObitDid


class ObitApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __download_obit_from_chain(
            self,
            **kwargs
        ):
            """Download Obit from Blockchain  # noqa: E501

            Downloads the Obit information from the blockchain to the client.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.download_obit_from_chain(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                obit_did (ObitDid): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ClientObitResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.download_obit_from_chain = _Endpoint(
            settings={
                'response_type': (ClientObitResponse,),
                'auth': [],
                'endpoint_path': '/server/obit/download',
                'operation_id': 'download_obit_from_chain',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'obit_did',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'obit_did':
                        (ObitDid,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'obit_did': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__download_obit_from_chain
        )

        def __fetch_obit_from_chain(
            self,
            obit_did,
            **kwargs
        ):
            """Get Obit From Blockchain  # noqa: E501

            Retrieves Obit information from blockchain but does not download it.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.fetch_obit_from_chain(obit_did, async_req=True)
            >>> result = thread.get()

            Args:
                obit_did (str): Required.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                BlockChainObitResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['obit_did'] = \
                obit_did
            return self.call_with_http_info(**kwargs)

        self.fetch_obit_from_chain = _Endpoint(
            settings={
                'response_type': (BlockChainObitResponse,),
                'auth': [],
                'endpoint_path': '/server/obit/{obit_did}',
                'operation_id': 'fetch_obit_from_chain',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'obit_did',
                ],
                'required': [
                    'obit_did',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'obit_did':
                        (str,),
                },
                'attribute_map': {
                    'obit_did': 'obit_did',
                },
                'location_map': {
                    'obit_did': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__fetch_obit_from_chain
        )

        def __generate_obit_def(
            self,
            manufacturer,
            part_number,
            serial_number,
            **kwargs
        ):
            """Generate Obit Definition  # noqa: E501

            Returns the Obit Definition for a given device_id, part_number and serial_number input.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.generate_obit_def(manufacturer, part_number, serial_number, async_req=True)
            >>> result = thread.get()

            Args:
                manufacturer (str): Device Id (Required)
                part_number (str): Part Number (Required)
                serial_number (str): Serial Number (Required)

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ObitDefinitionResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['manufacturer'] = \
                manufacturer
            kwargs['part_number'] = \
                part_number
            kwargs['serial_number'] = \
                serial_number
            return self.call_with_http_info(**kwargs)

        self.generate_obit_def = _Endpoint(
            settings={
                'response_type': (ObitDefinitionResponse,),
                'auth': [],
                'endpoint_path': '/obit/generate',
                'operation_id': 'generate_obit_def',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'manufacturer',
                    'part_number',
                    'serial_number',
                ],
                'required': [
                    'manufacturer',
                    'part_number',
                    'serial_number',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'manufacturer':
                        (str,),
                    'part_number':
                        (str,),
                    'serial_number':
                        (str,),
                },
                'attribute_map': {
                    'manufacturer': 'manufacturer',
                    'part_number': 'part_number',
                    'serial_number': 'serial_number',
                },
                'location_map': {
                    'manufacturer': 'query',
                    'part_number': 'query',
                    'serial_number': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__generate_obit_def
        )

        def __get_client_obit(
            self,
            obit_did,
            **kwargs
        ):
            """Get Client Obit  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_client_obit(obit_did, async_req=True)
            >>> result = thread.get()

            Args:
                obit_did (str): Required.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ClientObitResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['obit_did'] = \
                obit_did
            return self.call_with_http_info(**kwargs)

        self.get_client_obit = _Endpoint(
            settings={
                'response_type': (ClientObitResponse,),
                'auth': [],
                'endpoint_path': '/client/obit/{obit_did}',
                'operation_id': 'get_client_obit',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'obit_did',
                ],
                'required': [
                    'obit_did',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'obit_did':
                        (str,),
                },
                'attribute_map': {
                    'obit_did': 'obit_did',
                },
                'location_map': {
                    'obit_did': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_client_obit
        )

        def __save_client_obit(
            self,
            **kwargs
        ):
            """Save Client Obit  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.save_client_obit(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                local_obit (LocalObit): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ClientObitResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.save_client_obit = _Endpoint(
            settings={
                'response_type': (ClientObitResponse,),
                'auth': [],
                'endpoint_path': '/client/obit',
                'operation_id': 'save_client_obit',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'local_obit',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'local_obit':
                        (LocalObit,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'local_obit': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__save_client_obit
        )

        def __upload_obit(
            self,
            **kwargs
        ):
            """Upload Obit to Blockchain  # noqa: E501

            Uploads Obit from client to the Blockchain  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.upload_obit(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                obit_did (ObitDid): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                BaseResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.upload_obit = _Endpoint(
            settings={
                'response_type': (BaseResponse,),
                'auth': [],
                'endpoint_path': '/server/obit/upload',
                'operation_id': 'upload_obit',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'obit_did',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'obit_did':
                        (ObitDid,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'obit_did': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__upload_obit
        )
