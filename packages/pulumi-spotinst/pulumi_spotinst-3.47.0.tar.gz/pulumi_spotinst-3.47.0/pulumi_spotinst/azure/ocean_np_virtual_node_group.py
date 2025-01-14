# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['OceanNpVirtualNodeGroupArgs', 'OceanNpVirtualNodeGroup']

@pulumi.input_type
class OceanNpVirtualNodeGroupArgs:
    def __init__(__self__, *,
                 ocean_id: pulumi.Input[str],
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enable_node_public_ip: Optional[pulumi.Input[bool]] = None,
                 fallback_to_ondemand: Optional[pulumi.Input[bool]] = None,
                 filters: Optional[pulumi.Input['OceanNpVirtualNodeGroupFiltersArgs']] = None,
                 headrooms: Optional[pulumi.Input[Sequence[pulumi.Input['OceanNpVirtualNodeGroupHeadroomArgs']]]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 max_count: Optional[pulumi.Input[int]] = None,
                 max_pods_per_node: Optional[pulumi.Input[int]] = None,
                 min_count: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 os_disk_size_gb: Optional[pulumi.Input[int]] = None,
                 os_disk_type: Optional[pulumi.Input[str]] = None,
                 os_sku: Optional[pulumi.Input[str]] = None,
                 os_type: Optional[pulumi.Input[str]] = None,
                 spot_percentage: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 taints: Optional[pulumi.Input[Sequence[pulumi.Input['OceanNpVirtualNodeGroupTaintArgs']]]] = None):
        """
        The set of arguments for constructing a OceanNpVirtualNodeGroup resource.
        """
        pulumi.set(__self__, "ocean_id", ocean_id)
        if availability_zones is not None:
            pulumi.set(__self__, "availability_zones", availability_zones)
        if enable_node_public_ip is not None:
            pulumi.set(__self__, "enable_node_public_ip", enable_node_public_ip)
        if fallback_to_ondemand is not None:
            pulumi.set(__self__, "fallback_to_ondemand", fallback_to_ondemand)
        if filters is not None:
            pulumi.set(__self__, "filters", filters)
        if headrooms is not None:
            pulumi.set(__self__, "headrooms", headrooms)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if max_count is not None:
            pulumi.set(__self__, "max_count", max_count)
        if max_pods_per_node is not None:
            pulumi.set(__self__, "max_pods_per_node", max_pods_per_node)
        if min_count is not None:
            pulumi.set(__self__, "min_count", min_count)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if os_disk_size_gb is not None:
            pulumi.set(__self__, "os_disk_size_gb", os_disk_size_gb)
        if os_disk_type is not None:
            pulumi.set(__self__, "os_disk_type", os_disk_type)
        if os_sku is not None:
            pulumi.set(__self__, "os_sku", os_sku)
        if os_type is not None:
            pulumi.set(__self__, "os_type", os_type)
        if spot_percentage is not None:
            pulumi.set(__self__, "spot_percentage", spot_percentage)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if taints is not None:
            pulumi.set(__self__, "taints", taints)

    @property
    @pulumi.getter(name="oceanId")
    def ocean_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "ocean_id")

    @ocean_id.setter
    def ocean_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "ocean_id", value)

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "availability_zones")

    @availability_zones.setter
    def availability_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "availability_zones", value)

    @property
    @pulumi.getter(name="enableNodePublicIp")
    def enable_node_public_ip(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enable_node_public_ip")

    @enable_node_public_ip.setter
    def enable_node_public_ip(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_node_public_ip", value)

    @property
    @pulumi.getter(name="fallbackToOndemand")
    def fallback_to_ondemand(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "fallback_to_ondemand")

    @fallback_to_ondemand.setter
    def fallback_to_ondemand(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "fallback_to_ondemand", value)

    @property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input['OceanNpVirtualNodeGroupFiltersArgs']]:
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: Optional[pulumi.Input['OceanNpVirtualNodeGroupFiltersArgs']]):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter
    def headrooms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OceanNpVirtualNodeGroupHeadroomArgs']]]]:
        return pulumi.get(self, "headrooms")

    @headrooms.setter
    def headrooms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OceanNpVirtualNodeGroupHeadroomArgs']]]]):
        pulumi.set(self, "headrooms", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "max_count")

    @max_count.setter
    def max_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_count", value)

    @property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "max_pods_per_node")

    @max_pods_per_node.setter
    def max_pods_per_node(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_pods_per_node", value)

    @property
    @pulumi.getter(name="minCount")
    def min_count(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "min_count")

    @min_count.setter
    def min_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_count", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="osDiskSizeGb")
    def os_disk_size_gb(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "os_disk_size_gb")

    @os_disk_size_gb.setter
    def os_disk_size_gb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "os_disk_size_gb", value)

    @property
    @pulumi.getter(name="osDiskType")
    def os_disk_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "os_disk_type")

    @os_disk_type.setter
    def os_disk_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "os_disk_type", value)

    @property
    @pulumi.getter(name="osSku")
    def os_sku(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "os_sku")

    @os_sku.setter
    def os_sku(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "os_sku", value)

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "os_type")

    @os_type.setter
    def os_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "os_type", value)

    @property
    @pulumi.getter(name="spotPercentage")
    def spot_percentage(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "spot_percentage")

    @spot_percentage.setter
    def spot_percentage(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "spot_percentage", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def taints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OceanNpVirtualNodeGroupTaintArgs']]]]:
        return pulumi.get(self, "taints")

    @taints.setter
    def taints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OceanNpVirtualNodeGroupTaintArgs']]]]):
        pulumi.set(self, "taints", value)


@pulumi.input_type
class _OceanNpVirtualNodeGroupState:
    def __init__(__self__, *,
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enable_node_public_ip: Optional[pulumi.Input[bool]] = None,
                 fallback_to_ondemand: Optional[pulumi.Input[bool]] = None,
                 filters: Optional[pulumi.Input['OceanNpVirtualNodeGroupFiltersArgs']] = None,
                 headrooms: Optional[pulumi.Input[Sequence[pulumi.Input['OceanNpVirtualNodeGroupHeadroomArgs']]]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 max_count: Optional[pulumi.Input[int]] = None,
                 max_pods_per_node: Optional[pulumi.Input[int]] = None,
                 min_count: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ocean_id: Optional[pulumi.Input[str]] = None,
                 os_disk_size_gb: Optional[pulumi.Input[int]] = None,
                 os_disk_type: Optional[pulumi.Input[str]] = None,
                 os_sku: Optional[pulumi.Input[str]] = None,
                 os_type: Optional[pulumi.Input[str]] = None,
                 spot_percentage: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 taints: Optional[pulumi.Input[Sequence[pulumi.Input['OceanNpVirtualNodeGroupTaintArgs']]]] = None):
        """
        Input properties used for looking up and filtering OceanNpVirtualNodeGroup resources.
        """
        if availability_zones is not None:
            pulumi.set(__self__, "availability_zones", availability_zones)
        if enable_node_public_ip is not None:
            pulumi.set(__self__, "enable_node_public_ip", enable_node_public_ip)
        if fallback_to_ondemand is not None:
            pulumi.set(__self__, "fallback_to_ondemand", fallback_to_ondemand)
        if filters is not None:
            pulumi.set(__self__, "filters", filters)
        if headrooms is not None:
            pulumi.set(__self__, "headrooms", headrooms)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if max_count is not None:
            pulumi.set(__self__, "max_count", max_count)
        if max_pods_per_node is not None:
            pulumi.set(__self__, "max_pods_per_node", max_pods_per_node)
        if min_count is not None:
            pulumi.set(__self__, "min_count", min_count)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if ocean_id is not None:
            pulumi.set(__self__, "ocean_id", ocean_id)
        if os_disk_size_gb is not None:
            pulumi.set(__self__, "os_disk_size_gb", os_disk_size_gb)
        if os_disk_type is not None:
            pulumi.set(__self__, "os_disk_type", os_disk_type)
        if os_sku is not None:
            pulumi.set(__self__, "os_sku", os_sku)
        if os_type is not None:
            pulumi.set(__self__, "os_type", os_type)
        if spot_percentage is not None:
            pulumi.set(__self__, "spot_percentage", spot_percentage)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if taints is not None:
            pulumi.set(__self__, "taints", taints)

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "availability_zones")

    @availability_zones.setter
    def availability_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "availability_zones", value)

    @property
    @pulumi.getter(name="enableNodePublicIp")
    def enable_node_public_ip(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enable_node_public_ip")

    @enable_node_public_ip.setter
    def enable_node_public_ip(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_node_public_ip", value)

    @property
    @pulumi.getter(name="fallbackToOndemand")
    def fallback_to_ondemand(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "fallback_to_ondemand")

    @fallback_to_ondemand.setter
    def fallback_to_ondemand(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "fallback_to_ondemand", value)

    @property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input['OceanNpVirtualNodeGroupFiltersArgs']]:
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: Optional[pulumi.Input['OceanNpVirtualNodeGroupFiltersArgs']]):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter
    def headrooms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OceanNpVirtualNodeGroupHeadroomArgs']]]]:
        return pulumi.get(self, "headrooms")

    @headrooms.setter
    def headrooms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OceanNpVirtualNodeGroupHeadroomArgs']]]]):
        pulumi.set(self, "headrooms", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "max_count")

    @max_count.setter
    def max_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_count", value)

    @property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "max_pods_per_node")

    @max_pods_per_node.setter
    def max_pods_per_node(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_pods_per_node", value)

    @property
    @pulumi.getter(name="minCount")
    def min_count(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "min_count")

    @min_count.setter
    def min_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_count", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="oceanId")
    def ocean_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ocean_id")

    @ocean_id.setter
    def ocean_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ocean_id", value)

    @property
    @pulumi.getter(name="osDiskSizeGb")
    def os_disk_size_gb(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "os_disk_size_gb")

    @os_disk_size_gb.setter
    def os_disk_size_gb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "os_disk_size_gb", value)

    @property
    @pulumi.getter(name="osDiskType")
    def os_disk_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "os_disk_type")

    @os_disk_type.setter
    def os_disk_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "os_disk_type", value)

    @property
    @pulumi.getter(name="osSku")
    def os_sku(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "os_sku")

    @os_sku.setter
    def os_sku(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "os_sku", value)

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "os_type")

    @os_type.setter
    def os_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "os_type", value)

    @property
    @pulumi.getter(name="spotPercentage")
    def spot_percentage(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "spot_percentage")

    @spot_percentage.setter
    def spot_percentage(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "spot_percentage", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def taints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OceanNpVirtualNodeGroupTaintArgs']]]]:
        return pulumi.get(self, "taints")

    @taints.setter
    def taints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OceanNpVirtualNodeGroupTaintArgs']]]]):
        pulumi.set(self, "taints", value)


class OceanNpVirtualNodeGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enable_node_public_ip: Optional[pulumi.Input[bool]] = None,
                 fallback_to_ondemand: Optional[pulumi.Input[bool]] = None,
                 filters: Optional[pulumi.Input[pulumi.InputType['OceanNpVirtualNodeGroupFiltersArgs']]] = None,
                 headrooms: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OceanNpVirtualNodeGroupHeadroomArgs']]]]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 max_count: Optional[pulumi.Input[int]] = None,
                 max_pods_per_node: Optional[pulumi.Input[int]] = None,
                 min_count: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ocean_id: Optional[pulumi.Input[str]] = None,
                 os_disk_size_gb: Optional[pulumi.Input[int]] = None,
                 os_disk_type: Optional[pulumi.Input[str]] = None,
                 os_sku: Optional[pulumi.Input[str]] = None,
                 os_type: Optional[pulumi.Input[str]] = None,
                 spot_percentage: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 taints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OceanNpVirtualNodeGroupTaintArgs']]]]] = None,
                 __props__=None):
        """
        Create a OceanNpVirtualNodeGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OceanNpVirtualNodeGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a OceanNpVirtualNodeGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param OceanNpVirtualNodeGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OceanNpVirtualNodeGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enable_node_public_ip: Optional[pulumi.Input[bool]] = None,
                 fallback_to_ondemand: Optional[pulumi.Input[bool]] = None,
                 filters: Optional[pulumi.Input[pulumi.InputType['OceanNpVirtualNodeGroupFiltersArgs']]] = None,
                 headrooms: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OceanNpVirtualNodeGroupHeadroomArgs']]]]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 max_count: Optional[pulumi.Input[int]] = None,
                 max_pods_per_node: Optional[pulumi.Input[int]] = None,
                 min_count: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ocean_id: Optional[pulumi.Input[str]] = None,
                 os_disk_size_gb: Optional[pulumi.Input[int]] = None,
                 os_disk_type: Optional[pulumi.Input[str]] = None,
                 os_sku: Optional[pulumi.Input[str]] = None,
                 os_type: Optional[pulumi.Input[str]] = None,
                 spot_percentage: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 taints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OceanNpVirtualNodeGroupTaintArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OceanNpVirtualNodeGroupArgs.__new__(OceanNpVirtualNodeGroupArgs)

            __props__.__dict__["availability_zones"] = availability_zones
            __props__.__dict__["enable_node_public_ip"] = enable_node_public_ip
            __props__.__dict__["fallback_to_ondemand"] = fallback_to_ondemand
            __props__.__dict__["filters"] = filters
            __props__.__dict__["headrooms"] = headrooms
            __props__.__dict__["labels"] = labels
            __props__.__dict__["max_count"] = max_count
            __props__.__dict__["max_pods_per_node"] = max_pods_per_node
            __props__.__dict__["min_count"] = min_count
            __props__.__dict__["name"] = name
            if ocean_id is None and not opts.urn:
                raise TypeError("Missing required property 'ocean_id'")
            __props__.__dict__["ocean_id"] = ocean_id
            __props__.__dict__["os_disk_size_gb"] = os_disk_size_gb
            __props__.__dict__["os_disk_type"] = os_disk_type
            __props__.__dict__["os_sku"] = os_sku
            __props__.__dict__["os_type"] = os_type
            __props__.__dict__["spot_percentage"] = spot_percentage
            __props__.__dict__["tags"] = tags
            __props__.__dict__["taints"] = taints
        super(OceanNpVirtualNodeGroup, __self__).__init__(
            'spotinst:azure/oceanNpVirtualNodeGroup:OceanNpVirtualNodeGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            enable_node_public_ip: Optional[pulumi.Input[bool]] = None,
            fallback_to_ondemand: Optional[pulumi.Input[bool]] = None,
            filters: Optional[pulumi.Input[pulumi.InputType['OceanNpVirtualNodeGroupFiltersArgs']]] = None,
            headrooms: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OceanNpVirtualNodeGroupHeadroomArgs']]]]] = None,
            labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            max_count: Optional[pulumi.Input[int]] = None,
            max_pods_per_node: Optional[pulumi.Input[int]] = None,
            min_count: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            ocean_id: Optional[pulumi.Input[str]] = None,
            os_disk_size_gb: Optional[pulumi.Input[int]] = None,
            os_disk_type: Optional[pulumi.Input[str]] = None,
            os_sku: Optional[pulumi.Input[str]] = None,
            os_type: Optional[pulumi.Input[str]] = None,
            spot_percentage: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            taints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OceanNpVirtualNodeGroupTaintArgs']]]]] = None) -> 'OceanNpVirtualNodeGroup':
        """
        Get an existing OceanNpVirtualNodeGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OceanNpVirtualNodeGroupState.__new__(_OceanNpVirtualNodeGroupState)

        __props__.__dict__["availability_zones"] = availability_zones
        __props__.__dict__["enable_node_public_ip"] = enable_node_public_ip
        __props__.__dict__["fallback_to_ondemand"] = fallback_to_ondemand
        __props__.__dict__["filters"] = filters
        __props__.__dict__["headrooms"] = headrooms
        __props__.__dict__["labels"] = labels
        __props__.__dict__["max_count"] = max_count
        __props__.__dict__["max_pods_per_node"] = max_pods_per_node
        __props__.__dict__["min_count"] = min_count
        __props__.__dict__["name"] = name
        __props__.__dict__["ocean_id"] = ocean_id
        __props__.__dict__["os_disk_size_gb"] = os_disk_size_gb
        __props__.__dict__["os_disk_type"] = os_disk_type
        __props__.__dict__["os_sku"] = os_sku
        __props__.__dict__["os_type"] = os_type
        __props__.__dict__["spot_percentage"] = spot_percentage
        __props__.__dict__["tags"] = tags
        __props__.__dict__["taints"] = taints
        return OceanNpVirtualNodeGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter(name="enableNodePublicIp")
    def enable_node_public_ip(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "enable_node_public_ip")

    @property
    @pulumi.getter(name="fallbackToOndemand")
    def fallback_to_ondemand(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "fallback_to_ondemand")

    @property
    @pulumi.getter
    def filters(self) -> pulumi.Output[Optional['outputs.OceanNpVirtualNodeGroupFilters']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def headrooms(self) -> pulumi.Output[Optional[Sequence['outputs.OceanNpVirtualNodeGroupHeadroom']]]:
        return pulumi.get(self, "headrooms")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "max_count")

    @property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "max_pods_per_node")

    @property
    @pulumi.getter(name="minCount")
    def min_count(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "min_count")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="oceanId")
    def ocean_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "ocean_id")

    @property
    @pulumi.getter(name="osDiskSizeGb")
    def os_disk_size_gb(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "os_disk_size_gb")

    @property
    @pulumi.getter(name="osDiskType")
    def os_disk_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "os_disk_type")

    @property
    @pulumi.getter(name="osSku")
    def os_sku(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "os_sku")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter(name="spotPercentage")
    def spot_percentage(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "spot_percentage")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def taints(self) -> pulumi.Output[Optional[Sequence['outputs.OceanNpVirtualNodeGroupTaint']]]:
        return pulumi.get(self, "taints")

