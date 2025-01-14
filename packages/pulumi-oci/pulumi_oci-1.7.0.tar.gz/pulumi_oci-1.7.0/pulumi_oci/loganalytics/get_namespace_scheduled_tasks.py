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

__all__ = [
    'GetNamespaceScheduledTasksResult',
    'AwaitableGetNamespaceScheduledTasksResult',
    'get_namespace_scheduled_tasks',
    'get_namespace_scheduled_tasks_output',
]

@pulumi.output_type
class GetNamespaceScheduledTasksResult:
    """
    A collection of values returned by getNamespaceScheduledTasks.
    """
    def __init__(__self__, compartment_id=None, display_name=None, filters=None, id=None, namespace=None, scheduled_task_collections=None, task_type=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if scheduled_task_collections and not isinstance(scheduled_task_collections, list):
            raise TypeError("Expected argument 'scheduled_task_collections' to be a list")
        pulumi.set(__self__, "scheduled_task_collections", scheduled_task_collections)
        if task_type and not isinstance(task_type, str):
            raise TypeError("Expected argument 'task_type' to be a str")
        pulumi.set(__self__, "task_type", task_type)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        Compartment Identifier [OCID] (https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly name that is changeable and that does not have to be unique. Format: a leading alphanumeric, followed by zero or more alphanumerics, underscores, spaces, backslashes, or hyphens in any order). No trailing spaces allowed.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetNamespaceScheduledTasksFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="scheduledTaskCollections")
    def scheduled_task_collections(self) -> Sequence['outputs.GetNamespaceScheduledTasksScheduledTaskCollectionResult']:
        """
        The list of scheduled_task_collection.
        """
        return pulumi.get(self, "scheduled_task_collections")

    @property
    @pulumi.getter(name="taskType")
    def task_type(self) -> str:
        """
        Task type.
        """
        return pulumi.get(self, "task_type")


class AwaitableGetNamespaceScheduledTasksResult(GetNamespaceScheduledTasksResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNamespaceScheduledTasksResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            namespace=self.namespace,
            scheduled_task_collections=self.scheduled_task_collections,
            task_type=self.task_type)


def get_namespace_scheduled_tasks(compartment_id: Optional[str] = None,
                                  display_name: Optional[str] = None,
                                  filters: Optional[Sequence[pulumi.InputType['GetNamespaceScheduledTasksFilterArgs']]] = None,
                                  namespace: Optional[str] = None,
                                  task_type: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNamespaceScheduledTasksResult:
    """
    This data source provides the list of Namespace Scheduled Tasks in Oracle Cloud Infrastructure Log Analytics service.

    Lists scheduled tasks.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_namespace_scheduled_tasks = oci.LogAnalytics.get_namespace_scheduled_tasks(compartment_id=var["compartment_id"],
        namespace=var["namespace_scheduled_task_namespace"],
        display_name=var["namespace_scheduled_task_display_name"],
        task_type=var["namespace_scheduled_task_task_type"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the given display name exactly.
    :param str namespace: The Logging Analytics namespace used for the request.
    :param str task_type: Required parameter to specify schedule task type.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['namespace'] = namespace
    __args__['taskType'] = task_type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:LogAnalytics/getNamespaceScheduledTasks:getNamespaceScheduledTasks', __args__, opts=opts, typ=GetNamespaceScheduledTasksResult).value

    return AwaitableGetNamespaceScheduledTasksResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        namespace=pulumi.get(__ret__, 'namespace'),
        scheduled_task_collections=pulumi.get(__ret__, 'scheduled_task_collections'),
        task_type=pulumi.get(__ret__, 'task_type'))


@_utilities.lift_output_func(get_namespace_scheduled_tasks)
def get_namespace_scheduled_tasks_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                         display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                         filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetNamespaceScheduledTasksFilterArgs']]]]] = None,
                                         namespace: Optional[pulumi.Input[str]] = None,
                                         task_type: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNamespaceScheduledTasksResult]:
    """
    This data source provides the list of Namespace Scheduled Tasks in Oracle Cloud Infrastructure Log Analytics service.

    Lists scheduled tasks.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_namespace_scheduled_tasks = oci.LogAnalytics.get_namespace_scheduled_tasks(compartment_id=var["compartment_id"],
        namespace=var["namespace_scheduled_task_namespace"],
        display_name=var["namespace_scheduled_task_display_name"],
        task_type=var["namespace_scheduled_task_task_type"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the given display name exactly.
    :param str namespace: The Logging Analytics namespace used for the request.
    :param str task_type: Required parameter to specify schedule task type.
    """
    ...
