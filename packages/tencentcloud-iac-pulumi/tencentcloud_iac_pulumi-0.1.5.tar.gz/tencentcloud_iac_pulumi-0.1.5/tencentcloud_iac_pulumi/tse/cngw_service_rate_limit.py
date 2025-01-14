# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['CngwServiceRateLimitArgs', 'CngwServiceRateLimit']

@pulumi.input_type
class CngwServiceRateLimitArgs:
    def __init__(__self__, *,
                 gateway_id: pulumi.Input[str],
                 limit_detail: pulumi.Input['CngwServiceRateLimitLimitDetailArgs'],
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a CngwServiceRateLimit resource.
        :param pulumi.Input[str] gateway_id: gateway ID.
        :param pulumi.Input['CngwServiceRateLimitLimitDetailArgs'] limit_detail: rate limit configuration.
        :param pulumi.Input[str] name: service name or service ID.
        :param pulumi.Input[Mapping[str, Any]] tags: Tag description list.
        """
        pulumi.set(__self__, "gateway_id", gateway_id)
        pulumi.set(__self__, "limit_detail", limit_detail)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> pulumi.Input[str]:
        """
        gateway ID.
        """
        return pulumi.get(self, "gateway_id")

    @gateway_id.setter
    def gateway_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "gateway_id", value)

    @property
    @pulumi.getter(name="limitDetail")
    def limit_detail(self) -> pulumi.Input['CngwServiceRateLimitLimitDetailArgs']:
        """
        rate limit configuration.
        """
        return pulumi.get(self, "limit_detail")

    @limit_detail.setter
    def limit_detail(self, value: pulumi.Input['CngwServiceRateLimitLimitDetailArgs']):
        pulumi.set(self, "limit_detail", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        service name or service ID.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Tag description list.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _CngwServiceRateLimitState:
    def __init__(__self__, *,
                 gateway_id: Optional[pulumi.Input[str]] = None,
                 limit_detail: Optional[pulumi.Input['CngwServiceRateLimitLimitDetailArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        Input properties used for looking up and filtering CngwServiceRateLimit resources.
        :param pulumi.Input[str] gateway_id: gateway ID.
        :param pulumi.Input['CngwServiceRateLimitLimitDetailArgs'] limit_detail: rate limit configuration.
        :param pulumi.Input[str] name: service name or service ID.
        :param pulumi.Input[Mapping[str, Any]] tags: Tag description list.
        """
        if gateway_id is not None:
            pulumi.set(__self__, "gateway_id", gateway_id)
        if limit_detail is not None:
            pulumi.set(__self__, "limit_detail", limit_detail)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> Optional[pulumi.Input[str]]:
        """
        gateway ID.
        """
        return pulumi.get(self, "gateway_id")

    @gateway_id.setter
    def gateway_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gateway_id", value)

    @property
    @pulumi.getter(name="limitDetail")
    def limit_detail(self) -> Optional[pulumi.Input['CngwServiceRateLimitLimitDetailArgs']]:
        """
        rate limit configuration.
        """
        return pulumi.get(self, "limit_detail")

    @limit_detail.setter
    def limit_detail(self, value: Optional[pulumi.Input['CngwServiceRateLimitLimitDetailArgs']]):
        pulumi.set(self, "limit_detail", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        service name or service ID.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Tag description list.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)


class CngwServiceRateLimit(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 gateway_id: Optional[pulumi.Input[str]] = None,
                 limit_detail: Optional[pulumi.Input[pulumi.InputType['CngwServiceRateLimitLimitDetailArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        """
        Create a CngwServiceRateLimit resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] gateway_id: gateway ID.
        :param pulumi.Input[pulumi.InputType['CngwServiceRateLimitLimitDetailArgs']] limit_detail: rate limit configuration.
        :param pulumi.Input[str] name: service name or service ID.
        :param pulumi.Input[Mapping[str, Any]] tags: Tag description list.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CngwServiceRateLimitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a CngwServiceRateLimit resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param CngwServiceRateLimitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CngwServiceRateLimitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 gateway_id: Optional[pulumi.Input[str]] = None,
                 limit_detail: Optional[pulumi.Input[pulumi.InputType['CngwServiceRateLimitLimitDetailArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
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
            __props__ = CngwServiceRateLimitArgs.__new__(CngwServiceRateLimitArgs)

            if gateway_id is None and not opts.urn:
                raise TypeError("Missing required property 'gateway_id'")
            __props__.__dict__["gateway_id"] = gateway_id
            if limit_detail is None and not opts.urn:
                raise TypeError("Missing required property 'limit_detail'")
            __props__.__dict__["limit_detail"] = limit_detail
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
        super(CngwServiceRateLimit, __self__).__init__(
            'tencentcloud:Tse/cngwServiceRateLimit:CngwServiceRateLimit',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            gateway_id: Optional[pulumi.Input[str]] = None,
            limit_detail: Optional[pulumi.Input[pulumi.InputType['CngwServiceRateLimitLimitDetailArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None) -> 'CngwServiceRateLimit':
        """
        Get an existing CngwServiceRateLimit resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] gateway_id: gateway ID.
        :param pulumi.Input[pulumi.InputType['CngwServiceRateLimitLimitDetailArgs']] limit_detail: rate limit configuration.
        :param pulumi.Input[str] name: service name or service ID.
        :param pulumi.Input[Mapping[str, Any]] tags: Tag description list.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CngwServiceRateLimitState.__new__(_CngwServiceRateLimitState)

        __props__.__dict__["gateway_id"] = gateway_id
        __props__.__dict__["limit_detail"] = limit_detail
        __props__.__dict__["name"] = name
        __props__.__dict__["tags"] = tags
        return CngwServiceRateLimit(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> pulumi.Output[str]:
        """
        gateway ID.
        """
        return pulumi.get(self, "gateway_id")

    @property
    @pulumi.getter(name="limitDetail")
    def limit_detail(self) -> pulumi.Output['outputs.CngwServiceRateLimitLimitDetail']:
        """
        rate limit configuration.
        """
        return pulumi.get(self, "limit_detail")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        service name or service ID.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Tag description list.
        """
        return pulumi.get(self, "tags")

