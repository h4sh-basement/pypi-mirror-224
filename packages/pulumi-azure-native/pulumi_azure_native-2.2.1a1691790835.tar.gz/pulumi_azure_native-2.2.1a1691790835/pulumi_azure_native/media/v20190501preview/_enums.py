# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'LiveEventEncodingType',
    'LiveEventInputProtocol',
    'StreamOptionsFlag',
]


class LiveEventEncodingType(str, Enum):
    """
    The encoding type for Live Event.  This value is specified at creation time and cannot be updated.
    """
    NONE = "None"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM1080P = "Premium1080p"


class LiveEventInputProtocol(str, Enum):
    """
    The streaming protocol for the Live Event.  This is specified at creation time and cannot be updated.
    """
    FRAGMENTED_MP4 = "FragmentedMP4"
    RTMP = "RTMP"


class StreamOptionsFlag(str, Enum):
    DEFAULT = "Default"
    LOW_LATENCY = "LowLatency"
