# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AssessmentSizingCriterion',
    'AssessmentStage',
    'AutomationArtifactStatus',
    'AzureDiskType',
    'AzureHybridUseBenefit',
    'AzureLocation',
    'AzureOfferCode',
    'AzurePricingTier',
    'AzureStorageRedundancy',
    'AzureVmFamily',
    'ConfigurationType',
    'Currency',
    'LoadBalancerType',
    'OperatingSystemType',
    'Percentile',
    'ProjectStatus',
    'ProvisioningState',
    'ReservedInstance',
    'ResourceIdentityType',
    'ResourceIdentityTypes',
    'SecretStoreType',
    'Status',
    'TargetAvailabilityZone',
    'TargetHydrationStorageProviderType',
    'TargetStorageAccessType',
    'TargetStorageProjectionType',
    'TimeRange',
    'WorkloadDeploymentTarget',
    'WorkloadDeploymentType',
    'WorkloadType',
    'ZoneRedundant',
]


class AssessmentSizingCriterion(str, Enum):
    """
    Assessment sizing criterion.
    """
    PERFORMANCE_BASED = "PerformanceBased"
    AS_ON_PREMISES = "AsOnPremises"


class AssessmentStage(str, Enum):
    """
    User configurable setting that describes the status of the assessment.
    """
    IN_PROGRESS = "InProgress"
    UNDER_REVIEW = "UnderReview"
    APPROVED = "Approved"


class AutomationArtifactStatus(str, Enum):
    """
    Gets or sets the status of automation artifacts.
    """
    NOT_GENERATED = "NotGenerated"
    GENERATED = "Generated"


class AzureDiskType(str, Enum):
    """
    Storage type selected for this disk.
    """
    UNKNOWN = "Unknown"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    STANDARD_SSD = "StandardSSD"
    STANDARD_OR_PREMIUM = "StandardOrPremium"


class AzureHybridUseBenefit(str, Enum):
    """
    AHUB discount on windows virtual machines.
    """
    UNKNOWN = "Unknown"
    YES = "Yes"
    NO = "No"


class AzureLocation(str, Enum):
    """
    Target Azure location for which the machines should be assessed. These enums are the same as used by Compute API.
    """
    UNKNOWN = "Unknown"
    EAST_ASIA = "EastAsia"
    SOUTHEAST_ASIA = "SoutheastAsia"
    AUSTRALIA_EAST = "AustraliaEast"
    AUSTRALIA_SOUTHEAST = "AustraliaSoutheast"
    BRAZIL_SOUTH = "BrazilSouth"
    CANADA_CENTRAL = "CanadaCentral"
    CANADA_EAST = "CanadaEast"
    WEST_EUROPE = "WestEurope"
    NORTH_EUROPE = "NorthEurope"
    CENTRAL_INDIA = "CentralIndia"
    SOUTH_INDIA = "SouthIndia"
    WEST_INDIA = "WestIndia"
    JAPAN_EAST = "JapanEast"
    JAPAN_WEST = "JapanWest"
    KOREA_CENTRAL = "KoreaCentral"
    KOREA_SOUTH = "KoreaSouth"
    UK_WEST = "UkWest"
    UK_SOUTH = "UkSouth"
    NORTH_CENTRAL_US = "NorthCentralUs"
    EAST_US = "EastUs"
    WEST_US2 = "WestUs2"
    SOUTH_CENTRAL_US = "SouthCentralUs"
    CENTRAL_US = "CentralUs"
    EAST_US2 = "EastUs2"
    WEST_US = "WestUs"
    WEST_CENTRAL_US = "WestCentralUs"
    GERMANY_CENTRAL = "GermanyCentral"
    GERMANY_NORTHEAST = "GermanyNortheast"
    CHINA_NORTH = "ChinaNorth"
    CHINA_EAST = "ChinaEast"
    US_GOV_ARIZONA = "USGovArizona"
    US_GOV_TEXAS = "USGovTexas"
    US_GOV_IOWA = "USGovIowa"
    US_GOV_VIRGINIA = "USGovVirginia"
    US_DO_D_CENTRAL = "USDoDCentral"
    US_DO_D_EAST = "USDoDEast"


class AzureOfferCode(str, Enum):
    """
    Offer code according to which cost estimation is done.
    """
    UNKNOWN = "Unknown"
    MSAZR0003_P = "MSAZR0003P"
    MSAZR0044_P = "MSAZR0044P"
    MSAZR0059_P = "MSAZR0059P"
    MSAZR0060_P = "MSAZR0060P"
    MSAZR0062_P = "MSAZR0062P"
    MSAZR0063_P = "MSAZR0063P"
    MSAZR0064_P = "MSAZR0064P"
    MSAZR0029_P = "MSAZR0029P"
    MSAZR0022_P = "MSAZR0022P"
    MSAZR0023_P = "MSAZR0023P"
    MSAZR0148_P = "MSAZR0148P"
    MSAZR0025_P = "MSAZR0025P"
    MSAZR0036_P = "MSAZR0036P"
    MSAZR0120_P = "MSAZR0120P"
    MSAZR0121_P = "MSAZR0121P"
    MSAZR0122_P = "MSAZR0122P"
    MSAZR0123_P = "MSAZR0123P"
    MSAZR0124_P = "MSAZR0124P"
    MSAZR0125_P = "MSAZR0125P"
    MSAZR0126_P = "MSAZR0126P"
    MSAZR0127_P = "MSAZR0127P"
    MSAZR0128_P = "MSAZR0128P"
    MSAZR0129_P = "MSAZR0129P"
    MSAZR0130_P = "MSAZR0130P"
    MSAZR0111_P = "MSAZR0111P"
    MSAZR0144_P = "MSAZR0144P"
    MSAZR0149_P = "MSAZR0149P"
    MSMCAZR0044_P = "MSMCAZR0044P"
    MSMCAZR0059_P = "MSMCAZR0059P"
    MSMCAZR0060_P = "MSMCAZR0060P"
    MSMCAZR0063_P = "MSMCAZR0063P"
    MSMCAZR0120_P = "MSMCAZR0120P"
    MSMCAZR0121_P = "MSMCAZR0121P"
    MSMCAZR0125_P = "MSMCAZR0125P"
    MSMCAZR0128_P = "MSMCAZR0128P"
    MSAZRDE0003_P = "MSAZRDE0003P"
    MSAZRDE0044_P = "MSAZRDE0044P"
    MSAZRUSGOV0003_P = "MSAZRUSGOV0003P"
    EA = "EA"


class AzurePricingTier(str, Enum):
    """
    Pricing tier for Size evaluation.
    """
    STANDARD = "Standard"
    BASIC = "Basic"


class AzureStorageRedundancy(str, Enum):
    """
    Storage Redundancy type offered by Azure.
    """
    UNKNOWN = "Unknown"
    LOCALLY_REDUNDANT = "LocallyRedundant"
    ZONE_REDUNDANT = "ZoneRedundant"
    GEO_REDUNDANT = "GeoRedundant"
    READ_ACCESS_GEO_REDUNDANT = "ReadAccessGeoRedundant"


class AzureVmFamily(str, Enum):
    """
    Azure VM family.
    """
    UNKNOWN = "Unknown"
    BASIC_A0_A4 = "Basic_A0_A4"
    STANDARD_A0_A7 = "Standard_A0_A7"
    STANDARD_A8_A11 = "Standard_A8_A11"
    AV2_SERIES = "Av2_series"
    D_SERIES = "D_series"
    DV2_SERIES = "Dv2_series"
    D_S_SERIES = "DS_series"
    D_SV2_SERIES = "DSv2_series"
    F_SERIES = "F_series"
    FS_SERIES = "Fs_series"
    G_SERIES = "G_series"
    G_S_SERIES = "GS_series"
    H_SERIES = "H_series"
    LS_SERIES = "Ls_series"
    DSV3_SERIES = "Dsv3_series"
    DV3_SERIES = "Dv3_series"
    FSV2_SERIES = "Fsv2_series"
    EV3_SERIES = "Ev3_series"
    ESV3_SERIES = "Esv3_series"
    M_SERIES = "M_series"
    D_C_SERIES = "DC_Series"


class ConfigurationType(str, Enum):
    """
    Gets or sets the configuration type.
    """
    IIS_CONNECTION_STRING = "IISConnectionString"
    IIS_AUTHENTICATION = "IISAuthentication"
    APACHE_TOMCAT_CONTEXT_RESOURCE = "ApacheTomcatContextResource"


class Currency(str, Enum):
    """
    Currency to report prices in.
    """
    UNKNOWN = "Unknown"
    USD = "USD"
    DKK = "DKK"
    CAD = "CAD"
    IDR = "IDR"
    JPY = "JPY"
    KRW = "KRW"
    NZD = "NZD"
    NOK = "NOK"
    RUB = "RUB"
    SAR = "SAR"
    ZAR = "ZAR"
    SEK = "SEK"
    TRY_ = "TRY"
    GBP = "GBP"
    MXN = "MXN"
    MYR = "MYR"
    INR = "INR"
    HKD = "HKD"
    BRL = "BRL"
    TWD = "TWD"
    EUR = "EUR"
    CHF = "CHF"
    ARS = "ARS"
    AUD = "AUD"
    CNY = "CNY"


class LoadBalancerType(str, Enum):
    """
    Gets or sets the load balancer type.
    """
    PRIVATE = "Private"
    PUBLIC = "Public"


class OperatingSystemType(str, Enum):
    WINDOWS = "Windows"
    LINUX = "Linux"


class Percentile(str, Enum):
    """
    Percentile of performance data used to recommend Azure size.
    """
    PERCENTILE50 = "Percentile50"
    PERCENTILE90 = "Percentile90"
    PERCENTILE95 = "Percentile95"
    PERCENTILE99 = "Percentile99"


class ProjectStatus(str, Enum):
    """
    Assessment project status.
    """
    ACTIVE = "Active"
    INACTIVE = "Inactive"


class ProvisioningState(str, Enum):
    """
    Provisioning state of the migrate project.
    """
    ACCEPTED = "Accepted"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"
    MOVING = "Moving"
    SUCCEEDED = "Succeeded"


class ReservedInstance(str, Enum):
    """
    Azure reserved instance.
    """
    NONE = "None"
    RI1_YEAR = "RI1Year"
    RI3_YEAR = "RI3Year"


class ResourceIdentityType(str, Enum):
    """
    The type of identity used for the resource mover service.
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"


class ResourceIdentityTypes(str, Enum):
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"


class SecretStoreType(str, Enum):
    NONE = "None"
    KUBE_SECRET = "KubeSecret"
    KEY_VAULT_SECRET = "KeyVaultSecret"
    APP_SERVICE_APP_SETTINGS = "AppServiceAppSettings"


class Status(str, Enum):
    """
    Private link connection state.
    """
    APPROVED = "Approved"
    PENDING = "Pending"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class TargetAvailabilityZone(str, Enum):
    """
    Gets or sets the target availability zone.
    """
    ONE = "1"
    TWO = "2"
    THREE = "3"
    NA = "NA"


class TargetHydrationStorageProviderType(str, Enum):
    """
    Gets or sets the storage provider type on the target.
    Applicable when StorageProjectionType is not ContainerFileSystem.
    """
    AZURE_FILE_SHARE = "AzureFileShare"


class TargetStorageAccessType(str, Enum):
    """
    Gets or sets the target storage access type.
    """
    SHARED = "Shared"
    EXCLUSIVE = "Exclusive"


class TargetStorageProjectionType(str, Enum):
    """
    Gets or sets the target projection type.
    """
    CONTAINER_FILE_SYSTEM = "ContainerFileSystem"
    PERSISTENT_VOLUME = "PersistentVolume"


class TimeRange(str, Enum):
    """
    Time range of performance data used to recommend a size.
    """
    DAY = "Day"
    WEEK = "Week"
    MONTH = "Month"
    CUSTOM = "Custom"


class WorkloadDeploymentTarget(str, Enum):
    """
    Gets or sets the deployment target platform.
    """
    AZURE_KUBERNETES_SERVICE = "AzureKubernetesService"
    AZURE_APP_SERVICE_CONTAINER = "AzureAppServiceContainer"
    AZURE_APP_SERVICE_NATIVE = "AzureAppServiceNative"


class WorkloadDeploymentType(str, Enum):
    """
    Gets or sets the instance type.
    """
    IISAKS_WORKLOAD_DEPLOYMENT = "IISAKSWorkloadDeployment"
    APACHE_TOMCAT_AKS_WORKLOAD_DEPLOYMENT = "ApacheTomcatAKSWorkloadDeployment"


class WorkloadType(str, Enum):
    """
    Gets or sets the instance type.
    """
    IIS_WORKLOAD = "IISWorkload"
    APACHE_TOMCAT_WORKLOAD = "ApacheTomcatWorkload"


class ZoneRedundant(str, Enum):
    """
    Defines the zone redundant resource setting.
    """
    ENABLE = "Enable"
    DISABLE = "Disable"
