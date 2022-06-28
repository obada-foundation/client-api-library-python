# obada_client.AccountsApi

All URIs are relative to *http://obs.node.obada.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balance**](AccountsApi.md#balance) | **GET** /accounts/my-balance | Shows account balance of OBADA address
[**create_account**](AccountsApi.md#create_account) | **POST** /accounts | Creates a new Account


# **balance**
> AccountBalance balance()

Shows account balance of OBADA address

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import accounts_api
from obada_client.model.account_balance import AccountBalance
from obada_client.model.internal_server_error import InternalServerError
from obada_client.model.not_authorized import NotAuthorized
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
    api_instance = accounts_api.AccountsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Shows account balance of OBADA address
        api_response = api_instance.balance()
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling AccountsApi->balance: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountBalance**](AccountBalance.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account balance response |  -  |
**401** | The request is not authorized. |  -  |
**422** | The submitted entity could not be processed. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account**
> Account create_account()

Creates a new Account

Creates a new account, using JWT uid as a internal user id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import accounts_api
from obada_client.model.account import Account
from obada_client.model.internal_server_error import InternalServerError
from obada_client.model.not_authorized import NotAuthorized
from obada_client.model.unprocessable_entity import UnprocessableEntity
from obada_client.model.new_account_request import NewAccountRequest
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
    api_instance = accounts_api.AccountsApi(api_client)
    new_account_request = NewAccountRequest(
        email="john.doe@obada.io",
    ) # NewAccountRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a new Account
        api_response = api_instance.create_account(new_account_request=new_account_request)
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling AccountsApi->create_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_account_request** | [**NewAccountRequest**](NewAccountRequest.md)|  | [optional]

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create new Account response |  -  |
**401** | The request is not authorized. |  -  |
**422** | The submitted entity could not be processed. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

