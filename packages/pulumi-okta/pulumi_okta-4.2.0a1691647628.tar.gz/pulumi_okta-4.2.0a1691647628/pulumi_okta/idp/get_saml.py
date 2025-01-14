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
    'GetSamlResult',
    'AwaitableGetSamlResult',
    'get_saml',
    'get_saml_output',
]

@pulumi.output_type
class GetSamlResult:
    """
    A collection of values returned by getSaml.
    """
    def __init__(__self__, acs_binding=None, acs_type=None, audience=None, id=None, issuer=None, issuer_mode=None, kid=None, name=None, sso_binding=None, sso_destination=None, sso_url=None, subject_filter=None, subject_formats=None, type=None):
        if acs_binding and not isinstance(acs_binding, str):
            raise TypeError("Expected argument 'acs_binding' to be a str")
        pulumi.set(__self__, "acs_binding", acs_binding)
        if acs_type and not isinstance(acs_type, str):
            raise TypeError("Expected argument 'acs_type' to be a str")
        pulumi.set(__self__, "acs_type", acs_type)
        if audience and not isinstance(audience, str):
            raise TypeError("Expected argument 'audience' to be a str")
        pulumi.set(__self__, "audience", audience)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if issuer and not isinstance(issuer, str):
            raise TypeError("Expected argument 'issuer' to be a str")
        pulumi.set(__self__, "issuer", issuer)
        if issuer_mode and not isinstance(issuer_mode, str):
            raise TypeError("Expected argument 'issuer_mode' to be a str")
        pulumi.set(__self__, "issuer_mode", issuer_mode)
        if kid and not isinstance(kid, str):
            raise TypeError("Expected argument 'kid' to be a str")
        pulumi.set(__self__, "kid", kid)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sso_binding and not isinstance(sso_binding, str):
            raise TypeError("Expected argument 'sso_binding' to be a str")
        pulumi.set(__self__, "sso_binding", sso_binding)
        if sso_destination and not isinstance(sso_destination, str):
            raise TypeError("Expected argument 'sso_destination' to be a str")
        pulumi.set(__self__, "sso_destination", sso_destination)
        if sso_url and not isinstance(sso_url, str):
            raise TypeError("Expected argument 'sso_url' to be a str")
        pulumi.set(__self__, "sso_url", sso_url)
        if subject_filter and not isinstance(subject_filter, str):
            raise TypeError("Expected argument 'subject_filter' to be a str")
        pulumi.set(__self__, "subject_filter", subject_filter)
        if subject_formats and not isinstance(subject_formats, list):
            raise TypeError("Expected argument 'subject_formats' to be a list")
        pulumi.set(__self__, "subject_formats", subject_formats)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="acsBinding")
    def acs_binding(self) -> str:
        return pulumi.get(self, "acs_binding")

    @property
    @pulumi.getter(name="acsType")
    def acs_type(self) -> str:
        """
        Determines whether to publish an instance-specific (trust) or organization (shared) ACS endpoint in the SAML metadata.
        """
        return pulumi.get(self, "acs_type")

    @property
    @pulumi.getter
    def audience(self) -> str:
        """
        URI that identifies the target Okta IdP instance (SP)
        """
        return pulumi.get(self, "audience")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        id of idp.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def issuer(self) -> str:
        """
        URI that identifies the issuer (IdP).
        """
        return pulumi.get(self, "issuer")

    @property
    @pulumi.getter(name="issuerMode")
    def issuer_mode(self) -> str:
        """
        indicates whether Okta uses the original Okta org domain URL, or a custom domain URL in the request to the IdP.
        """
        return pulumi.get(self, "issuer_mode")

    @property
    @pulumi.getter
    def kid(self) -> str:
        """
        Key ID reference to the IdP's X.509 signature certificate.
        """
        return pulumi.get(self, "kid")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        name of the idp.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ssoBinding")
    def sso_binding(self) -> str:
        """
        single sign-on binding.
        """
        return pulumi.get(self, "sso_binding")

    @property
    @pulumi.getter(name="ssoDestination")
    def sso_destination(self) -> str:
        """
        SSO request binding, HTTP-POST or HTTP-REDIRECT.
        """
        return pulumi.get(self, "sso_destination")

    @property
    @pulumi.getter(name="ssoUrl")
    def sso_url(self) -> str:
        """
        single sign-on url.
        """
        return pulumi.get(self, "sso_url")

    @property
    @pulumi.getter(name="subjectFilter")
    def subject_filter(self) -> str:
        """
        regular expression pattern used to filter untrusted IdP usernames.
        """
        return pulumi.get(self, "subject_filter")

    @property
    @pulumi.getter(name="subjectFormats")
    def subject_formats(self) -> Sequence[str]:
        """
        Expression to generate or transform a unique username for the IdP user.
        """
        return pulumi.get(self, "subject_formats")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        type of idp.
        """
        return pulumi.get(self, "type")


class AwaitableGetSamlResult(GetSamlResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSamlResult(
            acs_binding=self.acs_binding,
            acs_type=self.acs_type,
            audience=self.audience,
            id=self.id,
            issuer=self.issuer,
            issuer_mode=self.issuer_mode,
            kid=self.kid,
            name=self.name,
            sso_binding=self.sso_binding,
            sso_destination=self.sso_destination,
            sso_url=self.sso_url,
            subject_filter=self.subject_filter,
            subject_formats=self.subject_formats,
            type=self.type)


def get_saml(id: Optional[str] = None,
             name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSamlResult:
    """
    Use this data source to retrieve a SAML IdP from Okta.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    example = okta.idp.get_saml(name="Example App")
    ```


    :param str id: The id of the idp to retrieve, conflicts with `name`.
    :param str name: The name of the idp to retrieve, conflicts with `id`.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('okta:idp/getSaml:getSaml', __args__, opts=opts, typ=GetSamlResult).value

    return AwaitableGetSamlResult(
        acs_binding=pulumi.get(__ret__, 'acs_binding'),
        acs_type=pulumi.get(__ret__, 'acs_type'),
        audience=pulumi.get(__ret__, 'audience'),
        id=pulumi.get(__ret__, 'id'),
        issuer=pulumi.get(__ret__, 'issuer'),
        issuer_mode=pulumi.get(__ret__, 'issuer_mode'),
        kid=pulumi.get(__ret__, 'kid'),
        name=pulumi.get(__ret__, 'name'),
        sso_binding=pulumi.get(__ret__, 'sso_binding'),
        sso_destination=pulumi.get(__ret__, 'sso_destination'),
        sso_url=pulumi.get(__ret__, 'sso_url'),
        subject_filter=pulumi.get(__ret__, 'subject_filter'),
        subject_formats=pulumi.get(__ret__, 'subject_formats'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_saml)
def get_saml_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                    name: Optional[pulumi.Input[Optional[str]]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSamlResult]:
    """
    Use this data source to retrieve a SAML IdP from Okta.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    example = okta.idp.get_saml(name="Example App")
    ```


    :param str id: The id of the idp to retrieve, conflicts with `name`.
    :param str name: The name of the idp to retrieve, conflicts with `id`.
    """
    ...
