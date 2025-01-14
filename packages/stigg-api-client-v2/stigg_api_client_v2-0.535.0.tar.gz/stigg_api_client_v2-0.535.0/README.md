# stigg-api-client-v2 (BETA)

This library provides a Python wrapper to [Stigg's GraphQL API](https://docs.stigg.io/docs/graphql-api) based on 
the operations that are in use by the [Stigg's Node.js SDK](https://docs.stigg.io/docs/nodejs-sdk).

The [ariadne-codegen](https://github.com/mirumee/ariadne-codegen) code generator is used to generate a typesafe Python API client.

## Documentation

TBD

## Installation

    pip install stigg-api-client-v2

## Usage

Initialize the client:

```python

import os
from stigg import Stigg

api_key = os.environ.get("STIGG_SERVER_API_KEY")

client = Stigg.create_async_client(api_key)

```

Provision a customer

```python



import os
from stigg import Stigg
from stigg.generated import ProvisionCustomerInput

api_key = os.environ.get("STIGG_SERVER_API_KEY")

client = Stigg.create_async_client(api_key)

customer_input = ProvisionCustomerInput(
    **{
        "customer_id": "1661115567186116608", # mandatory, everything else is optional
        "name": "Acme",
        "email": "billing@acme.com",
        "additional_meta_data": {"key": "value"},
        "subscription_params": {"plan_id": "plan-acme-free"},
    }
)
result = await client.provision_customer(customer_input)

print(result.provision_customer.customer)

```

Get a customer by ID

```python

import os
from stigg import Stigg
from stigg.generated import GetCustomerByRefIdInput

api_key = os.environ.get("STIGG_SERVER_API_KEY")

client = Stigg.create_async_client(api_key)

result = await client.get_customer_by_id(GetCustomerByRefIdInput(**{"customer_id": "1661115567186116608"}))

print(result.get_customer_by_ref_id.name)

```
