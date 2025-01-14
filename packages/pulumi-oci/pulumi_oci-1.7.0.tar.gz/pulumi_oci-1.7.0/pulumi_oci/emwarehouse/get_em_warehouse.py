# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetEmWarehouseResult',
    'AwaitableGetEmWarehouseResult',
    'get_em_warehouse',
    'get_em_warehouse_output',
]

@pulumi.output_type
class GetEmWarehouseResult:
    """
    A collection of values returned by getEmWarehouse.
    """
    def __init__(__self__, compartment_id=None, defined_tags=None, display_name=None, em_bridge_id=None, em_warehouse_id=None, em_warehouse_type=None, freeform_tags=None, id=None, latest_etl_run_message=None, latest_etl_run_status=None, latest_etl_run_time=None, lifecycle_details=None, operations_insights_warehouse_id=None, state=None, system_tags=None, time_created=None, time_updated=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if em_bridge_id and not isinstance(em_bridge_id, str):
            raise TypeError("Expected argument 'em_bridge_id' to be a str")
        pulumi.set(__self__, "em_bridge_id", em_bridge_id)
        if em_warehouse_id and not isinstance(em_warehouse_id, str):
            raise TypeError("Expected argument 'em_warehouse_id' to be a str")
        pulumi.set(__self__, "em_warehouse_id", em_warehouse_id)
        if em_warehouse_type and not isinstance(em_warehouse_type, str):
            raise TypeError("Expected argument 'em_warehouse_type' to be a str")
        pulumi.set(__self__, "em_warehouse_type", em_warehouse_type)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if latest_etl_run_message and not isinstance(latest_etl_run_message, str):
            raise TypeError("Expected argument 'latest_etl_run_message' to be a str")
        pulumi.set(__self__, "latest_etl_run_message", latest_etl_run_message)
        if latest_etl_run_status and not isinstance(latest_etl_run_status, str):
            raise TypeError("Expected argument 'latest_etl_run_status' to be a str")
        pulumi.set(__self__, "latest_etl_run_status", latest_etl_run_status)
        if latest_etl_run_time and not isinstance(latest_etl_run_time, str):
            raise TypeError("Expected argument 'latest_etl_run_time' to be a str")
        pulumi.set(__self__, "latest_etl_run_time", latest_etl_run_time)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if operations_insights_warehouse_id and not isinstance(operations_insights_warehouse_id, str):
            raise TypeError("Expected argument 'operations_insights_warehouse_id' to be a str")
        pulumi.set(__self__, "operations_insights_warehouse_id", operations_insights_warehouse_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        Compartment Identifier
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        EmWarehouse Identifier, can be renamed
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="emBridgeId")
    def em_bridge_id(self) -> str:
        """
        EMBridge Identifier
        """
        return pulumi.get(self, "em_bridge_id")

    @property
    @pulumi.getter(name="emWarehouseId")
    def em_warehouse_id(self) -> str:
        return pulumi.get(self, "em_warehouse_id")

    @property
    @pulumi.getter(name="emWarehouseType")
    def em_warehouse_type(self) -> str:
        """
        Type of the EmWarehouse.
        """
        return pulumi.get(self, "em_warehouse_type")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Unique identifier that is immutable on creation
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="latestEtlRunMessage")
    def latest_etl_run_message(self) -> str:
        """
        Data Flow Run Status Message
        """
        return pulumi.get(self, "latest_etl_run_message")

    @property
    @pulumi.getter(name="latestEtlRunStatus")
    def latest_etl_run_status(self) -> str:
        """
        Data Flow Run Status
        """
        return pulumi.get(self, "latest_etl_run_status")

    @property
    @pulumi.getter(name="latestEtlRunTime")
    def latest_etl_run_time(self) -> str:
        """
        Data Flow Run Total Time
        """
        return pulumi.get(self, "latest_etl_run_time")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="operationsInsightsWarehouseId")
    def operations_insights_warehouse_id(self) -> str:
        """
        operations Insights Warehouse Identifier
        """
        return pulumi.get(self, "operations_insights_warehouse_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the EmWarehouse.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time the the EmWarehouse was created. An RFC3339 formatted datetime string
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The time the EmWarehouse was updated. An RFC3339 formatted datetime string
        """
        return pulumi.get(self, "time_updated")


class AwaitableGetEmWarehouseResult(GetEmWarehouseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEmWarehouseResult(
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            em_bridge_id=self.em_bridge_id,
            em_warehouse_id=self.em_warehouse_id,
            em_warehouse_type=self.em_warehouse_type,
            freeform_tags=self.freeform_tags,
            id=self.id,
            latest_etl_run_message=self.latest_etl_run_message,
            latest_etl_run_status=self.latest_etl_run_status,
            latest_etl_run_time=self.latest_etl_run_time,
            lifecycle_details=self.lifecycle_details,
            operations_insights_warehouse_id=self.operations_insights_warehouse_id,
            state=self.state,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_updated=self.time_updated)


def get_em_warehouse(em_warehouse_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEmWarehouseResult:
    """
    This data source provides details about a specific Em Warehouse resource in Oracle Cloud Infrastructure Em Warehouse service.

    Gets a EmWarehouse by identifier

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_em_warehouse = oci.EmWarehouse.get_em_warehouse(em_warehouse_id=oci_em_warehouse_em_warehouse["test_em_warehouse"]["id"])
    ```


    :param str em_warehouse_id: unique EmWarehouse identifier
    """
    __args__ = dict()
    __args__['emWarehouseId'] = em_warehouse_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:EmWarehouse/getEmWarehouse:getEmWarehouse', __args__, opts=opts, typ=GetEmWarehouseResult).value

    return AwaitableGetEmWarehouseResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        em_bridge_id=pulumi.get(__ret__, 'em_bridge_id'),
        em_warehouse_id=pulumi.get(__ret__, 'em_warehouse_id'),
        em_warehouse_type=pulumi.get(__ret__, 'em_warehouse_type'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        latest_etl_run_message=pulumi.get(__ret__, 'latest_etl_run_message'),
        latest_etl_run_status=pulumi.get(__ret__, 'latest_etl_run_status'),
        latest_etl_run_time=pulumi.get(__ret__, 'latest_etl_run_time'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        operations_insights_warehouse_id=pulumi.get(__ret__, 'operations_insights_warehouse_id'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'))


@_utilities.lift_output_func(get_em_warehouse)
def get_em_warehouse_output(em_warehouse_id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEmWarehouseResult]:
    """
    This data source provides details about a specific Em Warehouse resource in Oracle Cloud Infrastructure Em Warehouse service.

    Gets a EmWarehouse by identifier

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_em_warehouse = oci.EmWarehouse.get_em_warehouse(em_warehouse_id=oci_em_warehouse_em_warehouse["test_em_warehouse"]["id"])
    ```


    :param str em_warehouse_id: unique EmWarehouse identifier
    """
    ...
