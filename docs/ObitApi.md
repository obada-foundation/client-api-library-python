# obada_client.ObitApi

All URIs are relative to *http://obs.node.obada.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](ObitApi.md#get) | **GET** /obits/{key} | Get Obit by DID or USN
[**history**](ObitApi.md#history) | **GET** /obits/{key}/history | Get Obit history by DID or USN
[**save**](ObitApi.md#save) | **POST** /obits | Save Obit
[**search**](ObitApi.md#search) | **GET** /obits | Search obits by query


# **get**
> Obit get(key)

Get Obit by DID or USN

Get a single Obit by given ObitDID or USN

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import obit_api
from obada_client.model.internal_server_error import InternalServerError
from obada_client.model.obit import Obit
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
    api_instance = obit_api.ObitApi(api_client)
    key = "did:obada:fe096095-e0f0-4918-9607-6567bd5756b5" # str | The given ObitDID or USN argument

    # example passing only required values which don't have defaults set
    try:
        # Get Obit by DID or USN
        api_response = api_instance.get(key)
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling ObitApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The given ObitDID or USN argument |

### Return type

[**Obit**](Obit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | The requested resource could not be found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **history**
> History200Response history(key)

Get Obit history by DID or USN

Shows the history of changes by given Obit with ObitDID or USN

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import obit_api
from obada_client.model.history200_response import History200Response
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
    api_instance = obit_api.ObitApi(api_client)
    key = "did:obada:fe096095-e0f0-4918-9607-6567bd5756b5" # str | The given ObitDID or USN argument

    # example passing only required values which don't have defaults set
    try:
        # Get Obit history by DID or USN
        api_response = api_instance.history(key)
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling ObitApi->history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The given ObitDID or USN argument |

### Return type

[**History200Response**](History200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collection of historical changes for given obit |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save**
> Obit save()

Save Obit

Returns Obit with updated checksum if data was changed.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import obit_api
from obada_client.model.save_obit_request import SaveObitRequest
from obada_client.model.internal_server_error import InternalServerError
from obada_client.model.obit import Obit
from obada_client.model.unprocessable_entity import UnprocessableEntity
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
    api_instance = obit_api.ObitApi(api_client)
    save_obit_request = SaveObitRequest(
        manufacturer="Sony",
        part_number="MWCN2LL/A",
        serial_number="f6fc84c9f21c24907d6bee6eec38cabab5fa9a7be8c4a7827fe9e56f245bd2d5",
        documents=[
            DeviceDocument(
                name="Link to device wipe report",
                document_file="document_file_example",
                should_encrypt=False,
            ),
        ],
    ) # SaveObitRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Save Obit
        api_response = api_instance.save(save_obit_request=save_obit_request)
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling ObitApi->save: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_obit_request** | [**SaveObitRequest**](SaveObitRequest.md)|  | [optional]

### Return type

[**Obit**](Obit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json:
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**422** | The submitted entity could not be processed. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> Obits search()

Search obits by query

Implements a fulltext search for obits by \"searchTerm\".

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import obit_api
from obada_client.model.obits import Obits
from obada_client.model.internal_server_error import InternalServerError
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
    api_instance = obit_api.ObitApi(api_client)
    q = "fe403a1afe16203f4b8bb3a0e72d3e17567897bc15293e4a87b663e441030aea" # str | Query argument that used for a fulltext search (optional)
    offset = 0 # int | Number of records to skip for pagination. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search obits by query
        api_response = api_instance.search(q=q, offset=offset)
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling ObitApi->search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Query argument that used for a fulltext search | [optional]
 **offset** | **int**| Number of records to skip for pagination. | [optional] if omitted the server will use the default value of 0

### Return type

[**Obits**](Obits.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of obits with pagination responded by given arguments. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

