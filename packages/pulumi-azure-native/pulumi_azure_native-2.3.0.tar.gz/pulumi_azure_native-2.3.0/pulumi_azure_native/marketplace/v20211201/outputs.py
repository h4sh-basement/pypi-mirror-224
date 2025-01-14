# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'NewNotificationsResponse',
    'PlanNotificationDetailsResponse',
    'StopSellOffersPlansNotificationsListPropertiesResponse',
]

@pulumi.output_type
class NewNotificationsResponse(dict):
    """
    New plans notification details
    """
    def __init__(__self__, *,
                 display_name: Optional[str] = None,
                 icon: Optional[str] = None,
                 is_future_plans_enabled: Optional[bool] = None,
                 message_code: Optional[float] = None,
                 offer_id: Optional[str] = None,
                 plans: Optional[Sequence['outputs.PlanNotificationDetailsResponse']] = None):
        """
        New plans notification details
        :param str display_name: Gets offer display name
        :param str icon: Gets or sets the icon url
        :param bool is_future_plans_enabled: Gets a value indicating whether future plans is enabled.
        :param float message_code: Gets or sets the notification message id
        :param str offer_id: Gets offer id
        :param Sequence['PlanNotificationDetailsResponse'] plans: Gets or sets removed plans notifications
        """
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if icon is not None:
            pulumi.set(__self__, "icon", icon)
        if is_future_plans_enabled is not None:
            pulumi.set(__self__, "is_future_plans_enabled", is_future_plans_enabled)
        if message_code is not None:
            pulumi.set(__self__, "message_code", message_code)
        if offer_id is not None:
            pulumi.set(__self__, "offer_id", offer_id)
        if plans is not None:
            pulumi.set(__self__, "plans", plans)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        Gets offer display name
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def icon(self) -> Optional[str]:
        """
        Gets or sets the icon url
        """
        return pulumi.get(self, "icon")

    @property
    @pulumi.getter(name="isFuturePlansEnabled")
    def is_future_plans_enabled(self) -> Optional[bool]:
        """
        Gets a value indicating whether future plans is enabled.
        """
        return pulumi.get(self, "is_future_plans_enabled")

    @property
    @pulumi.getter(name="messageCode")
    def message_code(self) -> Optional[float]:
        """
        Gets or sets the notification message id
        """
        return pulumi.get(self, "message_code")

    @property
    @pulumi.getter(name="offerId")
    def offer_id(self) -> Optional[str]:
        """
        Gets offer id
        """
        return pulumi.get(self, "offer_id")

    @property
    @pulumi.getter
    def plans(self) -> Optional[Sequence['outputs.PlanNotificationDetailsResponse']]:
        """
        Gets or sets removed plans notifications
        """
        return pulumi.get(self, "plans")


@pulumi.output_type
class PlanNotificationDetailsResponse(dict):
    """
    Plan notification details
    """
    def __init__(__self__, *,
                 plan_display_name: Optional[str] = None,
                 plan_id: Optional[str] = None):
        """
        Plan notification details
        :param str plan_display_name: Gets or sets the plan display name
        :param str plan_id: Gets or sets the plan id
        """
        if plan_display_name is not None:
            pulumi.set(__self__, "plan_display_name", plan_display_name)
        if plan_id is not None:
            pulumi.set(__self__, "plan_id", plan_id)

    @property
    @pulumi.getter(name="planDisplayName")
    def plan_display_name(self) -> Optional[str]:
        """
        Gets or sets the plan display name
        """
        return pulumi.get(self, "plan_display_name")

    @property
    @pulumi.getter(name="planId")
    def plan_id(self) -> Optional[str]:
        """
        Gets or sets the plan id
        """
        return pulumi.get(self, "plan_id")


@pulumi.output_type
class StopSellOffersPlansNotificationsListPropertiesResponse(dict):
    """
    List of stop sell offers and plans notifications.
    """
    def __init__(__self__, *,
                 display_name: str,
                 icon: str,
                 is_entire: bool,
                 message_code: float,
                 offer_id: str,
                 plans: Sequence['outputs.PlanNotificationDetailsResponse'],
                 public_context: bool,
                 subscriptions_ids: Sequence[str]):
        """
        List of stop sell offers and plans notifications.
        :param str display_name: The offer display name
        :param str icon: The icon url
        :param bool is_entire: A value indicating whether entire offer is in stop sell or only few of its plans
        :param float message_code: The notification message code
        :param str offer_id: The offer id
        :param Sequence['PlanNotificationDetailsResponse'] plans: The list of removed plans notifications
        :param bool public_context: True if the offer has public plans
        :param Sequence[str] subscriptions_ids: The subscriptions related to private plans
        """
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "icon", icon)
        pulumi.set(__self__, "is_entire", is_entire)
        pulumi.set(__self__, "message_code", message_code)
        pulumi.set(__self__, "offer_id", offer_id)
        pulumi.set(__self__, "plans", plans)
        pulumi.set(__self__, "public_context", public_context)
        pulumi.set(__self__, "subscriptions_ids", subscriptions_ids)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The offer display name
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def icon(self) -> str:
        """
        The icon url
        """
        return pulumi.get(self, "icon")

    @property
    @pulumi.getter(name="isEntire")
    def is_entire(self) -> bool:
        """
        A value indicating whether entire offer is in stop sell or only few of its plans
        """
        return pulumi.get(self, "is_entire")

    @property
    @pulumi.getter(name="messageCode")
    def message_code(self) -> float:
        """
        The notification message code
        """
        return pulumi.get(self, "message_code")

    @property
    @pulumi.getter(name="offerId")
    def offer_id(self) -> str:
        """
        The offer id
        """
        return pulumi.get(self, "offer_id")

    @property
    @pulumi.getter
    def plans(self) -> Sequence['outputs.PlanNotificationDetailsResponse']:
        """
        The list of removed plans notifications
        """
        return pulumi.get(self, "plans")

    @property
    @pulumi.getter(name="publicContext")
    def public_context(self) -> bool:
        """
        True if the offer has public plans
        """
        return pulumi.get(self, "public_context")

    @property
    @pulumi.getter(name="subscriptionsIds")
    def subscriptions_ids(self) -> Sequence[str]:
        """
        The subscriptions related to private plans
        """
        return pulumi.get(self, "subscriptions_ids")


