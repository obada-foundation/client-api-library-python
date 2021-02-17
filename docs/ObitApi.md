# obada_client.ObitApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_obit_from_chain**](ObitApi.md#download_obit_from_chain) | **POST** /api/server/obit/download | Download Obit from Blockchain
[**fetch_obit_from_chain**](ObitApi.md#fetch_obit_from_chain) | **GET** /api/server/obit/{obit_did} | Get Obit From Blockchain
[**generate_obit_def**](ObitApi.md#generate_obit_def) | **GET** /api/obit/definition | Generate Obit Definition
[**generate_root_hash**](ObitApi.md#generate_root_hash) | **POST** /api/obit/hash | Generates The Root Hash using the data provided.
[**get_client_obit**](ObitApi.md#get_client_obit) | **GET** /api/client/obit/{obit_did} | Get Client Obit
[**save_client_obit**](ObitApi.md#save_client_obit) | **POST** /api/client/obit | Save Client Obit
[**upload_obit**](ObitApi.md#upload_obit) | **POST** /api/server/obit/upload | Upload Obit to Blockchain


# **download_obit_from_chain**
> ClientObitResponse download_obit_from_chain()

Download Obit from Blockchain

Downloads the Obit information from the blockchain to the client.

### Example

```python
import time
import obada_client
from obada_client.api import obit_api
from obada_client.model.client_obit_response import ClientObitResponse
from obada_client.model.obit_did import ObitDid
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = obada_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with obada_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = obit_api.ObitApi(api_client)
    obit_did = ObitDid(
        obit_did="did:obada:fe096095-e0f0-4918-9607-6567bd5756b5",
    ) # ObitDid |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Download Obit from Blockchain
        api_response = api_instance.download_obit_from_chain(obit_did=obit_did)
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling ObitApi->download_obit_from_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obit_did** | [**ObitDid**](ObitDid.md)|  | [optional]

### Return type

[**ClientObitResponse**](ClientObitResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the client obit downloaded from blockchain |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_obit_from_chain**
> BlockChainObitResponse fetch_obit_from_chain(obit_did)

Get Obit From Blockchain

Retrieves Obit information from blockchain but does not download it.

### Example

```python
import time
import obada_client
from obada_client.api import obit_api
from obada_client.model.block_chain_obit_response import BlockChainObitResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = obada_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with obada_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = obit_api.ObitApi(api_client)
    obit_did = "did:obada:81413bc1ad2074a6ae35d1f65f64f1bca2e8a20959f37ef0349a729ddc567d9b" # str | Required.

    # example passing only required values which don't have defaults set
    try:
        # Get Obit From Blockchain
        api_response = api_instance.fetch_obit_from_chain(obit_did)
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling ObitApi->fetch_obit_from_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obit_did** | **str**| Required. |

### Return type

[**BlockChainObitResponse**](BlockChainObitResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array with ObitDID and USN Information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_obit_def**
> ObitDefinitionResponse generate_obit_def(manufacturer, part_number, serial_number)

Generate Obit Definition

Returns the Obit Definition for a given device_id, part_number and serial_number input.

### Example

```python
import time
import obada_client
from obada_client.api import obit_api
from obada_client.model.obit_definition_response import ObitDefinitionResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = obada_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with obada_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = obit_api.ObitApi(api_client)
    manufacturer = "Apple" # str | Device Id (Required)
    part_number = "123456789" # str | Part Number (Required)
    serial_number = "123456789" # str | Serial Number (Required)

    # example passing only required values which don't have defaults set
    try:
        # Generate Obit Definition
        api_response = api_instance.generate_obit_def(manufacturer, part_number, serial_number)
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling ObitApi->generate_obit_def: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manufacturer** | **str**| Device Id (Required) |
 **part_number** | **str**| Part Number (Required) |
 **serial_number** | **str**| Serial Number (Required) |

### Return type

[**ObitDefinitionResponse**](ObitDefinitionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the Obit Definition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_root_hash**
> RootHashResponse generate_root_hash()

Generates The Root Hash using the data provided.

### Example

```python
import time
import obada_client
from obada_client.api import obit_api
from obada_client.model.local_obit import LocalObit
from obada_client.model.root_hash_response import RootHashResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = obada_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with obada_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = obit_api.ObitApi(api_client)
    local_obit = LocalObit(
        owner="Tradeloop",
        obit_status="FUNCTIONAL",
        manufacturer="Sony",
        part_number="MWCN2LL/A",
        serial_number_hash="f6fc84c9f21c24907d6bee6eec38cabab5fa9a7be8c4a7827fe9e56f245bd2d5",
        metadata=[
            LocalObitMetadata(
                key="model",
                value="Dell R740",
            ),
        ],
        documents=[
            LocalObitDocuments(
                name="Link to device wipe report",
                hashlink="Link to device wipe report",
            ),
        ],
        structured_data=[
            LocalObitStructuredData(
                key="model",
                value="{"somekey":"somevalue"}",
            ),
        ],
        modified_at=dateutil_parser('2020-01-01T13:24:35Z'),
    ) # LocalObit |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generates The Root Hash using the data provided.
        api_response = api_instance.generate_root_hash(local_obit=local_obit)
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling ObitApi->generate_root_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local_obit** | [**LocalObit**](LocalObit.md)|  | [optional]

### Return type

[**RootHashResponse**](RootHashResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the root hash |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_obit**
> ClientObitResponse get_client_obit(obit_did)

Get Client Obit

### Example

```python
import time
import obada_client
from obada_client.api import obit_api
from obada_client.model.client_obit_response import ClientObitResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = obada_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with obada_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = obit_api.ObitApi(api_client)
    obit_did = "did:obada:81413bc1ad2074a6ae35d1f65f64f1bca2e8a20959f37ef0349a729ddc567d9b" # str | Required.

    # example passing only required values which don't have defaults set
    try:
        # Get Client Obit
        api_response = api_instance.get_client_obit(obit_did)
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling ObitApi->get_client_obit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obit_did** | **str**| Required. |

### Return type

[**ClientObitResponse**](ClientObitResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the obit saved on the client |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_client_obit**
> ClientObitResponse save_client_obit()

Save Client Obit

### Example

```python
import time
import obada_client
from obada_client.api import obit_api
from obada_client.model.client_obit_response import ClientObitResponse
from obada_client.model.local_obit import LocalObit
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = obada_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with obada_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = obit_api.ObitApi(api_client)
    local_obit = LocalObit(
        owner="Tradeloop",
        obit_status="FUNCTIONAL",
        manufacturer="Sony",
        part_number="MWCN2LL/A",
        serial_number_hash="f6fc84c9f21c24907d6bee6eec38cabab5fa9a7be8c4a7827fe9e56f245bd2d5",
        metadata=[
            LocalObitMetadata(
                key="model",
                value="Dell R740",
            ),
        ],
        documents=[
            LocalObitDocuments(
                name="Link to device wipe report",
                hashlink="Link to device wipe report",
            ),
        ],
        structured_data=[
            LocalObitStructuredData(
                key="model",
                value="{"somekey":"somevalue"}",
            ),
        ],
        modified_at=dateutil_parser('2020-01-01T13:24:35Z'),
    ) # LocalObit |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Save Client Obit
        api_response = api_instance.save_client_obit(local_obit=local_obit)
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling ObitApi->save_client_obit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local_obit** | [**LocalObit**](LocalObit.md)|  | [optional]

### Return type

[**ClientObitResponse**](ClientObitResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the obit that was saved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_obit**
> BaseResponse upload_obit()

Upload Obit to Blockchain

Uploads Obit from client to the Blockchain

### Example

```python
import time
import obada_client
from obada_client.api import obit_api
from obada_client.model.obit_did import ObitDid
from obada_client.model.base_response import BaseResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = obada_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with obada_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = obit_api.ObitApi(api_client)
    obit_did = ObitDid(
        obit_did="did:obada:fe096095-e0f0-4918-9607-6567bd5756b5",
    ) # ObitDid |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload Obit to Blockchain
        api_response = api_instance.upload_obit(obit_did=obit_did)
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling ObitApi->upload_obit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obit_did** | [**ObitDid**](ObitDid.md)|  | [optional]

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a status of the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

