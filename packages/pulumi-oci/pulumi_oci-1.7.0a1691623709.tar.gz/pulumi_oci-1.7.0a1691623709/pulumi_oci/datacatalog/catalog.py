# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['CatalogArgs', 'Catalog']

@pulumi.input_type
class CatalogArgs:
    def __init__(__self__, *,
                 compartment_id: pulumi.Input[str],
                 attached_catalog_private_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a Catalog resource.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment identifier.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] attached_catalog_private_endpoints: (Updatable) The list of private reverse connection endpoints attached to the catalog
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] display_name: (Updatable) Data catalog identifier.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        pulumi.set(__self__, "compartment_id", compartment_id)
        if attached_catalog_private_endpoints is not None:
            pulumi.set(__self__, "attached_catalog_private_endpoints", attached_catalog_private_endpoints)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Input[str]:
        """
        (Updatable) Compartment identifier.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="attachedCatalogPrivateEndpoints")
    def attached_catalog_private_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        (Updatable) The list of private reverse connection endpoints attached to the catalog


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "attached_catalog_private_endpoints")

    @attached_catalog_private_endpoints.setter
    def attached_catalog_private_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "attached_catalog_private_endpoints", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Data catalog identifier.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)


@pulumi.input_type
class _CatalogState:
    def __init__(__self__, *,
                 attached_catalog_private_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 lifecycle_details: Optional[pulumi.Input[str]] = None,
                 number_of_objects: Optional[pulumi.Input[int]] = None,
                 service_api_url: Optional[pulumi.Input[str]] = None,
                 service_console_url: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_updated: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Catalog resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] attached_catalog_private_endpoints: (Updatable) The list of private reverse connection endpoints attached to the catalog
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment identifier.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] display_name: (Updatable) Data catalog identifier.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[str] lifecycle_details: An message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in 'Failed' state.
        :param pulumi.Input[int] number_of_objects: The number of data objects added to the data catalog. Please see the data catalog documentation for further information on how this is calculated.
        :param pulumi.Input[str] service_api_url: The REST front endpoint URL to the data catalog instance.
        :param pulumi.Input[str] service_console_url: The console front endpoint URL to the data catalog instance.
        :param pulumi.Input[str] state: The current state of the data catalog resource.
        :param pulumi.Input[str] time_created: The time the data catalog was created. An [RFC3339](https://tools.ietf.org/html/rfc3339) formatted datetime string.
        :param pulumi.Input[str] time_updated: The time the data catalog was updated. An [RFC3339](https://tools.ietf.org/html/rfc3339) formatted datetime string.
        """
        if attached_catalog_private_endpoints is not None:
            pulumi.set(__self__, "attached_catalog_private_endpoints", attached_catalog_private_endpoints)
        if compartment_id is not None:
            pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if lifecycle_details is not None:
            pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if number_of_objects is not None:
            pulumi.set(__self__, "number_of_objects", number_of_objects)
        if service_api_url is not None:
            pulumi.set(__self__, "service_api_url", service_api_url)
        if service_console_url is not None:
            pulumi.set(__self__, "service_console_url", service_console_url)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if time_created is not None:
            pulumi.set(__self__, "time_created", time_created)
        if time_updated is not None:
            pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="attachedCatalogPrivateEndpoints")
    def attached_catalog_private_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        (Updatable) The list of private reverse connection endpoints attached to the catalog


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "attached_catalog_private_endpoints")

    @attached_catalog_private_endpoints.setter
    def attached_catalog_private_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "attached_catalog_private_endpoints", value)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Compartment identifier.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Data catalog identifier.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[str]]:
        """
        An message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in 'Failed' state.
        """
        return pulumi.get(self, "lifecycle_details")

    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_details", value)

    @property
    @pulumi.getter(name="numberOfObjects")
    def number_of_objects(self) -> Optional[pulumi.Input[int]]:
        """
        The number of data objects added to the data catalog. Please see the data catalog documentation for further information on how this is calculated.
        """
        return pulumi.get(self, "number_of_objects")

    @number_of_objects.setter
    def number_of_objects(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "number_of_objects", value)

    @property
    @pulumi.getter(name="serviceApiUrl")
    def service_api_url(self) -> Optional[pulumi.Input[str]]:
        """
        The REST front endpoint URL to the data catalog instance.
        """
        return pulumi.get(self, "service_api_url")

    @service_api_url.setter
    def service_api_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_api_url", value)

    @property
    @pulumi.getter(name="serviceConsoleUrl")
    def service_console_url(self) -> Optional[pulumi.Input[str]]:
        """
        The console front endpoint URL to the data catalog instance.
        """
        return pulumi.get(self, "service_console_url")

    @service_console_url.setter
    def service_console_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_console_url", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current state of the data catalog resource.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The time the data catalog was created. An [RFC3339](https://tools.ietf.org/html/rfc3339) formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> Optional[pulumi.Input[str]]:
        """
        The time the data catalog was updated. An [RFC3339](https://tools.ietf.org/html/rfc3339) formatted datetime string.
        """
        return pulumi.get(self, "time_updated")

    @time_updated.setter
    def time_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_updated", value)


class Catalog(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attached_catalog_private_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        """
        This resource provides the Catalog resource in Oracle Cloud Infrastructure Data Catalog service.

        Creates a new data catalog instance that includes a console and an API URL for managing metadata operations.
        For more information, please see the documentation.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_catalog = oci.data_catalog.Catalog("testCatalog",
            compartment_id=var["compartment_id"],
            defined_tags={
                "foo-namespace.bar-key": "value",
            },
            display_name=var["catalog_display_name"],
            freeform_tags={
                "bar-key": "value",
            })
        ```

        ## Import

        Catalogs can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:DataCatalog/catalog:Catalog test_catalog "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] attached_catalog_private_endpoints: (Updatable) The list of private reverse connection endpoints attached to the catalog
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment identifier.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] display_name: (Updatable) Data catalog identifier.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CatalogArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Catalog resource in Oracle Cloud Infrastructure Data Catalog service.

        Creates a new data catalog instance that includes a console and an API URL for managing metadata operations.
        For more information, please see the documentation.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_catalog = oci.data_catalog.Catalog("testCatalog",
            compartment_id=var["compartment_id"],
            defined_tags={
                "foo-namespace.bar-key": "value",
            },
            display_name=var["catalog_display_name"],
            freeform_tags={
                "bar-key": "value",
            })
        ```

        ## Import

        Catalogs can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:DataCatalog/catalog:Catalog test_catalog "id"
        ```

        :param str resource_name: The name of the resource.
        :param CatalogArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CatalogArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attached_catalog_private_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = CatalogArgs.__new__(CatalogArgs)

            __props__.__dict__["attached_catalog_private_endpoints"] = attached_catalog_private_endpoints
            if compartment_id is None and not opts.urn:
                raise TypeError("Missing required property 'compartment_id'")
            __props__.__dict__["compartment_id"] = compartment_id
            __props__.__dict__["defined_tags"] = defined_tags
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["freeform_tags"] = freeform_tags
            __props__.__dict__["lifecycle_details"] = None
            __props__.__dict__["number_of_objects"] = None
            __props__.__dict__["service_api_url"] = None
            __props__.__dict__["service_console_url"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_updated"] = None
        super(Catalog, __self__).__init__(
            'oci:DataCatalog/catalog:Catalog',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            attached_catalog_private_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            lifecycle_details: Optional[pulumi.Input[str]] = None,
            number_of_objects: Optional[pulumi.Input[int]] = None,
            service_api_url: Optional[pulumi.Input[str]] = None,
            service_console_url: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_updated: Optional[pulumi.Input[str]] = None) -> 'Catalog':
        """
        Get an existing Catalog resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] attached_catalog_private_endpoints: (Updatable) The list of private reverse connection endpoints attached to the catalog
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment identifier.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] display_name: (Updatable) Data catalog identifier.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[str] lifecycle_details: An message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in 'Failed' state.
        :param pulumi.Input[int] number_of_objects: The number of data objects added to the data catalog. Please see the data catalog documentation for further information on how this is calculated.
        :param pulumi.Input[str] service_api_url: The REST front endpoint URL to the data catalog instance.
        :param pulumi.Input[str] service_console_url: The console front endpoint URL to the data catalog instance.
        :param pulumi.Input[str] state: The current state of the data catalog resource.
        :param pulumi.Input[str] time_created: The time the data catalog was created. An [RFC3339](https://tools.ietf.org/html/rfc3339) formatted datetime string.
        :param pulumi.Input[str] time_updated: The time the data catalog was updated. An [RFC3339](https://tools.ietf.org/html/rfc3339) formatted datetime string.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CatalogState.__new__(_CatalogState)

        __props__.__dict__["attached_catalog_private_endpoints"] = attached_catalog_private_endpoints
        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["lifecycle_details"] = lifecycle_details
        __props__.__dict__["number_of_objects"] = number_of_objects
        __props__.__dict__["service_api_url"] = service_api_url
        __props__.__dict__["service_console_url"] = service_console_url
        __props__.__dict__["state"] = state
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_updated"] = time_updated
        return Catalog(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="attachedCatalogPrivateEndpoints")
    def attached_catalog_private_endpoints(self) -> pulumi.Output[Sequence[str]]:
        """
        (Updatable) The list of private reverse connection endpoints attached to the catalog


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "attached_catalog_private_endpoints")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        (Updatable) Compartment identifier.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        (Updatable) Data catalog identifier.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> pulumi.Output[str]:
        """
        An message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in 'Failed' state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="numberOfObjects")
    def number_of_objects(self) -> pulumi.Output[int]:
        """
        The number of data objects added to the data catalog. Please see the data catalog documentation for further information on how this is calculated.
        """
        return pulumi.get(self, "number_of_objects")

    @property
    @pulumi.getter(name="serviceApiUrl")
    def service_api_url(self) -> pulumi.Output[str]:
        """
        The REST front endpoint URL to the data catalog instance.
        """
        return pulumi.get(self, "service_api_url")

    @property
    @pulumi.getter(name="serviceConsoleUrl")
    def service_console_url(self) -> pulumi.Output[str]:
        """
        The console front endpoint URL to the data catalog instance.
        """
        return pulumi.get(self, "service_console_url")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the data catalog resource.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The time the data catalog was created. An [RFC3339](https://tools.ietf.org/html/rfc3339) formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> pulumi.Output[str]:
        """
        The time the data catalog was updated. An [RFC3339](https://tools.ietf.org/html/rfc3339) formatted datetime string.
        """
        return pulumi.get(self, "time_updated")

