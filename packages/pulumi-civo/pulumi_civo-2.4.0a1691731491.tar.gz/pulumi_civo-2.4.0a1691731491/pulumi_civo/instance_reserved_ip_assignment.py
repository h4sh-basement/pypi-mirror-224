# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['InstanceReservedIpAssignmentArgs', 'InstanceReservedIpAssignment']

@pulumi.input_type
class InstanceReservedIpAssignmentArgs:
    def __init__(__self__, *,
                 instance_id: pulumi.Input[str],
                 reserved_ip_id: pulumi.Input[str],
                 region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a InstanceReservedIpAssignment resource.
        :param pulumi.Input[str] instance_id: The instance id
        :param pulumi.Input[str] reserved_ip_id: The reserved ip id
        :param pulumi.Input[str] region: The region of the ip
        """
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "reserved_ip_id", reserved_ip_id)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[str]:
        """
        The instance id
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="reservedIpId")
    def reserved_ip_id(self) -> pulumi.Input[str]:
        """
        The reserved ip id
        """
        return pulumi.get(self, "reserved_ip_id")

    @reserved_ip_id.setter
    def reserved_ip_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "reserved_ip_id", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region of the ip
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class _InstanceReservedIpAssignmentState:
    def __init__(__self__, *,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 reserved_ip_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering InstanceReservedIpAssignment resources.
        :param pulumi.Input[str] instance_id: The instance id
        :param pulumi.Input[str] region: The region of the ip
        :param pulumi.Input[str] reserved_ip_id: The reserved ip id
        """
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if reserved_ip_id is not None:
            pulumi.set(__self__, "reserved_ip_id", reserved_ip_id)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The instance id
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region of the ip
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="reservedIpId")
    def reserved_ip_id(self) -> Optional[pulumi.Input[str]]:
        """
        The reserved ip id
        """
        return pulumi.get(self, "reserved_ip_id")

    @reserved_ip_id.setter
    def reserved_ip_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reserved_ip_id", value)


class InstanceReservedIpAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 reserved_ip_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The instance reserved ip assignment resource schema definition

        ## Example Usage

        ```python
        import pulumi
        import pulumi_civo as civo

        # Send to create a reserved IP
        www = civo.ReservedIp("www")
        # We assign the reserved IP to the instance
        webserver_www = civo.InstanceReservedIpAssignment("webserver-www",
            instance_id=civo_instance["www"]["id"],
            reserved_ip_id=civo_reserved_ip["web-server"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_id: The instance id
        :param pulumi.Input[str] region: The region of the ip
        :param pulumi.Input[str] reserved_ip_id: The reserved ip id
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceReservedIpAssignmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The instance reserved ip assignment resource schema definition

        ## Example Usage

        ```python
        import pulumi
        import pulumi_civo as civo

        # Send to create a reserved IP
        www = civo.ReservedIp("www")
        # We assign the reserved IP to the instance
        webserver_www = civo.InstanceReservedIpAssignment("webserver-www",
            instance_id=civo_instance["www"]["id"],
            reserved_ip_id=civo_reserved_ip["web-server"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param InstanceReservedIpAssignmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceReservedIpAssignmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 reserved_ip_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InstanceReservedIpAssignmentArgs.__new__(InstanceReservedIpAssignmentArgs)

            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            __props__.__dict__["region"] = region
            if reserved_ip_id is None and not opts.urn:
                raise TypeError("Missing required property 'reserved_ip_id'")
            __props__.__dict__["reserved_ip_id"] = reserved_ip_id
        super(InstanceReservedIpAssignment, __self__).__init__(
            'civo:index/instanceReservedIpAssignment:InstanceReservedIpAssignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            reserved_ip_id: Optional[pulumi.Input[str]] = None) -> 'InstanceReservedIpAssignment':
        """
        Get an existing InstanceReservedIpAssignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_id: The instance id
        :param pulumi.Input[str] region: The region of the ip
        :param pulumi.Input[str] reserved_ip_id: The reserved ip id
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InstanceReservedIpAssignmentState.__new__(_InstanceReservedIpAssignmentState)

        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["region"] = region
        __props__.__dict__["reserved_ip_id"] = reserved_ip_id
        return InstanceReservedIpAssignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        The instance id
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region of the ip
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="reservedIpId")
    def reserved_ip_id(self) -> pulumi.Output[str]:
        """
        The reserved ip id
        """
        return pulumi.get(self, "reserved_ip_id")

