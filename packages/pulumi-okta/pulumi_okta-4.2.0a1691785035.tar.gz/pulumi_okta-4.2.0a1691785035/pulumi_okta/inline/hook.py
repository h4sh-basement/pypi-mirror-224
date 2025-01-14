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

__all__ = ['HookArgs', 'Hook']

@pulumi.input_type
class HookArgs:
    def __init__(__self__, *,
                 channel: pulumi.Input[Mapping[str, pulumi.Input[str]]],
                 type: pulumi.Input[str],
                 version: pulumi.Input[str],
                 auth: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 headers: Optional[pulumi.Input[Sequence[pulumi.Input['HookHeaderArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Hook resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] channel: Details of the endpoint the inline hook will hit.
        :param pulumi.Input[str] type: The type of hook to trigger. Currently, the only supported type is `"HTTP"`.
        :param pulumi.Input[str] version: Version of the channel. The currently-supported version is `"1.0.0"`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] auth: Authentication required for inline hook request.
        :param pulumi.Input[Sequence[pulumi.Input['HookHeaderArgs']]] headers: Map of headers to send along in inline hook request.
        :param pulumi.Input[str] name: The inline hook display name.
        """
        pulumi.set(__self__, "channel", channel)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "version", version)
        if auth is not None:
            pulumi.set(__self__, "auth", auth)
        if headers is not None:
            pulumi.set(__self__, "headers", headers)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def channel(self) -> pulumi.Input[Mapping[str, pulumi.Input[str]]]:
        """
        Details of the endpoint the inline hook will hit.
        """
        return pulumi.get(self, "channel")

    @channel.setter
    def channel(self, value: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        pulumi.set(self, "channel", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of hook to trigger. Currently, the only supported type is `"HTTP"`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def version(self) -> pulumi.Input[str]:
        """
        Version of the channel. The currently-supported version is `"1.0.0"`.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: pulumi.Input[str]):
        pulumi.set(self, "version", value)

    @property
    @pulumi.getter
    def auth(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Authentication required for inline hook request.
        """
        return pulumi.get(self, "auth")

    @auth.setter
    def auth(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "auth", value)

    @property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['HookHeaderArgs']]]]:
        """
        Map of headers to send along in inline hook request.
        """
        return pulumi.get(self, "headers")

    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['HookHeaderArgs']]]]):
        pulumi.set(self, "headers", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The inline hook display name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class _HookState:
    def __init__(__self__, *,
                 auth: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 channel: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 headers: Optional[pulumi.Input[Sequence[pulumi.Input['HookHeaderArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Hook resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] auth: Authentication required for inline hook request.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] channel: Details of the endpoint the inline hook will hit.
        :param pulumi.Input[Sequence[pulumi.Input['HookHeaderArgs']]] headers: Map of headers to send along in inline hook request.
        :param pulumi.Input[str] name: The inline hook display name.
        :param pulumi.Input[str] type: The type of hook to trigger. Currently, the only supported type is `"HTTP"`.
        :param pulumi.Input[str] version: Version of the channel. The currently-supported version is `"1.0.0"`.
        """
        if auth is not None:
            pulumi.set(__self__, "auth", auth)
        if channel is not None:
            pulumi.set(__self__, "channel", channel)
        if headers is not None:
            pulumi.set(__self__, "headers", headers)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def auth(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Authentication required for inline hook request.
        """
        return pulumi.get(self, "auth")

    @auth.setter
    def auth(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "auth", value)

    @property
    @pulumi.getter
    def channel(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Details of the endpoint the inline hook will hit.
        """
        return pulumi.get(self, "channel")

    @channel.setter
    def channel(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "channel", value)

    @property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['HookHeaderArgs']]]]:
        """
        Map of headers to send along in inline hook request.
        """
        return pulumi.get(self, "headers")

    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['HookHeaderArgs']]]]):
        pulumi.set(self, "headers", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The inline hook display name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of hook to trigger. Currently, the only supported type is `"HTTP"`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        Version of the channel. The currently-supported version is `"1.0.0"`.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class Hook(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 channel: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 headers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HookHeaderArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates an inline hook.

        This resource allows you to create and configure an inline hook.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.inline.Hook("example",
            auth={
                "key": "Authorization",
                "type": "HEADER",
                "value": "secret",
            },
            channel={
                "method": "POST",
                "uri": "https://example.com/test",
                "version": "1.0.0",
            },
            type="com.okta.oauth2.tokens.transform",
            version="1.0.0")
        ```

        ## Import

        An inline hook can be imported via the Okta ID.

        ```sh
         $ pulumi import okta:inline/hook:Hook example &#60;hook id&#62;
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] auth: Authentication required for inline hook request.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] channel: Details of the endpoint the inline hook will hit.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HookHeaderArgs']]]] headers: Map of headers to send along in inline hook request.
        :param pulumi.Input[str] name: The inline hook display name.
        :param pulumi.Input[str] type: The type of hook to trigger. Currently, the only supported type is `"HTTP"`.
        :param pulumi.Input[str] version: Version of the channel. The currently-supported version is `"1.0.0"`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HookArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an inline hook.

        This resource allows you to create and configure an inline hook.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.inline.Hook("example",
            auth={
                "key": "Authorization",
                "type": "HEADER",
                "value": "secret",
            },
            channel={
                "method": "POST",
                "uri": "https://example.com/test",
                "version": "1.0.0",
            },
            type="com.okta.oauth2.tokens.transform",
            version="1.0.0")
        ```

        ## Import

        An inline hook can be imported via the Okta ID.

        ```sh
         $ pulumi import okta:inline/hook:Hook example &#60;hook id&#62;
        ```

        :param str resource_name: The name of the resource.
        :param HookArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HookArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 channel: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 headers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HookHeaderArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HookArgs.__new__(HookArgs)

            __props__.__dict__["auth"] = auth
            if channel is None and not opts.urn:
                raise TypeError("Missing required property 'channel'")
            __props__.__dict__["channel"] = channel
            __props__.__dict__["headers"] = headers
            __props__.__dict__["name"] = name
            __props__.__dict__["status"] = status
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            if version is None and not opts.urn:
                raise TypeError("Missing required property 'version'")
            __props__.__dict__["version"] = version
        super(Hook, __self__).__init__(
            'okta:inline/hook:Hook',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auth: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            channel: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            headers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HookHeaderArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[str]] = None) -> 'Hook':
        """
        Get an existing Hook resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] auth: Authentication required for inline hook request.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] channel: Details of the endpoint the inline hook will hit.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HookHeaderArgs']]]] headers: Map of headers to send along in inline hook request.
        :param pulumi.Input[str] name: The inline hook display name.
        :param pulumi.Input[str] type: The type of hook to trigger. Currently, the only supported type is `"HTTP"`.
        :param pulumi.Input[str] version: Version of the channel. The currently-supported version is `"1.0.0"`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _HookState.__new__(_HookState)

        __props__.__dict__["auth"] = auth
        __props__.__dict__["channel"] = channel
        __props__.__dict__["headers"] = headers
        __props__.__dict__["name"] = name
        __props__.__dict__["status"] = status
        __props__.__dict__["type"] = type
        __props__.__dict__["version"] = version
        return Hook(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def auth(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Authentication required for inline hook request.
        """
        return pulumi.get(self, "auth")

    @property
    @pulumi.getter
    def channel(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Details of the endpoint the inline hook will hit.
        """
        return pulumi.get(self, "channel")

    @property
    @pulumi.getter
    def headers(self) -> pulumi.Output[Optional[Sequence['outputs.HookHeader']]]:
        """
        Map of headers to send along in inline hook request.
        """
        return pulumi.get(self, "headers")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The inline hook display name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of hook to trigger. Currently, the only supported type is `"HTTP"`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        Version of the channel. The currently-supported version is `"1.0.0"`.
        """
        return pulumi.get(self, "version")

