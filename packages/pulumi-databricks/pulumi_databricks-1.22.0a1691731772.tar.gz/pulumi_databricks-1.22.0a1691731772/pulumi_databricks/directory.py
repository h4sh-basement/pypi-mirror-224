# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DirectoryArgs', 'Directory']

@pulumi.input_type
class DirectoryArgs:
    def __init__(__self__, *,
                 path: pulumi.Input[str],
                 delete_recursive: Optional[pulumi.Input[bool]] = None,
                 object_id: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Directory resource.
        :param pulumi.Input[str] path: The absolute path of the directory, beginning with "/", e.g. "/Demo".
        :param pulumi.Input[int] object_id: Unique identifier for a DIRECTORY
        """
        pulumi.set(__self__, "path", path)
        if delete_recursive is not None:
            pulumi.set(__self__, "delete_recursive", delete_recursive)
        if object_id is not None:
            pulumi.set(__self__, "object_id", object_id)

    @property
    @pulumi.getter
    def path(self) -> pulumi.Input[str]:
        """
        The absolute path of the directory, beginning with "/", e.g. "/Demo".
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: pulumi.Input[str]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter(name="deleteRecursive")
    def delete_recursive(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "delete_recursive")

    @delete_recursive.setter
    def delete_recursive(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "delete_recursive", value)

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[int]]:
        """
        Unique identifier for a DIRECTORY
        """
        return pulumi.get(self, "object_id")

    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "object_id", value)


@pulumi.input_type
class _DirectoryState:
    def __init__(__self__, *,
                 delete_recursive: Optional[pulumi.Input[bool]] = None,
                 object_id: Optional[pulumi.Input[int]] = None,
                 path: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Directory resources.
        :param pulumi.Input[int] object_id: Unique identifier for a DIRECTORY
        :param pulumi.Input[str] path: The absolute path of the directory, beginning with "/", e.g. "/Demo".
        """
        if delete_recursive is not None:
            pulumi.set(__self__, "delete_recursive", delete_recursive)
        if object_id is not None:
            pulumi.set(__self__, "object_id", object_id)
        if path is not None:
            pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter(name="deleteRecursive")
    def delete_recursive(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "delete_recursive")

    @delete_recursive.setter
    def delete_recursive(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "delete_recursive", value)

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[int]]:
        """
        Unique identifier for a DIRECTORY
        """
        return pulumi.get(self, "object_id")

    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "object_id", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        The absolute path of the directory, beginning with "/", e.g. "/Demo".
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)


class Directory(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delete_recursive: Optional[pulumi.Input[bool]] = None,
                 object_id: Optional[pulumi.Input[int]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Import

        The resource directory can be imported using directory pathbash

        ```sh
         $ pulumi import databricks:index/directory:Directory this /path/to/directory
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] object_id: Unique identifier for a DIRECTORY
        :param pulumi.Input[str] path: The absolute path of the directory, beginning with "/", e.g. "/Demo".
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DirectoryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        The resource directory can be imported using directory pathbash

        ```sh
         $ pulumi import databricks:index/directory:Directory this /path/to/directory
        ```

        :param str resource_name: The name of the resource.
        :param DirectoryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DirectoryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delete_recursive: Optional[pulumi.Input[bool]] = None,
                 object_id: Optional[pulumi.Input[int]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DirectoryArgs.__new__(DirectoryArgs)

            __props__.__dict__["delete_recursive"] = delete_recursive
            __props__.__dict__["object_id"] = object_id
            if path is None and not opts.urn:
                raise TypeError("Missing required property 'path'")
            __props__.__dict__["path"] = path
        super(Directory, __self__).__init__(
            'databricks:index/directory:Directory',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            delete_recursive: Optional[pulumi.Input[bool]] = None,
            object_id: Optional[pulumi.Input[int]] = None,
            path: Optional[pulumi.Input[str]] = None) -> 'Directory':
        """
        Get an existing Directory resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] object_id: Unique identifier for a DIRECTORY
        :param pulumi.Input[str] path: The absolute path of the directory, beginning with "/", e.g. "/Demo".
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DirectoryState.__new__(_DirectoryState)

        __props__.__dict__["delete_recursive"] = delete_recursive
        __props__.__dict__["object_id"] = object_id
        __props__.__dict__["path"] = path
        return Directory(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deleteRecursive")
    def delete_recursive(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "delete_recursive")

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Output[int]:
        """
        Unique identifier for a DIRECTORY
        """
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[str]:
        """
        The absolute path of the directory, beginning with "/", e.g. "/Demo".
        """
        return pulumi.get(self, "path")

