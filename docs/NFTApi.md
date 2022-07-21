# obada_client.NFTApi

All URIs are relative to *http://obs.node.obada.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mint**](NFTApi.md#mint) | **POST** /nft/{key}/mint | Mints NFT
[**nft**](NFTApi.md#nft) | **GET** /nft/{key} | Fetch NFT from OBADA blockchain Node
[**send**](NFTApi.md#send) | **POST** /nft/{key}/send | Send NFT to another address
[**update_metadata**](NFTApi.md#update_metadata) | **POST** /nft/{key}/metadata | Update NFT metadata


# **mint**
> mint(key)

Mints NFT

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import nft_api
from obada_client.model.internal_server_error import InternalServerError
from obada_client.model.not_found import NotFound
from pprint import pprint
# Defining the host is optional and defaults to http://obs.node.obada.io
# See configuration.py for a list of all supported configuration parameters.
configuration = obada_client.Configuration(
    host = "http://obs.node.obada.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = obada_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with obada_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nft_api.NFTApi(api_client)
    key = "did:obada:fe096095-e0f0-4918-9607-6567bd5756b5" # str | The given ObitDID or USN argument

    # example passing only required values which don't have defaults set
    try:
        # Mints NFT
        api_instance.mint(key)
    except obada_client.ApiException as e:
        print("Exception when calling NFTApi->mint: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The given ObitDID or USN argument |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Succesfully minted |  -  |
**404** | The requested resource could not be found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nft**
> NFT nft(key)

Fetch NFT from OBADA blockchain Node

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import nft_api
from obada_client.model.internal_server_error import InternalServerError
from obada_client.model.nft import NFT
from obada_client.model.not_found import NotFound
from pprint import pprint
# Defining the host is optional and defaults to http://obs.node.obada.io
# See configuration.py for a list of all supported configuration parameters.
configuration = obada_client.Configuration(
    host = "http://obs.node.obada.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = obada_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with obada_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nft_api.NFTApi(api_client)
    key = "did:obada:fe096095-e0f0-4918-9607-6567bd5756b5" # str | The given ObitDID or USN argument

    # example passing only required values which don't have defaults set
    try:
        # Fetch NFT from OBADA blockchain Node
        api_response = api_instance.nft(key)
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling NFTApi->nft: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The given ObitDID or USN argument |

### Return type

[**NFT**](NFT.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NFT hosted by blockchain |  -  |
**404** | The requested resource could not be found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send**
> send(key)

Send NFT to another address

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import nft_api
from obada_client.model.internal_server_error import InternalServerError
from obada_client.model.send_nft_request import SendNFTRequest
from obada_client.model.not_found import NotFound
from pprint import pprint
# Defining the host is optional and defaults to http://obs.node.obada.io
# See configuration.py for a list of all supported configuration parameters.
configuration = obada_client.Configuration(
    host = "http://obs.node.obada.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = obada_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with obada_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nft_api.NFTApi(api_client)
    key = "did:obada:fe096095-e0f0-4918-9607-6567bd5756b5" # str | The given ObitDID or USN argument
    send_nft_request = SendNFTRequest(
        receiver="receiver_example",
    ) # SendNFTRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send NFT to another address
        api_instance.send(key)
    except obada_client.ApiException as e:
        print("Exception when calling NFTApi->send: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send NFT to another address
        api_instance.send(key, send_nft_request=send_nft_request)
    except obada_client.ApiException as e:
        print("Exception when calling NFTApi->send: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The given ObitDID or USN argument |
 **send_nft_request** | [**SendNFTRequest**](SendNFTRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Succesfully transfered |  -  |
**404** | The requested resource could not be found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata**
> update_metadata(key)

Update NFT metadata

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import nft_api
from obada_client.model.internal_server_error import InternalServerError
from obada_client.model.not_found import NotFound
from pprint import pprint
# Defining the host is optional and defaults to http://obs.node.obada.io
# See configuration.py for a list of all supported configuration parameters.
configuration = obada_client.Configuration(
    host = "http://obs.node.obada.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = obada_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with obada_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nft_api.NFTApi(api_client)
    key = "did:obada:fe096095-e0f0-4918-9607-6567bd5756b5" # str | The given ObitDID or USN argument

    # example passing only required values which don't have defaults set
    try:
        # Update NFT metadata
        api_instance.update_metadata(key)
    except obada_client.ApiException as e:
        print("Exception when calling NFTApi->update_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The given ObitDID or USN argument |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata succesfully updated |  -  |
**404** | The requested resource could not be found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

