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

__all__ = ['BackendSetArgs', 'BackendSet']

@pulumi.input_type
class BackendSetArgs:
    def __init__(__self__, *,
                 health_checker: pulumi.Input['BackendSetHealthCheckerArgs'],
                 network_load_balancer_id: pulumi.Input[str],
                 policy: pulumi.Input[str],
                 ip_version: Optional[pulumi.Input[str]] = None,
                 is_preserve_source: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BackendSet resource.
        :param pulumi.Input['BackendSetHealthCheckerArgs'] health_checker: (Updatable) The health check policy configuration. For more information, see [Editing Health Check Policies](https://docs.cloud.oracle.com/iaas/Content/Balance/Tasks/editinghealthcheck.htm).
        :param pulumi.Input[str] network_load_balancer_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        :param pulumi.Input[str] policy: (Updatable) The network load balancer policy for the backend set.  Example: `FIVE_TUPLE`` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] ip_version: (Updatable) IP version associated with the backend set.
        :param pulumi.Input[bool] is_preserve_source: (Updatable) If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends. Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this parameter cannot be disabled. The value is true by default.
        :param pulumi.Input[str] name: A user-friendly name for the backend set that must be unique and cannot be changed.
               
               Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot contain spaces. Avoid entering confidential information.
               
               Example: `example_backend_set`
        """
        pulumi.set(__self__, "health_checker", health_checker)
        pulumi.set(__self__, "network_load_balancer_id", network_load_balancer_id)
        pulumi.set(__self__, "policy", policy)
        if ip_version is not None:
            pulumi.set(__self__, "ip_version", ip_version)
        if is_preserve_source is not None:
            pulumi.set(__self__, "is_preserve_source", is_preserve_source)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="healthChecker")
    def health_checker(self) -> pulumi.Input['BackendSetHealthCheckerArgs']:
        """
        (Updatable) The health check policy configuration. For more information, see [Editing Health Check Policies](https://docs.cloud.oracle.com/iaas/Content/Balance/Tasks/editinghealthcheck.htm).
        """
        return pulumi.get(self, "health_checker")

    @health_checker.setter
    def health_checker(self, value: pulumi.Input['BackendSetHealthCheckerArgs']):
        pulumi.set(self, "health_checker", value)

    @property
    @pulumi.getter(name="networkLoadBalancerId")
    def network_load_balancer_id(self) -> pulumi.Input[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        """
        return pulumi.get(self, "network_load_balancer_id")

    @network_load_balancer_id.setter
    def network_load_balancer_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_load_balancer_id", value)

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Input[str]:
        """
        (Updatable) The network load balancer policy for the backend set.  Example: `FIVE_TUPLE`` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) IP version associated with the backend set.
        """
        return pulumi.get(self, "ip_version")

    @ip_version.setter
    def ip_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_version", value)

    @property
    @pulumi.getter(name="isPreserveSource")
    def is_preserve_source(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends. Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this parameter cannot be disabled. The value is true by default.
        """
        return pulumi.get(self, "is_preserve_source")

    @is_preserve_source.setter
    def is_preserve_source(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_preserve_source", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A user-friendly name for the backend set that must be unique and cannot be changed.

        Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot contain spaces. Avoid entering confidential information.

        Example: `example_backend_set`
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _BackendSetState:
    def __init__(__self__, *,
                 backends: Optional[pulumi.Input[Sequence[pulumi.Input['BackendSetBackendArgs']]]] = None,
                 health_checker: Optional[pulumi.Input['BackendSetHealthCheckerArgs']] = None,
                 ip_version: Optional[pulumi.Input[str]] = None,
                 is_preserve_source: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_load_balancer_id: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BackendSet resources.
        :param pulumi.Input[Sequence[pulumi.Input['BackendSetBackendArgs']]] backends: Array of backends.
        :param pulumi.Input['BackendSetHealthCheckerArgs'] health_checker: (Updatable) The health check policy configuration. For more information, see [Editing Health Check Policies](https://docs.cloud.oracle.com/iaas/Content/Balance/Tasks/editinghealthcheck.htm).
        :param pulumi.Input[str] ip_version: (Updatable) IP version associated with the backend set.
        :param pulumi.Input[bool] is_preserve_source: (Updatable) If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends. Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this parameter cannot be disabled. The value is true by default.
        :param pulumi.Input[str] name: A user-friendly name for the backend set that must be unique and cannot be changed.
               
               Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot contain spaces. Avoid entering confidential information.
               
               Example: `example_backend_set`
        :param pulumi.Input[str] network_load_balancer_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        :param pulumi.Input[str] policy: (Updatable) The network load balancer policy for the backend set.  Example: `FIVE_TUPLE`` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        if backends is not None:
            pulumi.set(__self__, "backends", backends)
        if health_checker is not None:
            pulumi.set(__self__, "health_checker", health_checker)
        if ip_version is not None:
            pulumi.set(__self__, "ip_version", ip_version)
        if is_preserve_source is not None:
            pulumi.set(__self__, "is_preserve_source", is_preserve_source)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_load_balancer_id is not None:
            pulumi.set(__self__, "network_load_balancer_id", network_load_balancer_id)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)

    @property
    @pulumi.getter
    def backends(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BackendSetBackendArgs']]]]:
        """
        Array of backends.
        """
        return pulumi.get(self, "backends")

    @backends.setter
    def backends(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BackendSetBackendArgs']]]]):
        pulumi.set(self, "backends", value)

    @property
    @pulumi.getter(name="healthChecker")
    def health_checker(self) -> Optional[pulumi.Input['BackendSetHealthCheckerArgs']]:
        """
        (Updatable) The health check policy configuration. For more information, see [Editing Health Check Policies](https://docs.cloud.oracle.com/iaas/Content/Balance/Tasks/editinghealthcheck.htm).
        """
        return pulumi.get(self, "health_checker")

    @health_checker.setter
    def health_checker(self, value: Optional[pulumi.Input['BackendSetHealthCheckerArgs']]):
        pulumi.set(self, "health_checker", value)

    @property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) IP version associated with the backend set.
        """
        return pulumi.get(self, "ip_version")

    @ip_version.setter
    def ip_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_version", value)

    @property
    @pulumi.getter(name="isPreserveSource")
    def is_preserve_source(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends. Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this parameter cannot be disabled. The value is true by default.
        """
        return pulumi.get(self, "is_preserve_source")

    @is_preserve_source.setter
    def is_preserve_source(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_preserve_source", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A user-friendly name for the backend set that must be unique and cannot be changed.

        Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot contain spaces. Avoid entering confidential information.

        Example: `example_backend_set`
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkLoadBalancerId")
    def network_load_balancer_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        """
        return pulumi.get(self, "network_load_balancer_id")

    @network_load_balancer_id.setter
    def network_load_balancer_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_load_balancer_id", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The network load balancer policy for the backend set.  Example: `FIVE_TUPLE`` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy", value)


class BackendSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 health_checker: Optional[pulumi.Input[pulumi.InputType['BackendSetHealthCheckerArgs']]] = None,
                 ip_version: Optional[pulumi.Input[str]] = None,
                 is_preserve_source: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_load_balancer_id: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Backend Set resource in Oracle Cloud Infrastructure Network Load Balancer service.

        Adds a backend set to a network load balancer.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_backend_set = oci.network_load_balancer.BackendSet("testBackendSet",
            health_checker=oci.network_load_balancer.BackendSetHealthCheckerArgs(
                protocol=var["backend_set_health_checker_protocol"],
                interval_in_millis=var["backend_set_health_checker_interval_in_millis"],
                port=var["backend_set_health_checker_port"],
                request_data=var["backend_set_health_checker_request_data"],
                response_body_regex=var["backend_set_health_checker_response_body_regex"],
                response_data=var["backend_set_health_checker_response_data"],
                retries=var["backend_set_health_checker_retries"],
                return_code=var["backend_set_health_checker_return_code"],
                timeout_in_millis=var["backend_set_health_checker_timeout_in_millis"],
                url_path=var["backend_set_health_checker_url_path"],
            ),
            network_load_balancer_id=oci_network_load_balancer_network_load_balancer["test_network_load_balancer"]["id"],
            policy=var["backend_set_policy"],
            ip_version=var["backend_set_ip_version"],
            is_preserve_source=var["backend_set_is_preserve_source"])
        ```

        ## Import

        BackendSets can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:NetworkLoadBalancer/backendSet:BackendSet test_backend_set "networkLoadBalancers/{networkLoadBalancerId}/backendSets/{backendSetName}"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['BackendSetHealthCheckerArgs']] health_checker: (Updatable) The health check policy configuration. For more information, see [Editing Health Check Policies](https://docs.cloud.oracle.com/iaas/Content/Balance/Tasks/editinghealthcheck.htm).
        :param pulumi.Input[str] ip_version: (Updatable) IP version associated with the backend set.
        :param pulumi.Input[bool] is_preserve_source: (Updatable) If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends. Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this parameter cannot be disabled. The value is true by default.
        :param pulumi.Input[str] name: A user-friendly name for the backend set that must be unique and cannot be changed.
               
               Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot contain spaces. Avoid entering confidential information.
               
               Example: `example_backend_set`
        :param pulumi.Input[str] network_load_balancer_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        :param pulumi.Input[str] policy: (Updatable) The network load balancer policy for the backend set.  Example: `FIVE_TUPLE`` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BackendSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Backend Set resource in Oracle Cloud Infrastructure Network Load Balancer service.

        Adds a backend set to a network load balancer.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_backend_set = oci.network_load_balancer.BackendSet("testBackendSet",
            health_checker=oci.network_load_balancer.BackendSetHealthCheckerArgs(
                protocol=var["backend_set_health_checker_protocol"],
                interval_in_millis=var["backend_set_health_checker_interval_in_millis"],
                port=var["backend_set_health_checker_port"],
                request_data=var["backend_set_health_checker_request_data"],
                response_body_regex=var["backend_set_health_checker_response_body_regex"],
                response_data=var["backend_set_health_checker_response_data"],
                retries=var["backend_set_health_checker_retries"],
                return_code=var["backend_set_health_checker_return_code"],
                timeout_in_millis=var["backend_set_health_checker_timeout_in_millis"],
                url_path=var["backend_set_health_checker_url_path"],
            ),
            network_load_balancer_id=oci_network_load_balancer_network_load_balancer["test_network_load_balancer"]["id"],
            policy=var["backend_set_policy"],
            ip_version=var["backend_set_ip_version"],
            is_preserve_source=var["backend_set_is_preserve_source"])
        ```

        ## Import

        BackendSets can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:NetworkLoadBalancer/backendSet:BackendSet test_backend_set "networkLoadBalancers/{networkLoadBalancerId}/backendSets/{backendSetName}"
        ```

        :param str resource_name: The name of the resource.
        :param BackendSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BackendSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 health_checker: Optional[pulumi.Input[pulumi.InputType['BackendSetHealthCheckerArgs']]] = None,
                 ip_version: Optional[pulumi.Input[str]] = None,
                 is_preserve_source: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_load_balancer_id: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BackendSetArgs.__new__(BackendSetArgs)

            if health_checker is None and not opts.urn:
                raise TypeError("Missing required property 'health_checker'")
            __props__.__dict__["health_checker"] = health_checker
            __props__.__dict__["ip_version"] = ip_version
            __props__.__dict__["is_preserve_source"] = is_preserve_source
            __props__.__dict__["name"] = name
            if network_load_balancer_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_load_balancer_id'")
            __props__.__dict__["network_load_balancer_id"] = network_load_balancer_id
            if policy is None and not opts.urn:
                raise TypeError("Missing required property 'policy'")
            __props__.__dict__["policy"] = policy
            __props__.__dict__["backends"] = None
        super(BackendSet, __self__).__init__(
            'oci:NetworkLoadBalancer/backendSet:BackendSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            backends: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BackendSetBackendArgs']]]]] = None,
            health_checker: Optional[pulumi.Input[pulumi.InputType['BackendSetHealthCheckerArgs']]] = None,
            ip_version: Optional[pulumi.Input[str]] = None,
            is_preserve_source: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_load_balancer_id: Optional[pulumi.Input[str]] = None,
            policy: Optional[pulumi.Input[str]] = None) -> 'BackendSet':
        """
        Get an existing BackendSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BackendSetBackendArgs']]]] backends: Array of backends.
        :param pulumi.Input[pulumi.InputType['BackendSetHealthCheckerArgs']] health_checker: (Updatable) The health check policy configuration. For more information, see [Editing Health Check Policies](https://docs.cloud.oracle.com/iaas/Content/Balance/Tasks/editinghealthcheck.htm).
        :param pulumi.Input[str] ip_version: (Updatable) IP version associated with the backend set.
        :param pulumi.Input[bool] is_preserve_source: (Updatable) If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends. Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this parameter cannot be disabled. The value is true by default.
        :param pulumi.Input[str] name: A user-friendly name for the backend set that must be unique and cannot be changed.
               
               Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot contain spaces. Avoid entering confidential information.
               
               Example: `example_backend_set`
        :param pulumi.Input[str] network_load_balancer_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        :param pulumi.Input[str] policy: (Updatable) The network load balancer policy for the backend set.  Example: `FIVE_TUPLE`` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BackendSetState.__new__(_BackendSetState)

        __props__.__dict__["backends"] = backends
        __props__.__dict__["health_checker"] = health_checker
        __props__.__dict__["ip_version"] = ip_version
        __props__.__dict__["is_preserve_source"] = is_preserve_source
        __props__.__dict__["name"] = name
        __props__.__dict__["network_load_balancer_id"] = network_load_balancer_id
        __props__.__dict__["policy"] = policy
        return BackendSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def backends(self) -> pulumi.Output[Sequence['outputs.BackendSetBackend']]:
        """
        Array of backends.
        """
        return pulumi.get(self, "backends")

    @property
    @pulumi.getter(name="healthChecker")
    def health_checker(self) -> pulumi.Output['outputs.BackendSetHealthChecker']:
        """
        (Updatable) The health check policy configuration. For more information, see [Editing Health Check Policies](https://docs.cloud.oracle.com/iaas/Content/Balance/Tasks/editinghealthcheck.htm).
        """
        return pulumi.get(self, "health_checker")

    @property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> pulumi.Output[str]:
        """
        (Updatable) IP version associated with the backend set.
        """
        return pulumi.get(self, "ip_version")

    @property
    @pulumi.getter(name="isPreserveSource")
    def is_preserve_source(self) -> pulumi.Output[bool]:
        """
        (Updatable) If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends. Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this parameter cannot be disabled. The value is true by default.
        """
        return pulumi.get(self, "is_preserve_source")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A user-friendly name for the backend set that must be unique and cannot be changed.

        Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot contain spaces. Avoid entering confidential information.

        Example: `example_backend_set`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkLoadBalancerId")
    def network_load_balancer_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        """
        return pulumi.get(self, "network_load_balancer_id")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[str]:
        """
        (Updatable) The network load balancer policy for the backend set.  Example: `FIVE_TUPLE`` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "policy")

