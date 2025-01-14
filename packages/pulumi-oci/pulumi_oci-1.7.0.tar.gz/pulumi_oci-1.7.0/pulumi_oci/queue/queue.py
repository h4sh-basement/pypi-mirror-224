# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['QueueArgs', 'Queue']

@pulumi.input_type
class QueueArgs:
    def __init__(__self__, *,
                 compartment_id: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 custom_encryption_key_id: Optional[pulumi.Input[str]] = None,
                 dead_letter_queue_delivery_count: Optional[pulumi.Input[int]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 purge_queue: Optional[pulumi.Input[bool]] = None,
                 purge_type: Optional[pulumi.Input[str]] = None,
                 retention_in_seconds: Optional[pulumi.Input[int]] = None,
                 timeout_in_seconds: Optional[pulumi.Input[int]] = None,
                 visibility_in_seconds: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Queue resource.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment Identifier
        :param pulumi.Input[str] display_name: (Updatable) Queue Identifier
        :param pulumi.Input[str] custom_encryption_key_id: (Updatable) Id of the custom master encryption key which will be used to encrypt messages content
        :param pulumi.Input[int] dead_letter_queue_delivery_count: (Updatable) The number of times a message can be delivered to a consumer before being moved to the dead letter queue. A value of 0 indicates that the DLQ is not used.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[int] retention_in_seconds: The retention period of the messages in the queue, in seconds.
        :param pulumi.Input[int] timeout_in_seconds: (Updatable) The default polling timeout of the messages in the queue, in seconds.
        :param pulumi.Input[int] visibility_in_seconds: (Updatable) The default visibility of the messages consumed from the queue.
        """
        pulumi.set(__self__, "compartment_id", compartment_id)
        pulumi.set(__self__, "display_name", display_name)
        if custom_encryption_key_id is not None:
            pulumi.set(__self__, "custom_encryption_key_id", custom_encryption_key_id)
        if dead_letter_queue_delivery_count is not None:
            pulumi.set(__self__, "dead_letter_queue_delivery_count", dead_letter_queue_delivery_count)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if purge_queue is not None:
            pulumi.set(__self__, "purge_queue", purge_queue)
        if purge_type is not None:
            pulumi.set(__self__, "purge_type", purge_type)
        if retention_in_seconds is not None:
            pulumi.set(__self__, "retention_in_seconds", retention_in_seconds)
        if timeout_in_seconds is not None:
            pulumi.set(__self__, "timeout_in_seconds", timeout_in_seconds)
        if visibility_in_seconds is not None:
            pulumi.set(__self__, "visibility_in_seconds", visibility_in_seconds)

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
        (Updatable) Queue Identifier
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="customEncryptionKeyId")
    def custom_encryption_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Id of the custom master encryption key which will be used to encrypt messages content
        """
        return pulumi.get(self, "custom_encryption_key_id")

    @custom_encryption_key_id.setter
    def custom_encryption_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_encryption_key_id", value)

    @property
    @pulumi.getter(name="deadLetterQueueDeliveryCount")
    def dead_letter_queue_delivery_count(self) -> Optional[pulumi.Input[int]]:
        """
        (Updatable) The number of times a message can be delivered to a consumer before being moved to the dead letter queue. A value of 0 indicates that the DLQ is not used.
        """
        return pulumi.get(self, "dead_letter_queue_delivery_count")

    @dead_letter_queue_delivery_count.setter
    def dead_letter_queue_delivery_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "dead_letter_queue_delivery_count", value)

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
    @pulumi.getter(name="purgeQueue")
    def purge_queue(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "purge_queue")

    @purge_queue.setter
    def purge_queue(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "purge_queue", value)

    @property
    @pulumi.getter(name="purgeType")
    def purge_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "purge_type")

    @purge_type.setter
    def purge_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "purge_type", value)

    @property
    @pulumi.getter(name="retentionInSeconds")
    def retention_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        The retention period of the messages in the queue, in seconds.
        """
        return pulumi.get(self, "retention_in_seconds")

    @retention_in_seconds.setter
    def retention_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retention_in_seconds", value)

    @property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        (Updatable) The default polling timeout of the messages in the queue, in seconds.
        """
        return pulumi.get(self, "timeout_in_seconds")

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout_in_seconds", value)

    @property
    @pulumi.getter(name="visibilityInSeconds")
    def visibility_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        (Updatable) The default visibility of the messages consumed from the queue.
        """
        return pulumi.get(self, "visibility_in_seconds")

    @visibility_in_seconds.setter
    def visibility_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "visibility_in_seconds", value)


@pulumi.input_type
class _QueueState:
    def __init__(__self__, *,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 custom_encryption_key_id: Optional[pulumi.Input[str]] = None,
                 dead_letter_queue_delivery_count: Optional[pulumi.Input[int]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 lifecycle_details: Optional[pulumi.Input[str]] = None,
                 messages_endpoint: Optional[pulumi.Input[str]] = None,
                 purge_queue: Optional[pulumi.Input[bool]] = None,
                 purge_type: Optional[pulumi.Input[str]] = None,
                 retention_in_seconds: Optional[pulumi.Input[int]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_updated: Optional[pulumi.Input[str]] = None,
                 timeout_in_seconds: Optional[pulumi.Input[int]] = None,
                 visibility_in_seconds: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Queue resources.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment Identifier
        :param pulumi.Input[str] custom_encryption_key_id: (Updatable) Id of the custom master encryption key which will be used to encrypt messages content
        :param pulumi.Input[int] dead_letter_queue_delivery_count: (Updatable) The number of times a message can be delivered to a consumer before being moved to the dead letter queue. A value of 0 indicates that the DLQ is not used.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] display_name: (Updatable) Queue Identifier
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[str] lifecycle_details: A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        :param pulumi.Input[str] messages_endpoint: The endpoint to use to consume or publish messages in the queue.
        :param pulumi.Input[int] retention_in_seconds: The retention period of the messages in the queue, in seconds.
        :param pulumi.Input[str] state: The current state of the Queue.
        :param pulumi.Input[Mapping[str, Any]] system_tags: Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        :param pulumi.Input[str] time_created: The time the the Queue was created. An RFC3339 formatted datetime string
        :param pulumi.Input[str] time_updated: The time the Queue was updated. An RFC3339 formatted datetime string
        :param pulumi.Input[int] timeout_in_seconds: (Updatable) The default polling timeout of the messages in the queue, in seconds.
        :param pulumi.Input[int] visibility_in_seconds: (Updatable) The default visibility of the messages consumed from the queue.
        """
        if compartment_id is not None:
            pulumi.set(__self__, "compartment_id", compartment_id)
        if custom_encryption_key_id is not None:
            pulumi.set(__self__, "custom_encryption_key_id", custom_encryption_key_id)
        if dead_letter_queue_delivery_count is not None:
            pulumi.set(__self__, "dead_letter_queue_delivery_count", dead_letter_queue_delivery_count)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if lifecycle_details is not None:
            pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if messages_endpoint is not None:
            pulumi.set(__self__, "messages_endpoint", messages_endpoint)
        if purge_queue is not None:
            pulumi.set(__self__, "purge_queue", purge_queue)
        if purge_type is not None:
            pulumi.set(__self__, "purge_type", purge_type)
        if retention_in_seconds is not None:
            pulumi.set(__self__, "retention_in_seconds", retention_in_seconds)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if system_tags is not None:
            pulumi.set(__self__, "system_tags", system_tags)
        if time_created is not None:
            pulumi.set(__self__, "time_created", time_created)
        if time_updated is not None:
            pulumi.set(__self__, "time_updated", time_updated)
        if timeout_in_seconds is not None:
            pulumi.set(__self__, "timeout_in_seconds", timeout_in_seconds)
        if visibility_in_seconds is not None:
            pulumi.set(__self__, "visibility_in_seconds", visibility_in_seconds)

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
    @pulumi.getter(name="customEncryptionKeyId")
    def custom_encryption_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Id of the custom master encryption key which will be used to encrypt messages content
        """
        return pulumi.get(self, "custom_encryption_key_id")

    @custom_encryption_key_id.setter
    def custom_encryption_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_encryption_key_id", value)

    @property
    @pulumi.getter(name="deadLetterQueueDeliveryCount")
    def dead_letter_queue_delivery_count(self) -> Optional[pulumi.Input[int]]:
        """
        (Updatable) The number of times a message can be delivered to a consumer before being moved to the dead letter queue. A value of 0 indicates that the DLQ is not used.
        """
        return pulumi.get(self, "dead_letter_queue_delivery_count")

    @dead_letter_queue_delivery_count.setter
    def dead_letter_queue_delivery_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "dead_letter_queue_delivery_count", value)

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
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Queue Identifier
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
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[str]]:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_details", value)

    @property
    @pulumi.getter(name="messagesEndpoint")
    def messages_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        The endpoint to use to consume or publish messages in the queue.
        """
        return pulumi.get(self, "messages_endpoint")

    @messages_endpoint.setter
    def messages_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "messages_endpoint", value)

    @property
    @pulumi.getter(name="purgeQueue")
    def purge_queue(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "purge_queue")

    @purge_queue.setter
    def purge_queue(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "purge_queue", value)

    @property
    @pulumi.getter(name="purgeType")
    def purge_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "purge_type")

    @purge_type.setter
    def purge_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "purge_type", value)

    @property
    @pulumi.getter(name="retentionInSeconds")
    def retention_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        The retention period of the messages in the queue, in seconds.
        """
        return pulumi.get(self, "retention_in_seconds")

    @retention_in_seconds.setter
    def retention_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retention_in_seconds", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current state of the Queue.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @system_tags.setter
    def system_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "system_tags", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The time the the Queue was created. An RFC3339 formatted datetime string
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> Optional[pulumi.Input[str]]:
        """
        The time the Queue was updated. An RFC3339 formatted datetime string
        """
        return pulumi.get(self, "time_updated")

    @time_updated.setter
    def time_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_updated", value)

    @property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        (Updatable) The default polling timeout of the messages in the queue, in seconds.
        """
        return pulumi.get(self, "timeout_in_seconds")

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout_in_seconds", value)

    @property
    @pulumi.getter(name="visibilityInSeconds")
    def visibility_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        (Updatable) The default visibility of the messages consumed from the queue.
        """
        return pulumi.get(self, "visibility_in_seconds")

    @visibility_in_seconds.setter
    def visibility_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "visibility_in_seconds", value)


class Queue(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 custom_encryption_key_id: Optional[pulumi.Input[str]] = None,
                 dead_letter_queue_delivery_count: Optional[pulumi.Input[int]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 purge_queue: Optional[pulumi.Input[bool]] = None,
                 purge_type: Optional[pulumi.Input[str]] = None,
                 retention_in_seconds: Optional[pulumi.Input[int]] = None,
                 timeout_in_seconds: Optional[pulumi.Input[int]] = None,
                 visibility_in_seconds: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        This resource provides the Queue resource in Oracle Cloud Infrastructure Queue service.

        Creates a new Queue.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_queue = oci.queue.Queue("testQueue",
            compartment_id=var["compartment_id"],
            display_name=var["queue_display_name"],
            custom_encryption_key_id=oci_kms_key["test_key"]["id"],
            dead_letter_queue_delivery_count=var["queue_dead_letter_queue_delivery_count"],
            defined_tags={
                "foo-namespace.bar-key": "value",
            },
            freeform_tags={
                "bar-key": "value",
            },
            retention_in_seconds=var["queue_retention_in_seconds"],
            timeout_in_seconds=var["queue_timeout_in_seconds"],
            visibility_in_seconds=var["queue_visibility_in_seconds"])
        ```

        ## Import

        Queues can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:Queue/queue:Queue test_queue "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment Identifier
        :param pulumi.Input[str] custom_encryption_key_id: (Updatable) Id of the custom master encryption key which will be used to encrypt messages content
        :param pulumi.Input[int] dead_letter_queue_delivery_count: (Updatable) The number of times a message can be delivered to a consumer before being moved to the dead letter queue. A value of 0 indicates that the DLQ is not used.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] display_name: (Updatable) Queue Identifier
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[int] retention_in_seconds: The retention period of the messages in the queue, in seconds.
        :param pulumi.Input[int] timeout_in_seconds: (Updatable) The default polling timeout of the messages in the queue, in seconds.
        :param pulumi.Input[int] visibility_in_seconds: (Updatable) The default visibility of the messages consumed from the queue.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: QueueArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Queue resource in Oracle Cloud Infrastructure Queue service.

        Creates a new Queue.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_queue = oci.queue.Queue("testQueue",
            compartment_id=var["compartment_id"],
            display_name=var["queue_display_name"],
            custom_encryption_key_id=oci_kms_key["test_key"]["id"],
            dead_letter_queue_delivery_count=var["queue_dead_letter_queue_delivery_count"],
            defined_tags={
                "foo-namespace.bar-key": "value",
            },
            freeform_tags={
                "bar-key": "value",
            },
            retention_in_seconds=var["queue_retention_in_seconds"],
            timeout_in_seconds=var["queue_timeout_in_seconds"],
            visibility_in_seconds=var["queue_visibility_in_seconds"])
        ```

        ## Import

        Queues can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:Queue/queue:Queue test_queue "id"
        ```

        :param str resource_name: The name of the resource.
        :param QueueArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(QueueArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 custom_encryption_key_id: Optional[pulumi.Input[str]] = None,
                 dead_letter_queue_delivery_count: Optional[pulumi.Input[int]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 purge_queue: Optional[pulumi.Input[bool]] = None,
                 purge_type: Optional[pulumi.Input[str]] = None,
                 retention_in_seconds: Optional[pulumi.Input[int]] = None,
                 timeout_in_seconds: Optional[pulumi.Input[int]] = None,
                 visibility_in_seconds: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = QueueArgs.__new__(QueueArgs)

            if compartment_id is None and not opts.urn:
                raise TypeError("Missing required property 'compartment_id'")
            __props__.__dict__["compartment_id"] = compartment_id
            __props__.__dict__["custom_encryption_key_id"] = custom_encryption_key_id
            __props__.__dict__["dead_letter_queue_delivery_count"] = dead_letter_queue_delivery_count
            __props__.__dict__["defined_tags"] = defined_tags
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["freeform_tags"] = freeform_tags
            __props__.__dict__["purge_queue"] = purge_queue
            __props__.__dict__["purge_type"] = purge_type
            __props__.__dict__["retention_in_seconds"] = retention_in_seconds
            __props__.__dict__["timeout_in_seconds"] = timeout_in_seconds
            __props__.__dict__["visibility_in_seconds"] = visibility_in_seconds
            __props__.__dict__["lifecycle_details"] = None
            __props__.__dict__["messages_endpoint"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["system_tags"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_updated"] = None
        super(Queue, __self__).__init__(
            'oci:Queue/queue:Queue',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            custom_encryption_key_id: Optional[pulumi.Input[str]] = None,
            dead_letter_queue_delivery_count: Optional[pulumi.Input[int]] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            lifecycle_details: Optional[pulumi.Input[str]] = None,
            messages_endpoint: Optional[pulumi.Input[str]] = None,
            purge_queue: Optional[pulumi.Input[bool]] = None,
            purge_type: Optional[pulumi.Input[str]] = None,
            retention_in_seconds: Optional[pulumi.Input[int]] = None,
            state: Optional[pulumi.Input[str]] = None,
            system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_updated: Optional[pulumi.Input[str]] = None,
            timeout_in_seconds: Optional[pulumi.Input[int]] = None,
            visibility_in_seconds: Optional[pulumi.Input[int]] = None) -> 'Queue':
        """
        Get an existing Queue resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment Identifier
        :param pulumi.Input[str] custom_encryption_key_id: (Updatable) Id of the custom master encryption key which will be used to encrypt messages content
        :param pulumi.Input[int] dead_letter_queue_delivery_count: (Updatable) The number of times a message can be delivered to a consumer before being moved to the dead letter queue. A value of 0 indicates that the DLQ is not used.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] display_name: (Updatable) Queue Identifier
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[str] lifecycle_details: A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        :param pulumi.Input[str] messages_endpoint: The endpoint to use to consume or publish messages in the queue.
        :param pulumi.Input[int] retention_in_seconds: The retention period of the messages in the queue, in seconds.
        :param pulumi.Input[str] state: The current state of the Queue.
        :param pulumi.Input[Mapping[str, Any]] system_tags: Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        :param pulumi.Input[str] time_created: The time the the Queue was created. An RFC3339 formatted datetime string
        :param pulumi.Input[str] time_updated: The time the Queue was updated. An RFC3339 formatted datetime string
        :param pulumi.Input[int] timeout_in_seconds: (Updatable) The default polling timeout of the messages in the queue, in seconds.
        :param pulumi.Input[int] visibility_in_seconds: (Updatable) The default visibility of the messages consumed from the queue.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _QueueState.__new__(_QueueState)

        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["custom_encryption_key_id"] = custom_encryption_key_id
        __props__.__dict__["dead_letter_queue_delivery_count"] = dead_letter_queue_delivery_count
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["lifecycle_details"] = lifecycle_details
        __props__.__dict__["messages_endpoint"] = messages_endpoint
        __props__.__dict__["purge_queue"] = purge_queue
        __props__.__dict__["purge_type"] = purge_type
        __props__.__dict__["retention_in_seconds"] = retention_in_seconds
        __props__.__dict__["state"] = state
        __props__.__dict__["system_tags"] = system_tags
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_updated"] = time_updated
        __props__.__dict__["timeout_in_seconds"] = timeout_in_seconds
        __props__.__dict__["visibility_in_seconds"] = visibility_in_seconds
        return Queue(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        (Updatable) Compartment Identifier
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="customEncryptionKeyId")
    def custom_encryption_key_id(self) -> pulumi.Output[str]:
        """
        (Updatable) Id of the custom master encryption key which will be used to encrypt messages content
        """
        return pulumi.get(self, "custom_encryption_key_id")

    @property
    @pulumi.getter(name="deadLetterQueueDeliveryCount")
    def dead_letter_queue_delivery_count(self) -> pulumi.Output[int]:
        """
        (Updatable) The number of times a message can be delivered to a consumer before being moved to the dead letter queue. A value of 0 indicates that the DLQ is not used.
        """
        return pulumi.get(self, "dead_letter_queue_delivery_count")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        (Updatable) Queue Identifier
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> pulumi.Output[str]:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="messagesEndpoint")
    def messages_endpoint(self) -> pulumi.Output[str]:
        """
        The endpoint to use to consume or publish messages in the queue.
        """
        return pulumi.get(self, "messages_endpoint")

    @property
    @pulumi.getter(name="purgeQueue")
    def purge_queue(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "purge_queue")

    @property
    @pulumi.getter(name="purgeType")
    def purge_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "purge_type")

    @property
    @pulumi.getter(name="retentionInSeconds")
    def retention_in_seconds(self) -> pulumi.Output[int]:
        """
        The retention period of the messages in the queue, in seconds.
        """
        return pulumi.get(self, "retention_in_seconds")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the Queue.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The time the the Queue was created. An RFC3339 formatted datetime string
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> pulumi.Output[str]:
        """
        The time the Queue was updated. An RFC3339 formatted datetime string
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> pulumi.Output[int]:
        """
        (Updatable) The default polling timeout of the messages in the queue, in seconds.
        """
        return pulumi.get(self, "timeout_in_seconds")

    @property
    @pulumi.getter(name="visibilityInSeconds")
    def visibility_in_seconds(self) -> pulumi.Output[int]:
        """
        (Updatable) The default visibility of the messages consumed from the queue.
        """
        return pulumi.get(self, "visibility_in_seconds")

