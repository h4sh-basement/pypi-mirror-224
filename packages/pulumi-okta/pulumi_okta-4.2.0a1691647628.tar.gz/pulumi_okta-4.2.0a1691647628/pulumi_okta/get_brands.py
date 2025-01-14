# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetBrandsResult',
    'AwaitableGetBrandsResult',
    'get_brands',
]

@pulumi.output_type
class GetBrandsResult:
    """
    A collection of values returned by getBrands.
    """
    def __init__(__self__, brands=None, id=None):
        if brands and not isinstance(brands, list):
            raise TypeError("Expected argument 'brands' to be a list")
        pulumi.set(__self__, "brands", brands)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def brands(self) -> Sequence['outputs.GetBrandsBrandResult']:
        """
        List of `Brand` belonging to the organization
        """
        return pulumi.get(self, "brands")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetBrandsResult(GetBrandsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBrandsResult(
            brands=self.brands,
            id=self.id)


def get_brands(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBrandsResult:
    """
    Use this data source to retrieve the brands belonging to an Okta organization.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    test = okta.get_brands()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('okta:index/getBrands:getBrands', __args__, opts=opts, typ=GetBrandsResult).value

    return AwaitableGetBrandsResult(
        brands=pulumi.get(__ret__, 'brands'),
        id=pulumi.get(__ret__, 'id'))
