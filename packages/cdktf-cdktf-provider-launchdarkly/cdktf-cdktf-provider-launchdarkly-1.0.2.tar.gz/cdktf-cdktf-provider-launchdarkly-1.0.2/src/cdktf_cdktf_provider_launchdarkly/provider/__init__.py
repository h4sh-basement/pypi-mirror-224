'''
# `provider`

Refer to the Terraform Registory for docs: [`launchdarkly`](https://registry.terraform.io/providers/launchdarkly/launchdarkly/2.14.0/docs).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class LaunchdarklyProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-launchdarkly.provider.LaunchdarklyProvider",
):
    '''Represents a {@link https://registry.terraform.io/providers/launchdarkly/launchdarkly/2.14.0/docs launchdarkly}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        access_token: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        api_host: typing.Optional[builtins.str] = None,
        oauth_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/launchdarkly/launchdarkly/2.14.0/docs launchdarkly} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param access_token: The `personal access token <https://docs.launchdarkly.com/home/account-security/api-access-tokens#personal-tokens>`_ or `service token <https://docs.launchdarkly.com/home/account-security/api-access-tokens#service-tokens>`_ used to authenticate with LaunchDarkly. You can also set this with the ``LAUNCHDARKLY_ACCESS_TOKEN`` environment variable. You must provide either ``access_token`` or ``oauth_token``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/launchdarkly/launchdarkly/2.14.0/docs#access_token LaunchdarklyProvider#access_token}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/launchdarkly/launchdarkly/2.14.0/docs#alias LaunchdarklyProvider#alias}
        :param api_host: The LaunchDarkly host address. If this argument is not specified, the default host address is ``https://app.launchdarkly.com``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/launchdarkly/launchdarkly/2.14.0/docs#api_host LaunchdarklyProvider#api_host}
        :param oauth_token: An OAuth V2 token you use to authenticate with LaunchDarkly. You can also set this with the ``LAUNCHDARKLY_OAUTH_TOKEN`` environment variable. You must provide either ``access_token`` or ``oauth_token``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/launchdarkly/launchdarkly/2.14.0/docs#oauth_token LaunchdarklyProvider#oauth_token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__361329afd854bf518b4157de0781ee1d4b0e0a1ed34515261d7ac92f9008aa00)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = LaunchdarklyProviderConfig(
            access_token=access_token,
            alias=alias,
            api_host=api_host,
            oauth_token=oauth_token,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetApiHost")
    def reset_api_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiHost", []))

    @jsii.member(jsii_name="resetOauthToken")
    def reset_oauth_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthToken", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="apiHostInput")
    def api_host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiHostInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthTokenInput")
    def oauth_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d9f18a06a44e2715c1f4984802ef7619d80459a41472a2355fa6547ec3866b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20a9a4c4b9ff0a1d184551298988ab89fca9ec5ee306923a72e26d029b23aa8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="apiHost")
    def api_host(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiHost"))

    @api_host.setter
    def api_host(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d3f8ce64191581ce37de8bd5a26b71512329b8d8ee57e9e50dcff33577b4364)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiHost", value)

    @builtins.property
    @jsii.member(jsii_name="oauthToken")
    def oauth_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthToken"))

    @oauth_token.setter
    def oauth_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__084fac65756dbc178b8171d12cdc29c68277c46c6048625bf4170e48165295f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthToken", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-launchdarkly.provider.LaunchdarklyProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "access_token": "accessToken",
        "alias": "alias",
        "api_host": "apiHost",
        "oauth_token": "oauthToken",
    },
)
class LaunchdarklyProviderConfig:
    def __init__(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        api_host: typing.Optional[builtins.str] = None,
        oauth_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: The `personal access token <https://docs.launchdarkly.com/home/account-security/api-access-tokens#personal-tokens>`_ or `service token <https://docs.launchdarkly.com/home/account-security/api-access-tokens#service-tokens>`_ used to authenticate with LaunchDarkly. You can also set this with the ``LAUNCHDARKLY_ACCESS_TOKEN`` environment variable. You must provide either ``access_token`` or ``oauth_token``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/launchdarkly/launchdarkly/2.14.0/docs#access_token LaunchdarklyProvider#access_token}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/launchdarkly/launchdarkly/2.14.0/docs#alias LaunchdarklyProvider#alias}
        :param api_host: The LaunchDarkly host address. If this argument is not specified, the default host address is ``https://app.launchdarkly.com``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/launchdarkly/launchdarkly/2.14.0/docs#api_host LaunchdarklyProvider#api_host}
        :param oauth_token: An OAuth V2 token you use to authenticate with LaunchDarkly. You can also set this with the ``LAUNCHDARKLY_OAUTH_TOKEN`` environment variable. You must provide either ``access_token`` or ``oauth_token``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/launchdarkly/launchdarkly/2.14.0/docs#oauth_token LaunchdarklyProvider#oauth_token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63a271634d8257ba9984a180dcb9f63b6327bde59eac52f68c8ec5802d84c5e8)
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument api_host", value=api_host, expected_type=type_hints["api_host"])
            check_type(argname="argument oauth_token", value=oauth_token, expected_type=type_hints["oauth_token"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_token is not None:
            self._values["access_token"] = access_token
        if alias is not None:
            self._values["alias"] = alias
        if api_host is not None:
            self._values["api_host"] = api_host
        if oauth_token is not None:
            self._values["oauth_token"] = oauth_token

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''The `personal access token <https://docs.launchdarkly.com/home/account-security/api-access-tokens#personal-tokens>`_ or `service token <https://docs.launchdarkly.com/home/account-security/api-access-tokens#service-tokens>`_ used to authenticate with LaunchDarkly. You can also set this with the ``LAUNCHDARKLY_ACCESS_TOKEN`` environment variable. You must provide either ``access_token`` or ``oauth_token``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/launchdarkly/launchdarkly/2.14.0/docs#access_token LaunchdarklyProvider#access_token}
        '''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/launchdarkly/launchdarkly/2.14.0/docs#alias LaunchdarklyProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_host(self) -> typing.Optional[builtins.str]:
        '''The LaunchDarkly host address. If this argument is not specified, the default host address is ``https://app.launchdarkly.com``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/launchdarkly/launchdarkly/2.14.0/docs#api_host LaunchdarklyProvider#api_host}
        '''
        result = self._values.get("api_host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_token(self) -> typing.Optional[builtins.str]:
        '''An OAuth V2 token you use to authenticate with LaunchDarkly.

        You can also set this with the ``LAUNCHDARKLY_OAUTH_TOKEN`` environment variable. You must provide either ``access_token`` or ``oauth_token``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/launchdarkly/launchdarkly/2.14.0/docs#oauth_token LaunchdarklyProvider#oauth_token}
        '''
        result = self._values.get("oauth_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchdarklyProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "LaunchdarklyProvider",
    "LaunchdarklyProviderConfig",
]

publication.publish()

def _typecheckingstub__361329afd854bf518b4157de0781ee1d4b0e0a1ed34515261d7ac92f9008aa00(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_token: typing.Optional[builtins.str] = None,
    alias: typing.Optional[builtins.str] = None,
    api_host: typing.Optional[builtins.str] = None,
    oauth_token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d9f18a06a44e2715c1f4984802ef7619d80459a41472a2355fa6547ec3866b5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20a9a4c4b9ff0a1d184551298988ab89fca9ec5ee306923a72e26d029b23aa8b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d3f8ce64191581ce37de8bd5a26b71512329b8d8ee57e9e50dcff33577b4364(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__084fac65756dbc178b8171d12cdc29c68277c46c6048625bf4170e48165295f0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63a271634d8257ba9984a180dcb9f63b6327bde59eac52f68c8ec5802d84c5e8(
    *,
    access_token: typing.Optional[builtins.str] = None,
    alias: typing.Optional[builtins.str] = None,
    api_host: typing.Optional[builtins.str] = None,
    oauth_token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
