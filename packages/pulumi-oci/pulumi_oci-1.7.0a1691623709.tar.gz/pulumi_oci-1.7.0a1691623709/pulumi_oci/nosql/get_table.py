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

__all__ = [
    'GetTableResult',
    'AwaitableGetTableResult',
    'get_table',
    'get_table_output',
]

@pulumi.output_type
class GetTableResult:
    """
    A collection of values returned by getTable.
    """
    def __init__(__self__, compartment_id=None, ddl_statement=None, defined_tags=None, freeform_tags=None, id=None, is_auto_reclaimable=None, lifecycle_details=None, name=None, schemas=None, state=None, system_tags=None, table_limits=None, table_name_or_id=None, time_created=None, time_of_expiration=None, time_updated=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if ddl_statement and not isinstance(ddl_statement, str):
            raise TypeError("Expected argument 'ddl_statement' to be a str")
        pulumi.set(__self__, "ddl_statement", ddl_statement)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_auto_reclaimable and not isinstance(is_auto_reclaimable, bool):
            raise TypeError("Expected argument 'is_auto_reclaimable' to be a bool")
        pulumi.set(__self__, "is_auto_reclaimable", is_auto_reclaimable)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if schemas and not isinstance(schemas, list):
            raise TypeError("Expected argument 'schemas' to be a list")
        pulumi.set(__self__, "schemas", schemas)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if table_limits and not isinstance(table_limits, list):
            raise TypeError("Expected argument 'table_limits' to be a list")
        pulumi.set(__self__, "table_limits", table_limits)
        if table_name_or_id and not isinstance(table_name_or_id, str):
            raise TypeError("Expected argument 'table_name_or_id' to be a str")
        pulumi.set(__self__, "table_name_or_id", table_name_or_id)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_of_expiration and not isinstance(time_of_expiration, str):
            raise TypeError("Expected argument 'time_of_expiration' to be a str")
        pulumi.set(__self__, "time_of_expiration", time_of_expiration)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        Compartment Identifier.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="ddlStatement")
    def ddl_statement(self) -> str:
        """
        A DDL statement representing the schema.
        """
        return pulumi.get(self, "ddl_statement")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace.  Example: `{"foo-namespace": {"bar-key": "value"}}`
        """
        return pulumi.get(self, "defined_tags")

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
        Unique identifier that is immutable.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isAutoReclaimable")
    def is_auto_reclaimable(self) -> bool:
        """
        True if this table can be reclaimed after an idle period.
        """
        return pulumi.get(self, "is_auto_reclaimable")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        A message describing the current state in more detail.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The column name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def schemas(self) -> Sequence['outputs.GetTableSchemaResult']:
        """
        The table schema information as a JSON object.
        """
        return pulumi.get(self, "schemas")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of a table.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        Read-only system tag. These predefined keys are scoped to namespaces.  At present the only supported namespace is `"orcl-cloud"`; and the only key in that namespace is `"free-tier-retained"`. Example: `{"orcl-cloud"": {"free-tier-retained": "true"}}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="tableLimits")
    def table_limits(self) -> Sequence['outputs.GetTableTableLimitResult']:
        """
        Throughput and storage limits configuration of a table.
        """
        return pulumi.get(self, "table_limits")

    @property
    @pulumi.getter(name="tableNameOrId")
    def table_name_or_id(self) -> str:
        return pulumi.get(self, "table_name_or_id")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time the the table was created. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeOfExpiration")
    def time_of_expiration(self) -> str:
        """
        If lifecycleState is INACTIVE, indicates when this table will be automatically removed. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_of_expiration")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The time the the table's metadata was last updated. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_updated")


class AwaitableGetTableResult(GetTableResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTableResult(
            compartment_id=self.compartment_id,
            ddl_statement=self.ddl_statement,
            defined_tags=self.defined_tags,
            freeform_tags=self.freeform_tags,
            id=self.id,
            is_auto_reclaimable=self.is_auto_reclaimable,
            lifecycle_details=self.lifecycle_details,
            name=self.name,
            schemas=self.schemas,
            state=self.state,
            system_tags=self.system_tags,
            table_limits=self.table_limits,
            table_name_or_id=self.table_name_or_id,
            time_created=self.time_created,
            time_of_expiration=self.time_of_expiration,
            time_updated=self.time_updated)


def get_table(compartment_id: Optional[str] = None,
              table_name_or_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTableResult:
    """
    This data source provides details about a specific Table resource in Oracle Cloud Infrastructure NoSQL Database service.

    Get table info by identifier.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_table = oci.Nosql.get_table(table_name_or_id=oci_nosql_table_name_or["test_table_name_or"]["id"],
        compartment_id=var["compartment_id"])
    ```


    :param str compartment_id: The ID of a table's compartment. When a table is identified by name, the compartmentId is often needed to provide context for interpreting the name.
    :param str table_name_or_id: A table name within the compartment, or a table OCID.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['tableNameOrId'] = table_name_or_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Nosql/getTable:getTable', __args__, opts=opts, typ=GetTableResult).value

    return AwaitableGetTableResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        ddl_statement=pulumi.get(__ret__, 'ddl_statement'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        is_auto_reclaimable=pulumi.get(__ret__, 'is_auto_reclaimable'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        name=pulumi.get(__ret__, 'name'),
        schemas=pulumi.get(__ret__, 'schemas'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        table_limits=pulumi.get(__ret__, 'table_limits'),
        table_name_or_id=pulumi.get(__ret__, 'table_name_or_id'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_of_expiration=pulumi.get(__ret__, 'time_of_expiration'),
        time_updated=pulumi.get(__ret__, 'time_updated'))


@_utilities.lift_output_func(get_table)
def get_table_output(compartment_id: Optional[pulumi.Input[str]] = None,
                     table_name_or_id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTableResult]:
    """
    This data source provides details about a specific Table resource in Oracle Cloud Infrastructure NoSQL Database service.

    Get table info by identifier.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_table = oci.Nosql.get_table(table_name_or_id=oci_nosql_table_name_or["test_table_name_or"]["id"],
        compartment_id=var["compartment_id"])
    ```


    :param str compartment_id: The ID of a table's compartment. When a table is identified by name, the compartmentId is often needed to provide context for interpreting the name.
    :param str table_name_or_id: A table name within the compartment, or a table OCID.
    """
    ...
