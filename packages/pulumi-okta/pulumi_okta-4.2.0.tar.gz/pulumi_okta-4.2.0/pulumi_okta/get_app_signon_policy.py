# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetAppSignonPolicyResult',
    'AwaitableGetAppSignonPolicyResult',
    'get_app_signon_policy',
    'get_app_signon_policy_output',
]

@pulumi.output_type
class GetAppSignonPolicyResult:
    """
    A collection of values returned by getAppSignonPolicy.
    """
    def __init__(__self__, app_id=None, id=None, name=None):
        if app_id and not isinstance(app_id, str):
            raise TypeError("Expected argument 'app_id' to be a str")
        pulumi.set(__self__, "app_id", app_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> str:
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


class AwaitableGetAppSignonPolicyResult(GetAppSignonPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAppSignonPolicyResult(
            app_id=self.app_id,
            id=self.id,
            name=self.name)


def get_app_signon_policy(app_id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAppSignonPolicyResult:
    """
    > **WARNING:** This feature is only available as a part of the Identity Engine. Contact support for further information.

    Use this data source to retrieve a sign-on policy for the application.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    example = okta.get_app_signon_policy(app_id="app_id")
    ```


    :param str app_id: The application ID.
    """
    __args__ = dict()
    __args__['appId'] = app_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('okta:index/getAppSignonPolicy:getAppSignonPolicy', __args__, opts=opts, typ=GetAppSignonPolicyResult).value

    return AwaitableGetAppSignonPolicyResult(
        app_id=pulumi.get(__ret__, 'app_id'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'))


@_utilities.lift_output_func(get_app_signon_policy)
def get_app_signon_policy_output(app_id: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAppSignonPolicyResult]:
    """
    > **WARNING:** This feature is only available as a part of the Identity Engine. Contact support for further information.

    Use this data source to retrieve a sign-on policy for the application.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    example = okta.get_app_signon_policy(app_id="app_id")
    ```


    :param str app_id: The application ID.
    """
    ...
