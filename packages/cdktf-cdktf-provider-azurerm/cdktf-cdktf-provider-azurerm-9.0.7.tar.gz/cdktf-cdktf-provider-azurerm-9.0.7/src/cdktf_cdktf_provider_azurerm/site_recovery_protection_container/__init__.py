'''
# `azurerm_site_recovery_protection_container`

Refer to the Terraform Registory for docs: [`azurerm_site_recovery_protection_container`](https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container).
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


class SiteRecoveryProtectionContainer(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.siteRecoveryProtectionContainer.SiteRecoveryProtectionContainer",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container azurerm_site_recovery_protection_container}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        recovery_fabric_name: builtins.str,
        recovery_vault_name: builtins.str,
        resource_group_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SiteRecoveryProtectionContainerTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container azurerm_site_recovery_protection_container} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#name SiteRecoveryProtectionContainer#name}.
        :param recovery_fabric_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#recovery_fabric_name SiteRecoveryProtectionContainer#recovery_fabric_name}.
        :param recovery_vault_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#recovery_vault_name SiteRecoveryProtectionContainer#recovery_vault_name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#resource_group_name SiteRecoveryProtectionContainer#resource_group_name}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#id SiteRecoveryProtectionContainer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#timeouts SiteRecoveryProtectionContainer#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__926255614b9736071a9063816975d64ad99301ef2675fb19a7a4fc6dff3ad013)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SiteRecoveryProtectionContainerConfig(
            name=name,
            recovery_fabric_name=recovery_fabric_name,
            recovery_vault_name=recovery_vault_name,
            resource_group_name=resource_group_name,
            id=id,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#create SiteRecoveryProtectionContainer#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#delete SiteRecoveryProtectionContainer#delete}.
        :param read: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#read SiteRecoveryProtectionContainer#read}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#update SiteRecoveryProtectionContainer#update}.
        '''
        value = SiteRecoveryProtectionContainerTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SiteRecoveryProtectionContainerTimeoutsOutputReference":
        return typing.cast("SiteRecoveryProtectionContainerTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="recoveryFabricNameInput")
    def recovery_fabric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recoveryFabricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="recoveryVaultNameInput")
    def recovery_vault_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recoveryVaultNameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "SiteRecoveryProtectionContainerTimeouts"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "SiteRecoveryProtectionContainerTimeouts"]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2205e4f47cba9b6dea04cd852ccd958caca0f6e085ab86e6a4ca568f5835880f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d6285eb09b555e89c1a7a54eb3f6bfe8aada507d1735ada2b793a7618f9034c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="recoveryFabricName")
    def recovery_fabric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recoveryFabricName"))

    @recovery_fabric_name.setter
    def recovery_fabric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f70888b4dbe44096052145176babc366c4b4cbe227e0c5e7e22a1935278cd8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryFabricName", value)

    @builtins.property
    @jsii.member(jsii_name="recoveryVaultName")
    def recovery_vault_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recoveryVaultName"))

    @recovery_vault_name.setter
    def recovery_vault_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d42fc26dfba81211289c4384066bd23499b8bf3dccbf55785c022052ed6caf71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryVaultName", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__874b77620676a2c2f8fa9d8582b28ac973ccdf3c3f7d525338fe603aacac13aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.siteRecoveryProtectionContainer.SiteRecoveryProtectionContainerConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "recovery_fabric_name": "recoveryFabricName",
        "recovery_vault_name": "recoveryVaultName",
        "resource_group_name": "resourceGroupName",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class SiteRecoveryProtectionContainerConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        name: builtins.str,
        recovery_fabric_name: builtins.str,
        recovery_vault_name: builtins.str,
        resource_group_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SiteRecoveryProtectionContainerTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#name SiteRecoveryProtectionContainer#name}.
        :param recovery_fabric_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#recovery_fabric_name SiteRecoveryProtectionContainer#recovery_fabric_name}.
        :param recovery_vault_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#recovery_vault_name SiteRecoveryProtectionContainer#recovery_vault_name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#resource_group_name SiteRecoveryProtectionContainer#resource_group_name}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#id SiteRecoveryProtectionContainer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#timeouts SiteRecoveryProtectionContainer#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = SiteRecoveryProtectionContainerTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db73132a8f7d8821fce857fc6b5c7978c34cd39a641afe8bfd810340d121e8e5)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument recovery_fabric_name", value=recovery_fabric_name, expected_type=type_hints["recovery_fabric_name"])
            check_type(argname="argument recovery_vault_name", value=recovery_vault_name, expected_type=type_hints["recovery_vault_name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "recovery_fabric_name": recovery_fabric_name,
            "recovery_vault_name": recovery_vault_name,
            "resource_group_name": resource_group_name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if id is not None:
            self._values["id"] = id
        if timeouts is not None:
            self._values["timeouts"] = timeouts

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#name SiteRecoveryProtectionContainer#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recovery_fabric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#recovery_fabric_name SiteRecoveryProtectionContainer#recovery_fabric_name}.'''
        result = self._values.get("recovery_fabric_name")
        assert result is not None, "Required property 'recovery_fabric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recovery_vault_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#recovery_vault_name SiteRecoveryProtectionContainer#recovery_vault_name}.'''
        result = self._values.get("recovery_vault_name")
        assert result is not None, "Required property 'recovery_vault_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#resource_group_name SiteRecoveryProtectionContainer#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#id SiteRecoveryProtectionContainer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SiteRecoveryProtectionContainerTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#timeouts SiteRecoveryProtectionContainer#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SiteRecoveryProtectionContainerTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SiteRecoveryProtectionContainerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.siteRecoveryProtectionContainer.SiteRecoveryProtectionContainerTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class SiteRecoveryProtectionContainerTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#create SiteRecoveryProtectionContainer#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#delete SiteRecoveryProtectionContainer#delete}.
        :param read: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#read SiteRecoveryProtectionContainer#read}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#update SiteRecoveryProtectionContainer#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c55e1f741b93dff79fd8d3795ee449fd22a06743147c5288bf0fa0c70039c9b4)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#create SiteRecoveryProtectionContainer#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#delete SiteRecoveryProtectionContainer#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#read SiteRecoveryProtectionContainer#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.69.0/docs/resources/site_recovery_protection_container#update SiteRecoveryProtectionContainer#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SiteRecoveryProtectionContainerTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SiteRecoveryProtectionContainerTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.siteRecoveryProtectionContainer.SiteRecoveryProtectionContainerTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b161b324a43b6181d0830ee288f934a6e453bac3f4277e43573a819710abd174)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4101f8af3c806c593a5f59c2a989ca35abfb3c2df20f68afbf78d4c25cf2213)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5733d3ecf129f216ee6e0edf230c9275f91a9f51a37a74dfe035395e2fb2ba9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4e1da57afade810cc3a6568317aa02fb79041130bb3cd39c9a086235f9b2d5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__404d2907d64d05a5f171d9b6ca80bc52cbc70c42428b7d778ae1dd2cd116b862)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SiteRecoveryProtectionContainerTimeouts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SiteRecoveryProtectionContainerTimeouts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SiteRecoveryProtectionContainerTimeouts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8fde588b989b2359ac55d607fed7e3b26a894bb3f5d1ccf746264b50e9e9775)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SiteRecoveryProtectionContainer",
    "SiteRecoveryProtectionContainerConfig",
    "SiteRecoveryProtectionContainerTimeouts",
    "SiteRecoveryProtectionContainerTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__926255614b9736071a9063816975d64ad99301ef2675fb19a7a4fc6dff3ad013(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    recovery_fabric_name: builtins.str,
    recovery_vault_name: builtins.str,
    resource_group_name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[SiteRecoveryProtectionContainerTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2205e4f47cba9b6dea04cd852ccd958caca0f6e085ab86e6a4ca568f5835880f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d6285eb09b555e89c1a7a54eb3f6bfe8aada507d1735ada2b793a7618f9034c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f70888b4dbe44096052145176babc366c4b4cbe227e0c5e7e22a1935278cd8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d42fc26dfba81211289c4384066bd23499b8bf3dccbf55785c022052ed6caf71(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__874b77620676a2c2f8fa9d8582b28ac973ccdf3c3f7d525338fe603aacac13aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db73132a8f7d8821fce857fc6b5c7978c34cd39a641afe8bfd810340d121e8e5(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    recovery_fabric_name: builtins.str,
    recovery_vault_name: builtins.str,
    resource_group_name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[SiteRecoveryProtectionContainerTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c55e1f741b93dff79fd8d3795ee449fd22a06743147c5288bf0fa0c70039c9b4(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b161b324a43b6181d0830ee288f934a6e453bac3f4277e43573a819710abd174(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4101f8af3c806c593a5f59c2a989ca35abfb3c2df20f68afbf78d4c25cf2213(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5733d3ecf129f216ee6e0edf230c9275f91a9f51a37a74dfe035395e2fb2ba9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4e1da57afade810cc3a6568317aa02fb79041130bb3cd39c9a086235f9b2d5c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__404d2907d64d05a5f171d9b6ca80bc52cbc70c42428b7d778ae1dd2cd116b862(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8fde588b989b2359ac55d607fed7e3b26a894bb3f5d1ccf746264b50e9e9775(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SiteRecoveryProtectionContainerTimeouts]],
) -> None:
    """Type checking stubs"""
    pass
