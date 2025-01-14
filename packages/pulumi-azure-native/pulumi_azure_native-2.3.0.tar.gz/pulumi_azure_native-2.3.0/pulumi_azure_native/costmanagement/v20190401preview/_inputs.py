# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'BudgetTimePeriodArgs',
    'NotificationArgs',
    'ReportConfigComparisonExpressionArgs',
    'ReportConfigFilterArgs',
]

@pulumi.input_type
class BudgetTimePeriodArgs:
    def __init__(__self__, *,
                 start_date: pulumi.Input[str],
                 end_date: Optional[pulumi.Input[str]] = None):
        """
        The start and end date for a budget.
        :param pulumi.Input[str] start_date: The start date for the budget.
        :param pulumi.Input[str] end_date: The end date for the budget. If not provided, we default this to 10 years from the start date.
        """
        pulumi.set(__self__, "start_date", start_date)
        if end_date is not None:
            pulumi.set(__self__, "end_date", end_date)

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Input[str]:
        """
        The start date for the budget.
        """
        return pulumi.get(self, "start_date")

    @start_date.setter
    def start_date(self, value: pulumi.Input[str]):
        pulumi.set(self, "start_date", value)

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[pulumi.Input[str]]:
        """
        The end date for the budget. If not provided, we default this to 10 years from the start date.
        """
        return pulumi.get(self, "end_date")

    @end_date.setter
    def end_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_date", value)


@pulumi.input_type
class NotificationArgs:
    def __init__(__self__, *,
                 contact_emails: pulumi.Input[Sequence[pulumi.Input[str]]],
                 enabled: pulumi.Input[bool],
                 operator: pulumi.Input[Union[str, 'NotificationOperatorType']],
                 threshold: pulumi.Input[float],
                 contact_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 contact_roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The notification associated with a budget.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] contact_emails: Email addresses to send the budget notification to when the threshold is exceeded.
        :param pulumi.Input[bool] enabled: The notification is enabled or not.
        :param pulumi.Input[Union[str, 'NotificationOperatorType']] operator: The comparison operator.
        :param pulumi.Input[float] threshold: Threshold value associated with a notification. Notification is sent when the cost exceeded the threshold. It is always percent and has to be between 0 and 1000.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] contact_groups: Action groups to send the budget notification to when the threshold is exceeded.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] contact_roles: Contact roles to send the budget notification to when the threshold is exceeded.
        """
        pulumi.set(__self__, "contact_emails", contact_emails)
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "operator", operator)
        pulumi.set(__self__, "threshold", threshold)
        if contact_groups is not None:
            pulumi.set(__self__, "contact_groups", contact_groups)
        if contact_roles is not None:
            pulumi.set(__self__, "contact_roles", contact_roles)

    @property
    @pulumi.getter(name="contactEmails")
    def contact_emails(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Email addresses to send the budget notification to when the threshold is exceeded.
        """
        return pulumi.get(self, "contact_emails")

    @contact_emails.setter
    def contact_emails(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "contact_emails", value)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        The notification is enabled or not.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[str, 'NotificationOperatorType']]:
        """
        The comparison operator.
        """
        return pulumi.get(self, "operator")

    @operator.setter
    def operator(self, value: pulumi.Input[Union[str, 'NotificationOperatorType']]):
        pulumi.set(self, "operator", value)

    @property
    @pulumi.getter
    def threshold(self) -> pulumi.Input[float]:
        """
        Threshold value associated with a notification. Notification is sent when the cost exceeded the threshold. It is always percent and has to be between 0 and 1000.
        """
        return pulumi.get(self, "threshold")

    @threshold.setter
    def threshold(self, value: pulumi.Input[float]):
        pulumi.set(self, "threshold", value)

    @property
    @pulumi.getter(name="contactGroups")
    def contact_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Action groups to send the budget notification to when the threshold is exceeded.
        """
        return pulumi.get(self, "contact_groups")

    @contact_groups.setter
    def contact_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "contact_groups", value)

    @property
    @pulumi.getter(name="contactRoles")
    def contact_roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Contact roles to send the budget notification to when the threshold is exceeded.
        """
        return pulumi.get(self, "contact_roles")

    @contact_roles.setter
    def contact_roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "contact_roles", value)


@pulumi.input_type
class ReportConfigComparisonExpressionArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 operator: pulumi.Input[Union[str, 'OperatorType']],
                 values: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        The comparison expression to be used in the report.
        :param pulumi.Input[str] name: The name of the column to use in comparison.
        :param pulumi.Input[Union[str, 'OperatorType']] operator: The operator to use for comparison.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] values: Array of values to use for comparison
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "operator", operator)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the column to use in comparison.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[str, 'OperatorType']]:
        """
        The operator to use for comparison.
        """
        return pulumi.get(self, "operator")

    @operator.setter
    def operator(self, value: pulumi.Input[Union[str, 'OperatorType']]):
        pulumi.set(self, "operator", value)

    @property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Array of values to use for comparison
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "values", value)


@pulumi.input_type
class ReportConfigFilterArgs:
    def __init__(__self__, *,
                 and_: Optional[pulumi.Input[Sequence[pulumi.Input['ReportConfigFilterArgs']]]] = None,
                 dimension: Optional[pulumi.Input['ReportConfigComparisonExpressionArgs']] = None,
                 not_: Optional[pulumi.Input['ReportConfigFilterArgs']] = None,
                 or_: Optional[pulumi.Input[Sequence[pulumi.Input['ReportConfigFilterArgs']]]] = None,
                 tag: Optional[pulumi.Input['ReportConfigComparisonExpressionArgs']] = None):
        """
        The filter expression to be used in the report.
        :param pulumi.Input[Sequence[pulumi.Input['ReportConfigFilterArgs']]] and_: The logical "AND" expression. Must have at least 2 items.
        :param pulumi.Input['ReportConfigComparisonExpressionArgs'] dimension: Has comparison expression for a dimension
        :param pulumi.Input['ReportConfigFilterArgs'] not_: The logical "NOT" expression.
        :param pulumi.Input[Sequence[pulumi.Input['ReportConfigFilterArgs']]] or_: The logical "OR" expression. Must have at least 2 items.
        :param pulumi.Input['ReportConfigComparisonExpressionArgs'] tag: Has comparison expression for a tag
        """
        if and_ is not None:
            pulumi.set(__self__, "and_", and_)
        if dimension is not None:
            pulumi.set(__self__, "dimension", dimension)
        if not_ is not None:
            pulumi.set(__self__, "not_", not_)
        if or_ is not None:
            pulumi.set(__self__, "or_", or_)
        if tag is not None:
            pulumi.set(__self__, "tag", tag)

    @property
    @pulumi.getter(name="and")
    def and_(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ReportConfigFilterArgs']]]]:
        """
        The logical "AND" expression. Must have at least 2 items.
        """
        return pulumi.get(self, "and_")

    @and_.setter
    def and_(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ReportConfigFilterArgs']]]]):
        pulumi.set(self, "and_", value)

    @property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input['ReportConfigComparisonExpressionArgs']]:
        """
        Has comparison expression for a dimension
        """
        return pulumi.get(self, "dimension")

    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input['ReportConfigComparisonExpressionArgs']]):
        pulumi.set(self, "dimension", value)

    @property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[pulumi.Input['ReportConfigFilterArgs']]:
        """
        The logical "NOT" expression.
        """
        return pulumi.get(self, "not_")

    @not_.setter
    def not_(self, value: Optional[pulumi.Input['ReportConfigFilterArgs']]):
        pulumi.set(self, "not_", value)

    @property
    @pulumi.getter(name="or")
    def or_(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ReportConfigFilterArgs']]]]:
        """
        The logical "OR" expression. Must have at least 2 items.
        """
        return pulumi.get(self, "or_")

    @or_.setter
    def or_(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ReportConfigFilterArgs']]]]):
        pulumi.set(self, "or_", value)

    @property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input['ReportConfigComparisonExpressionArgs']]:
        """
        Has comparison expression for a tag
        """
        return pulumi.get(self, "tag")

    @tag.setter
    def tag(self, value: Optional[pulumi.Input['ReportConfigComparisonExpressionArgs']]):
        pulumi.set(self, "tag", value)


