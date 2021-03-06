# obada-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.obada.io](https://www.obada.io)

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/obada-foundation/client-api-library-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/obada-foundation/client-api-library-python.git`)

Then import the package:
```python
import obada_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import obada_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import obada_client
from pprint import pprint
from obada_client.api import obit_api
from obada_client.model.base_response import BaseResponse
from obada_client.model.block_chain_obit_response import BlockChainObitResponse
from obada_client.model.client_obit_response import ClientObitResponse
from obada_client.model.local_obit import LocalObit
from obada_client.model.obit_definition_response import ObitDefinitionResponse
from obada_client.model.obit_did import ObitDid
from obada_client.model.root_hash_response import RootHashResponse
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = obada_client.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with obada_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = obit_api.ObitApi(api_client)
    obit_did = ObitDid(
        obit_did="did:obada:fe096095-e0f0-4918-9607-6567bd5756b5",
    ) # ObitDid |  (optional)

    try:
        # Download Obit from Blockchain
        api_response = api_instance.download_obit_from_chain(obit_did=obit_did)
        pprint(api_response)
    except obada_client.ApiException as e:
        print("Exception when calling ObitApi->download_obit_from_chain: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ObitApi* | [**download_obit_from_chain**](docs/ObitApi.md#download_obit_from_chain) | **POST** /api/server/obit/download | Download Obit from Blockchain
*ObitApi* | [**fetch_obit_from_chain**](docs/ObitApi.md#fetch_obit_from_chain) | **GET** /api/server/obit/{obit_did} | Get Obit From Blockchain
*ObitApi* | [**generate_obit_def**](docs/ObitApi.md#generate_obit_def) | **GET** /api/obit/definition | Generate Obit Definition
*ObitApi* | [**generate_root_hash**](docs/ObitApi.md#generate_root_hash) | **POST** /api/obit/hash | Generates The Root Hash using the data provided.
*ObitApi* | [**get_client_obit**](docs/ObitApi.md#get_client_obit) | **GET** /api/client/obit/{obit_did} | Get Client Obit
*ObitApi* | [**save_client_obit**](docs/ObitApi.md#save_client_obit) | **POST** /api/client/obit | Save Client Obit
*ObitApi* | [**upload_obit**](docs/ObitApi.md#upload_obit) | **POST** /api/server/obit/upload | Upload Obit to Blockchain


## Documentation For Models

 - [BaseResponse](docs/BaseResponse.md)
 - [BlockChainObit](docs/BlockChainObit.md)
 - [BlockChainObitResponse](docs/BlockChainObitResponse.md)
 - [ClientObit](docs/ClientObit.md)
 - [ClientObitResponse](docs/ClientObitResponse.md)
 - [LocalObit](docs/LocalObit.md)
 - [LocalObitDocuments](docs/LocalObitDocuments.md)
 - [LocalObitMetadata](docs/LocalObitMetadata.md)
 - [LocalObitStructuredData](docs/LocalObitStructuredData.md)
 - [ObitDefinition](docs/ObitDefinition.md)
 - [ObitDefinitionResponse](docs/ObitDefinitionResponse.md)
 - [ObitDid](docs/ObitDid.md)
 - [RootHashResponse](docs/RootHashResponse.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author

techops@obada.io


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in obada_client.apis and obada_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from obada_client.api.default_api import DefaultApi`
- `from obada_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import obada_client
from obada_client.apis import *
from obada_client.models import *
```

