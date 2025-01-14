# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AccountEncryptionKeyType',
    'AssetContainerPermission',
    'ContentKeyPolicyFairPlayRentalAndLeaseKeyType',
    'ContentKeyPolicyPlayReadyContentType',
    'ContentKeyPolicyPlayReadyLicenseType',
    'ContentKeyPolicyPlayReadyUnknownOutputPassingOption',
    'ContentKeyPolicyRestrictionTokenType',
    'DefaultAction',
    'FilterTrackPropertyCompareOperation',
    'FilterTrackPropertyType',
    'MinimumTlsVersion',
    'PrivateEndpointServiceConnectionStatus',
    'PublicNetworkAccess',
    'SecurityLevel',
    'StorageAccountType',
    'StorageAuthentication',
    'TrackPropertyCompareOperation',
    'TrackPropertyType',
    'Visibility',
]


class AccountEncryptionKeyType(str, Enum):
    """
    The type of key used to encrypt the Account Key.
    """
    SYSTEM_KEY = "SystemKey"
    """
    The Account Key is encrypted with a System Key.
    """
    CUSTOMER_KEY = "CustomerKey"
    """
    The Account Key is encrypted with a Customer Key.
    """


class AssetContainerPermission(str, Enum):
    """
    The permissions to set on the SAS URL.
    """
    READ = "Read"
    """
    The SAS URL will allow read access to the container.
    """
    READ_WRITE = "ReadWrite"
    """
    The SAS URL will allow read and write access to the container.
    """
    READ_WRITE_DELETE = "ReadWriteDelete"
    """
    The SAS URL will allow read, write and delete access to the container.
    """


class ContentKeyPolicyFairPlayRentalAndLeaseKeyType(str, Enum):
    """
    The rental and lease key type.
    """
    UNKNOWN = "Unknown"
    """
    Represents a ContentKeyPolicyFairPlayRentalAndLeaseKeyType that is unavailable in current API version.
    """
    UNDEFINED = "Undefined"
    """
    Key duration is not specified.
    """
    DUAL_EXPIRY = "DualExpiry"
    """
    Dual expiry for offline rental.
    """
    PERSISTENT_UNLIMITED = "PersistentUnlimited"
    """
    Content key can be persisted with an unlimited duration
    """
    PERSISTENT_LIMITED = "PersistentLimited"
    """
    Content key can be persisted and the valid duration is limited by the Rental Duration value
    """


class ContentKeyPolicyPlayReadyContentType(str, Enum):
    """
    The PlayReady content type.
    """
    UNKNOWN = "Unknown"
    """
    Represents a ContentKeyPolicyPlayReadyContentType that is unavailable in current API version.
    """
    UNSPECIFIED = "Unspecified"
    """
    Unspecified content type.
    """
    ULTRA_VIOLET_DOWNLOAD = "UltraVioletDownload"
    """
    Ultraviolet download content type.
    """
    ULTRA_VIOLET_STREAMING = "UltraVioletStreaming"
    """
    Ultraviolet streaming content type.
    """


class ContentKeyPolicyPlayReadyLicenseType(str, Enum):
    """
    The license type.
    """
    UNKNOWN = "Unknown"
    """
    Represents a ContentKeyPolicyPlayReadyLicenseType that is unavailable in current API version.
    """
    NON_PERSISTENT = "NonPersistent"
    """
    Non persistent license.
    """
    PERSISTENT = "Persistent"
    """
    Persistent license. Allows offline playback.
    """


class ContentKeyPolicyPlayReadyUnknownOutputPassingOption(str, Enum):
    """
    Configures Unknown output handling settings of the license.
    """
    UNKNOWN = "Unknown"
    """
    Represents a ContentKeyPolicyPlayReadyUnknownOutputPassingOption that is unavailable in current API version.
    """
    NOT_ALLOWED = "NotAllowed"
    """
    Passing the video portion of protected content to an Unknown Output is not allowed.
    """
    ALLOWED = "Allowed"
    """
    Passing the video portion of protected content to an Unknown Output is allowed.
    """
    ALLOWED_WITH_VIDEO_CONSTRICTION = "AllowedWithVideoConstriction"
    """
    Passing the video portion of protected content to an Unknown Output is allowed but with constrained resolution.
    """


class ContentKeyPolicyRestrictionTokenType(str, Enum):
    """
    The type of token.
    """
    UNKNOWN = "Unknown"
    """
    Represents a ContentKeyPolicyRestrictionTokenType that is unavailable in current API version.
    """
    SWT = "Swt"
    """
    Simple Web Token.
    """
    JWT = "Jwt"
    """
    JSON Web Token.
    """


class DefaultAction(str, Enum):
    """
    The behavior for IP access control in Key Delivery.
    """
    ALLOW = "Allow"
    """
    All public IP addresses are allowed.
    """
    DENY = "Deny"
    """
    Public IP addresses are blocked.
    """


class FilterTrackPropertyCompareOperation(str, Enum):
    """
    The track property condition operation.
    """
    EQUAL = "Equal"
    """
    The equal operation.
    """
    NOT_EQUAL = "NotEqual"
    """
    The not equal operation.
    """


class FilterTrackPropertyType(str, Enum):
    """
    The track property type.
    """
    UNKNOWN = "Unknown"
    """
    The unknown track property type.
    """
    TYPE = "Type"
    """
    The type.
    """
    NAME = "Name"
    """
    The name.
    """
    LANGUAGE = "Language"
    """
    The language.
    """
    FOUR_CC = "FourCC"
    """
    The fourCC.
    """
    BITRATE = "Bitrate"
    """
    The bitrate.
    """


class MinimumTlsVersion(str, Enum):
    """
    The minimum TLS version allowed for this account's requests. This is an optional property. If unspecified, a secure default value will be used.
    """
    TLS10 = "Tls10"
    """
    Minimum TLS version is TLS 1.0.
    """
    TLS11 = "Tls11"
    """
    Minimum TLS version is TLS 1.1.
    """
    TLS12 = "Tls12"
    """
    Minimum TLS version is TLS 1.2.
    """
    TLS13 = "Tls13"
    """
    Minimum TLS version is TLS 1.3.
    """


class PrivateEndpointServiceConnectionStatus(str, Enum):
    """
    Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class PublicNetworkAccess(str, Enum):
    """
    Whether or not public network access is allowed for resources under the Media Services account.
    """
    ENABLED = "Enabled"
    """
    Public network access is enabled.
    """
    DISABLED = "Disabled"
    """
    Public network access is disabled.
    """


class SecurityLevel(str, Enum):
    """
    The security level.
    """
    UNKNOWN = "Unknown"
    """
    Represents a SecurityLevel that is unavailable in current API version.
    """
    SL150 = "SL150"
    """
    For clients under development or test. No protection against unauthorized use.
    """
    SL2000 = "SL2000"
    """
    For hardened devices and applications consuming commercial content. Software or hardware protection.
    """
    SL3000 = "SL3000"
    """
    For hardened devices only. Hardware protection.
    """


class StorageAccountType(str, Enum):
    """
    The type of the storage account.
    """
    PRIMARY = "Primary"
    """
    The primary storage account for the Media Services account.
    """
    SECONDARY = "Secondary"
    """
    A secondary storage account for the Media Services account.
    """


class StorageAuthentication(str, Enum):
    SYSTEM = "System"
    """
    System authentication.
    """
    MANAGED_IDENTITY = "ManagedIdentity"
    """
    Managed Identity authentication.
    """


class TrackPropertyCompareOperation(str, Enum):
    """
    Track property condition operation
    """
    UNKNOWN = "Unknown"
    """
    Unknown track property compare operation
    """
    EQUAL = "Equal"
    """
    Equal operation
    """


class TrackPropertyType(str, Enum):
    """
    Track property type
    """
    UNKNOWN = "Unknown"
    """
    Unknown track property
    """
    FOUR_CC = "FourCC"
    """
    Track FourCC
    """


class Visibility(str, Enum):
    """
    When PlayerVisibility is set to "Visible", the text track will be present in the DASH manifest or HLS playlist when requested by a client. When the PlayerVisibility is set to "Hidden", the text will not be available to the client. The default value is "Visible".
    """
    HIDDEN = "Hidden"
    """
    The track is hidden to video player.
    """
    VISIBLE = "Visible"
    """
    The track is visible to video player.
    """
