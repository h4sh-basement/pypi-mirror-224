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

import aws_cdk as _aws_cdk_ceddda9d
import aws_cdk.aws_config as _aws_cdk_aws_config_ceddda9d
import aws_cdk.aws_iam as _aws_cdk_aws_iam_ceddda9d
import constructs as _constructs_77d1e7e8
from ..config import RemediationConfiguration as _RemediationConfiguration_ddf657d5


class IamPasswordPolicy(
    _aws_cdk_aws_config_ceddda9d.ManagedRule,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-extensions.config_rules.IamPasswordPolicy",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.IConstruct,
        id: builtins.str,
        *,
        auto_remediation: typing.Optional[builtins.bool] = None,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        maximum_execution_frequency: typing.Optional[_aws_cdk_aws_config_ceddda9d.MaximumExecutionFrequency] = None,
        max_password_age: typing.Optional[jsii.Number] = None,
        minimum_password_length: typing.Optional[jsii.Number] = None,
        password_reuse_prevention: typing.Optional[jsii.Number] = None,
        require_lowercase_characters: typing.Optional[builtins.bool] = None,
        require_numbers: typing.Optional[builtins.bool] = None,
        require_symbols: typing.Optional[builtins.bool] = None,
        require_uppercase_characters: typing.Optional[builtins.bool] = None,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param auto_remediation: 
        :param config_rule_name: 
        :param description: 
        :param maximum_execution_frequency: 
        :param max_password_age: 
        :param minimum_password_length: 
        :param password_reuse_prevention: 
        :param require_lowercase_characters: 
        :param require_numbers: 
        :param require_symbols: 
        :param require_uppercase_characters: 
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbaef20938eea2e2bf01240351290cd5b6b990b61b708f27525cb57f727b113c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = IamPasswordPolicyProps(
            auto_remediation=auto_remediation,
            config_rule_name=config_rule_name,
            description=description,
            maximum_execution_frequency=maximum_execution_frequency,
            max_password_age=max_password_age,
            minimum_password_length=minimum_password_length,
            password_reuse_prevention=password_reuse_prevention,
            require_lowercase_characters=require_lowercase_characters,
            require_numbers=require_numbers,
            require_symbols=require_symbols,
            require_uppercase_characters=require_uppercase_characters,
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="DEFAULT_DESCRIPTION")
    def DEFAULT_DESCRIPTION(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "DEFAULT_DESCRIPTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DEFAULT_MAX_PASSWORD_AGE")
    def DEFAULT_MAX_PASSWORD_AGE(cls) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.sget(cls, "DEFAULT_MAX_PASSWORD_AGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DEFAULT_MINIMUM_PASSWORD_LENGTH")
    def DEFAULT_MINIMUM_PASSWORD_LENGTH(cls) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.sget(cls, "DEFAULT_MINIMUM_PASSWORD_LENGTH"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DEFAULT_PASSWORD_REUSE_PREVENTION")
    def DEFAULT_PASSWORD_REUSE_PREVENTION(cls) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.sget(cls, "DEFAULT_PASSWORD_REUSE_PREVENTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DEFAULT_REQUIRE_LOWERCASE_CHARACTERS")
    def DEFAULT_REQUIRE_LOWERCASE_CHARACTERS(cls) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.sget(cls, "DEFAULT_REQUIRE_LOWERCASE_CHARACTERS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DEFAULT_REQUIRE_NUMBERS")
    def DEFAULT_REQUIRE_NUMBERS(cls) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.sget(cls, "DEFAULT_REQUIRE_NUMBERS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DEFAULT_REQUIRE_SYMBOLS")
    def DEFAULT_REQUIRE_SYMBOLS(cls) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.sget(cls, "DEFAULT_REQUIRE_SYMBOLS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DEFAULT_REQUIRE_UPPERCASE_CHARACTERS")
    def DEFAULT_REQUIRE_UPPERCASE_CHARACTERS(cls) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.sget(cls, "DEFAULT_REQUIRE_UPPERCASE_CHARACTERS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="MANAGED_RULE_NAME")
    def MANAGED_RULE_NAME(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "MANAGED_RULE_NAME"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REMEDIATION_DOCUMENT_NAME")
    def REMEDIATION_DOCUMENT_NAME(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "REMEDIATION_DOCUMENT_NAME"))

    @builtins.property
    @jsii.member(jsii_name="maxPasswordAge")
    def max_password_age(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxPasswordAge"))

    @builtins.property
    @jsii.member(jsii_name="minimumPasswordLength")
    def minimum_password_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumPasswordLength"))

    @builtins.property
    @jsii.member(jsii_name="passwordReusePrevention")
    def password_reuse_prevention(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "passwordReusePrevention"))

    @builtins.property
    @jsii.member(jsii_name="remediationConfiguration")
    def remediation_configuration(self) -> _RemediationConfiguration_ddf657d5:
        return typing.cast(_RemediationConfiguration_ddf657d5, jsii.get(self, "remediationConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="remediationPolicy")
    def remediation_policy(self) -> _aws_cdk_aws_iam_ceddda9d.ManagedPolicy:
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.ManagedPolicy, jsii.get(self, "remediationPolicy"))

    @builtins.property
    @jsii.member(jsii_name="remediationRole")
    def remediation_role(self) -> _aws_cdk_aws_iam_ceddda9d.Role:
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.Role, jsii.get(self, "remediationRole"))

    @builtins.property
    @jsii.member(jsii_name="requireLowercaseCharacters")
    def require_lowercase_characters(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "requireLowercaseCharacters"))

    @builtins.property
    @jsii.member(jsii_name="requireNumbers")
    def require_numbers(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "requireNumbers"))

    @builtins.property
    @jsii.member(jsii_name="requireSymbols")
    def require_symbols(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "requireSymbols"))

    @builtins.property
    @jsii.member(jsii_name="requireUppercaseCharacters")
    def require_uppercase_characters(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "requireUppercaseCharacters"))


@jsii.data_type(
    jsii_type="cdk-extensions.config_rules.IamPasswordPolicyProps",
    jsii_struct_bases=[_aws_cdk_ceddda9d.ResourceProps],
    name_mapping={
        "account": "account",
        "environment_from_arn": "environmentFromArn",
        "physical_name": "physicalName",
        "region": "region",
        "auto_remediation": "autoRemediation",
        "config_rule_name": "configRuleName",
        "description": "description",
        "maximum_execution_frequency": "maximumExecutionFrequency",
        "max_password_age": "maxPasswordAge",
        "minimum_password_length": "minimumPasswordLength",
        "password_reuse_prevention": "passwordReusePrevention",
        "require_lowercase_characters": "requireLowercaseCharacters",
        "require_numbers": "requireNumbers",
        "require_symbols": "requireSymbols",
        "require_uppercase_characters": "requireUppercaseCharacters",
    },
)
class IamPasswordPolicyProps(_aws_cdk_ceddda9d.ResourceProps):
    def __init__(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        auto_remediation: typing.Optional[builtins.bool] = None,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        maximum_execution_frequency: typing.Optional[_aws_cdk_aws_config_ceddda9d.MaximumExecutionFrequency] = None,
        max_password_age: typing.Optional[jsii.Number] = None,
        minimum_password_length: typing.Optional[jsii.Number] = None,
        password_reuse_prevention: typing.Optional[jsii.Number] = None,
        require_lowercase_characters: typing.Optional[builtins.bool] = None,
        require_numbers: typing.Optional[builtins.bool] = None,
        require_symbols: typing.Optional[builtins.bool] = None,
        require_uppercase_characters: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        :param auto_remediation: 
        :param config_rule_name: 
        :param description: 
        :param maximum_execution_frequency: 
        :param max_password_age: 
        :param minimum_password_length: 
        :param password_reuse_prevention: 
        :param require_lowercase_characters: 
        :param require_numbers: 
        :param require_symbols: 
        :param require_uppercase_characters: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17518a3ffb803b4ea560ba6c040e5485c13ad12a235324ab1d368a7f0566219f)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument environment_from_arn", value=environment_from_arn, expected_type=type_hints["environment_from_arn"])
            check_type(argname="argument physical_name", value=physical_name, expected_type=type_hints["physical_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument auto_remediation", value=auto_remediation, expected_type=type_hints["auto_remediation"])
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
            check_type(argname="argument max_password_age", value=max_password_age, expected_type=type_hints["max_password_age"])
            check_type(argname="argument minimum_password_length", value=minimum_password_length, expected_type=type_hints["minimum_password_length"])
            check_type(argname="argument password_reuse_prevention", value=password_reuse_prevention, expected_type=type_hints["password_reuse_prevention"])
            check_type(argname="argument require_lowercase_characters", value=require_lowercase_characters, expected_type=type_hints["require_lowercase_characters"])
            check_type(argname="argument require_numbers", value=require_numbers, expected_type=type_hints["require_numbers"])
            check_type(argname="argument require_symbols", value=require_symbols, expected_type=type_hints["require_symbols"])
            check_type(argname="argument require_uppercase_characters", value=require_uppercase_characters, expected_type=type_hints["require_uppercase_characters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if account is not None:
            self._values["account"] = account
        if environment_from_arn is not None:
            self._values["environment_from_arn"] = environment_from_arn
        if physical_name is not None:
            self._values["physical_name"] = physical_name
        if region is not None:
            self._values["region"] = region
        if auto_remediation is not None:
            self._values["auto_remediation"] = auto_remediation
        if config_rule_name is not None:
            self._values["config_rule_name"] = config_rule_name
        if description is not None:
            self._values["description"] = description
        if maximum_execution_frequency is not None:
            self._values["maximum_execution_frequency"] = maximum_execution_frequency
        if max_password_age is not None:
            self._values["max_password_age"] = max_password_age
        if minimum_password_length is not None:
            self._values["minimum_password_length"] = minimum_password_length
        if password_reuse_prevention is not None:
            self._values["password_reuse_prevention"] = password_reuse_prevention
        if require_lowercase_characters is not None:
            self._values["require_lowercase_characters"] = require_lowercase_characters
        if require_numbers is not None:
            self._values["require_numbers"] = require_numbers
        if require_symbols is not None:
            self._values["require_symbols"] = require_symbols
        if require_uppercase_characters is not None:
            self._values["require_uppercase_characters"] = require_uppercase_characters

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID this resource belongs to.

        :default: - the resource is in the same account as the stack it belongs to
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_from_arn(self) -> typing.Optional[builtins.str]:
        '''ARN to deduce region and account from.

        The ARN is parsed and the account and region are taken from the ARN.
        This should be used for imported resources.

        Cannot be supplied together with either ``account`` or ``region``.

        :default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        '''
        result = self._values.get("environment_from_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def physical_name(self) -> typing.Optional[builtins.str]:
        '''The value passed in by users to the physical name prop of the resource.

        - ``undefined`` implies that a physical name will be allocated by
          CloudFormation during deployment.
        - a concrete value implies a specific physical name
        - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated
          by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation.

        :default: - The physical name will be allocated by CloudFormation at deployment time
        '''
        result = self._values.get("physical_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The AWS region this resource belongs to.

        :default: - the resource is in the same region as the stack it belongs to
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_remediation(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("auto_remediation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def config_rule_name(self) -> typing.Optional[builtins.str]:
        result = self._values.get("config_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maximum_execution_frequency(
        self,
    ) -> typing.Optional[_aws_cdk_aws_config_ceddda9d.MaximumExecutionFrequency]:
        result = self._values.get("maximum_execution_frequency")
        return typing.cast(typing.Optional[_aws_cdk_aws_config_ceddda9d.MaximumExecutionFrequency], result)

    @builtins.property
    def max_password_age(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("max_password_age")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def minimum_password_length(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("minimum_password_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password_reuse_prevention(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("password_reuse_prevention")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def require_lowercase_characters(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("require_lowercase_characters")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def require_numbers(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("require_numbers")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def require_symbols(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("require_symbols")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def require_uppercase_characters(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("require_uppercase_characters")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IamPasswordPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpcDefaultSecurityGroupClosed(
    _aws_cdk_aws_config_ceddda9d.ManagedRule,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-extensions.config_rules.VpcDefaultSecurityGroupClosed",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.IConstruct,
        id: builtins.str,
        *,
        auto_remediation: typing.Optional[builtins.bool] = None,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        maximum_execution_frequency: typing.Optional[_aws_cdk_aws_config_ceddda9d.MaximumExecutionFrequency] = None,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param auto_remediation: 
        :param config_rule_name: 
        :param description: 
        :param maximum_execution_frequency: 
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11d7229848bc04b1128e4db81c8f3b2737335e86186608261b9305f4ec75f4da)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = VpcDefaultSecurityGroupClosedProps(
            auto_remediation=auto_remediation,
            config_rule_name=config_rule_name,
            description=description,
            maximum_execution_frequency=maximum_execution_frequency,
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="DEFAULT_DESCRIPTION")
    def DEFAULT_DESCRIPTION(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "DEFAULT_DESCRIPTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="MANAGED_RULE_NAME")
    def MANAGED_RULE_NAME(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "MANAGED_RULE_NAME"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REMEDIATION_DOCUMENT_NAME")
    def REMEDIATION_DOCUMENT_NAME(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "REMEDIATION_DOCUMENT_NAME"))

    @builtins.property
    @jsii.member(jsii_name="remediationConfiguration")
    def remediation_configuration(self) -> _RemediationConfiguration_ddf657d5:
        return typing.cast(_RemediationConfiguration_ddf657d5, jsii.get(self, "remediationConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="remediationPolicy")
    def remediation_policy(self) -> _aws_cdk_aws_iam_ceddda9d.ManagedPolicy:
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.ManagedPolicy, jsii.get(self, "remediationPolicy"))

    @builtins.property
    @jsii.member(jsii_name="remediationRole")
    def remediation_role(self) -> _aws_cdk_aws_iam_ceddda9d.Role:
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.Role, jsii.get(self, "remediationRole"))


@jsii.data_type(
    jsii_type="cdk-extensions.config_rules.VpcDefaultSecurityGroupClosedProps",
    jsii_struct_bases=[_aws_cdk_ceddda9d.ResourceProps],
    name_mapping={
        "account": "account",
        "environment_from_arn": "environmentFromArn",
        "physical_name": "physicalName",
        "region": "region",
        "auto_remediation": "autoRemediation",
        "config_rule_name": "configRuleName",
        "description": "description",
        "maximum_execution_frequency": "maximumExecutionFrequency",
    },
)
class VpcDefaultSecurityGroupClosedProps(_aws_cdk_ceddda9d.ResourceProps):
    def __init__(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        auto_remediation: typing.Optional[builtins.bool] = None,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        maximum_execution_frequency: typing.Optional[_aws_cdk_aws_config_ceddda9d.MaximumExecutionFrequency] = None,
    ) -> None:
        '''
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        :param auto_remediation: 
        :param config_rule_name: 
        :param description: 
        :param maximum_execution_frequency: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88046e1726952b7c07ae0f5a9e06e1c06f7915c2febb2d232dcf350de5476bf5)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument environment_from_arn", value=environment_from_arn, expected_type=type_hints["environment_from_arn"])
            check_type(argname="argument physical_name", value=physical_name, expected_type=type_hints["physical_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument auto_remediation", value=auto_remediation, expected_type=type_hints["auto_remediation"])
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if account is not None:
            self._values["account"] = account
        if environment_from_arn is not None:
            self._values["environment_from_arn"] = environment_from_arn
        if physical_name is not None:
            self._values["physical_name"] = physical_name
        if region is not None:
            self._values["region"] = region
        if auto_remediation is not None:
            self._values["auto_remediation"] = auto_remediation
        if config_rule_name is not None:
            self._values["config_rule_name"] = config_rule_name
        if description is not None:
            self._values["description"] = description
        if maximum_execution_frequency is not None:
            self._values["maximum_execution_frequency"] = maximum_execution_frequency

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID this resource belongs to.

        :default: - the resource is in the same account as the stack it belongs to
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_from_arn(self) -> typing.Optional[builtins.str]:
        '''ARN to deduce region and account from.

        The ARN is parsed and the account and region are taken from the ARN.
        This should be used for imported resources.

        Cannot be supplied together with either ``account`` or ``region``.

        :default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        '''
        result = self._values.get("environment_from_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def physical_name(self) -> typing.Optional[builtins.str]:
        '''The value passed in by users to the physical name prop of the resource.

        - ``undefined`` implies that a physical name will be allocated by
          CloudFormation during deployment.
        - a concrete value implies a specific physical name
        - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated
          by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation.

        :default: - The physical name will be allocated by CloudFormation at deployment time
        '''
        result = self._values.get("physical_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The AWS region this resource belongs to.

        :default: - the resource is in the same region as the stack it belongs to
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_remediation(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("auto_remediation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def config_rule_name(self) -> typing.Optional[builtins.str]:
        result = self._values.get("config_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maximum_execution_frequency(
        self,
    ) -> typing.Optional[_aws_cdk_aws_config_ceddda9d.MaximumExecutionFrequency]:
        result = self._values.get("maximum_execution_frequency")
        return typing.cast(typing.Optional[_aws_cdk_aws_config_ceddda9d.MaximumExecutionFrequency], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcDefaultSecurityGroupClosedProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IamPasswordPolicy",
    "IamPasswordPolicyProps",
    "VpcDefaultSecurityGroupClosed",
    "VpcDefaultSecurityGroupClosedProps",
]

publication.publish()

def _typecheckingstub__bbaef20938eea2e2bf01240351290cd5b6b990b61b708f27525cb57f727b113c(
    scope: _constructs_77d1e7e8.IConstruct,
    id: builtins.str,
    *,
    auto_remediation: typing.Optional[builtins.bool] = None,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    maximum_execution_frequency: typing.Optional[_aws_cdk_aws_config_ceddda9d.MaximumExecutionFrequency] = None,
    max_password_age: typing.Optional[jsii.Number] = None,
    minimum_password_length: typing.Optional[jsii.Number] = None,
    password_reuse_prevention: typing.Optional[jsii.Number] = None,
    require_lowercase_characters: typing.Optional[builtins.bool] = None,
    require_numbers: typing.Optional[builtins.bool] = None,
    require_symbols: typing.Optional[builtins.bool] = None,
    require_uppercase_characters: typing.Optional[builtins.bool] = None,
    account: typing.Optional[builtins.str] = None,
    environment_from_arn: typing.Optional[builtins.str] = None,
    physical_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17518a3ffb803b4ea560ba6c040e5485c13ad12a235324ab1d368a7f0566219f(
    *,
    account: typing.Optional[builtins.str] = None,
    environment_from_arn: typing.Optional[builtins.str] = None,
    physical_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    auto_remediation: typing.Optional[builtins.bool] = None,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    maximum_execution_frequency: typing.Optional[_aws_cdk_aws_config_ceddda9d.MaximumExecutionFrequency] = None,
    max_password_age: typing.Optional[jsii.Number] = None,
    minimum_password_length: typing.Optional[jsii.Number] = None,
    password_reuse_prevention: typing.Optional[jsii.Number] = None,
    require_lowercase_characters: typing.Optional[builtins.bool] = None,
    require_numbers: typing.Optional[builtins.bool] = None,
    require_symbols: typing.Optional[builtins.bool] = None,
    require_uppercase_characters: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11d7229848bc04b1128e4db81c8f3b2737335e86186608261b9305f4ec75f4da(
    scope: _constructs_77d1e7e8.IConstruct,
    id: builtins.str,
    *,
    auto_remediation: typing.Optional[builtins.bool] = None,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    maximum_execution_frequency: typing.Optional[_aws_cdk_aws_config_ceddda9d.MaximumExecutionFrequency] = None,
    account: typing.Optional[builtins.str] = None,
    environment_from_arn: typing.Optional[builtins.str] = None,
    physical_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88046e1726952b7c07ae0f5a9e06e1c06f7915c2febb2d232dcf350de5476bf5(
    *,
    account: typing.Optional[builtins.str] = None,
    environment_from_arn: typing.Optional[builtins.str] = None,
    physical_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    auto_remediation: typing.Optional[builtins.bool] = None,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    maximum_execution_frequency: typing.Optional[_aws_cdk_aws_config_ceddda9d.MaximumExecutionFrequency] = None,
) -> None:
    """Type checking stubs"""
    pass
