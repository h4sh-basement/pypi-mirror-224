# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetDefaultCniNetworkResult',
    'AwaitableGetDefaultCniNetworkResult',
    'get_default_cni_network',
    'get_default_cni_network_output',
]

@pulumi.output_type
class GetDefaultCniNetworkResult:
    def __init__(__self__, cluster_id=None, cni_as_number=None, cni_bgp_configuration=None, detailed_status=None, detailed_status_message=None, extended_location=None, fabric_bgp_peers=None, hybrid_aks_clusters_associated_ids=None, id=None, interface_name=None, ip_allocation_type=None, ipv4_connected_prefix=None, ipv6_connected_prefix=None, l3_isolation_domain_id=None, location=None, name=None, provisioning_state=None, system_data=None, tags=None, type=None, vlan=None):
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if cni_as_number and not isinstance(cni_as_number, float):
            raise TypeError("Expected argument 'cni_as_number' to be a float")
        pulumi.set(__self__, "cni_as_number", cni_as_number)
        if cni_bgp_configuration and not isinstance(cni_bgp_configuration, dict):
            raise TypeError("Expected argument 'cni_bgp_configuration' to be a dict")
        pulumi.set(__self__, "cni_bgp_configuration", cni_bgp_configuration)
        if detailed_status and not isinstance(detailed_status, str):
            raise TypeError("Expected argument 'detailed_status' to be a str")
        pulumi.set(__self__, "detailed_status", detailed_status)
        if detailed_status_message and not isinstance(detailed_status_message, str):
            raise TypeError("Expected argument 'detailed_status_message' to be a str")
        pulumi.set(__self__, "detailed_status_message", detailed_status_message)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if fabric_bgp_peers and not isinstance(fabric_bgp_peers, list):
            raise TypeError("Expected argument 'fabric_bgp_peers' to be a list")
        pulumi.set(__self__, "fabric_bgp_peers", fabric_bgp_peers)
        if hybrid_aks_clusters_associated_ids and not isinstance(hybrid_aks_clusters_associated_ids, list):
            raise TypeError("Expected argument 'hybrid_aks_clusters_associated_ids' to be a list")
        pulumi.set(__self__, "hybrid_aks_clusters_associated_ids", hybrid_aks_clusters_associated_ids)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if interface_name and not isinstance(interface_name, str):
            raise TypeError("Expected argument 'interface_name' to be a str")
        pulumi.set(__self__, "interface_name", interface_name)
        if ip_allocation_type and not isinstance(ip_allocation_type, str):
            raise TypeError("Expected argument 'ip_allocation_type' to be a str")
        pulumi.set(__self__, "ip_allocation_type", ip_allocation_type)
        if ipv4_connected_prefix and not isinstance(ipv4_connected_prefix, str):
            raise TypeError("Expected argument 'ipv4_connected_prefix' to be a str")
        pulumi.set(__self__, "ipv4_connected_prefix", ipv4_connected_prefix)
        if ipv6_connected_prefix and not isinstance(ipv6_connected_prefix, str):
            raise TypeError("Expected argument 'ipv6_connected_prefix' to be a str")
        pulumi.set(__self__, "ipv6_connected_prefix", ipv6_connected_prefix)
        if l3_isolation_domain_id and not isinstance(l3_isolation_domain_id, str):
            raise TypeError("Expected argument 'l3_isolation_domain_id' to be a str")
        pulumi.set(__self__, "l3_isolation_domain_id", l3_isolation_domain_id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vlan and not isinstance(vlan, float):
            raise TypeError("Expected argument 'vlan' to be a float")
        pulumi.set(__self__, "vlan", vlan)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        """
        The resource ID of the Network Cloud cluster this default CNI network is associated with.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="cniAsNumber")
    def cni_as_number(self) -> float:
        """
        The autonomous system number that the fabric expects to peer with, derived from the associated L3 isolation domain.
        """
        return pulumi.get(self, "cni_as_number")

    @property
    @pulumi.getter(name="cniBgpConfiguration")
    def cni_bgp_configuration(self) -> Optional['outputs.CniBgpConfigurationResponse']:
        """
        The Calico BGP configuration.
        """
        return pulumi.get(self, "cni_bgp_configuration")

    @property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> str:
        """
        The more detailed status of the default CNI network.
        """
        return pulumi.get(self, "detailed_status")

    @property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> str:
        """
        The descriptive message about the current detailed status.
        """
        return pulumi.get(self, "detailed_status_message")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> 'outputs.ExtendedLocationResponse':
        """
        The extended location of the cluster associated with the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="fabricBgpPeers")
    def fabric_bgp_peers(self) -> Sequence['outputs.BgpPeerResponse']:
        """
        The L3 isolation fabric BGP peering connectivity information necessary for BGP peering the Hybrid AKS Cluster with the switch fabric.
        """
        return pulumi.get(self, "fabric_bgp_peers")

    @property
    @pulumi.getter(name="hybridAksClustersAssociatedIds")
    def hybrid_aks_clusters_associated_ids(self) -> Sequence[str]:
        """
        The list of Hybrid AKS cluster resource ID(s) that are associated with this default CNI network.
        """
        return pulumi.get(self, "hybrid_aks_clusters_associated_ids")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="interfaceName")
    def interface_name(self) -> str:
        """
        The name of the interface that will be present in the virtual machine to represent this network.
        """
        return pulumi.get(self, "interface_name")

    @property
    @pulumi.getter(name="ipAllocationType")
    def ip_allocation_type(self) -> Optional[str]:
        """
        The type of the IP address allocation.
        """
        return pulumi.get(self, "ip_allocation_type")

    @property
    @pulumi.getter(name="ipv4ConnectedPrefix")
    def ipv4_connected_prefix(self) -> Optional[str]:
        """
        The IPV4 prefix (CIDR) assigned to this default CNI network. It is required when the IP allocation type
        is IPV4 or DualStack.
        """
        return pulumi.get(self, "ipv4_connected_prefix")

    @property
    @pulumi.getter(name="ipv6ConnectedPrefix")
    def ipv6_connected_prefix(self) -> Optional[str]:
        """
        The IPV6 prefix (CIDR) assigned to this default CNI network. It is required when the IP allocation type
        is IPV6 or DualStack.
        """
        return pulumi.get(self, "ipv6_connected_prefix")

    @property
    @pulumi.getter(name="l3IsolationDomainId")
    def l3_isolation_domain_id(self) -> str:
        """
        The resource ID of the Network Fabric l3IsolationDomain.
        """
        return pulumi.get(self, "l3_isolation_domain_id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the default CNI network.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def vlan(self) -> float:
        """
        The VLAN from the l3IsolationDomain that is used for this network.
        """
        return pulumi.get(self, "vlan")


class AwaitableGetDefaultCniNetworkResult(GetDefaultCniNetworkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDefaultCniNetworkResult(
            cluster_id=self.cluster_id,
            cni_as_number=self.cni_as_number,
            cni_bgp_configuration=self.cni_bgp_configuration,
            detailed_status=self.detailed_status,
            detailed_status_message=self.detailed_status_message,
            extended_location=self.extended_location,
            fabric_bgp_peers=self.fabric_bgp_peers,
            hybrid_aks_clusters_associated_ids=self.hybrid_aks_clusters_associated_ids,
            id=self.id,
            interface_name=self.interface_name,
            ip_allocation_type=self.ip_allocation_type,
            ipv4_connected_prefix=self.ipv4_connected_prefix,
            ipv6_connected_prefix=self.ipv6_connected_prefix,
            l3_isolation_domain_id=self.l3_isolation_domain_id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            vlan=self.vlan)


def get_default_cni_network(default_cni_network_name: Optional[str] = None,
                            resource_group_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDefaultCniNetworkResult:
    """
    Get properties of the provided default CNI network.
    Azure REST API version: 2022-12-12-preview.


    :param str default_cni_network_name: The name of the default CNI network.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['defaultCniNetworkName'] = default_cni_network_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:networkcloud:getDefaultCniNetwork', __args__, opts=opts, typ=GetDefaultCniNetworkResult).value

    return AwaitableGetDefaultCniNetworkResult(
        cluster_id=__ret__.cluster_id,
        cni_as_number=__ret__.cni_as_number,
        cni_bgp_configuration=__ret__.cni_bgp_configuration,
        detailed_status=__ret__.detailed_status,
        detailed_status_message=__ret__.detailed_status_message,
        extended_location=__ret__.extended_location,
        fabric_bgp_peers=__ret__.fabric_bgp_peers,
        hybrid_aks_clusters_associated_ids=__ret__.hybrid_aks_clusters_associated_ids,
        id=__ret__.id,
        interface_name=__ret__.interface_name,
        ip_allocation_type=__ret__.ip_allocation_type,
        ipv4_connected_prefix=__ret__.ipv4_connected_prefix,
        ipv6_connected_prefix=__ret__.ipv6_connected_prefix,
        l3_isolation_domain_id=__ret__.l3_isolation_domain_id,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type,
        vlan=__ret__.vlan)


@_utilities.lift_output_func(get_default_cni_network)
def get_default_cni_network_output(default_cni_network_name: Optional[pulumi.Input[str]] = None,
                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDefaultCniNetworkResult]:
    """
    Get properties of the provided default CNI network.
    Azure REST API version: 2022-12-12-preview.


    :param str default_cni_network_name: The name of the default CNI network.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
