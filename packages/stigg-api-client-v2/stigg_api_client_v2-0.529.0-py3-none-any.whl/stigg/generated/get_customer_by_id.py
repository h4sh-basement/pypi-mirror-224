# Generated by ariadne-codegen on 2023-08-09 07:55
# Source: operations.graphql

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .fragments import CustomerWithSubscriptionsFragment


class GetCustomerById(BaseModel):
    get_customer_by_ref_id: Optional["GetCustomerByIdGetCustomerByRefId"] = Field(
        alias="getCustomerByRefId"
    )


class GetCustomerByIdGetCustomerByRefId(CustomerWithSubscriptionsFragment):
    pass


GetCustomerById.update_forward_refs()
GetCustomerByIdGetCustomerByRefId.update_forward_refs()
