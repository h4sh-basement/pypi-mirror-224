# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ReplicaArgs', 'Replica']

@pulumi.input_type
class ReplicaArgs:
    def __init__(__self__, *,
                 db_system_id: pulumi.Input[str],
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 is_delete_protected: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Replica resource.
        :param pulumi.Input[str] db_system_id: The OCID of the DB System the read replica is associated with.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) User provided description of the read replica.
        :param pulumi.Input[str] display_name: (Updatable) The user-friendly name for the read replica. It does not have to be unique.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[bool] is_delete_protected: (Updatable) Specifies whether the read replica can be deleted. Set to true to prevent deletion, false (default) to allow. Note that if a read replica is delete protected it also prevents the entire DB System from being deleted. If the DB System is delete protected, read replicas can still be deleted individually if they are not delete  protected themselves. 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        pulumi.set(__self__, "db_system_id", db_system_id)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if is_delete_protected is not None:
            pulumi.set(__self__, "is_delete_protected", is_delete_protected)

    @property
    @pulumi.getter(name="dbSystemId")
    def db_system_id(self) -> pulumi.Input[str]:
        """
        The OCID of the DB System the read replica is associated with.
        """
        return pulumi.get(self, "db_system_id")

    @db_system_id.setter
    def db_system_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "db_system_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) User provided description of the read replica.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The user-friendly name for the read replica. It does not have to be unique.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="isDeleteProtected")
    def is_delete_protected(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Specifies whether the read replica can be deleted. Set to true to prevent deletion, false (default) to allow. Note that if a read replica is delete protected it also prevents the entire DB System from being deleted. If the DB System is delete protected, read replicas can still be deleted individually if they are not delete  protected themselves. 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "is_delete_protected")

    @is_delete_protected.setter
    def is_delete_protected(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_delete_protected", value)


@pulumi.input_type
class _ReplicaState:
    def __init__(__self__, *,
                 availability_domain: Optional[pulumi.Input[str]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 db_system_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 fault_domain: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 is_delete_protected: Optional[pulumi.Input[bool]] = None,
                 lifecycle_details: Optional[pulumi.Input[str]] = None,
                 mysql_version: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 port_x: Optional[pulumi.Input[int]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_updated: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Replica resources.
        :param pulumi.Input[str] availability_domain: The name of the Availability Domain the read replica is located in.
        :param pulumi.Input[str] compartment_id: The OCID of the compartment that contains the read replica.
        :param pulumi.Input[str] db_system_id: The OCID of the DB System the read replica is associated with.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) User provided description of the read replica.
        :param pulumi.Input[str] display_name: (Updatable) The user-friendly name for the read replica. It does not have to be unique.
        :param pulumi.Input[str] fault_domain: The name of the Fault Domain the read replica is located in.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[str] ip_address: The IP address the read replica is configured to listen on.
        :param pulumi.Input[bool] is_delete_protected: (Updatable) Specifies whether the read replica can be deleted. Set to true to prevent deletion, false (default) to allow. Note that if a read replica is delete protected it also prevents the entire DB System from being deleted. If the DB System is delete protected, read replicas can still be deleted individually if they are not delete  protected themselves. 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] lifecycle_details: A message describing the state of the read replica.
        :param pulumi.Input[str] mysql_version: The MySQL version used by the read replica.
        :param pulumi.Input[int] port: The port the read replica is configured to listen on.
        :param pulumi.Input[int] port_x: The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.
        :param pulumi.Input[str] state: The state of the read replica.
        :param pulumi.Input[str] time_created: The date and time the read replica was created, as described by [RFC 3339](https://tools.ietf.org/rfc/rfc3339).
        :param pulumi.Input[str] time_updated: The time the read replica was last updated, as described by [RFC 3339](https://tools.ietf.org/rfc/rfc3339).
        """
        if availability_domain is not None:
            pulumi.set(__self__, "availability_domain", availability_domain)
        if compartment_id is not None:
            pulumi.set(__self__, "compartment_id", compartment_id)
        if db_system_id is not None:
            pulumi.set(__self__, "db_system_id", db_system_id)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if fault_domain is not None:
            pulumi.set(__self__, "fault_domain", fault_domain)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if ip_address is not None:
            pulumi.set(__self__, "ip_address", ip_address)
        if is_delete_protected is not None:
            pulumi.set(__self__, "is_delete_protected", is_delete_protected)
        if lifecycle_details is not None:
            pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if mysql_version is not None:
            pulumi.set(__self__, "mysql_version", mysql_version)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if port_x is not None:
            pulumi.set(__self__, "port_x", port_x)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if time_created is not None:
            pulumi.set(__self__, "time_created", time_created)
        if time_updated is not None:
            pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="availabilityDomain")
    def availability_domain(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Availability Domain the read replica is located in.
        """
        return pulumi.get(self, "availability_domain")

    @availability_domain.setter
    def availability_domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_domain", value)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The OCID of the compartment that contains the read replica.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="dbSystemId")
    def db_system_id(self) -> Optional[pulumi.Input[str]]:
        """
        The OCID of the DB System the read replica is associated with.
        """
        return pulumi.get(self, "db_system_id")

    @db_system_id.setter
    def db_system_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "db_system_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) User provided description of the read replica.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The user-friendly name for the read replica. It does not have to be unique.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="faultDomain")
    def fault_domain(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Fault Domain the read replica is located in.
        """
        return pulumi.get(self, "fault_domain")

    @fault_domain.setter
    def fault_domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fault_domain", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address the read replica is configured to listen on.
        """
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_address", value)

    @property
    @pulumi.getter(name="isDeleteProtected")
    def is_delete_protected(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Specifies whether the read replica can be deleted. Set to true to prevent deletion, false (default) to allow. Note that if a read replica is delete protected it also prevents the entire DB System from being deleted. If the DB System is delete protected, read replicas can still be deleted individually if they are not delete  protected themselves. 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "is_delete_protected")

    @is_delete_protected.setter
    def is_delete_protected(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_delete_protected", value)

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[str]]:
        """
        A message describing the state of the read replica.
        """
        return pulumi.get(self, "lifecycle_details")

    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_details", value)

    @property
    @pulumi.getter(name="mysqlVersion")
    def mysql_version(self) -> Optional[pulumi.Input[str]]:
        """
        The MySQL version used by the read replica.
        """
        return pulumi.get(self, "mysql_version")

    @mysql_version.setter
    def mysql_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mysql_version", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        The port the read replica is configured to listen on.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="portX")
    def port_x(self) -> Optional[pulumi.Input[int]]:
        """
        The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.
        """
        return pulumi.get(self, "port_x")

    @port_x.setter
    def port_x(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port_x", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The state of the read replica.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time the read replica was created, as described by [RFC 3339](https://tools.ietf.org/rfc/rfc3339).
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> Optional[pulumi.Input[str]]:
        """
        The time the read replica was last updated, as described by [RFC 3339](https://tools.ietf.org/rfc/rfc3339).
        """
        return pulumi.get(self, "time_updated")

    @time_updated.setter
    def time_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_updated", value)


class Replica(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 db_system_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 is_delete_protected: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        This resource provides the Replica resource in Oracle Cloud Infrastructure MySQL Database service.

        Creates a DB System read replica.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_replica = oci.mysql.Replica("testReplica",
            db_system_id=oci_mysql_mysql_db_system["test_mysql_db_system"]["id"],
            defined_tags={
                "foo-namespace.bar-key": "value",
            },
            description=var["replica_description"],
            display_name=var["replica_display_name"],
            freeform_tags={
                "bar-key": "value",
            },
            is_delete_protected=var["replica_is_delete_protected"])
        ```

        ## Import

        Replicas can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:Mysql/replica:Replica test_replica "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] db_system_id: The OCID of the DB System the read replica is associated with.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) User provided description of the read replica.
        :param pulumi.Input[str] display_name: (Updatable) The user-friendly name for the read replica. It does not have to be unique.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[bool] is_delete_protected: (Updatable) Specifies whether the read replica can be deleted. Set to true to prevent deletion, false (default) to allow. Note that if a read replica is delete protected it also prevents the entire DB System from being deleted. If the DB System is delete protected, read replicas can still be deleted individually if they are not delete  protected themselves. 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReplicaArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Replica resource in Oracle Cloud Infrastructure MySQL Database service.

        Creates a DB System read replica.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_replica = oci.mysql.Replica("testReplica",
            db_system_id=oci_mysql_mysql_db_system["test_mysql_db_system"]["id"],
            defined_tags={
                "foo-namespace.bar-key": "value",
            },
            description=var["replica_description"],
            display_name=var["replica_display_name"],
            freeform_tags={
                "bar-key": "value",
            },
            is_delete_protected=var["replica_is_delete_protected"])
        ```

        ## Import

        Replicas can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:Mysql/replica:Replica test_replica "id"
        ```

        :param str resource_name: The name of the resource.
        :param ReplicaArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReplicaArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 db_system_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 is_delete_protected: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ReplicaArgs.__new__(ReplicaArgs)

            if db_system_id is None and not opts.urn:
                raise TypeError("Missing required property 'db_system_id'")
            __props__.__dict__["db_system_id"] = db_system_id
            __props__.__dict__["defined_tags"] = defined_tags
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["freeform_tags"] = freeform_tags
            __props__.__dict__["is_delete_protected"] = is_delete_protected
            __props__.__dict__["availability_domain"] = None
            __props__.__dict__["compartment_id"] = None
            __props__.__dict__["fault_domain"] = None
            __props__.__dict__["ip_address"] = None
            __props__.__dict__["lifecycle_details"] = None
            __props__.__dict__["mysql_version"] = None
            __props__.__dict__["port"] = None
            __props__.__dict__["port_x"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_updated"] = None
        super(Replica, __self__).__init__(
            'oci:Mysql/replica:Replica',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            availability_domain: Optional[pulumi.Input[str]] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            db_system_id: Optional[pulumi.Input[str]] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            fault_domain: Optional[pulumi.Input[str]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            ip_address: Optional[pulumi.Input[str]] = None,
            is_delete_protected: Optional[pulumi.Input[bool]] = None,
            lifecycle_details: Optional[pulumi.Input[str]] = None,
            mysql_version: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            port_x: Optional[pulumi.Input[int]] = None,
            state: Optional[pulumi.Input[str]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_updated: Optional[pulumi.Input[str]] = None) -> 'Replica':
        """
        Get an existing Replica resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] availability_domain: The name of the Availability Domain the read replica is located in.
        :param pulumi.Input[str] compartment_id: The OCID of the compartment that contains the read replica.
        :param pulumi.Input[str] db_system_id: The OCID of the DB System the read replica is associated with.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) User provided description of the read replica.
        :param pulumi.Input[str] display_name: (Updatable) The user-friendly name for the read replica. It does not have to be unique.
        :param pulumi.Input[str] fault_domain: The name of the Fault Domain the read replica is located in.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[str] ip_address: The IP address the read replica is configured to listen on.
        :param pulumi.Input[bool] is_delete_protected: (Updatable) Specifies whether the read replica can be deleted. Set to true to prevent deletion, false (default) to allow. Note that if a read replica is delete protected it also prevents the entire DB System from being deleted. If the DB System is delete protected, read replicas can still be deleted individually if they are not delete  protected themselves. 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] lifecycle_details: A message describing the state of the read replica.
        :param pulumi.Input[str] mysql_version: The MySQL version used by the read replica.
        :param pulumi.Input[int] port: The port the read replica is configured to listen on.
        :param pulumi.Input[int] port_x: The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.
        :param pulumi.Input[str] state: The state of the read replica.
        :param pulumi.Input[str] time_created: The date and time the read replica was created, as described by [RFC 3339](https://tools.ietf.org/rfc/rfc3339).
        :param pulumi.Input[str] time_updated: The time the read replica was last updated, as described by [RFC 3339](https://tools.ietf.org/rfc/rfc3339).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ReplicaState.__new__(_ReplicaState)

        __props__.__dict__["availability_domain"] = availability_domain
        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["db_system_id"] = db_system_id
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["description"] = description
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["fault_domain"] = fault_domain
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["ip_address"] = ip_address
        __props__.__dict__["is_delete_protected"] = is_delete_protected
        __props__.__dict__["lifecycle_details"] = lifecycle_details
        __props__.__dict__["mysql_version"] = mysql_version
        __props__.__dict__["port"] = port
        __props__.__dict__["port_x"] = port_x
        __props__.__dict__["state"] = state
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_updated"] = time_updated
        return Replica(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="availabilityDomain")
    def availability_domain(self) -> pulumi.Output[str]:
        """
        The name of the Availability Domain the read replica is located in.
        """
        return pulumi.get(self, "availability_domain")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        The OCID of the compartment that contains the read replica.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="dbSystemId")
    def db_system_id(self) -> pulumi.Output[str]:
        """
        The OCID of the DB System the read replica is associated with.
        """
        return pulumi.get(self, "db_system_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        (Updatable) User provided description of the read replica.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        (Updatable) The user-friendly name for the read replica. It does not have to be unique.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="faultDomain")
    def fault_domain(self) -> pulumi.Output[str]:
        """
        The name of the Fault Domain the read replica is located in.
        """
        return pulumi.get(self, "fault_domain")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[str]:
        """
        The IP address the read replica is configured to listen on.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="isDeleteProtected")
    def is_delete_protected(self) -> pulumi.Output[bool]:
        """
        (Updatable) Specifies whether the read replica can be deleted. Set to true to prevent deletion, false (default) to allow. Note that if a read replica is delete protected it also prevents the entire DB System from being deleted. If the DB System is delete protected, read replicas can still be deleted individually if they are not delete  protected themselves. 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "is_delete_protected")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> pulumi.Output[str]:
        """
        A message describing the state of the read replica.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="mysqlVersion")
    def mysql_version(self) -> pulumi.Output[str]:
        """
        The MySQL version used by the read replica.
        """
        return pulumi.get(self, "mysql_version")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[int]:
        """
        The port the read replica is configured to listen on.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="portX")
    def port_x(self) -> pulumi.Output[int]:
        """
        The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.
        """
        return pulumi.get(self, "port_x")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the read replica.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The date and time the read replica was created, as described by [RFC 3339](https://tools.ietf.org/rfc/rfc3339).
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> pulumi.Output[str]:
        """
        The time the read replica was last updated, as described by [RFC 3339](https://tools.ietf.org/rfc/rfc3339).
        """
        return pulumi.get(self, "time_updated")

