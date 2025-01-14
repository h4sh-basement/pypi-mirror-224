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
    'GetKeyResult',
    'AwaitableGetKeyResult',
    'get_key',
    'get_key_output',
]

@pulumi.output_type
class GetKeyResult:
    """
    A collection of values returned by getKey.
    """
    def __init__(__self__, compartment_id=None, current_key_version=None, defined_tags=None, desired_state=None, display_name=None, freeform_tags=None, id=None, is_primary=None, key_id=None, key_shapes=None, management_endpoint=None, protection_mode=None, replica_details=None, restore_from_files=None, restore_from_object_stores=None, restore_trigger=None, restored_from_key_id=None, state=None, time_created=None, time_of_deletion=None, vault_id=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if current_key_version and not isinstance(current_key_version, str):
            raise TypeError("Expected argument 'current_key_version' to be a str")
        pulumi.set(__self__, "current_key_version", current_key_version)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if desired_state and not isinstance(desired_state, str):
            raise TypeError("Expected argument 'desired_state' to be a str")
        pulumi.set(__self__, "desired_state", desired_state)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_primary and not isinstance(is_primary, bool):
            raise TypeError("Expected argument 'is_primary' to be a bool")
        pulumi.set(__self__, "is_primary", is_primary)
        if key_id and not isinstance(key_id, str):
            raise TypeError("Expected argument 'key_id' to be a str")
        pulumi.set(__self__, "key_id", key_id)
        if key_shapes and not isinstance(key_shapes, list):
            raise TypeError("Expected argument 'key_shapes' to be a list")
        pulumi.set(__self__, "key_shapes", key_shapes)
        if management_endpoint and not isinstance(management_endpoint, str):
            raise TypeError("Expected argument 'management_endpoint' to be a str")
        pulumi.set(__self__, "management_endpoint", management_endpoint)
        if protection_mode and not isinstance(protection_mode, str):
            raise TypeError("Expected argument 'protection_mode' to be a str")
        pulumi.set(__self__, "protection_mode", protection_mode)
        if replica_details and not isinstance(replica_details, list):
            raise TypeError("Expected argument 'replica_details' to be a list")
        pulumi.set(__self__, "replica_details", replica_details)
        if restore_from_files and not isinstance(restore_from_files, list):
            raise TypeError("Expected argument 'restore_from_files' to be a list")
        pulumi.set(__self__, "restore_from_files", restore_from_files)
        if restore_from_object_stores and not isinstance(restore_from_object_stores, list):
            raise TypeError("Expected argument 'restore_from_object_stores' to be a list")
        pulumi.set(__self__, "restore_from_object_stores", restore_from_object_stores)
        if restore_trigger and not isinstance(restore_trigger, bool):
            raise TypeError("Expected argument 'restore_trigger' to be a bool")
        pulumi.set(__self__, "restore_trigger", restore_trigger)
        if restored_from_key_id and not isinstance(restored_from_key_id, str):
            raise TypeError("Expected argument 'restored_from_key_id' to be a str")
        pulumi.set(__self__, "restored_from_key_id", restored_from_key_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_of_deletion and not isinstance(time_of_deletion, str):
            raise TypeError("Expected argument 'time_of_deletion' to be a str")
        pulumi.set(__self__, "time_of_deletion", time_of_deletion)
        if vault_id and not isinstance(vault_id, str):
            raise TypeError("Expected argument 'vault_id' to be a str")
        pulumi.set(__self__, "vault_id", vault_id)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment that contains this master encryption key.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="currentKeyVersion")
    def current_key_version(self) -> str:
        """
        The OCID of the key version used in cryptographic operations. During key rotation, the service might be in a transitional state where this or a newer key version are used intermittently. The `currentKeyVersion` property is updated when the service is guaranteed to use the new key version for all subsequent encryption operations.
        """
        return pulumi.get(self, "current_key_version")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> str:
        return pulumi.get(self, "desired_state")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        A user-friendly name for the key. It does not have to be unique, and it is changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The OCID of the key.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isPrimary")
    def is_primary(self) -> bool:
        """
        A boolean that will be true when key is primary, and will be false when key is a replica from a primary key.
        """
        return pulumi.get(self, "is_primary")

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> str:
        return pulumi.get(self, "key_id")

    @property
    @pulumi.getter(name="keyShapes")
    def key_shapes(self) -> Sequence['outputs.GetKeyKeyShapeResult']:
        """
        The cryptographic properties of a key.
        """
        return pulumi.get(self, "key_shapes")

    @property
    @pulumi.getter(name="managementEndpoint")
    def management_endpoint(self) -> str:
        return pulumi.get(self, "management_endpoint")

    @property
    @pulumi.getter(name="protectionMode")
    def protection_mode(self) -> str:
        """
        The key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed. A protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are performed inside the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's RSA wrapping key which persists  on the HSM. All cryptographic operations that use a key with a protection mode of `SOFTWARE` are performed on the server. By default,  a key's protection mode is set to `HSM`. You can't change a key's protection mode after the key is created or imported.
        """
        return pulumi.get(self, "protection_mode")

    @property
    @pulumi.getter(name="replicaDetails")
    def replica_details(self) -> Sequence['outputs.GetKeyReplicaDetailResult']:
        """
        Key replica details
        """
        return pulumi.get(self, "replica_details")

    @property
    @pulumi.getter(name="restoreFromFiles")
    def restore_from_files(self) -> Sequence['outputs.GetKeyRestoreFromFileResult']:
        """
        Details where key was backed up.
        """
        return pulumi.get(self, "restore_from_files")

    @property
    @pulumi.getter(name="restoreFromObjectStores")
    def restore_from_object_stores(self) -> Sequence['outputs.GetKeyRestoreFromObjectStoreResult']:
        """
        Details where key was backed up
        """
        return pulumi.get(self, "restore_from_object_stores")

    @property
    @pulumi.getter(name="restoreTrigger")
    def restore_trigger(self) -> bool:
        """
        When flipped, triggers restore if restore options are provided. Values of 0 or 1 are supported.
        """
        return pulumi.get(self, "restore_trigger")

    @property
    @pulumi.getter(name="restoredFromKeyId")
    def restored_from_key_id(self) -> str:
        """
        The OCID of the key from which this key was restored.
        """
        return pulumi.get(self, "restored_from_key_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The key's current lifecycle state.  Example: `ENABLED`
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the key was created, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.  Example: `2018-04-03T21:10:29.600Z`
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeOfDeletion")
    def time_of_deletion(self) -> str:
        """
        An optional property indicating when to delete the key, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format. Example: `2019-04-03T21:10:29.600Z`
        """
        return pulumi.get(self, "time_of_deletion")

    @property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> str:
        """
        The OCID of the vault that contains this key.
        """
        return pulumi.get(self, "vault_id")


class AwaitableGetKeyResult(GetKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKeyResult(
            compartment_id=self.compartment_id,
            current_key_version=self.current_key_version,
            defined_tags=self.defined_tags,
            desired_state=self.desired_state,
            display_name=self.display_name,
            freeform_tags=self.freeform_tags,
            id=self.id,
            is_primary=self.is_primary,
            key_id=self.key_id,
            key_shapes=self.key_shapes,
            management_endpoint=self.management_endpoint,
            protection_mode=self.protection_mode,
            replica_details=self.replica_details,
            restore_from_files=self.restore_from_files,
            restore_from_object_stores=self.restore_from_object_stores,
            restore_trigger=self.restore_trigger,
            restored_from_key_id=self.restored_from_key_id,
            state=self.state,
            time_created=self.time_created,
            time_of_deletion=self.time_of_deletion,
            vault_id=self.vault_id)


def get_key(key_id: Optional[str] = None,
            management_endpoint: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKeyResult:
    """
    This data source provides details about a specific Key resource in Oracle Cloud Infrastructure Kms service.

    Gets information about the specified master encryption key.

    As a management operation, this call is subject to a Key Management limit that applies to the total number
    of requests across all management read operations. Key Management might throttle this call to reject an
    otherwise valid request when the total rate of management read operations exceeds 10 requests per second for
    a given tenancy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_key = oci.Kms.get_key(key_id=oci_kms_key["test_key"]["id"],
        management_endpoint=var["key_management_endpoint"])
    ```


    :param str key_id: The OCID of the key.
    :param str management_endpoint: The service endpoint to perform management operations against. Management operations include 'Create,' 'Update,' 'List,' 'Get,' and 'Delete' operations. See Vault Management endpoint.
    """
    __args__ = dict()
    __args__['keyId'] = key_id
    __args__['managementEndpoint'] = management_endpoint
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Kms/getKey:getKey', __args__, opts=opts, typ=GetKeyResult).value

    return AwaitableGetKeyResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        current_key_version=pulumi.get(__ret__, 'current_key_version'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        desired_state=pulumi.get(__ret__, 'desired_state'),
        display_name=pulumi.get(__ret__, 'display_name'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        is_primary=pulumi.get(__ret__, 'is_primary'),
        key_id=pulumi.get(__ret__, 'key_id'),
        key_shapes=pulumi.get(__ret__, 'key_shapes'),
        management_endpoint=pulumi.get(__ret__, 'management_endpoint'),
        protection_mode=pulumi.get(__ret__, 'protection_mode'),
        replica_details=pulumi.get(__ret__, 'replica_details'),
        restore_from_files=pulumi.get(__ret__, 'restore_from_files'),
        restore_from_object_stores=pulumi.get(__ret__, 'restore_from_object_stores'),
        restore_trigger=pulumi.get(__ret__, 'restore_trigger'),
        restored_from_key_id=pulumi.get(__ret__, 'restored_from_key_id'),
        state=pulumi.get(__ret__, 'state'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_of_deletion=pulumi.get(__ret__, 'time_of_deletion'),
        vault_id=pulumi.get(__ret__, 'vault_id'))


@_utilities.lift_output_func(get_key)
def get_key_output(key_id: Optional[pulumi.Input[str]] = None,
                   management_endpoint: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKeyResult]:
    """
    This data source provides details about a specific Key resource in Oracle Cloud Infrastructure Kms service.

    Gets information about the specified master encryption key.

    As a management operation, this call is subject to a Key Management limit that applies to the total number
    of requests across all management read operations. Key Management might throttle this call to reject an
    otherwise valid request when the total rate of management read operations exceeds 10 requests per second for
    a given tenancy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_key = oci.Kms.get_key(key_id=oci_kms_key["test_key"]["id"],
        management_endpoint=var["key_management_endpoint"])
    ```


    :param str key_id: The OCID of the key.
    :param str management_endpoint: The service endpoint to perform management operations against. Management operations include 'Create,' 'Update,' 'List,' 'Get,' and 'Delete' operations. See Vault Management endpoint.
    """
    ...
