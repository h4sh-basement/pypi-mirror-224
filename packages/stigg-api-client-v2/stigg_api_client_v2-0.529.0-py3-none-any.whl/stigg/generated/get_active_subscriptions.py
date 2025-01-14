# Generated by ariadne-codegen on 2023-08-09 07:55
# Source: operations.graphql

from typing import List

from pydantic import Field

from .base_model import BaseModel
from .fragments import SubscriptionFragment


class GetActiveSubscriptions(BaseModel):
    get_active_subscriptions: List[
        "GetActiveSubscriptionsGetActiveSubscriptions"
    ] = Field(alias="getActiveSubscriptions")


class GetActiveSubscriptionsGetActiveSubscriptions(SubscriptionFragment):
    pass


GetActiveSubscriptions.update_forward_refs()
GetActiveSubscriptionsGetActiveSubscriptions.update_forward_refs()
