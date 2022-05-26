import inspect
import typing

from vkbottle_types.objects import (
    DonutDonatorSubscriptionInfo,
    GroupsGroupFull,
    UsersUserFull,
)

from .base_response import BaseResponse


class GetSubscriptionResponse(BaseResponse):
    response: DonutDonatorSubscriptionInfo


class GetSubscriptionsResponse(BaseResponse):
    response: "GetSubscriptionsResponseModel"


class GetSubscriptionsResponseModel(BaseResponse):
    subscriptions: typing.Optional[typing.List["DonutDonatorSubscriptionInfo"]] = None
    count: typing.Optional[int] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()


__all__ = (
    "GetSubscriptionResponse",
    "GetSubscriptionsResponse",
)