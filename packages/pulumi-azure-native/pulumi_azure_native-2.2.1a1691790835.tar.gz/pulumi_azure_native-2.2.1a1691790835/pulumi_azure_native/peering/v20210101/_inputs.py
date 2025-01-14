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
    'ContactDetailArgs',
]

@pulumi.input_type
class ContactDetailArgs:
    def __init__(__self__, *,
                 email: Optional[pulumi.Input[str]] = None,
                 phone: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[Union[str, 'Role']]] = None):
        """
        The contact detail class.
        :param pulumi.Input[str] email: The e-mail address of the contact.
        :param pulumi.Input[str] phone: The phone number of the contact.
        :param pulumi.Input[Union[str, 'Role']] role: The role of the contact.
        """
        if email is not None:
            pulumi.set(__self__, "email", email)
        if phone is not None:
            pulumi.set(__self__, "phone", phone)
        if role is not None:
            pulumi.set(__self__, "role", role)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        The e-mail address of the contact.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter
    def phone(self) -> Optional[pulumi.Input[str]]:
        """
        The phone number of the contact.
        """
        return pulumi.get(self, "phone")

    @phone.setter
    def phone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "phone", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[Union[str, 'Role']]]:
        """
        The role of the contact.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[Union[str, 'Role']]]):
        pulumi.set(self, "role", value)


