# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ImageSharePermissionArgs', 'ImageSharePermission']

@pulumi.input_type
class ImageSharePermissionArgs:
    def __init__(__self__, *,
                 account_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 image_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a ImageSharePermission resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] account_ids: List of account IDs with which an image is shared.
        :param pulumi.Input[str] image_id: Image ID such as `img-gvbnzy6f`. You can only specify an image in the NORMAL state.
        """
        pulumi.set(__self__, "account_ids", account_ids)
        pulumi.set(__self__, "image_id", image_id)

    @property
    @pulumi.getter(name="accountIds")
    def account_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        List of account IDs with which an image is shared.
        """
        return pulumi.get(self, "account_ids")

    @account_ids.setter
    def account_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "account_ids", value)

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> pulumi.Input[str]:
        """
        Image ID such as `img-gvbnzy6f`. You can only specify an image in the NORMAL state.
        """
        return pulumi.get(self, "image_id")

    @image_id.setter
    def image_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "image_id", value)


@pulumi.input_type
class _ImageSharePermissionState:
    def __init__(__self__, *,
                 account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 image_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ImageSharePermission resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] account_ids: List of account IDs with which an image is shared.
        :param pulumi.Input[str] image_id: Image ID such as `img-gvbnzy6f`. You can only specify an image in the NORMAL state.
        """
        if account_ids is not None:
            pulumi.set(__self__, "account_ids", account_ids)
        if image_id is not None:
            pulumi.set(__self__, "image_id", image_id)

    @property
    @pulumi.getter(name="accountIds")
    def account_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of account IDs with which an image is shared.
        """
        return pulumi.get(self, "account_ids")

    @account_ids.setter
    def account_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "account_ids", value)

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> Optional[pulumi.Input[str]]:
        """
        Image ID such as `img-gvbnzy6f`. You can only specify an image in the NORMAL state.
        """
        return pulumi.get(self, "image_id")

    @image_id.setter
    def image_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_id", value)


class ImageSharePermission(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 image_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a resource to create a cvm image_share_permission

        ## Example Usage

        ```python
        import pulumi
        import tencentcloud_iac_pulumi as tencentcloud

        image_share_permission = tencentcloud.cvm.ImageSharePermission("imageSharePermission",
            account_ids=["xxxxxx"],
            image_id="img-xxxxxx")
        ```

        ## Import

        cvm image_share_permission can be imported using the id, e.g.

        ```sh
         $ pulumi import tencentcloud:Cvm/imageSharePermission:ImageSharePermission image_share_permission image_share_permission_id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] account_ids: List of account IDs with which an image is shared.
        :param pulumi.Input[str] image_id: Image ID such as `img-gvbnzy6f`. You can only specify an image in the NORMAL state.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ImageSharePermissionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to create a cvm image_share_permission

        ## Example Usage

        ```python
        import pulumi
        import tencentcloud_iac_pulumi as tencentcloud

        image_share_permission = tencentcloud.cvm.ImageSharePermission("imageSharePermission",
            account_ids=["xxxxxx"],
            image_id="img-xxxxxx")
        ```

        ## Import

        cvm image_share_permission can be imported using the id, e.g.

        ```sh
         $ pulumi import tencentcloud:Cvm/imageSharePermission:ImageSharePermission image_share_permission image_share_permission_id
        ```

        :param str resource_name: The name of the resource.
        :param ImageSharePermissionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ImageSharePermissionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 image_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ImageSharePermissionArgs.__new__(ImageSharePermissionArgs)

            if account_ids is None and not opts.urn:
                raise TypeError("Missing required property 'account_ids'")
            __props__.__dict__["account_ids"] = account_ids
            if image_id is None and not opts.urn:
                raise TypeError("Missing required property 'image_id'")
            __props__.__dict__["image_id"] = image_id
        super(ImageSharePermission, __self__).__init__(
            'tencentcloud:Cvm/imageSharePermission:ImageSharePermission',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            image_id: Optional[pulumi.Input[str]] = None) -> 'ImageSharePermission':
        """
        Get an existing ImageSharePermission resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] account_ids: List of account IDs with which an image is shared.
        :param pulumi.Input[str] image_id: Image ID such as `img-gvbnzy6f`. You can only specify an image in the NORMAL state.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ImageSharePermissionState.__new__(_ImageSharePermissionState)

        __props__.__dict__["account_ids"] = account_ids
        __props__.__dict__["image_id"] = image_id
        return ImageSharePermission(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountIds")
    def account_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        List of account IDs with which an image is shared.
        """
        return pulumi.get(self, "account_ids")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> pulumi.Output[str]:
        """
        Image ID such as `img-gvbnzy6f`. You can only specify an image in the NORMAL state.
        """
        return pulumi.get(self, "image_id")

