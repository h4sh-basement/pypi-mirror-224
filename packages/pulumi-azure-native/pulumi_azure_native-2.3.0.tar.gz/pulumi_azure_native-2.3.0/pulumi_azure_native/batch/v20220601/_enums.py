# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CertificateFormat',
]


class CertificateFormat(str, Enum):
    """
    The format of the certificate - either Pfx or Cer. If omitted, the default is Pfx.
    """
    PFX = "Pfx"
    """
    The certificate is a PFX (PKCS#12) formatted certificate or certificate chain.
    """
    CER = "Cer"
    """
    The certificate is a base64-encoded X.509 certificate.
    """
