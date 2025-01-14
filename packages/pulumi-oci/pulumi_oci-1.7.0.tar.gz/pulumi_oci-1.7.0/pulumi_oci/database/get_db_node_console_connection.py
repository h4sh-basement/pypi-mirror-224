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
    'GetDbNodeConsoleConnectionResult',
    'AwaitableGetDbNodeConsoleConnectionResult',
    'get_db_node_console_connection',
    'get_db_node_console_connection_output',
]

@pulumi.output_type
class GetDbNodeConsoleConnectionResult:
    """
    A collection of values returned by getDbNodeConsoleConnection.
    """
    def __init__(__self__, compartment_id=None, connection_string=None, db_node_id=None, fingerprint=None, id=None, public_key=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if connection_string and not isinstance(connection_string, str):
            raise TypeError("Expected argument 'connection_string' to be a str")
        pulumi.set(__self__, "connection_string", connection_string)
        if db_node_id and not isinstance(db_node_id, str):
            raise TypeError("Expected argument 'db_node_id' to be a str")
        pulumi.set(__self__, "db_node_id", db_node_id)
        if fingerprint and not isinstance(fingerprint, str):
            raise TypeError("Expected argument 'fingerprint' to be a str")
        pulumi.set(__self__, "fingerprint", fingerprint)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if public_key and not isinstance(public_key, str):
            raise TypeError("Expected argument 'public_key' to be a str")
        pulumi.set(__self__, "public_key", public_key)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment to contain the console connection.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> str:
        """
        The SSH connection string for the console connection.
        """
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter(name="dbNodeId")
    def db_node_id(self) -> str:
        """
        The OCID of the database node.
        """
        return pulumi.get(self, "db_node_id")

    @property
    @pulumi.getter
    def fingerprint(self) -> str:
        """
        The SSH public key fingerprint for the console connection.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The OCID of the console connection.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> str:
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the console connection.
        """
        return pulumi.get(self, "state")


class AwaitableGetDbNodeConsoleConnectionResult(GetDbNodeConsoleConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDbNodeConsoleConnectionResult(
            compartment_id=self.compartment_id,
            connection_string=self.connection_string,
            db_node_id=self.db_node_id,
            fingerprint=self.fingerprint,
            id=self.id,
            public_key=self.public_key,
            state=self.state)


def get_db_node_console_connection(db_node_id: Optional[str] = None,
                                   id: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDbNodeConsoleConnectionResult:
    """
    This data source provides details about a specific Db Node Console Connection resource in Oracle Cloud Infrastructure Database service.

    Gets the specified database node console connection's information.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_db_node_console_connection = oci.Database.get_db_node_console_connection(db_node_id=oci_database_db_node["test_db_node"]["id"],
        id=var["db_node_console_connection_id"])
    ```


    :param str db_node_id: The database node [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str id: The OCID of the console connection.
    """
    __args__ = dict()
    __args__['dbNodeId'] = db_node_id
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Database/getDbNodeConsoleConnection:getDbNodeConsoleConnection', __args__, opts=opts, typ=GetDbNodeConsoleConnectionResult).value

    return AwaitableGetDbNodeConsoleConnectionResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        connection_string=pulumi.get(__ret__, 'connection_string'),
        db_node_id=pulumi.get(__ret__, 'db_node_id'),
        fingerprint=pulumi.get(__ret__, 'fingerprint'),
        id=pulumi.get(__ret__, 'id'),
        public_key=pulumi.get(__ret__, 'public_key'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_db_node_console_connection)
def get_db_node_console_connection_output(db_node_id: Optional[pulumi.Input[str]] = None,
                                          id: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDbNodeConsoleConnectionResult]:
    """
    This data source provides details about a specific Db Node Console Connection resource in Oracle Cloud Infrastructure Database service.

    Gets the specified database node console connection's information.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_db_node_console_connection = oci.Database.get_db_node_console_connection(db_node_id=oci_database_db_node["test_db_node"]["id"],
        id=var["db_node_console_connection_id"])
    ```


    :param str db_node_id: The database node [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str id: The OCID of the console connection.
    """
    ...
