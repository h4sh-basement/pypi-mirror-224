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
    'GetEveryoneGroupResult',
    'AwaitableGetEveryoneGroupResult',
    'get_everyone_group',
    'get_everyone_group_output',
]

@pulumi.output_type
class GetEveryoneGroupResult:
    """
    A collection of values returned by getEveryoneGroup.
    """
    def __init__(__self__, description=None, id=None, include_users=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if include_users and not isinstance(include_users, bool):
            raise TypeError("Expected argument 'include_users' to be a bool")
        pulumi.set(__self__, "include_users", include_users)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        description of group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="includeUsers")
    def include_users(self) -> Optional[bool]:
        return pulumi.get(self, "include_users")


class AwaitableGetEveryoneGroupResult(GetEveryoneGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEveryoneGroupResult(
            description=self.description,
            id=self.id,
            include_users=self.include_users)


def get_everyone_group(include_users: Optional[bool] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEveryoneGroupResult:
    """
    Use this data source to retrieve the `Everyone` group from Okta. The same can be achieved with the `group.Group` data
    source with `name = "Everyone"`. This is simply a shortcut.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    example = okta.group.get_everyone_group()
    ```


    :param bool include_users: whether to retrieve all member ids.
    """
    __args__ = dict()
    __args__['includeUsers'] = include_users
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('okta:group/getEveryoneGroup:getEveryoneGroup', __args__, opts=opts, typ=GetEveryoneGroupResult).value

    return AwaitableGetEveryoneGroupResult(
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        include_users=pulumi.get(__ret__, 'include_users'))


@_utilities.lift_output_func(get_everyone_group)
def get_everyone_group_output(include_users: Optional[pulumi.Input[Optional[bool]]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEveryoneGroupResult]:
    """
    Use this data source to retrieve the `Everyone` group from Okta. The same can be achieved with the `group.Group` data
    source with `name = "Everyone"`. This is simply a shortcut.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    example = okta.group.get_everyone_group()
    ```


    :param bool include_users: whether to retrieve all member ids.
    """
    ...
