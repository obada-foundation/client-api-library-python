# obada_client.AccountsApi

All URIs are relative to *http://obs.node.obada.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account**](AccountsApi.md#account) | **GET** /accounts/{address} | Fetches an information about single account
[**accounts**](AccountsApi.md#accounts) | **GET** /accounts | Returns a list of OBADA accounts
[**balance**](AccountsApi.md#balance) | **GET** /accounts/my-balance | Shows account balance of OBADA address
[**export_account**](AccountsApi.md#export_account) | **POST** /accounts/export-account | Export OBADA account (private key) from client-helper
[**get_mnemonic**](AccountsApi.md#get_mnemonic) | **GET** /accounts/mnemonic | Fetching an existing mnemonic phrase
[**import_account**](AccountsApi.md#import_account) | **POST** /accounts/import-account | Imports an existing OBADA account (private key) to the client-helper user profile
[**import_wallet**](AccountsApi.md#import_wallet) | **POST** /accounts/import-wallet | Imports an existing HD wallet to the client-helper user profile
[**new_account**](AccountsApi.md#new_account) | **POST** /accounts/new-account | Creates a new OBADA account from HD wallet master key
[**new_mnemonic**](AccountsApi.md#new_mnemonic) | **GET** /accounts/new-mnemonic | Generate a new mnemonic phrase for seeding wallet
[**new_wallet**](AccountsApi.md#new_wallet) | **POST** /accounts/new-wallet | Creates profile HD wallet
[**register**](AccountsApi.md#register) | **POST** /accounts/register | Register a new client-helper user profile
[**send_coins**](AccountsApi.md#send_coins) | **POST** /accounts/{address}/send-coins | Send coins from selected account
[**update_account**](AccountsApi.md#update_account) | **POST** /accounts/{address} | Sets account specific information


# **account**
> Account account(address)

Fetches an information about single account

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import accounts_api
from obada_client.model.account import Account
from obada_client.model.internal_server_error import InternalServerError
from obada_client.model.not_authorized import NotAuthorized
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
    address = "obada1yxxnd624tgwqm3eyv5smdvjrrydfh9h943qptg" # str | OBADA address

    # example passing only required values which don't have defaults set
    try:
        # Fetches an information about single account
        api_response = api_instance.account(address)
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling AccountsApi->account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| OBADA address |

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns OBADA account |  -  |
**401** | The request is not authorized. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts**
> Accounts accounts()

Returns a list of OBADA accounts

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import accounts_api
from obada_client.model.internal_server_error import InternalServerError
from obada_client.model.not_authorized import NotAuthorized
from obada_client.model.accounts import Accounts
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
        # Returns a list of OBADA accounts
        api_response = api_instance.accounts()
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling AccountsApi->accounts: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Accounts**](Accounts.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all OBADA accounts associated with client-helper profile |  -  |
**401** | The request is not authorized. |  -  |
**422** | The submitted entity could not be processed. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **export_account**
> ExportAccountResponse export_account()

Export OBADA account (private key) from client-helper

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import accounts_api
from obada_client.model.wallet_exists_error import WalletExistsError
from obada_client.model.internal_server_error import InternalServerError
from obada_client.model.export_account_response import ExportAccountResponse
from obada_client.model.not_authorized import NotAuthorized
from obada_client.model.export_account_request import ExportAccountRequest
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
    export_account_request = ExportAccountRequest(
        address="address_example",
        passphrase="passphrase_example",
    ) # ExportAccountRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export OBADA account (private key) from client-helper
        api_response = api_instance.export_account(export_account_request=export_account_request)
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling AccountsApi->export_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_account_request** | [**ExportAccountRequest**](ExportAccountRequest.md)|  | [optional]

### Return type

[**ExportAccountResponse**](ExportAccountResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Single OBADA account (private key) encrypted with password |  -  |
**401** | The request is not authorized. |  -  |
**409** |  |  -  |
**422** | The submitted entity could not be processed. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mnemonic**
> NewMnemonic get_mnemonic()

Fetching an existing mnemonic phrase

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import accounts_api
from obada_client.model.new_mnemonic import NewMnemonic
from obada_client.model.internal_server_error import InternalServerError
from obada_client.model.not_authorized import NotAuthorized
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
        # Fetching an existing mnemonic phrase
        api_response = api_instance.get_mnemonic()
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling AccountsApi->get_mnemonic: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**NewMnemonic**](NewMnemonic.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New mnemonic phrase for wallet seeding |  -  |
**401** | The request is not authorized. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_account**
> import_account()

Imports an existing OBADA account (private key) to the client-helper user profile

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import accounts_api
from obada_client.model.wallet_exists_error import WalletExistsError
from obada_client.model.internal_server_error import InternalServerError
from obada_client.model.not_authorized import NotAuthorized
from obada_client.model.import_account_request import ImportAccountRequest
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
    import_account_request = ImportAccountRequest(
        private_key="private_key_example",
        account_name="My test account",
    ) # ImportAccountRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Imports an existing OBADA account (private key) to the client-helper user profile
        api_instance.import_account(import_account_request=import_account_request)
    except obada_client.ApiException as e:
        print("Exception when calling AccountsApi->import_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_account_request** | [**ImportAccountRequest**](ImportAccountRequest.md)|  | [optional]

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
**201** | Account was imported |  -  |
**401** | The request is not authorized. |  -  |
**409** |  |  -  |
**422** | The submitted entity could not be processed. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_wallet**
> import_wallet()

Imports an existing HD wallet to the client-helper user profile

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import accounts_api
from obada_client.model.mnemonic_request import MnemonicRequest
from obada_client.model.wallet_exists_error import WalletExistsError
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
    mnemonic_request = MnemonicRequest(
        mnemonic="fantasy route flavor zoo laptop rent knife stick fancy flame black fan oval stairs express identify crane truly anxiety wave notable gather toe tag",
        force=False,
    ) # MnemonicRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Imports an existing HD wallet to the client-helper user profile
        api_instance.import_wallet(mnemonic_request=mnemonic_request)
    except obada_client.ApiException as e:
        print("Exception when calling AccountsApi->import_wallet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mnemonic_request** | [**MnemonicRequest**](MnemonicRequest.md)|  | [optional]

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
**201** | HD wallet was imported |  -  |
**401** | The request is not authorized. |  -  |
**409** |  |  -  |
**422** | The submitted entity could not be processed. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_account**
> new_account()

Creates a new OBADA account from HD wallet master key

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import accounts_api
from obada_client.model.account_request import AccountRequest
from obada_client.model.internal_server_error import InternalServerError
from obada_client.model.not_authorized import NotAuthorized
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
    account_request = AccountRequest(
        account_name="My test account",
    ) # AccountRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a new OBADA account from HD wallet master key
        api_instance.new_account(account_request=account_request)
    except obada_client.ApiException as e:
        print("Exception when calling AccountsApi->new_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_request** | [**AccountRequest**](AccountRequest.md)|  | [optional]

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
**201** | Account was created |  -  |
**401** | The request is not authorized. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_mnemonic**
> NewMnemonic new_mnemonic()

Generate a new mnemonic phrase for seeding wallet

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import accounts_api
from obada_client.model.new_mnemonic import NewMnemonic
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
        # Generate a new mnemonic phrase for seeding wallet
        api_response = api_instance.new_mnemonic()
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling AccountsApi->new_mnemonic: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**NewMnemonic**](NewMnemonic.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New mnemonic phrase for wallet seeding |  -  |
**401** | The request is not authorized. |  -  |
**422** | The submitted entity could not be processed. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_wallet**
> new_wallet()

Creates profile HD wallet

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import accounts_api
from obada_client.model.mnemonic_request import MnemonicRequest
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
    mnemonic_request = MnemonicRequest(
        mnemonic="fantasy route flavor zoo laptop rent knife stick fancy flame black fan oval stairs express identify crane truly anxiety wave notable gather toe tag",
        force=False,
    ) # MnemonicRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates profile HD wallet
        api_instance.new_wallet(mnemonic_request=mnemonic_request)
    except obada_client.ApiException as e:
        print("Exception when calling AccountsApi->new_wallet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mnemonic_request** | [**MnemonicRequest**](MnemonicRequest.md)|  | [optional]

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
**201** | HD wallet was created |  -  |
**401** | The request is not authorized. |  -  |
**422** | The submitted entity could not be processed. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register**
> Profile register()

Register a new client-helper user profile

Creates a new profile, using JWT uid as a internal user id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import accounts_api
from obada_client.model.register_request import RegisterRequest
from obada_client.model.internal_server_error import InternalServerError
from obada_client.model.not_authorized import NotAuthorized
from obada_client.model.unprocessable_entity import UnprocessableEntity
from obada_client.model.profile import Profile
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
    register_request = RegisterRequest(
        email="john.doe@obada.io",
    ) # RegisterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Register a new client-helper user profile
        api_response = api_instance.register(register_request=register_request)
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling AccountsApi->register: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_request** | [**RegisterRequest**](RegisterRequest.md)|  | [optional]

### Return type

[**Profile**](Profile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created profile response |  -  |
**401** | The request is not authorized. |  -  |
**422** | The submitted entity could not be processed. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_coins**
> send_coins(address)

Send coins from selected account

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import accounts_api
from obada_client.model.internal_server_error import InternalServerError
from obada_client.model.not_authorized import NotAuthorized
from obada_client.model.send_coins_request import SendCoinsRequest
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
    address = "obada1yxxnd624tgwqm3eyv5smdvjrrydfh9h943qptg" # str | OBADA address
    send_coins_request = SendCoinsRequest(
        recepient_address="recepient_address_example",
        amount="amount_example",
        denom="denom_example",
    ) # SendCoinsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send coins from selected account
        api_instance.send_coins(address)
    except obada_client.ApiException as e:
        print("Exception when calling AccountsApi->send_coins: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send coins from selected account
        api_instance.send_coins(address, send_coins_request=send_coins_request)
    except obada_client.ApiException as e:
        print("Exception when calling AccountsApi->send_coins: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| OBADA address |
 **send_coins_request** | [**SendCoinsRequest**](SendCoinsRequest.md)|  | [optional]

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
**201** | Coins were sent |  -  |
**401** | The request is not authorized. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account**
> update_account(address)

Sets account specific information

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import obada_client
from obada_client.api import accounts_api
from obada_client.model.account_request import AccountRequest
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
    address = "obada1yxxnd624tgwqm3eyv5smdvjrrydfh9h943qptg" # str | OBADA address
    account_request = AccountRequest(
        account_name="My test account",
    ) # AccountRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Sets account specific information
        api_instance.update_account(address)
    except obada_client.ApiException as e:
        print("Exception when calling AccountsApi->update_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sets account specific information
        api_instance.update_account(address, account_request=account_request)
    except obada_client.ApiException as e:
        print("Exception when calling AccountsApi->update_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| OBADA address |
 **account_request** | [**AccountRequest**](AccountRequest.md)|  | [optional]

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
**201** | Account was updated |  -  |
**422** | The submitted entity could not be processed. |  -  |
**401** | The request is not authorized. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

