# obada_client.UtilsApi

All URIs are relative to *http://obs.node.obada.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_checksum**](UtilsApi.md#generate_checksum) | **POST** /obit/checksum | Generates Obit checksum
[**generate_did**](UtilsApi.md#generate_did) | **POST** /obit/did | Generate Obit DID


# **generate_checksum**
> GenerateObitChecksumResponse generate_checksum()

Generates Obit checksum

Generates Obit checksum and provides a log of generation details

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import utils_api
from obada_client.model.generate_obit_checksum_request import GenerateObitChecksumRequest
from obada_client.model.internal_server_error import InternalServerError
from obada_client.model.generate_obit_checksum_response import GenerateObitChecksumResponse
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
    api_instance = utils_api.UtilsApi(api_client)
    generate_obit_checksum_request = GenerateObitChecksumRequest(
        manufacturer="Apple",
        part_number="PN123456789",
        serial_number="SN123456789",
        metadata_uri="http://somedomain.com/metadata",
        metadata_uri_hash="eac615cf446cad706b2364f974cbd3ec90620c52575aa1902418572f5a8d1fb5",
        trust_anchor_token="eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NDc5NDEzNzksImlzcyI6ImFzY2lkaSIsInN1YiI6ImNkZDU1ZDIyLTI3NzAtNDk4Ny05YTI3LTNlNDg1ZDIzMjg1NCIsInZlcmlmeVVybCI6Imh0dHBzOi8vd3d3LmFzY2RpLmNvbS9hcGkvdjEvdmVyaWZ5In0.yEHMUUuJKFZYe04afAsPWEoX35ATb6JQj9aspY_yiY2W3HZKoKHq6rcUV02OL3hptZmByeC02yL-mkczbLLlCQ",
    ) # GenerateObitChecksumRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generates Obit checksum
        api_response = api_instance.generate_checksum(generate_obit_checksum_request=generate_obit_checksum_request)
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling UtilsApi->generate_checksum: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_obit_checksum_request** | [**GenerateObitChecksumRequest**](GenerateObitChecksumRequest.md)|  | [optional]

### Return type

[**GenerateObitChecksumResponse**](GenerateObitChecksumResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Obit checksum response |  -  |
**422** | The submitted entity could not be processed. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_did**
> GenerateObitDIDResponse generate_did()

Generate Obit DID

Returns the Obit DID for a given device_id, part_number and serial_number input.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import utils_api
from obada_client.model.internal_server_error import InternalServerError
from obada_client.model.generate_obit_did_request import GenerateObitDIDRequest
from obada_client.model.generate_obit_did_response import GenerateObitDIDResponse
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
    api_instance = utils_api.UtilsApi(api_client)
    generate_obit_did_request = GenerateObitDIDRequest(
        manufacturer="Apple",
        part_number="PN123456789",
        serial_number="SN123456789",
    ) # GenerateObitDIDRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate Obit DID
        api_response = api_instance.generate_did(generate_obit_did_request=generate_obit_did_request)
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling UtilsApi->generate_did: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_obit_did_request** | [**GenerateObitDIDRequest**](GenerateObitDIDRequest.md)|  | [optional]

### Return type

[**GenerateObitDIDResponse**](GenerateObitDIDResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Obit DID response |  -  |
**422** | The submitted entity could not be processed. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

