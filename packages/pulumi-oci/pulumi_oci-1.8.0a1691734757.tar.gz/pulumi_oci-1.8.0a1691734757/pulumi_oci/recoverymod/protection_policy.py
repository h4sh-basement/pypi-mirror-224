# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ProtectionPolicyArgs', 'ProtectionPolicy']

@pulumi.input_type
class ProtectionPolicyArgs:
    def __init__(__self__, *,
                 backup_retention_period_in_days: pulumi.Input[int],
                 compartment_id: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a ProtectionPolicy resource.
        :param pulumi.Input[int] backup_retention_period_in_days: (Updatable) The maximum number of days to retain backups for a protected database.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment Identifier
        :param pulumi.Input[str] display_name: (Updatable) A user provided name for the protection policy. The 'displayName' does not have to be unique, and it can be modified. Avoid entering confidential information.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`. For more information, see [Resource Tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        pulumi.set(__self__, "backup_retention_period_in_days", backup_retention_period_in_days)
        pulumi.set(__self__, "compartment_id", compartment_id)
        pulumi.set(__self__, "display_name", display_name)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)

    @property
    @pulumi.getter(name="backupRetentionPeriodInDays")
    def backup_retention_period_in_days(self) -> pulumi.Input[int]:
        """
        (Updatable) The maximum number of days to retain backups for a protected database.
        """
        return pulumi.get(self, "backup_retention_period_in_days")

    @backup_retention_period_in_days.setter
    def backup_retention_period_in_days(self, value: pulumi.Input[int]):
        pulumi.set(self, "backup_retention_period_in_days", value)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Input[str]:
        """
        (Updatable) Compartment Identifier
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        (Updatable) A user provided name for the protection policy. The 'displayName' does not have to be unique, and it can be modified. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`. For more information, see [Resource Tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)


@pulumi.input_type
class _ProtectionPolicyState:
    def __init__(__self__, *,
                 backup_retention_period_in_days: Optional[pulumi.Input[int]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 is_predefined_policy: Optional[pulumi.Input[bool]] = None,
                 lifecycle_details: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_updated: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ProtectionPolicy resources.
        :param pulumi.Input[int] backup_retention_period_in_days: (Updatable) The maximum number of days to retain backups for a protected database.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment Identifier
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`. For more information, see [Resource Tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
        :param pulumi.Input[str] display_name: (Updatable) A user provided name for the protection policy. The 'displayName' does not have to be unique, and it can be modified. Avoid entering confidential information.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[bool] is_predefined_policy: Set to TRUE if the policy is Oracle-defined, and FALSE for a user-defined custom policy. You can modify only the custom policies.
        :param pulumi.Input[str] lifecycle_details: Detailed description about the current lifecycle state of the protection policy. For example, it can be used to provide actionable information for a resource in a Failed state.
        :param pulumi.Input[str] state: The current state of the protection policy. Allowed values are:
               * CREATING
               * UPDATING
               * ACTIVE
               * DELETING
               * DELETED
               * FAILED
        :param pulumi.Input[Mapping[str, Any]] system_tags: Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`. For more information, see [Resource Tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
        :param pulumi.Input[str] time_created: An RFC3339 formatted datetime string that indicates the created time for the protection policy. For example: '2020-05-22T21:10:29.600Z'.
        :param pulumi.Input[str] time_updated: An RFC3339 formatted datetime string that indicates the updated time for the protection policy. For example: '2020-05-22T21:10:29.600Z'.
        """
        if backup_retention_period_in_days is not None:
            pulumi.set(__self__, "backup_retention_period_in_days", backup_retention_period_in_days)
        if compartment_id is not None:
            pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if is_predefined_policy is not None:
            pulumi.set(__self__, "is_predefined_policy", is_predefined_policy)
        if lifecycle_details is not None:
            pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if system_tags is not None:
            pulumi.set(__self__, "system_tags", system_tags)
        if time_created is not None:
            pulumi.set(__self__, "time_created", time_created)
        if time_updated is not None:
            pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="backupRetentionPeriodInDays")
    def backup_retention_period_in_days(self) -> Optional[pulumi.Input[int]]:
        """
        (Updatable) The maximum number of days to retain backups for a protected database.
        """
        return pulumi.get(self, "backup_retention_period_in_days")

    @backup_retention_period_in_days.setter
    def backup_retention_period_in_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "backup_retention_period_in_days", value)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Compartment Identifier
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`. For more information, see [Resource Tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A user provided name for the protection policy. The 'displayName' does not have to be unique, and it can be modified. Avoid entering confidential information.
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


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="isPredefinedPolicy")
    def is_predefined_policy(self) -> Optional[pulumi.Input[bool]]:
        """
        Set to TRUE if the policy is Oracle-defined, and FALSE for a user-defined custom policy. You can modify only the custom policies.
        """
        return pulumi.get(self, "is_predefined_policy")

    @is_predefined_policy.setter
    def is_predefined_policy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_predefined_policy", value)

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[str]]:
        """
        Detailed description about the current lifecycle state of the protection policy. For example, it can be used to provide actionable information for a resource in a Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_details", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current state of the protection policy. Allowed values are:
        * CREATING
        * UPDATING
        * ACTIVE
        * DELETING
        * DELETED
        * FAILED
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`. For more information, see [Resource Tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
        """
        return pulumi.get(self, "system_tags")

    @system_tags.setter
    def system_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "system_tags", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        An RFC3339 formatted datetime string that indicates the created time for the protection policy. For example: '2020-05-22T21:10:29.600Z'.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> Optional[pulumi.Input[str]]:
        """
        An RFC3339 formatted datetime string that indicates the updated time for the protection policy. For example: '2020-05-22T21:10:29.600Z'.
        """
        return pulumi.get(self, "time_updated")

    @time_updated.setter
    def time_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_updated", value)


class ProtectionPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backup_retention_period_in_days: Optional[pulumi.Input[int]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        """
        This resource provides the Protection Policy resource in Oracle Cloud Infrastructure Recovery service.

        Creates a new Protection Policy.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_protection_policy = oci.recovery_mod.ProtectionPolicy("testProtectionPolicy",
            backup_retention_period_in_days=var["protection_policy_backup_retention_period_in_days"],
            compartment_id=var["compartment_id"],
            display_name=var["protection_policy_display_name"],
            defined_tags={
                "foo-namespace.bar-key": "value",
            },
            freeform_tags={
                "bar-key": "value",
            })
        ```

        ## Import

        ProtectionPolicies can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:RecoveryMod/protectionPolicy:ProtectionPolicy test_protection_policy "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] backup_retention_period_in_days: (Updatable) The maximum number of days to retain backups for a protected database.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment Identifier
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`. For more information, see [Resource Tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
        :param pulumi.Input[str] display_name: (Updatable) A user provided name for the protection policy. The 'displayName' does not have to be unique, and it can be modified. Avoid entering confidential information.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProtectionPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Protection Policy resource in Oracle Cloud Infrastructure Recovery service.

        Creates a new Protection Policy.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_protection_policy = oci.recovery_mod.ProtectionPolicy("testProtectionPolicy",
            backup_retention_period_in_days=var["protection_policy_backup_retention_period_in_days"],
            compartment_id=var["compartment_id"],
            display_name=var["protection_policy_display_name"],
            defined_tags={
                "foo-namespace.bar-key": "value",
            },
            freeform_tags={
                "bar-key": "value",
            })
        ```

        ## Import

        ProtectionPolicies can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:RecoveryMod/protectionPolicy:ProtectionPolicy test_protection_policy "id"
        ```

        :param str resource_name: The name of the resource.
        :param ProtectionPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProtectionPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backup_retention_period_in_days: Optional[pulumi.Input[int]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProtectionPolicyArgs.__new__(ProtectionPolicyArgs)

            if backup_retention_period_in_days is None and not opts.urn:
                raise TypeError("Missing required property 'backup_retention_period_in_days'")
            __props__.__dict__["backup_retention_period_in_days"] = backup_retention_period_in_days
            if compartment_id is None and not opts.urn:
                raise TypeError("Missing required property 'compartment_id'")
            __props__.__dict__["compartment_id"] = compartment_id
            __props__.__dict__["defined_tags"] = defined_tags
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["freeform_tags"] = freeform_tags
            __props__.__dict__["is_predefined_policy"] = None
            __props__.__dict__["lifecycle_details"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["system_tags"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_updated"] = None
        super(ProtectionPolicy, __self__).__init__(
            'oci:RecoveryMod/protectionPolicy:ProtectionPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            backup_retention_period_in_days: Optional[pulumi.Input[int]] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            is_predefined_policy: Optional[pulumi.Input[bool]] = None,
            lifecycle_details: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_updated: Optional[pulumi.Input[str]] = None) -> 'ProtectionPolicy':
        """
        Get an existing ProtectionPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] backup_retention_period_in_days: (Updatable) The maximum number of days to retain backups for a protected database.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment Identifier
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`. For more information, see [Resource Tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
        :param pulumi.Input[str] display_name: (Updatable) A user provided name for the protection policy. The 'displayName' does not have to be unique, and it can be modified. Avoid entering confidential information.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[bool] is_predefined_policy: Set to TRUE if the policy is Oracle-defined, and FALSE for a user-defined custom policy. You can modify only the custom policies.
        :param pulumi.Input[str] lifecycle_details: Detailed description about the current lifecycle state of the protection policy. For example, it can be used to provide actionable information for a resource in a Failed state.
        :param pulumi.Input[str] state: The current state of the protection policy. Allowed values are:
               * CREATING
               * UPDATING
               * ACTIVE
               * DELETING
               * DELETED
               * FAILED
        :param pulumi.Input[Mapping[str, Any]] system_tags: Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`. For more information, see [Resource Tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
        :param pulumi.Input[str] time_created: An RFC3339 formatted datetime string that indicates the created time for the protection policy. For example: '2020-05-22T21:10:29.600Z'.
        :param pulumi.Input[str] time_updated: An RFC3339 formatted datetime string that indicates the updated time for the protection policy. For example: '2020-05-22T21:10:29.600Z'.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProtectionPolicyState.__new__(_ProtectionPolicyState)

        __props__.__dict__["backup_retention_period_in_days"] = backup_retention_period_in_days
        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["is_predefined_policy"] = is_predefined_policy
        __props__.__dict__["lifecycle_details"] = lifecycle_details
        __props__.__dict__["state"] = state
        __props__.__dict__["system_tags"] = system_tags
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_updated"] = time_updated
        return ProtectionPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backupRetentionPeriodInDays")
    def backup_retention_period_in_days(self) -> pulumi.Output[int]:
        """
        (Updatable) The maximum number of days to retain backups for a protected database.
        """
        return pulumi.get(self, "backup_retention_period_in_days")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        (Updatable) Compartment Identifier
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`. For more information, see [Resource Tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        (Updatable) A user provided name for the protection policy. The 'displayName' does not have to be unique, and it can be modified. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="isPredefinedPolicy")
    def is_predefined_policy(self) -> pulumi.Output[bool]:
        """
        Set to TRUE if the policy is Oracle-defined, and FALSE for a user-defined custom policy. You can modify only the custom policies.
        """
        return pulumi.get(self, "is_predefined_policy")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> pulumi.Output[str]:
        """
        Detailed description about the current lifecycle state of the protection policy. For example, it can be used to provide actionable information for a resource in a Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the protection policy. Allowed values are:
        * CREATING
        * UPDATING
        * ACTIVE
        * DELETING
        * DELETED
        * FAILED
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`. For more information, see [Resource Tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        An RFC3339 formatted datetime string that indicates the created time for the protection policy. For example: '2020-05-22T21:10:29.600Z'.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> pulumi.Output[str]:
        """
        An RFC3339 formatted datetime string that indicates the updated time for the protection policy. For example: '2020-05-22T21:10:29.600Z'.
        """
        return pulumi.get(self, "time_updated")

