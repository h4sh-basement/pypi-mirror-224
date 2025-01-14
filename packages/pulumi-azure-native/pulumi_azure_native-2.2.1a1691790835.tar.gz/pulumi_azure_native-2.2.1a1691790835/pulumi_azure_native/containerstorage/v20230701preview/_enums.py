# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AzureDiskSkuName',
    'ElasticSanSkuName',
    'ManagedServiceIdentityType',
    'ReclaimPolicy',
    'Zone',
]


class AzureDiskSkuName(str, Enum):
    """
    Sku name
    """
    PREMIUM_LRS = "Premium_LRS"
    """
    Premium_LRS SKU
    """
    STANDARD_LRS = "Standard_LRS"
    """
    Standard_LRS SKU
    """
    STANDARD_SS_D_LRS = "StandardSSD_LRS"
    """
    StandardSSD_LRS SKU
    """
    ULTRA_SS_D_LRS = "UltraSSD_LRS"
    """
    UltraSSD_LRS SKU
    """
    PREMIUM_ZRS = "Premium_ZRS"
    """
    Premium_ZRS SKU
    """
    PREMIUM_V2_LRS = "PremiumV2_LRS"
    """
    PremiumV2_LRS SKU
    """
    STANDARD_SS_D_ZRS = "StandardSSD_ZRS"
    """
    StandardSSD_ZRS SKU
    """


class ElasticSanSkuName(str, Enum):
    """
    Sku name
    """
    PREMIUM_LRS = "Premium_LRS"
    """
    Premium_LRS SKU
    """
    PREMIUM_ZRS = "Premium_ZRS"
    """
    Premium_ZRS SKU
    """


class ManagedServiceIdentityType(str, Enum):
    """
    Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"


class ReclaimPolicy(str, Enum):
    """
    ReclaimPolicy defines what happens to the backend storage when StoragePool is deleted
    """
    DELETE = "Delete"
    """
    Delete resource
    """
    RETAIN = "Retain"
    """
    Retain resource
    """


class Zone(str, Enum):
    """
    Availability Zones
    """
    ZONE1 = "1"
    """
    First availability zone.
    """
    ZONE2 = "2"
    """
    Second availability zone.
    """
    ZONE3 = "3"
    """
    Third availability zone.
    """
