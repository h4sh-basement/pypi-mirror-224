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
    'GetDefaultPolicyResult',
    'AwaitableGetDefaultPolicyResult',
    'get_default_policy',
    'get_default_policy_output',
]

@pulumi.output_type
class GetDefaultPolicyResult:
    """
    A collection of values returned by getDefaultPolicy.
    """
    def __init__(__self__, id=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        type of policy.
        """
        return pulumi.get(self, "type")


class AwaitableGetDefaultPolicyResult(GetDefaultPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDefaultPolicyResult(
            id=self.id,
            type=self.type)


def get_default_policy(type: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDefaultPolicyResult:
    """
    Use this data source to retrieve a default policy from Okta. This same thing can be achieved using the `policy_get_policy` with default names, this is simply a shortcut.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    example = okta.policy.get_default_policy(type="PASSWORD")
    ```


    :param str type: Type of policy to retrieve.  Valid values: `OKTA_SIGN_ON`, `PASSWORD`, `MFA_ENROLL`, `IDP_DISCOVERY`
           `"IDP_DISCOVERY"`, `"ACCESS_POLICY"` (**only available as a part of the Identity Engine**), `"PROFILE_ENROLLMENT"` (**only available as a part of the Identity Engine**)
    """
    __args__ = dict()
    __args__['type'] = type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('okta:policy/getDefaultPolicy:getDefaultPolicy', __args__, opts=opts, typ=GetDefaultPolicyResult).value

    return AwaitableGetDefaultPolicyResult(
        id=pulumi.get(__ret__, 'id'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_default_policy)
def get_default_policy_output(type: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDefaultPolicyResult]:
    """
    Use this data source to retrieve a default policy from Okta. This same thing can be achieved using the `policy_get_policy` with default names, this is simply a shortcut.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    example = okta.policy.get_default_policy(type="PASSWORD")
    ```


    :param str type: Type of policy to retrieve.  Valid values: `OKTA_SIGN_ON`, `PASSWORD`, `MFA_ENROLL`, `IDP_DISCOVERY`
           `"IDP_DISCOVERY"`, `"ACCESS_POLICY"` (**only available as a part of the Identity Engine**), `"PROFILE_ENROLLMENT"` (**only available as a part of the Identity Engine**)
    """
    ...
