'''
# MongoDB Atlas AWS CDK Resources

[![Code Health](https://github.com/mongodb/awscdk-resources-mongodbatlas/actions/workflows/code-health.yml/badge.svg?event=push)](https://github.com/mongodb/awscdk-resources-mongodbatlas/actions/workflows/code-health.yml)
[![Package CDK](https://github.com/mongodb/awscdk-resources-mongodbatlas/actions/workflows/package.yml/badge.svg?branch=main)](https://github.com/mongodb/awscdk-resources-mongodbatlas/actions/workflows/package.yml)
[![npm version](https://badge.fury.io/js/awscdk-resources-mongodbatlas.svg)](https://badge.fury.io/js/awscdk-resources-mongodbatlas)
[![PyPI version](https://badge.fury.io/py/awscdk-resources-mongodbatlas.svg)](https://badge.fury.io/py/awscdk-resources-mongodbatlas)
[![NuGet version](https://badge.fury.io/nu/MongoDB.AWSCDKResourcesMongoDBAtlas.svg)](https://badge.fury.io/nu/MongoDB.AWSCDKResourcesMongoDBAtlas)
[![Maven Central](https://maven-badges.herokuapp.com/maven-central/org.mongodb/awscdk-resources-mongodbatlas/badge.svg)](https://central.sonatype.com/artifact/org.mongodb/awscdk-resources-mongodbatlas)
[![Go Reference](https://pkg.go.dev/badge/github.com/mongodb/awscdk-resources-mongodbatlas-go/awscdkresourcesmongodbatlas.svg)](https://pkg.go.dev/github.com/mongodb/awscdk-resources-mongodbatlas-go/awscdkresourcesmongodbatlas)

[![View on Construct Hub](https://constructs.dev/badge?package=aws-cdk-lib)](https://constructs.dev/packages/awscdk-resources-mongodbatlas)

Use MongoDB Atlas [AWS CDK](https://aws.amazon.com/cdk/) (or Cloud Development Kit) constructs to manage [MongoDB Atlas](https://www.mongodb.com/cloud/atlas). The AWS CDK is a framework for defining infrastructure as code (IaC). It allows developers to write code in their preferred programming language, such as TypeScript for example, to define and deploy infrastructure. AWS CDK gets synthesized down into [AWS CloudFormation](https://aws.amazon.com/cloudformation/) templates at deployment so users no longer have to write or maintain YAML/JSON based CloudFormation templates.

## Available Packages

### NPM

The npm package is available at [awscdk-resources-mongodbatlas](https://www.npmjs.com/package/awscdk-resources-mongodbatlas)

```bash
npm i awscdk-resources-mongodbatlas
```

### PyPI

The PyPI package is available at [awscdk-resources-mongodbatlas](https://pypi.org/project/awscdk-resources-mongodbatlas/)

```bash
pip install awscdk-resources-mongodbatlas
```

### Nuget

The Nuget package is available at [MongoDB.AWSCDKResourcesMongoDBAtlas](https://www.nuget.org/packages/MongoDB.AWSCDKResourcesMongoDBAtlas)

```bash
dotnet add package MongoDB.AWSCDKResourcesMongoDBAtlas --version 1.0.0
```

### Maven

The Maven package is available at [awscdk-resources-mongodbatlas](https://central.sonatype.com/artifact/org.mongodb/awscdk-resources-mongodbatlas/1.0.0)

```Maven
<dependency>
    <groupId>org.mongodb</groupId>
    <artifactId>awscdk-resources-mongodbatlas</artifactId>
    <version>1.0.0</version>
</dependency>
```

### Go

The go package is generated into the [github.com/mongodb/awscdk-resources-mongodbatlas-go](https://github.com/mongodb/awscdk-resources-mongodbatlas-go) package.

```bash
go get github.com/mongodb/awscdk-resources-mongodbatlas-go/awscdkresourcesmongodbatlas
```

## Available Constructors

MongoDB Atlas AWS CDK Resources provides L1, L2 and L3 CDK constructors. Please, have a look at [README.md](src/README.md#cdk-constructors) for a full lists of constructors and examples.

## Getting Started

See the [cdk examples](examples/README.md) for how to setup prerequisites & get started with your first cluster, using our AWS CDK sample code. We also provide a quick guide on [How to Deploy MongoDB Atlas with AWS CDK in TypeScript](https://www.mongodb.com/developer/products/atlas/deploy-mongodb-atlas-aws-cdk-typescript/).

## Support, Bugs, Feature Requests

Feature requests can be submitted at [feedback.mongodb.com](https://feedback.mongodb.com/forums/924145-atlas/category/392596-atlas-cloudformation-resources) - just select "Atlas CloudFormation Resources" as the category or vote for an already suggested feature.

Support for the MongoDB Atlas Resource Provider for CloudFormation is provided under MongoDB Atlas support plans, starting with Developer. Please submit support questions within the Atlas UI. In addition, support questions submitted under the Issues section of this repo are also being monitored. Bugs should be filed under the Issues section of this repo.

## MongoDB Atlas API Keys Credential Management

Atlas API keys Configuration are required for both CloudFormation and CDK resources, and this Atlas API key pair are provided as input by the use of a Profile

AWS CloudFormation limits Third Parties from using non-AWS API Keys as either hardcoded secrets in CloudFormation templates or via CDK, hence we now require all the users store MongoDB Atlas API Keys via [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/).

`NOTE: the process for configuring the PROFILE is the same and is required both for CloudFormation and CDK`

### 1. Configure your MongoDB Atlas API Keys

You'll need to generate an API key pair (public and private keys) for your Atlas organization and configure them to grant CloudFormation access to your Atlas project.
Refer to the [Atlas documentation](https://www.mongodb.com/docs/atlas/configure-api-access/#manage-programmatic-access-to-an-organization) for detailed instructions.

### 2. Configure your Profile

To use Atlas CloudFormation resources, you must configure a "profile" with your API keys using [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/).

The secret should follow this format:

```
SecretName: cfn/atlas/profile/{ProfileName}
SecretValue: {"PublicKey": "YourPublicKey", "PrivateKey": "YourPrivateKey"}
```

To create a new secret for a default profile, use the [PROFILE SECRET TEMPLATE](/examples/profile-secret.yaml) file provided in this repository.

Here are some examples of how to use this template:

#### example 1:

```
  ProfileName: default
  SecretName: cfn/atlas/profile/default
  SecretValue: {"PublicKey": "YourPublicKey", "PrivateKey": "YourPrivateKey"}
```

#### example 2:

```
  ProfileName: testProfile
  SecretName: cfn/atlas/profile/testProfile
  SecretValue: {"PublicKey": "YourPublicKey", "PrivateKey": "YourPrivateKey"}
```

## Contributing

See our [CONTRIBUTING.md](CONTRIBUTING.md) guide.
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

from ._jsii import *

import aws_cdk as _aws_cdk_ceddda9d
import constructs as _constructs_77d1e7e8


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.AccessListDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "aws_security_group": "awsSecurityGroup",
        "cidr_block": "cidrBlock",
        "comment": "comment",
        "delete_after_date": "deleteAfterDate",
        "ip_address": "ipAddress",
        "project_id": "projectId",
    },
)
class AccessListDefinition:
    def __init__(
        self,
        *,
        aws_security_group: typing.Optional[builtins.str] = None,
        cidr_block: typing.Optional[builtins.str] = None,
        comment: typing.Optional[builtins.str] = None,
        delete_after_date: typing.Optional[builtins.str] = None,
        ip_address: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_security_group: Unique string of the Amazon Web Services (AWS) security group that you want to add to the project's IP access list. Your IP access list entry can be one awsSecurityGroup, one cidrBlock, or one ipAddress. You must configure Virtual Private Connection (VPC) peering for your project before you can add an AWS security group to an IP access list. You cannot set AWS security groups as temporary access list entries. Don't set this parameter if you set cidrBlock or ipAddress.
        :param cidr_block: Range of IP addresses in Classless Inter-Domain Routing (CIDR) notation that you want to add to the project's IP access list. Your IP access list entry can be one awsSecurityGroup, one cidrBlock, or one ipAddress. Don't set this parameter if you set awsSecurityGroup or ipAddress
        :param comment: Remark that explains the purpose or scope of this IP access list entry.
        :param delete_after_date: Date and time after which MongoDB Cloud deletes the temporary access list entry. This parameter expresses its value in the ISO 8601 timestamp format in UTC and can include the time zone designation. The date must be later than the current date but no later than one week after you submit this request. The resource returns this parameter if you specified an expiration date when creating this IP access list entry.
        :param ip_address: IP address that you want to add to the project's IP access list. Your IP access list entry can be one awsSecurityGroup, one cidrBlock, or one ipAddress. Don't set this parameter if you set awsSecurityGroup or cidrBlock.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.

        :schema: accessListDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c95ca92412af9e60fd32fabdf8a64b384ec620641a1767b8699a24ce265e8c77)
            check_type(argname="argument aws_security_group", value=aws_security_group, expected_type=type_hints["aws_security_group"])
            check_type(argname="argument cidr_block", value=cidr_block, expected_type=type_hints["cidr_block"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument delete_after_date", value=delete_after_date, expected_type=type_hints["delete_after_date"])
            check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_security_group is not None:
            self._values["aws_security_group"] = aws_security_group
        if cidr_block is not None:
            self._values["cidr_block"] = cidr_block
        if comment is not None:
            self._values["comment"] = comment
        if delete_after_date is not None:
            self._values["delete_after_date"] = delete_after_date
        if ip_address is not None:
            self._values["ip_address"] = ip_address
        if project_id is not None:
            self._values["project_id"] = project_id

    @builtins.property
    def aws_security_group(self) -> typing.Optional[builtins.str]:
        '''Unique string of the Amazon Web Services (AWS) security group that you want to add to the project's IP access list.

        Your IP access list entry can be one awsSecurityGroup, one cidrBlock, or one ipAddress. You must configure Virtual Private Connection (VPC) peering for your project before you can add an AWS security group to an IP access list. You cannot set AWS security groups as temporary access list entries. Don't set this parameter if you set cidrBlock or ipAddress.

        :schema: accessListDefinition#AwsSecurityGroup
        '''
        result = self._values.get("aws_security_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cidr_block(self) -> typing.Optional[builtins.str]:
        '''Range of IP addresses in Classless Inter-Domain Routing (CIDR) notation that you want to add to the project's IP access list.

        Your IP access list entry can be one awsSecurityGroup, one cidrBlock, or one ipAddress. Don't set this parameter if you set awsSecurityGroup or ipAddress

        :schema: accessListDefinition#CIDRBlock
        '''
        result = self._values.get("cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Remark that explains the purpose or scope of this IP access list entry.

        :schema: accessListDefinition#Comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_after_date(self) -> typing.Optional[builtins.str]:
        '''Date and time after which MongoDB Cloud deletes the temporary access list entry.

        This parameter expresses its value in the ISO 8601 timestamp format in UTC and can include the time zone designation. The date must be later than the current date but no later than one week after you submit this request. The resource returns this parameter if you specified an expiration date when creating this IP access list entry.

        :schema: accessListDefinition#DeleteAfterDate
        '''
        result = self._values.get("delete_after_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''IP address that you want to add to the project's IP access list.

        Your IP access list entry can be one awsSecurityGroup, one cidrBlock, or one ipAddress. Don't set this parameter if you set awsSecurityGroup or cidrBlock.

        :schema: accessListDefinition#IPAddress
        '''
        result = self._values.get("ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: accessListDefinition#ProjectId
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessListDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.Action",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "resources": "resources"},
)
class Action:
    def __init__(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        resources: typing.Optional[typing.Sequence[typing.Union["Resource", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param action: Human-readable label that identifies the privilege action.
        :param resources: List of resources on which you grant the action.

        :schema: Action
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4c2b51f44f5320b4b6204a6c2e4237c395d8be8b851a1aff6fd2fbaccebffde)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the privilege action.

        :schema: Action#Action
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resources(self) -> typing.Optional[typing.List["Resource"]]:
        '''List of resources on which you grant the action.

        :schema: Action#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional[typing.List["Resource"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Action(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.AdvancedAutoScaling",
    jsii_struct_bases=[],
    name_mapping={"compute": "compute", "disk_gb": "diskGb"},
)
class AdvancedAutoScaling:
    def __init__(
        self,
        *,
        compute: typing.Optional[typing.Union["Compute", typing.Dict[builtins.str, typing.Any]]] = None,
        disk_gb: typing.Optional[typing.Union["DiskGb", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''AWS Automatic Cluster Scaling.

        :param compute: 
        :param disk_gb: 

        :schema: advancedAutoScaling
        '''
        if isinstance(compute, dict):
            compute = Compute(**compute)
        if isinstance(disk_gb, dict):
            disk_gb = DiskGb(**disk_gb)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac917b855a047532ce73b0f00ca7514f93d4661841803d30fd263b12ed2a4b57)
            check_type(argname="argument compute", value=compute, expected_type=type_hints["compute"])
            check_type(argname="argument disk_gb", value=disk_gb, expected_type=type_hints["disk_gb"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if compute is not None:
            self._values["compute"] = compute
        if disk_gb is not None:
            self._values["disk_gb"] = disk_gb

    @builtins.property
    def compute(self) -> typing.Optional["Compute"]:
        '''
        :schema: advancedAutoScaling#Compute
        '''
        result = self._values.get("compute")
        return typing.cast(typing.Optional["Compute"], result)

    @builtins.property
    def disk_gb(self) -> typing.Optional["DiskGb"]:
        '''
        :schema: advancedAutoScaling#DiskGB
        '''
        result = self._values.get("disk_gb")
        return typing.cast(typing.Optional["DiskGb"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AdvancedAutoScaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.AdvancedRegionConfig",
    jsii_struct_bases=[],
    name_mapping={
        "analytics_auto_scaling": "analyticsAutoScaling",
        "analytics_specs": "analyticsSpecs",
        "auto_scaling": "autoScaling",
        "backing_provider_name": "backingProviderName",
        "electable_specs": "electableSpecs",
        "priority": "priority",
        "provider_name": "providerName",
        "read_only_specs": "readOnlySpecs",
        "region_name": "regionName",
    },
)
class AdvancedRegionConfig:
    def __init__(
        self,
        *,
        analytics_auto_scaling: typing.Optional[typing.Union[AdvancedAutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
        analytics_specs: typing.Optional[typing.Union["Specs", typing.Dict[builtins.str, typing.Any]]] = None,
        auto_scaling: typing.Optional[typing.Union[AdvancedAutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
        backing_provider_name: typing.Optional[builtins.str] = None,
        electable_specs: typing.Optional[typing.Union["Specs", typing.Dict[builtins.str, typing.Any]]] = None,
        priority: typing.Optional[jsii.Number] = None,
        provider_name: typing.Optional["AdvancedRegionConfigProviderName"] = None,
        read_only_specs: typing.Optional[typing.Union["Specs", typing.Dict[builtins.str, typing.Any]]] = None,
        region_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Hardware specifications for nodes set for a given region.

        Each regionConfigs object describes the region's priority in elections and the number and type of MongoDB nodes that MongoDB Cloud deploys to the region. Each regionConfigs object must have either an analyticsSpecs object, electableSpecs object, or readOnlySpecs object. Tenant clusters only require electableSpecs. Dedicated clusters can specify any of these specifications, but must have at least one electableSpecs object within a replicationSpec. Every hardware specification must use the same instanceSize.

        Example:

        If you set "replicationSpecs[n].regionConfigs[m].analyticsSpecs.instanceSize" : "M30", set "replicationSpecs[n].regionConfigs[m].electableSpecs.instanceSize" : "M30"if you have electable nodes and"replicationSpecs[n].regionConfigs[m].readOnlySpecs.instanceSize" : "M30" if you have read-only nodes.",

        :param analytics_auto_scaling: 
        :param analytics_specs: 
        :param auto_scaling: 
        :param backing_provider_name: 
        :param electable_specs: 
        :param priority: 
        :param provider_name: 
        :param read_only_specs: 
        :param region_name: 

        :schema: advancedRegionConfig
        '''
        if isinstance(analytics_auto_scaling, dict):
            analytics_auto_scaling = AdvancedAutoScaling(**analytics_auto_scaling)
        if isinstance(analytics_specs, dict):
            analytics_specs = Specs(**analytics_specs)
        if isinstance(auto_scaling, dict):
            auto_scaling = AdvancedAutoScaling(**auto_scaling)
        if isinstance(electable_specs, dict):
            electable_specs = Specs(**electable_specs)
        if isinstance(read_only_specs, dict):
            read_only_specs = Specs(**read_only_specs)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__862cd9358d07b2b78562a3e3584bc148b035b9f38266e5522b3bea0cbaae1473)
            check_type(argname="argument analytics_auto_scaling", value=analytics_auto_scaling, expected_type=type_hints["analytics_auto_scaling"])
            check_type(argname="argument analytics_specs", value=analytics_specs, expected_type=type_hints["analytics_specs"])
            check_type(argname="argument auto_scaling", value=auto_scaling, expected_type=type_hints["auto_scaling"])
            check_type(argname="argument backing_provider_name", value=backing_provider_name, expected_type=type_hints["backing_provider_name"])
            check_type(argname="argument electable_specs", value=electable_specs, expected_type=type_hints["electable_specs"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument provider_name", value=provider_name, expected_type=type_hints["provider_name"])
            check_type(argname="argument read_only_specs", value=read_only_specs, expected_type=type_hints["read_only_specs"])
            check_type(argname="argument region_name", value=region_name, expected_type=type_hints["region_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if analytics_auto_scaling is not None:
            self._values["analytics_auto_scaling"] = analytics_auto_scaling
        if analytics_specs is not None:
            self._values["analytics_specs"] = analytics_specs
        if auto_scaling is not None:
            self._values["auto_scaling"] = auto_scaling
        if backing_provider_name is not None:
            self._values["backing_provider_name"] = backing_provider_name
        if electable_specs is not None:
            self._values["electable_specs"] = electable_specs
        if priority is not None:
            self._values["priority"] = priority
        if provider_name is not None:
            self._values["provider_name"] = provider_name
        if read_only_specs is not None:
            self._values["read_only_specs"] = read_only_specs
        if region_name is not None:
            self._values["region_name"] = region_name

    @builtins.property
    def analytics_auto_scaling(self) -> typing.Optional[AdvancedAutoScaling]:
        '''
        :schema: advancedRegionConfig#AnalyticsAutoScaling
        '''
        result = self._values.get("analytics_auto_scaling")
        return typing.cast(typing.Optional[AdvancedAutoScaling], result)

    @builtins.property
    def analytics_specs(self) -> typing.Optional["Specs"]:
        '''
        :schema: advancedRegionConfig#AnalyticsSpecs
        '''
        result = self._values.get("analytics_specs")
        return typing.cast(typing.Optional["Specs"], result)

    @builtins.property
    def auto_scaling(self) -> typing.Optional[AdvancedAutoScaling]:
        '''
        :schema: advancedRegionConfig#AutoScaling
        '''
        result = self._values.get("auto_scaling")
        return typing.cast(typing.Optional[AdvancedAutoScaling], result)

    @builtins.property
    def backing_provider_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: advancedRegionConfig#BackingProviderName
        '''
        result = self._values.get("backing_provider_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def electable_specs(self) -> typing.Optional["Specs"]:
        '''
        :schema: advancedRegionConfig#ElectableSpecs
        '''
        result = self._values.get("electable_specs")
        return typing.cast(typing.Optional["Specs"], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: advancedRegionConfig#Priority
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def provider_name(self) -> typing.Optional["AdvancedRegionConfigProviderName"]:
        '''
        :schema: advancedRegionConfig#ProviderName
        '''
        result = self._values.get("provider_name")
        return typing.cast(typing.Optional["AdvancedRegionConfigProviderName"], result)

    @builtins.property
    def read_only_specs(self) -> typing.Optional["Specs"]:
        '''
        :schema: advancedRegionConfig#ReadOnlySpecs
        '''
        result = self._values.get("read_only_specs")
        return typing.cast(typing.Optional["Specs"], result)

    @builtins.property
    def region_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: advancedRegionConfig#RegionName
        '''
        result = self._values.get("region_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AdvancedRegionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.AdvancedRegionConfigProviderName")
class AdvancedRegionConfigProviderName(enum.Enum):
    '''
    :schema: AdvancedRegionConfigProviderName
    '''

    AWS = "AWS"
    '''AWS.'''
    GCP = "GCP"
    '''GCP.'''
    AZURE = "AZURE"
    '''AZURE.'''
    TENANT = "TENANT"
    '''TENANT.'''


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.AdvancedReplicationSpec",
    jsii_struct_bases=[],
    name_mapping={
        "advanced_region_configs": "advancedRegionConfigs",
        "id": "id",
        "num_shards": "numShards",
        "zone_name": "zoneName",
    },
)
class AdvancedReplicationSpec:
    def __init__(
        self,
        *,
        advanced_region_configs: typing.Optional[typing.Sequence[typing.Union[AdvancedRegionConfig, typing.Dict[builtins.str, typing.Any]]]] = None,
        id: typing.Optional[builtins.str] = None,
        num_shards: typing.Optional[jsii.Number] = None,
        zone_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''List of settings that configure your cluster regions.

        For Global Clusters, each object in the array represents a zone where your clusters nodes deploy. For non-Global replica sets and sharded clusters, this array has one object representing where your clusters nodes deploy.

        :param advanced_region_configs: Hardware specifications for nodes set for a given region. Each regionConfigs object describes the region's priority in elections and the number and type of MongoDB nodes that MongoDB Cloud deploys to the region. Each regionConfigs object must have either an analyticsSpecs object, electableSpecs object, or readOnlySpecs object. Tenant clusters only require electableSpecs. Dedicated clusters can specify any of these specifications, but must have at least one electableSpecs object within a replicationSpec. Every hardware specification must use the same instanceSize. Example: If you set "replicationSpecs[n].regionConfigs[m].analyticsSpecs.instanceSize" : "M30", set "replicationSpecs[n].regionConfigs[m].electableSpecs.instanceSize" : "M30"if you have electable nodes and"replicationSpecs[n].regionConfigs[m].readOnlySpecs.instanceSize" : "M30" if you have read-only nodes.",
        :param id: Unique 24-hexadecimal digit string that identifies the replication object for a zone in a Multi-Cloud Cluster. If you include existing zones in the request, you must specify this parameter. If you add a new zone to an existing Multi-Cloud Cluster, you may specify this parameter. The request deletes any existing zones in the Multi-Cloud Cluster that you exclude from the request.
        :param num_shards: Positive integer that specifies the number of shards to deploy in each specified zone. If you set this value to 1 and "clusterType" : "SHARDED", MongoDB Cloud deploys a single-shard sharded cluster. Don't create a sharded cluster with a single shard for production environments. Single-shard sharded clusters don't provide the same benefits as multi-shard configurations.
        :param zone_name: Human-readable label that identifies the zone in a Global Cluster. Provide this value only if "clusterType" : "GEOSHARDED".

        :schema: advancedReplicationSpec
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58913fadf8dd44199500c4dc60f4d148cb0bb418b7eea67df88294e1559ac5db)
            check_type(argname="argument advanced_region_configs", value=advanced_region_configs, expected_type=type_hints["advanced_region_configs"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument num_shards", value=num_shards, expected_type=type_hints["num_shards"])
            check_type(argname="argument zone_name", value=zone_name, expected_type=type_hints["zone_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if advanced_region_configs is not None:
            self._values["advanced_region_configs"] = advanced_region_configs
        if id is not None:
            self._values["id"] = id
        if num_shards is not None:
            self._values["num_shards"] = num_shards
        if zone_name is not None:
            self._values["zone_name"] = zone_name

    @builtins.property
    def advanced_region_configs(
        self,
    ) -> typing.Optional[typing.List[AdvancedRegionConfig]]:
        '''Hardware specifications for nodes set for a given region.

        Each regionConfigs object describes the region's priority in elections and the number and type of MongoDB nodes that MongoDB Cloud deploys to the region. Each regionConfigs object must have either an analyticsSpecs object, electableSpecs object, or readOnlySpecs object. Tenant clusters only require electableSpecs. Dedicated clusters can specify any of these specifications, but must have at least one electableSpecs object within a replicationSpec. Every hardware specification must use the same instanceSize.

        Example:

        If you set "replicationSpecs[n].regionConfigs[m].analyticsSpecs.instanceSize" : "M30", set "replicationSpecs[n].regionConfigs[m].electableSpecs.instanceSize" : "M30"if you have electable nodes and"replicationSpecs[n].regionConfigs[m].readOnlySpecs.instanceSize" : "M30" if you have read-only nodes.",

        :schema: advancedReplicationSpec#AdvancedRegionConfigs
        '''
        result = self._values.get("advanced_region_configs")
        return typing.cast(typing.Optional[typing.List[AdvancedRegionConfig]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies the replication object for a zone in a Multi-Cloud Cluster.

        If you include existing zones in the request, you must specify this parameter. If you add a new zone to an existing Multi-Cloud Cluster, you may specify this parameter. The request deletes any existing zones in the Multi-Cloud Cluster that you exclude from the request.

        :schema: advancedReplicationSpec#ID
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_shards(self) -> typing.Optional[jsii.Number]:
        '''Positive integer that specifies the number of shards to deploy in each specified zone.

        If you set this value to 1 and "clusterType" : "SHARDED", MongoDB Cloud deploys a single-shard sharded cluster. Don't create a sharded cluster with a single shard for production environments. Single-shard sharded clusters don't provide the same benefits as multi-shard configurations.

        :schema: advancedReplicationSpec#NumShards
        '''
        result = self._values.get("num_shards")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def zone_name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the zone in a Global Cluster.

        Provide this value only if "clusterType" : "GEOSHARDED".

        :schema: advancedReplicationSpec#ZoneName
        '''
        result = self._values.get("zone_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AdvancedReplicationSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ApiAtlasDiskBackupCopySettingView",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_provider": "cloudProvider",
        "frequencies": "frequencies",
        "region_name": "regionName",
        "replication_spec_id": "replicationSpecId",
        "should_copy_oplogs": "shouldCopyOplogs",
    },
)
class ApiAtlasDiskBackupCopySettingView:
    def __init__(
        self,
        *,
        cloud_provider: typing.Optional[builtins.str] = None,
        frequencies: typing.Optional[typing.Sequence[builtins.str]] = None,
        region_name: typing.Optional[builtins.str] = None,
        replication_spec_id: typing.Optional[builtins.str] = None,
        should_copy_oplogs: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param cloud_provider: A label that identifies the cloud provider that stores the snapshot copy.
        :param frequencies: List that describes which types of snapshots to copy.
        :param region_name: Target region to copy snapshots belonging to replicationSpecId to.
        :param replication_spec_id: Unique 24-hexadecimal digit string that identifies the replication object for a zone in a cluster.
        :param should_copy_oplogs: Flag that indicates whether to copy the oplogs to the target region.

        :schema: ApiAtlasDiskBackupCopySettingView
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5fa3e8f2afa69a76f26b01b4b454e19ee37ec11540b5696c986feed55bdd551)
            check_type(argname="argument cloud_provider", value=cloud_provider, expected_type=type_hints["cloud_provider"])
            check_type(argname="argument frequencies", value=frequencies, expected_type=type_hints["frequencies"])
            check_type(argname="argument region_name", value=region_name, expected_type=type_hints["region_name"])
            check_type(argname="argument replication_spec_id", value=replication_spec_id, expected_type=type_hints["replication_spec_id"])
            check_type(argname="argument should_copy_oplogs", value=should_copy_oplogs, expected_type=type_hints["should_copy_oplogs"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cloud_provider is not None:
            self._values["cloud_provider"] = cloud_provider
        if frequencies is not None:
            self._values["frequencies"] = frequencies
        if region_name is not None:
            self._values["region_name"] = region_name
        if replication_spec_id is not None:
            self._values["replication_spec_id"] = replication_spec_id
        if should_copy_oplogs is not None:
            self._values["should_copy_oplogs"] = should_copy_oplogs

    @builtins.property
    def cloud_provider(self) -> typing.Optional[builtins.str]:
        '''A label that identifies the cloud provider that stores the snapshot copy.

        :schema: ApiAtlasDiskBackupCopySettingView#CloudProvider
        '''
        result = self._values.get("cloud_provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def frequencies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List that describes which types of snapshots to copy.

        :schema: ApiAtlasDiskBackupCopySettingView#Frequencies
        '''
        result = self._values.get("frequencies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def region_name(self) -> typing.Optional[builtins.str]:
        '''Target region to copy snapshots belonging to replicationSpecId to.

        :schema: ApiAtlasDiskBackupCopySettingView#RegionName
        '''
        result = self._values.get("region_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_spec_id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies the replication object for a zone in a cluster.

        :schema: ApiAtlasDiskBackupCopySettingView#ReplicationSpecId
        '''
        result = self._values.get("replication_spec_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def should_copy_oplogs(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether to copy the oplogs to the target region.

        :schema: ApiAtlasDiskBackupCopySettingView#ShouldCopyOplogs
        '''
        result = self._values.get("should_copy_oplogs")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiAtlasDiskBackupCopySettingView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ApiAtlasDiskBackupShardedClusterSnapshotMemberView",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_provider": "cloudProvider",
        "id": "id",
        "replica_set_name": "replicaSetName",
    },
)
class ApiAtlasDiskBackupShardedClusterSnapshotMemberView:
    def __init__(
        self,
        *,
        cloud_provider: typing.Optional["ApiAtlasDiskBackupShardedClusterSnapshotMemberViewCloudProvider"] = None,
        id: typing.Optional[builtins.str] = None,
        replica_set_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cloud_provider: Human-readable label that identifies the cloud provider that stores this snapshot. The resource returns this parameter when ``"type": "replicaSet".``
        :param id: Unique 24-hexadecimal digit string that identifies the snapshot.
        :param replica_set_name: Human-readable label that identifies the shard or config host from which MongoDB Cloud took this snapshot.

        :schema: ApiAtlasDiskBackupShardedClusterSnapshotMemberView
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4e6b3d1e03871f93cf35cef4e9b9a9e64e19a6371d56a868de493caabcdf7f8)
            check_type(argname="argument cloud_provider", value=cloud_provider, expected_type=type_hints["cloud_provider"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument replica_set_name", value=replica_set_name, expected_type=type_hints["replica_set_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cloud_provider is not None:
            self._values["cloud_provider"] = cloud_provider
        if id is not None:
            self._values["id"] = id
        if replica_set_name is not None:
            self._values["replica_set_name"] = replica_set_name

    @builtins.property
    def cloud_provider(
        self,
    ) -> typing.Optional["ApiAtlasDiskBackupShardedClusterSnapshotMemberViewCloudProvider"]:
        '''Human-readable label that identifies the cloud provider that stores this snapshot.

        The resource returns this parameter when ``"type": "replicaSet".``

        :schema: ApiAtlasDiskBackupShardedClusterSnapshotMemberView#CloudProvider
        '''
        result = self._values.get("cloud_provider")
        return typing.cast(typing.Optional["ApiAtlasDiskBackupShardedClusterSnapshotMemberViewCloudProvider"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies the snapshot.

        :schema: ApiAtlasDiskBackupShardedClusterSnapshotMemberView#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replica_set_name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the shard or config host from which MongoDB Cloud took this snapshot.

        :schema: ApiAtlasDiskBackupShardedClusterSnapshotMemberView#ReplicaSetName
        '''
        result = self._values.get("replica_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiAtlasDiskBackupShardedClusterSnapshotMemberView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="awscdk-resources-mongodbatlas.ApiAtlasDiskBackupShardedClusterSnapshotMemberViewCloudProvider"
)
class ApiAtlasDiskBackupShardedClusterSnapshotMemberViewCloudProvider(enum.Enum):
    '''Human-readable label that identifies the cloud provider that stores this snapshot.

    The resource returns this parameter when ``"type": "replicaSet".``

    :schema: ApiAtlasDiskBackupShardedClusterSnapshotMemberViewCloudProvider
    '''

    AWS = "AWS"
    '''AWS.'''
    AZURE = "AZURE"
    '''AZURE.'''
    GCP = "GCP"
    '''GCP.'''


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ApiAtlasDiskBackupShardedClusterSnapshotView",
    jsii_struct_bases=[],
    name_mapping={
        "created_at": "createdAt",
        "description": "description",
        "expires_at": "expiresAt",
        "frequency_type": "frequencyType",
        "id": "id",
        "master_key_uuid": "masterKeyUuid",
        "members": "members",
        "mongod_version": "mongodVersion",
        "policy_items": "policyItems",
        "snapshot_ids": "snapshotIds",
        "snapshot_type": "snapshotType",
        "status": "status",
        "storage_size_bytes": "storageSizeBytes",
        "type": "type",
    },
)
class ApiAtlasDiskBackupShardedClusterSnapshotView:
    def __init__(
        self,
        *,
        created_at: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        expires_at: typing.Optional[builtins.str] = None,
        frequency_type: typing.Optional["ApiAtlasDiskBackupShardedClusterSnapshotViewFrequencyType"] = None,
        id: typing.Optional[builtins.str] = None,
        master_key_uuid: typing.Optional[builtins.str] = None,
        members: typing.Optional[typing.Sequence[typing.Union[ApiAtlasDiskBackupShardedClusterSnapshotMemberView, typing.Dict[builtins.str, typing.Any]]]] = None,
        mongod_version: typing.Optional[builtins.str] = None,
        policy_items: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_type: typing.Optional["ApiAtlasDiskBackupShardedClusterSnapshotViewSnapshotType"] = None,
        status: typing.Optional["ApiAtlasDiskBackupShardedClusterSnapshotViewStatus"] = None,
        storage_size_bytes: typing.Optional[builtins.str] = None,
        type: typing.Optional["ApiAtlasDiskBackupShardedClusterSnapshotViewType"] = None,
    ) -> None:
        '''
        :param created_at: Date and time when MongoDB Cloud took the snapshot. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
        :param description: Human-readable phrase or sentence that explains the purpose of the snapshot. The resource returns this parameter when ``"status": "onDemand"``.
        :param expires_at: Date and time when MongoDB Cloud deletes the snapshot. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
        :param frequency_type: Human-readable label that identifies how often this snapshot triggers.
        :param id: Unique 24-hexadecimal digit string that identifies the snapshot.
        :param master_key_uuid: Unique string that identifies the Amazon Web Services (AWS) Key Management Service (KMS) Customer Master Key (CMK) used to encrypt the snapshot. The resource returns this value when ``"encryptionEnabled" : true``.
        :param members: List that includes the snapshots and the cloud provider that stores the snapshots. The resource returns this parameter when ``"type" : "SHARDED_CLUSTER"``.
        :param mongod_version: Version of the MongoDB host that this snapshot backs up.
        :param policy_items: List that contains unique identifiers for the policy items.
        :param snapshot_ids: List that contains the unique identifiers of the snapshots created for the shards and config host for a sharded cluster. The resource returns this parameter when ``"type": "SHARDED_CLUSTER"``. These identifiers should match the ones specified in the **members[n].id** parameters. This allows you to map a snapshot to its shard or config host name.
        :param snapshot_type: Human-readable label that identifies when this snapshot triggers.
        :param status: Human-readable label that indicates the stage of the backup process for this snapshot.
        :param storage_size_bytes: Number of bytes taken to store the backup snapshot.
        :param type: Human-readable label that categorizes the cluster as a replica set or sharded cluster.

        :schema: ApiAtlasDiskBackupShardedClusterSnapshotView
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__146d6e2792ffe8ca573648d29829309cd1ab0dae9b194541f355d17534634fa1)
            check_type(argname="argument created_at", value=created_at, expected_type=type_hints["created_at"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument expires_at", value=expires_at, expected_type=type_hints["expires_at"])
            check_type(argname="argument frequency_type", value=frequency_type, expected_type=type_hints["frequency_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument master_key_uuid", value=master_key_uuid, expected_type=type_hints["master_key_uuid"])
            check_type(argname="argument members", value=members, expected_type=type_hints["members"])
            check_type(argname="argument mongod_version", value=mongod_version, expected_type=type_hints["mongod_version"])
            check_type(argname="argument policy_items", value=policy_items, expected_type=type_hints["policy_items"])
            check_type(argname="argument snapshot_ids", value=snapshot_ids, expected_type=type_hints["snapshot_ids"])
            check_type(argname="argument snapshot_type", value=snapshot_type, expected_type=type_hints["snapshot_type"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument storage_size_bytes", value=storage_size_bytes, expected_type=type_hints["storage_size_bytes"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if created_at is not None:
            self._values["created_at"] = created_at
        if description is not None:
            self._values["description"] = description
        if expires_at is not None:
            self._values["expires_at"] = expires_at
        if frequency_type is not None:
            self._values["frequency_type"] = frequency_type
        if id is not None:
            self._values["id"] = id
        if master_key_uuid is not None:
            self._values["master_key_uuid"] = master_key_uuid
        if members is not None:
            self._values["members"] = members
        if mongod_version is not None:
            self._values["mongod_version"] = mongod_version
        if policy_items is not None:
            self._values["policy_items"] = policy_items
        if snapshot_ids is not None:
            self._values["snapshot_ids"] = snapshot_ids
        if snapshot_type is not None:
            self._values["snapshot_type"] = snapshot_type
        if status is not None:
            self._values["status"] = status
        if storage_size_bytes is not None:
            self._values["storage_size_bytes"] = storage_size_bytes
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def created_at(self) -> typing.Optional[builtins.str]:
        '''Date and time when MongoDB Cloud took the snapshot.

        This parameter expresses its value in the ISO 8601 timestamp format in UTC.

        :schema: ApiAtlasDiskBackupShardedClusterSnapshotView#CreatedAt
        '''
        result = self._values.get("created_at")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Human-readable phrase or sentence that explains the purpose of the snapshot.

        The resource returns this parameter when ``"status": "onDemand"``.

        :schema: ApiAtlasDiskBackupShardedClusterSnapshotView#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expires_at(self) -> typing.Optional[builtins.str]:
        '''Date and time when MongoDB Cloud deletes the snapshot.

        This parameter expresses its value in the ISO 8601 timestamp format in UTC.

        :schema: ApiAtlasDiskBackupShardedClusterSnapshotView#ExpiresAt
        '''
        result = self._values.get("expires_at")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def frequency_type(
        self,
    ) -> typing.Optional["ApiAtlasDiskBackupShardedClusterSnapshotViewFrequencyType"]:
        '''Human-readable label that identifies how often this snapshot triggers.

        :schema: ApiAtlasDiskBackupShardedClusterSnapshotView#FrequencyType
        '''
        result = self._values.get("frequency_type")
        return typing.cast(typing.Optional["ApiAtlasDiskBackupShardedClusterSnapshotViewFrequencyType"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies the snapshot.

        :schema: ApiAtlasDiskBackupShardedClusterSnapshotView#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_key_uuid(self) -> typing.Optional[builtins.str]:
        '''Unique string that identifies the Amazon Web Services (AWS) Key Management Service (KMS) Customer Master Key (CMK) used to encrypt the snapshot.

        The resource returns this value when ``"encryptionEnabled" : true``.

        :schema: ApiAtlasDiskBackupShardedClusterSnapshotView#MasterKeyUUID
        '''
        result = self._values.get("master_key_uuid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def members(
        self,
    ) -> typing.Optional[typing.List[ApiAtlasDiskBackupShardedClusterSnapshotMemberView]]:
        '''List that includes the snapshots and the cloud provider that stores the snapshots.

        The resource returns this parameter when ``"type" : "SHARDED_CLUSTER"``.

        :schema: ApiAtlasDiskBackupShardedClusterSnapshotView#Members
        '''
        result = self._values.get("members")
        return typing.cast(typing.Optional[typing.List[ApiAtlasDiskBackupShardedClusterSnapshotMemberView]], result)

    @builtins.property
    def mongod_version(self) -> typing.Optional[builtins.str]:
        '''Version of the MongoDB host that this snapshot backs up.

        :schema: ApiAtlasDiskBackupShardedClusterSnapshotView#MongodVersion
        '''
        result = self._values.get("mongod_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_items(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List that contains unique identifiers for the policy items.

        :schema: ApiAtlasDiskBackupShardedClusterSnapshotView#PolicyItems
        '''
        result = self._values.get("policy_items")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def snapshot_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List that contains the unique identifiers of the snapshots created for the shards and config host for a sharded cluster.

        The resource returns this parameter when ``"type": "SHARDED_CLUSTER"``. These identifiers should match the ones specified in the **members[n].id** parameters. This allows you to map a snapshot to its shard or config host name.

        :schema: ApiAtlasDiskBackupShardedClusterSnapshotView#SnapshotIds
        '''
        result = self._values.get("snapshot_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def snapshot_type(
        self,
    ) -> typing.Optional["ApiAtlasDiskBackupShardedClusterSnapshotViewSnapshotType"]:
        '''Human-readable label that identifies when this snapshot triggers.

        :schema: ApiAtlasDiskBackupShardedClusterSnapshotView#SnapshotType
        '''
        result = self._values.get("snapshot_type")
        return typing.cast(typing.Optional["ApiAtlasDiskBackupShardedClusterSnapshotViewSnapshotType"], result)

    @builtins.property
    def status(
        self,
    ) -> typing.Optional["ApiAtlasDiskBackupShardedClusterSnapshotViewStatus"]:
        '''Human-readable label that indicates the stage of the backup process for this snapshot.

        :schema: ApiAtlasDiskBackupShardedClusterSnapshotView#Status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional["ApiAtlasDiskBackupShardedClusterSnapshotViewStatus"], result)

    @builtins.property
    def storage_size_bytes(self) -> typing.Optional[builtins.str]:
        '''Number of bytes taken to store the backup snapshot.

        :schema: ApiAtlasDiskBackupShardedClusterSnapshotView#StorageSizeBytes
        '''
        result = self._values.get("storage_size_bytes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(
        self,
    ) -> typing.Optional["ApiAtlasDiskBackupShardedClusterSnapshotViewType"]:
        '''Human-readable label that categorizes the cluster as a replica set or sharded cluster.

        :schema: ApiAtlasDiskBackupShardedClusterSnapshotView#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["ApiAtlasDiskBackupShardedClusterSnapshotViewType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiAtlasDiskBackupShardedClusterSnapshotView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="awscdk-resources-mongodbatlas.ApiAtlasDiskBackupShardedClusterSnapshotViewFrequencyType"
)
class ApiAtlasDiskBackupShardedClusterSnapshotViewFrequencyType(enum.Enum):
    '''Human-readable label that identifies how often this snapshot triggers.

    :schema: ApiAtlasDiskBackupShardedClusterSnapshotViewFrequencyType
    '''

    HOURLY = "HOURLY"
    '''hourly.'''
    DAILY = "DAILY"
    '''daily.'''
    WEEKLY = "WEEKLY"
    '''weekly.'''
    MONTHLY = "MONTHLY"
    '''monthly.'''


@jsii.enum(
    jsii_type="awscdk-resources-mongodbatlas.ApiAtlasDiskBackupShardedClusterSnapshotViewSnapshotType"
)
class ApiAtlasDiskBackupShardedClusterSnapshotViewSnapshotType(enum.Enum):
    '''Human-readable label that identifies when this snapshot triggers.

    :schema: ApiAtlasDiskBackupShardedClusterSnapshotViewSnapshotType
    '''

    ON_DEMAND = "ON_DEMAND"
    '''onDemand.'''
    SCHEDULED = "SCHEDULED"
    '''scheduled.'''


@jsii.enum(
    jsii_type="awscdk-resources-mongodbatlas.ApiAtlasDiskBackupShardedClusterSnapshotViewStatus"
)
class ApiAtlasDiskBackupShardedClusterSnapshotViewStatus(enum.Enum):
    '''Human-readable label that indicates the stage of the backup process for this snapshot.

    :schema: ApiAtlasDiskBackupShardedClusterSnapshotViewStatus
    '''

    QUEUED = "QUEUED"
    '''queued.'''
    IN_PROGRESS = "IN_PROGRESS"
    '''inProgress.'''
    COMPLETED = "COMPLETED"
    '''completed.'''
    FAILED = "FAILED"
    '''failed.'''


@jsii.enum(
    jsii_type="awscdk-resources-mongodbatlas.ApiAtlasDiskBackupShardedClusterSnapshotViewType"
)
class ApiAtlasDiskBackupShardedClusterSnapshotViewType(enum.Enum):
    '''Human-readable label that categorizes the cluster as a replica set or sharded cluster.

    :schema: ApiAtlasDiskBackupShardedClusterSnapshotViewType
    '''

    REPLICA_SET = "REPLICA_SET"
    '''REPLICA_SET.'''
    SHARDED_CLUSTER = "SHARDED_CLUSTER"
    '''SHARDED_CLUSTER.'''


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ApiAtlasFtsAnalyzersViewManual",
    jsii_struct_bases=[],
    name_mapping={
        "char_filters": "charFilters",
        "name": "name",
        "token_filters": "tokenFilters",
        "tokenizer": "tokenizer",
    },
)
class ApiAtlasFtsAnalyzersViewManual:
    def __init__(
        self,
        *,
        char_filters: typing.Optional[typing.Sequence[typing.Any]] = None,
        name: typing.Optional[builtins.str] = None,
        token_filters: typing.Optional[typing.Sequence[typing.Any]] = None,
        tokenizer: typing.Any = None,
    ) -> None:
        '''
        :param char_filters: Filters that examine text one character at a time and perform filtering operations.
        :param name: Human-readable name that identifies the custom analyzer. Names must be unique within an index, and must not start with any of the following strings: - ``lucene.`` - ``builtin.`` - ``mongodb.``
        :param token_filters: Filter that performs operations such as:. - Stemming, which reduces related words, such as "talking", "talked", and "talks" to their root word "talk". - Redaction, the removal of sensitive information from public documents.
        :param tokenizer: Tokenizer that you want to use to create tokens. Tokens determine how Atlas Search splits up text into discrete chunks for indexing.

        :schema: ApiAtlasFTSAnalyzersViewManual
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d95cf8751425648c9192218f3c835c3361006d1555b7ef3c0ade93a78a633a7)
            check_type(argname="argument char_filters", value=char_filters, expected_type=type_hints["char_filters"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument token_filters", value=token_filters, expected_type=type_hints["token_filters"])
            check_type(argname="argument tokenizer", value=tokenizer, expected_type=type_hints["tokenizer"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if char_filters is not None:
            self._values["char_filters"] = char_filters
        if name is not None:
            self._values["name"] = name
        if token_filters is not None:
            self._values["token_filters"] = token_filters
        if tokenizer is not None:
            self._values["tokenizer"] = tokenizer

    @builtins.property
    def char_filters(self) -> typing.Optional[typing.List[typing.Any]]:
        '''Filters that examine text one character at a time and perform filtering operations.

        :schema: ApiAtlasFTSAnalyzersViewManual#CharFilters
        '''
        result = self._values.get("char_filters")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Human-readable name that identifies the custom analyzer.

        Names must be unique within an index, and must not start with any of the following strings:

        - ``lucene.``
        - ``builtin.``
        - ``mongodb.``

        :schema: ApiAtlasFTSAnalyzersViewManual#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_filters(self) -> typing.Optional[typing.List[typing.Any]]:
        '''Filter that performs operations such as:.

        - Stemming, which reduces related words, such as "talking", "talked", and "talks" to their root word "talk".
        - Redaction, the removal of sensitive information from public documents.

        :schema: ApiAtlasFTSAnalyzersViewManual#TokenFilters
        '''
        result = self._values.get("token_filters")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def tokenizer(self) -> typing.Any:
        '''Tokenizer that you want to use to create tokens.

        Tokens determine how Atlas Search splits up text into discrete chunks for indexing.

        :schema: ApiAtlasFTSAnalyzersViewManual#Tokenizer
        '''
        result = self._values.get("tokenizer")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiAtlasFtsAnalyzersViewManual(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ApiAtlasFtsMappingsViewManual",
    jsii_struct_bases=[],
    name_mapping={"dynamic": "dynamic", "fields": "fields"},
)
class ApiAtlasFtsMappingsViewManual:
    def __init__(
        self,
        *,
        dynamic: typing.Optional[builtins.bool] = None,
        fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param dynamic: Flag that indicates whether the index uses dynamic or static mappings. Required if **mappings.fields** is omitted.
        :param fields: One or more field specifications for the Atlas Search index. The element of the array must have the format fieldName:fieldType. Required if **mappings.dynamic** is omitted or set to **false**.

        :schema: ApiAtlasFTSMappingsViewManual
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf0b4b56e5803c25ffcc1d174524561964e5439926621ecbc2210ca575e55357)
            check_type(argname="argument dynamic", value=dynamic, expected_type=type_hints["dynamic"])
            check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dynamic is not None:
            self._values["dynamic"] = dynamic
        if fields is not None:
            self._values["fields"] = fields

    @builtins.property
    def dynamic(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether the index uses dynamic or static mappings.

        Required if **mappings.fields** is omitted.

        :schema: ApiAtlasFTSMappingsViewManual#Dynamic
        '''
        result = self._values.get("dynamic")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''One or more field specifications for the Atlas Search index.

        The element of the array must have the format fieldName:fieldType. Required if **mappings.dynamic** is omitted or set to **false**.

        :schema: ApiAtlasFTSMappingsViewManual#Fields
        '''
        result = self._values.get("fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiAtlasFtsMappingsViewManual(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ApiAtlasFtsSynonymMappingDefinitionView",
    jsii_struct_bases=[],
    name_mapping={"analyzer": "analyzer", "name": "name", "source": "source"},
)
class ApiAtlasFtsSynonymMappingDefinitionView:
    def __init__(
        self,
        *,
        analyzer: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        source: typing.Optional[typing.Union["SynonymSource", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param analyzer: Specific pre-defined method chosen to apply to the synonyms to be searched.
        :param name: Human-readable label that identifies the synonym definition. Each **synonym.name** must be unique within the same index definition.
        :param source: Data set that stores the mapping one or more words map to one or more synonyms of those words.

        :schema: ApiAtlasFTSSynonymMappingDefinitionView
        '''
        if isinstance(source, dict):
            source = SynonymSource(**source)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab7d3cb96638b70da5f4ee06bbaca4e02962e20e1fc0b57368a6f8a5491c5833)
            check_type(argname="argument analyzer", value=analyzer, expected_type=type_hints["analyzer"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if analyzer is not None:
            self._values["analyzer"] = analyzer
        if name is not None:
            self._values["name"] = name
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def analyzer(self) -> typing.Optional[builtins.str]:
        '''Specific pre-defined method chosen to apply to the synonyms to be searched.

        :schema: ApiAtlasFTSSynonymMappingDefinitionView#Analyzer
        '''
        result = self._values.get("analyzer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the synonym definition.

        Each **synonym.name** must be unique within the same index definition.

        :schema: ApiAtlasFTSSynonymMappingDefinitionView#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(self) -> typing.Optional["SynonymSource"]:
        '''Data set that stores the mapping one or more words map to one or more synonyms of those words.

        :schema: ApiAtlasFTSSynonymMappingDefinitionView#Source
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional["SynonymSource"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiAtlasFtsSynonymMappingDefinitionView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ApiAtlasNdsUserToDnMappingView",
    jsii_struct_bases=[],
    name_mapping={
        "ldap_query": "ldapQuery",
        "match": "match",
        "substitution": "substitution",
    },
)
class ApiAtlasNdsUserToDnMappingView:
    def __init__(
        self,
        *,
        ldap_query: typing.Optional[builtins.str] = None,
        match: typing.Optional[builtins.str] = None,
        substitution: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ldap_query: Lightweight Directory Access Protocol (LDAP) query template that inserts the LDAP name that the regular expression matches into an LDAP query Uniform Resource Identifier (URI). The formatting for the query must conform to `RFC 4515 <https://datatracker.ietf.org/doc/html/rfc4515>`_ and `RFC 4516 <https://datatracker.ietf.org/doc/html/rfc4516>`_.
        :param match: Regular expression that MongoDB Cloud uses to match against the provided Lightweight Directory Access Protocol (LDAP) username. Each parenthesis-enclosed section represents a regular expression capture group that the substitution or ``ldapQuery`` template uses.
        :param substitution: Lightweight Directory Access Protocol (LDAP) Distinguished Name (DN) template that converts the LDAP username that matches regular expression in the *match* parameter into an LDAP Distinguished Name (DN).

        :schema: ApiAtlasNDSUserToDNMappingView
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6d3a9fa0d7784b3a1c43d99716c4869d5dc8be079748328cd1c43a4e49538b3)
            check_type(argname="argument ldap_query", value=ldap_query, expected_type=type_hints["ldap_query"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
            check_type(argname="argument substitution", value=substitution, expected_type=type_hints["substitution"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ldap_query is not None:
            self._values["ldap_query"] = ldap_query
        if match is not None:
            self._values["match"] = match
        if substitution is not None:
            self._values["substitution"] = substitution

    @builtins.property
    def ldap_query(self) -> typing.Optional[builtins.str]:
        '''Lightweight Directory Access Protocol (LDAP) query template that inserts the LDAP name that the regular expression matches into an LDAP query Uniform Resource Identifier (URI).

        The formatting for the query must conform to `RFC 4515 <https://datatracker.ietf.org/doc/html/rfc4515>`_ and `RFC 4516 <https://datatracker.ietf.org/doc/html/rfc4516>`_.

        :schema: ApiAtlasNDSUserToDNMappingView#LdapQuery
        '''
        result = self._values.get("ldap_query")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match(self) -> typing.Optional[builtins.str]:
        '''Regular expression that MongoDB Cloud uses to match against the provided Lightweight Directory Access Protocol (LDAP) username.

        Each parenthesis-enclosed section represents a regular expression capture group that the substitution or ``ldapQuery`` template uses.

        :schema: ApiAtlasNDSUserToDNMappingView#Match
        '''
        result = self._values.get("match")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def substitution(self) -> typing.Optional[builtins.str]:
        '''Lightweight Directory Access Protocol (LDAP) Distinguished Name (DN) template that converts the LDAP username that matches regular expression in the *match* parameter into an LDAP Distinguished Name (DN).

        :schema: ApiAtlasNDSUserToDNMappingView#Substitution
        '''
        result = self._values.get("substitution")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiAtlasNdsUserToDnMappingView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ApiDeleteCopiedBackupsView",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_provider": "cloudProvider",
        "region_name": "regionName",
        "replication_spec_id": "replicationSpecId",
    },
)
class ApiDeleteCopiedBackupsView:
    def __init__(
        self,
        *,
        cloud_provider: typing.Optional[builtins.str] = None,
        region_name: typing.Optional[builtins.str] = None,
        replication_spec_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cloud_provider: A label that identifies the cloud provider for the deleted copy setting whose backup copies you want to delete.
        :param region_name: Target region for the deleted copy setting whose backup copies you want to delete.
        :param replication_spec_id: Unique 24-hexadecimal digit string that identifies the replication object for a zone in a cluster.

        :schema: ApiDeleteCopiedBackupsView
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30bd9d2e1004548ab815b4223767fb9673db3b56f9e7b7d327bf025e34d0f506)
            check_type(argname="argument cloud_provider", value=cloud_provider, expected_type=type_hints["cloud_provider"])
            check_type(argname="argument region_name", value=region_name, expected_type=type_hints["region_name"])
            check_type(argname="argument replication_spec_id", value=replication_spec_id, expected_type=type_hints["replication_spec_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cloud_provider is not None:
            self._values["cloud_provider"] = cloud_provider
        if region_name is not None:
            self._values["region_name"] = region_name
        if replication_spec_id is not None:
            self._values["replication_spec_id"] = replication_spec_id

    @builtins.property
    def cloud_provider(self) -> typing.Optional[builtins.str]:
        '''A label that identifies the cloud provider for the deleted copy setting whose backup copies you want to delete.

        :schema: ApiDeleteCopiedBackupsView#CloudProvider
        '''
        result = self._values.get("cloud_provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region_name(self) -> typing.Optional[builtins.str]:
        '''Target region for the deleted copy setting whose backup copies you want to delete.

        :schema: ApiDeleteCopiedBackupsView#RegionName
        '''
        result = self._values.get("region_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_spec_id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies the replication object for a zone in a cluster.

        :schema: ApiDeleteCopiedBackupsView#ReplicationSpecId
        '''
        result = self._values.get("replication_spec_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiDeleteCopiedBackupsView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ApiPolicyItemView",
    jsii_struct_bases=[],
    name_mapping={
        "frequency_interval": "frequencyInterval",
        "frequency_type": "frequencyType",
        "id": "id",
        "retention_unit": "retentionUnit",
        "retention_value": "retentionValue",
    },
)
class ApiPolicyItemView:
    def __init__(
        self,
        *,
        frequency_interval: typing.Optional[jsii.Number] = None,
        frequency_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        retention_unit: typing.Optional[builtins.str] = None,
        retention_value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param frequency_interval: Desired frequency of the new backup policy item specified by frequencyType.
        :param frequency_type: Frequency associated with the backup policy item. One of the following values: hourly, daily, weekly or monthly.
        :param id: Unique identifier of the backup policy item.
        :param retention_unit: Metric of duration of the backup policy item: days, weeks, or months.
        :param retention_value: Duration for which the backup is kept. Associated with retentionUnit.

        :schema: ApiPolicyItemView
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2f115084308517a41f040e7fb2335843a23bfc5b583498250061514ac4d3f96)
            check_type(argname="argument frequency_interval", value=frequency_interval, expected_type=type_hints["frequency_interval"])
            check_type(argname="argument frequency_type", value=frequency_type, expected_type=type_hints["frequency_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument retention_unit", value=retention_unit, expected_type=type_hints["retention_unit"])
            check_type(argname="argument retention_value", value=retention_value, expected_type=type_hints["retention_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if frequency_interval is not None:
            self._values["frequency_interval"] = frequency_interval
        if frequency_type is not None:
            self._values["frequency_type"] = frequency_type
        if id is not None:
            self._values["id"] = id
        if retention_unit is not None:
            self._values["retention_unit"] = retention_unit
        if retention_value is not None:
            self._values["retention_value"] = retention_value

    @builtins.property
    def frequency_interval(self) -> typing.Optional[jsii.Number]:
        '''Desired frequency of the new backup policy item specified by frequencyType.

        :schema: ApiPolicyItemView#FrequencyInterval
        '''
        result = self._values.get("frequency_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def frequency_type(self) -> typing.Optional[builtins.str]:
        '''Frequency associated with the backup policy item.

        One of the following values: hourly, daily, weekly or monthly.

        :schema: ApiPolicyItemView#FrequencyType
        '''
        result = self._values.get("frequency_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier of the backup policy item.

        :schema: ApiPolicyItemView#ID
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retention_unit(self) -> typing.Optional[builtins.str]:
        '''Metric of duration of the backup policy item: days, weeks, or months.

        :schema: ApiPolicyItemView#RetentionUnit
        '''
        result = self._values.get("retention_unit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retention_value(self) -> typing.Optional[jsii.Number]:
        '''Duration for which the backup is kept.

        Associated with retentionUnit.

        :schema: ApiPolicyItemView#RetentionValue
        '''
        result = self._values.get("retention_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiPolicyItemView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ApiPolicyView",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "policy_items": "policyItems"},
)
class ApiPolicyView:
    def __init__(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        policy_items: typing.Optional[typing.Sequence[typing.Union[ApiPolicyItemView, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param id: 
        :param policy_items: 

        :schema: ApiPolicyView
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66300e76f7281d11014f5beeeb5c606f84ee2abc698090f850a29d9967bd5218)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument policy_items", value=policy_items, expected_type=type_hints["policy_items"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if policy_items is not None:
            self._values["policy_items"] = policy_items

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ApiPolicyView#ID
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_items(self) -> typing.Optional[typing.List[ApiPolicyItemView]]:
        '''
        :schema: ApiPolicyView#PolicyItems
        '''
        result = self._values.get("policy_items")
        return typing.cast(typing.Optional[typing.List[ApiPolicyItemView]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiPolicyView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AtlasBasic(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.AtlasBasic",
):
    '''
    :class: AtlasBasic
    :description: true
    :export: true
    :extends: Construct
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster_props: typing.Union["ClusterProps", typing.Dict[builtins.str, typing.Any]],
        project_props: typing.Union["ProjectProps", typing.Dict[builtins.str, typing.Any]],
        db_user_props: typing.Optional[typing.Union["DatabaseUserProps", typing.Dict[builtins.str, typing.Any]]] = None,
        ip_access_list_props: typing.Optional[typing.Union["IpAccessListProps", typing.Dict[builtins.str, typing.Any]]] = None,
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Creates an instance of AtlasBasic.

        :param scope: -
        :param id: -
        :param cluster_props: 
        :param project_props: 
        :param db_user_props: 
        :param ip_access_list_props: 
        :param profile: 

        :memberof: AtlasBasic
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09a55f3bb77dc35f1cf8e82985ed9e9356b19aef3b78a58f27213fea7ac0ae72)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AtlasBasicProps(
            cluster_props=cluster_props,
            project_props=project_props,
            db_user_props=db_user_props,
            ip_access_list_props=ip_access_list_props,
            profile=profile,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="ipAccessList")
    def ip_access_list(self) -> "CfnProjectIpAccessList":
        '''
        :description: true
        :memberof: AtlasBasic
        :type: {ipAccessList.CfnProjectIpAccessList}
        '''
        return typing.cast("CfnProjectIpAccessList", jsii.get(self, "ipAccessList"))

    @builtins.property
    @jsii.member(jsii_name="mCluster")
    def m_cluster(self) -> "CfnCluster":
        '''
        :description: true
        :memberof: AtlasBasic
        :type: {atlas.CfnCluster}
        '''
        return typing.cast("CfnCluster", jsii.get(self, "mCluster"))

    @builtins.property
    @jsii.member(jsii_name="mDBUser")
    def m_db_user(self) -> "CfnDatabaseUser":
        '''
        :description: true
        :memberof: AtlasBasic
        :type: {user.CfnDatabaseUser}
        '''
        return typing.cast("CfnDatabaseUser", jsii.get(self, "mDBUser"))

    @builtins.property
    @jsii.member(jsii_name="mProject")
    def m_project(self) -> "CfnProject":
        '''
        :description: true
        :memberof: AtlasBasic
        :type: {project.CfnProject}
        '''
        return typing.cast("CfnProject", jsii.get(self, "mProject"))


class AtlasBasicPrivateEndpoint(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.AtlasBasicPrivateEndpoint",
):
    '''
    :class: AtlasBasicPrivateEndpoint
    :description: true
    :export: true
    :extends: Construct
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        atlas_basic_props: typing.Union["AtlasBasicProps", typing.Dict[builtins.str, typing.Any]],
        private_endpoint_props: typing.Union["PrivateEndpointProps", typing.Dict[builtins.str, typing.Any]],
        profile: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Creates an instance of AtlasBasicPrivateEndpoint.

        :param scope: -
        :param id: -
        :param atlas_basic_props: 
        :param private_endpoint_props: 
        :param profile: 
        :param region: Default: us-east-1

        :memberof: AtlasBasicPrivateEndpoint
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b95159a964749cd6793dc2842badabf780be08d986e82290a4538e7f33fa987)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AtlasBasicPrivateEndpointProps(
            atlas_basic_props=atlas_basic_props,
            private_endpoint_props=private_endpoint_props,
            profile=profile,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="atlasBasic")
    def atlas_basic(self) -> AtlasBasic:
        return typing.cast(AtlasBasic, jsii.get(self, "atlasBasic"))

    @builtins.property
    @jsii.member(jsii_name="privateEndpoint")
    def private_endpoint(self) -> "CfnPrivateEndpoint":
        return typing.cast("CfnPrivateEndpoint", jsii.get(self, "privateEndpoint"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.AtlasBasicPrivateEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "atlas_basic_props": "atlasBasicProps",
        "private_endpoint_props": "privateEndpointProps",
        "profile": "profile",
        "region": "region",
    },
)
class AtlasBasicPrivateEndpointProps:
    def __init__(
        self,
        *,
        atlas_basic_props: typing.Union["AtlasBasicProps", typing.Dict[builtins.str, typing.Any]],
        private_endpoint_props: typing.Union["PrivateEndpointProps", typing.Dict[builtins.str, typing.Any]],
        profile: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param atlas_basic_props: 
        :param private_endpoint_props: 
        :param profile: 
        :param region: Default: us-east-1

        :description: true
        :export: true
        :interface: AtlasBasicPrivateEndpointProps
        '''
        if isinstance(atlas_basic_props, dict):
            atlas_basic_props = AtlasBasicProps(**atlas_basic_props)
        if isinstance(private_endpoint_props, dict):
            private_endpoint_props = PrivateEndpointProps(**private_endpoint_props)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0861be50ce20d9bd65c7aab5af1aaefaefa9301d16772a9e668ce3ba885df54f)
            check_type(argname="argument atlas_basic_props", value=atlas_basic_props, expected_type=type_hints["atlas_basic_props"])
            check_type(argname="argument private_endpoint_props", value=private_endpoint_props, expected_type=type_hints["private_endpoint_props"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "atlas_basic_props": atlas_basic_props,
            "private_endpoint_props": private_endpoint_props,
        }
        if profile is not None:
            self._values["profile"] = profile
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def atlas_basic_props(self) -> "AtlasBasicProps":
        '''
        :description: true
        :memberof: AtlasPrivateEndpointProps
        :type: {AtlasBasicProps}
        '''
        result = self._values.get("atlas_basic_props")
        assert result is not None, "Required property 'atlas_basic_props' is missing"
        return typing.cast("AtlasBasicProps", result)

    @builtins.property
    def private_endpoint_props(self) -> "PrivateEndpointProps":
        '''
        :description: true
        :memberof: AtlasPrivateEndpointProps
        :type: {CfnPrivateEndpointProps}
        '''
        result = self._values.get("private_endpoint_props")
        assert result is not None, "Required property 'private_endpoint_props' is missing"
        return typing.cast("PrivateEndpointProps", result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''
        :default: us-east-1

        :description: AWS Region
        :memberof: AtlasPrivateEndpointProps
        :type: {string}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AtlasBasicPrivateEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.AtlasBasicProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_props": "clusterProps",
        "project_props": "projectProps",
        "db_user_props": "dbUserProps",
        "ip_access_list_props": "ipAccessListProps",
        "profile": "profile",
    },
)
class AtlasBasicProps:
    def __init__(
        self,
        *,
        cluster_props: typing.Union["ClusterProps", typing.Dict[builtins.str, typing.Any]],
        project_props: typing.Union["ProjectProps", typing.Dict[builtins.str, typing.Any]],
        db_user_props: typing.Optional[typing.Union["DatabaseUserProps", typing.Dict[builtins.str, typing.Any]]] = None,
        ip_access_list_props: typing.Optional[typing.Union["IpAccessListProps", typing.Dict[builtins.str, typing.Any]]] = None,
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cluster_props: 
        :param project_props: 
        :param db_user_props: 
        :param ip_access_list_props: 
        :param profile: 

        :description: true
        :export: true
        :interface: AtlasBasicProps
        '''
        if isinstance(cluster_props, dict):
            cluster_props = ClusterProps(**cluster_props)
        if isinstance(project_props, dict):
            project_props = ProjectProps(**project_props)
        if isinstance(db_user_props, dict):
            db_user_props = DatabaseUserProps(**db_user_props)
        if isinstance(ip_access_list_props, dict):
            ip_access_list_props = IpAccessListProps(**ip_access_list_props)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93da559aa417299c3d6c0b4d6d651c13874200057b5e18bd3f6cb3c0ba8f05a7)
            check_type(argname="argument cluster_props", value=cluster_props, expected_type=type_hints["cluster_props"])
            check_type(argname="argument project_props", value=project_props, expected_type=type_hints["project_props"])
            check_type(argname="argument db_user_props", value=db_user_props, expected_type=type_hints["db_user_props"])
            check_type(argname="argument ip_access_list_props", value=ip_access_list_props, expected_type=type_hints["ip_access_list_props"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_props": cluster_props,
            "project_props": project_props,
        }
        if db_user_props is not None:
            self._values["db_user_props"] = db_user_props
        if ip_access_list_props is not None:
            self._values["ip_access_list_props"] = ip_access_list_props
        if profile is not None:
            self._values["profile"] = profile

    @builtins.property
    def cluster_props(self) -> "ClusterProps":
        '''
        :description: true
        :memberof: AtlasBasicProps
        :type: {ClusterProps}
        '''
        result = self._values.get("cluster_props")
        assert result is not None, "Required property 'cluster_props' is missing"
        return typing.cast("ClusterProps", result)

    @builtins.property
    def project_props(self) -> "ProjectProps":
        '''
        :description: true
        :memberof: AtlasBasicProps
        :type: {ProjectProps}
        '''
        result = self._values.get("project_props")
        assert result is not None, "Required property 'project_props' is missing"
        return typing.cast("ProjectProps", result)

    @builtins.property
    def db_user_props(self) -> typing.Optional["DatabaseUserProps"]:
        '''
        :description: true
        :memberof: AtlasBasicProps
        :type: {DatabaseUserProps}
        '''
        result = self._values.get("db_user_props")
        return typing.cast(typing.Optional["DatabaseUserProps"], result)

    @builtins.property
    def ip_access_list_props(self) -> typing.Optional["IpAccessListProps"]:
        '''
        :description: true
        :memberof: AtlasBasicProps
        :type: {IpAccessListProps}
        '''
        result = self._values.get("ip_access_list_props")
        return typing.cast(typing.Optional["IpAccessListProps"], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''
        :description: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided ``default`` is used
        :memberof: AtlasBasicProps
        :type: {string}
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AtlasBasicProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AtlasEncryptionAtRest(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.AtlasEncryptionAtRest",
):
    '''
    :class: AtlasEncryptionAtRest
    :export: true
    :extends: Construct
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        customer_master_key_id: builtins.str,
        project_id: builtins.str,
        role_id: builtins.str,
        enabled: typing.Optional[builtins.bool] = None,
        profile: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param customer_master_key_id: The AWS customer master key used to encrypt and decrypt the MongoDB master keys.
        :param project_id: Unique identifier of the Atlas project to which the user belongs.
        :param role_id: ID of an AWS IAM role authorized to manage an AWS customer master key.
        :param enabled: Specifies whether Encryption at Rest is enabled for an Atlas project. To disable Encryption at Rest, pass only this parameter with a value of false. When you disable Encryption at Rest, Atlas also removes the configuration details. Default Value: true
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param region: The AWS region in which the AWS customer master key exists. Default Value: US_EAST_1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4eb2b1030acc5acca2fc4d2ecdf71aeb4a3143194e1f8a93dab798e2f0ffd4ef)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AtlasEncryptionAtRestProps(
            customer_master_key_id=customer_master_key_id,
            project_id=project_id,
            role_id=role_id,
            enabled=enabled,
            profile=profile,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="cfnEncryptionAtRest")
    def cfn_encryption_at_rest(self) -> "CfnEncryptionAtRest":
        '''
        :memberof: AtlasEncryptionAtRest
        :type: {CfnEncryptionAtRest}
        '''
        return typing.cast("CfnEncryptionAtRest", jsii.get(self, "cfnEncryptionAtRest"))


class AtlasEncryptionAtRestExpress(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.AtlasEncryptionAtRestExpress",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        encryption_at_rest: typing.Union["EncryptionAtRestProps", typing.Dict[builtins.str, typing.Any]],
        project_id: builtins.str,
        access_list: typing.Optional[typing.Union["IpAccessListProps", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster: typing.Optional[typing.Union["ClusterProps", typing.Dict[builtins.str, typing.Any]]] = None,
        database_user: typing.Optional[typing.Union["DatabaseUserProps", typing.Dict[builtins.str, typing.Any]]] = None,
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param encryption_at_rest: 
        :param project_id: 
        :param access_list: 
        :param cluster: 
        :param database_user: 
        :param profile: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8b33dd54ddc5da7412cb321438f6afb0d99afb6e8988b1007798ea762133760)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AtlasEncryptionAtRestExpressProps(
            encryption_at_rest=encryption_at_rest,
            project_id=project_id,
            access_list=access_list,
            cluster=cluster,
            database_user=database_user,
            profile=profile,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="encryptionAtRest")
    def encryption_at_rest(self) -> "CfnEncryptionAtRest":
        return typing.cast("CfnEncryptionAtRest", jsii.get(self, "encryptionAtRest"))

    @builtins.property
    @jsii.member(jsii_name="accessList")
    def access_list(self) -> typing.Optional["CfnProjectIpAccessList"]:
        return typing.cast(typing.Optional["CfnProjectIpAccessList"], jsii.get(self, "accessList"))

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> typing.Optional["CfnCluster"]:
        return typing.cast(typing.Optional["CfnCluster"], jsii.get(self, "cluster"))

    @builtins.property
    @jsii.member(jsii_name="databaseUser")
    def database_user(self) -> typing.Optional["CfnDatabaseUser"]:
        return typing.cast(typing.Optional["CfnDatabaseUser"], jsii.get(self, "databaseUser"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.AtlasEncryptionAtRestExpressProps",
    jsii_struct_bases=[],
    name_mapping={
        "encryption_at_rest": "encryptionAtRest",
        "project_id": "projectId",
        "access_list": "accessList",
        "cluster": "cluster",
        "database_user": "databaseUser",
        "profile": "profile",
    },
)
class AtlasEncryptionAtRestExpressProps:
    def __init__(
        self,
        *,
        encryption_at_rest: typing.Union["EncryptionAtRestProps", typing.Dict[builtins.str, typing.Any]],
        project_id: builtins.str,
        access_list: typing.Optional[typing.Union["IpAccessListProps", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster: typing.Optional[typing.Union["ClusterProps", typing.Dict[builtins.str, typing.Any]]] = None,
        database_user: typing.Optional[typing.Union["DatabaseUserProps", typing.Dict[builtins.str, typing.Any]]] = None,
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param encryption_at_rest: 
        :param project_id: 
        :param access_list: 
        :param cluster: 
        :param database_user: 
        :param profile: 
        '''
        if isinstance(encryption_at_rest, dict):
            encryption_at_rest = EncryptionAtRestProps(**encryption_at_rest)
        if isinstance(access_list, dict):
            access_list = IpAccessListProps(**access_list)
        if isinstance(cluster, dict):
            cluster = ClusterProps(**cluster)
        if isinstance(database_user, dict):
            database_user = DatabaseUserProps(**database_user)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0852dfead77edf0f28ec2bd3a9cbb3609afa983a72902f7f9c51444eb18eff2c)
            check_type(argname="argument encryption_at_rest", value=encryption_at_rest, expected_type=type_hints["encryption_at_rest"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument access_list", value=access_list, expected_type=type_hints["access_list"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument database_user", value=database_user, expected_type=type_hints["database_user"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "encryption_at_rest": encryption_at_rest,
            "project_id": project_id,
        }
        if access_list is not None:
            self._values["access_list"] = access_list
        if cluster is not None:
            self._values["cluster"] = cluster
        if database_user is not None:
            self._values["database_user"] = database_user
        if profile is not None:
            self._values["profile"] = profile

    @builtins.property
    def encryption_at_rest(self) -> "EncryptionAtRestProps":
        result = self._values.get("encryption_at_rest")
        assert result is not None, "Required property 'encryption_at_rest' is missing"
        return typing.cast("EncryptionAtRestProps", result)

    @builtins.property
    def project_id(self) -> builtins.str:
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_list(self) -> typing.Optional["IpAccessListProps"]:
        result = self._values.get("access_list")
        return typing.cast(typing.Optional["IpAccessListProps"], result)

    @builtins.property
    def cluster(self) -> typing.Optional["ClusterProps"]:
        result = self._values.get("cluster")
        return typing.cast(typing.Optional["ClusterProps"], result)

    @builtins.property
    def database_user(self) -> typing.Optional["DatabaseUserProps"]:
        result = self._values.get("database_user")
        return typing.cast(typing.Optional["DatabaseUserProps"], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AtlasEncryptionAtRestExpressProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.AtlasEncryptionAtRestProps",
    jsii_struct_bases=[],
    name_mapping={
        "customer_master_key_id": "customerMasterKeyId",
        "project_id": "projectId",
        "role_id": "roleId",
        "enabled": "enabled",
        "profile": "profile",
        "region": "region",
    },
)
class AtlasEncryptionAtRestProps:
    def __init__(
        self,
        *,
        customer_master_key_id: builtins.str,
        project_id: builtins.str,
        role_id: builtins.str,
        enabled: typing.Optional[builtins.bool] = None,
        profile: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param customer_master_key_id: The AWS customer master key used to encrypt and decrypt the MongoDB master keys.
        :param project_id: Unique identifier of the Atlas project to which the user belongs.
        :param role_id: ID of an AWS IAM role authorized to manage an AWS customer master key.
        :param enabled: Specifies whether Encryption at Rest is enabled for an Atlas project. To disable Encryption at Rest, pass only this parameter with a value of false. When you disable Encryption at Rest, Atlas also removes the configuration details. Default Value: true
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param region: The AWS region in which the AWS customer master key exists. Default Value: US_EAST_1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2055422c6e521e83bb98bde13173f68b0fcf55f218fc6c7eb6ed9d6b0fe46bbe)
            check_type(argname="argument customer_master_key_id", value=customer_master_key_id, expected_type=type_hints["customer_master_key_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument role_id", value=role_id, expected_type=type_hints["role_id"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "customer_master_key_id": customer_master_key_id,
            "project_id": project_id,
            "role_id": role_id,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if profile is not None:
            self._values["profile"] = profile
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def customer_master_key_id(self) -> builtins.str:
        '''The AWS customer master key used to encrypt and decrypt the MongoDB master keys.

        :schema: AwsKms#CustomerMasterKeyID
        '''
        result = self._values.get("customer_master_key_id")
        assert result is not None, "Required property 'customer_master_key_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique identifier of the Atlas project to which the user belongs.

        :schema: CfnEncryptionAtRestProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_id(self) -> builtins.str:
        '''ID of an AWS IAM role authorized to manage an AWS customer master key.

        :schema: AwsKms#RoleID
        '''
        result = self._values.get("role_id")
        assert result is not None, "Required property 'role_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether Encryption at Rest is enabled for an Atlas project.

        To disable Encryption at Rest, pass only this parameter with a value of false. When you disable Encryption at Rest, Atlas also removes the configuration details.
        Default Value: true

        :schema: AwsKms#Enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''The profile is defined in AWS Secret manager.

        See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnEncryptionAtRestProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The AWS region in which the AWS customer master key exists.

        Default Value: US_EAST_1

        :schema: AwsKms#Region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AtlasEncryptionAtRestProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.AtlasRole",
    jsii_struct_bases=[],
    name_mapping={
        "org_id": "orgId",
        "project_id": "projectId",
        "role_name": "roleName",
    },
)
class AtlasRole:
    def __init__(
        self,
        *,
        org_id: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        role_name: typing.Optional["AtlasRoleRoleName"] = None,
    ) -> None:
        '''
        :param org_id: Unique 24-hexadecimal digit string that identifies the organization to which this role belongs. You can set a value for this parameter or **groupId** but not both in the same request
        :param project_id: Unique 24-hexadecimal digit string that identifies the project to which this role belongs. You can set a value for this parameter or **orgId** but not both in the same request.
        :param role_name: Human-readable label that identifies the collection of privileges that MongoDB Cloud grants a specific API key, MongoDB Cloud user, or MongoDB Cloud team. These roles include organization- and project-level roles. Organization Roles - ORG_OWNER - ORG_MEMBER - ORG_GROUP_CREATOR - ORG_BILLING_ADMIN - ORG_READ_ONLY Project Roles - GROUP_CLUSTER_MANAGER - GROUP_DATA_ACCESS_ADMIN - GROUP_DATA_ACCESS_READ_ONLY - GROUP_DATA_ACCESS_READ_WRITE - GROUP_OWNER - GROUP_READ_ONLY

        :schema: AtlasRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2e9b38f68e7180f738aab12a9bcebcfdd6b552b0f1f800a61f7073a2a26bf21)
            check_type(argname="argument org_id", value=org_id, expected_type=type_hints["org_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if org_id is not None:
            self._values["org_id"] = org_id
        if project_id is not None:
            self._values["project_id"] = project_id
        if role_name is not None:
            self._values["role_name"] = role_name

    @builtins.property
    def org_id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies the organization to which this role belongs.

        You can set a value for this parameter or **groupId** but not both in the same request

        :schema: AtlasRole#OrgId
        '''
        result = self._values.get("org_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies the project to which this role belongs.

        You can set a value for this parameter or **orgId** but not both in the same request.

        :schema: AtlasRole#ProjectId
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_name(self) -> typing.Optional["AtlasRoleRoleName"]:
        '''Human-readable label that identifies the collection of privileges that MongoDB Cloud grants a specific API key, MongoDB Cloud user, or MongoDB Cloud team.

        These roles include organization- and project-level roles.

        Organization Roles

        - ORG_OWNER
        - ORG_MEMBER
        - ORG_GROUP_CREATOR
        - ORG_BILLING_ADMIN
        - ORG_READ_ONLY

        Project Roles

        - GROUP_CLUSTER_MANAGER
        - GROUP_DATA_ACCESS_ADMIN
        - GROUP_DATA_ACCESS_READ_ONLY
        - GROUP_DATA_ACCESS_READ_WRITE
        - GROUP_OWNER
        - GROUP_READ_ONLY

        :schema: AtlasRole#RoleName
        '''
        result = self._values.get("role_name")
        return typing.cast(typing.Optional["AtlasRoleRoleName"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AtlasRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.AtlasRoleRoleName")
class AtlasRoleRoleName(enum.Enum):
    '''Human-readable label that identifies the collection of privileges that MongoDB Cloud grants a specific API key, MongoDB Cloud user, or MongoDB Cloud team.

    These roles include organization- and project-level roles.

    Organization Roles

    - ORG_OWNER
    - ORG_MEMBER
    - ORG_GROUP_CREATOR
    - ORG_BILLING_ADMIN
    - ORG_READ_ONLY

    Project Roles

    - GROUP_CLUSTER_MANAGER
    - GROUP_DATA_ACCESS_ADMIN
    - GROUP_DATA_ACCESS_READ_ONLY
    - GROUP_DATA_ACCESS_READ_WRITE
    - GROUP_OWNER
    - GROUP_READ_ONLY

    :schema: AtlasRoleRoleName
    '''

    ORG_OWNER = "ORG_OWNER"
    '''ORG_OWNER.'''
    ORG_MEMBER = "ORG_MEMBER"
    '''ORG_MEMBER.'''
    ORG_GROUP_CREATOR = "ORG_GROUP_CREATOR"
    '''ORG_GROUP_CREATOR.'''
    ORG_BILLING_ADMIN = "ORG_BILLING_ADMIN"
    '''ORG_BILLING_ADMIN.'''
    ORG_READ_ONLY = "ORG_READ_ONLY"
    '''ORG_READ_ONLY.'''
    GROUP_CLUSTER_MANAGER = "GROUP_CLUSTER_MANAGER"
    '''GROUP_CLUSTER_MANAGER.'''
    GROUP_DATA_ACCESS_ADMIN = "GROUP_DATA_ACCESS_ADMIN"
    '''GROUP_DATA_ACCESS_ADMIN.'''
    GROUP_DATA_ACCESS_READ_ONLY = "GROUP_DATA_ACCESS_READ_ONLY"
    '''GROUP_DATA_ACCESS_READ_ONLY.'''
    GROUP_DATA_ACCESS_READ_WRITE = "GROUP_DATA_ACCESS_READ_WRITE"
    '''GROUP_DATA_ACCESS_READ_WRITE.'''
    GROUP_OWNER = "GROUP_OWNER"
    '''GROUP_OWNER.'''
    GROUP_READ_ONLY = "GROUP_READ_ONLY"
    '''GROUP_READ_ONLY.'''


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.AtlasUser",
    jsii_struct_bases=[],
    name_mapping={
        "country": "country",
        "email_address": "emailAddress",
        "first_name": "firstName",
        "id": "id",
        "last_name": "lastName",
        "links": "links",
        "mobile_number": "mobileNumber",
        "password": "password",
        "roles": "roles",
        "team_ids": "teamIds",
        "username": "username",
    },
)
class AtlasUser:
    def __init__(
        self,
        *,
        country: typing.Optional[builtins.str] = None,
        email_address: typing.Optional[builtins.str] = None,
        first_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        last_name: typing.Optional[builtins.str] = None,
        links: typing.Optional[typing.Sequence[typing.Union["Link", typing.Dict[builtins.str, typing.Any]]]] = None,
        mobile_number: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.Sequence[typing.Union[AtlasRole, typing.Dict[builtins.str, typing.Any]]]] = None,
        team_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param country: Two alphabet characters that identifies MongoDB Cloud user's geographic location. This parameter uses the ISO 3166-1a2 code format.
        :param email_address: Email address that belongs to the MongoDB Cloud user.
        :param first_name: First or given name that belongs to the MongoDB Cloud user.
        :param id: Unique 24-hexadecimal digit string that identifies the MongoDB Cloud user.
        :param last_name: Last name, family name, or surname that belongs to the MongoDB Cloud user.
        :param links: List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.
        :param mobile_number: Mobile phone number that belongs to the MongoDB Cloud user.
        :param password: Password applied with the username to log in to MongoDB Cloud. MongoDB Cloud does not return this parameter except in response to creating a new MongoDB Cloud user. Only the MongoDB Cloud user can update their password after it has been set from the MongoDB Cloud console.
        :param roles: List of objects that display the MongoDB Cloud user's roles and the corresponding organization or project to which that role applies. A role can apply to one organization or one project but not both.
        :param team_ids: List of unique 24-hexadecimal digit strings that identifies the teams to which this MongoDB Cloud user belongs.
        :param username: Email address that represents the username of the MongoDB Cloud user.

        :schema: AtlasUser
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1db857eabeffa5d4ead7ea85b91a863188acc280436bd51eb07ccab300640459)
            check_type(argname="argument country", value=country, expected_type=type_hints["country"])
            check_type(argname="argument email_address", value=email_address, expected_type=type_hints["email_address"])
            check_type(argname="argument first_name", value=first_name, expected_type=type_hints["first_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument last_name", value=last_name, expected_type=type_hints["last_name"])
            check_type(argname="argument links", value=links, expected_type=type_hints["links"])
            check_type(argname="argument mobile_number", value=mobile_number, expected_type=type_hints["mobile_number"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument team_ids", value=team_ids, expected_type=type_hints["team_ids"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if country is not None:
            self._values["country"] = country
        if email_address is not None:
            self._values["email_address"] = email_address
        if first_name is not None:
            self._values["first_name"] = first_name
        if id is not None:
            self._values["id"] = id
        if last_name is not None:
            self._values["last_name"] = last_name
        if links is not None:
            self._values["links"] = links
        if mobile_number is not None:
            self._values["mobile_number"] = mobile_number
        if password is not None:
            self._values["password"] = password
        if roles is not None:
            self._values["roles"] = roles
        if team_ids is not None:
            self._values["team_ids"] = team_ids
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def country(self) -> typing.Optional[builtins.str]:
        '''Two alphabet characters that identifies MongoDB Cloud user's geographic location.

        This parameter uses the ISO 3166-1a2 code format.

        :schema: AtlasUser#Country
        '''
        result = self._values.get("country")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_address(self) -> typing.Optional[builtins.str]:
        '''Email address that belongs to the MongoDB Cloud user.

        :schema: AtlasUser#EmailAddress
        '''
        result = self._values.get("email_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def first_name(self) -> typing.Optional[builtins.str]:
        '''First or given name that belongs to the MongoDB Cloud user.

        :schema: AtlasUser#FirstName
        '''
        result = self._values.get("first_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies the MongoDB Cloud user.

        :schema: AtlasUser#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_name(self) -> typing.Optional[builtins.str]:
        '''Last name, family name, or surname that belongs to the MongoDB Cloud user.

        :schema: AtlasUser#LastName
        '''
        result = self._values.get("last_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def links(self) -> typing.Optional[typing.List["Link"]]:
        '''List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both.

        RFC 5988 outlines these relationships.

        :schema: AtlasUser#Links
        '''
        result = self._values.get("links")
        return typing.cast(typing.Optional[typing.List["Link"]], result)

    @builtins.property
    def mobile_number(self) -> typing.Optional[builtins.str]:
        '''Mobile phone number that belongs to the MongoDB Cloud user.

        :schema: AtlasUser#MobileNumber
        '''
        result = self._values.get("mobile_number")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Password applied with the username to log in to MongoDB Cloud.

        MongoDB Cloud does not return this parameter except in response to creating a new MongoDB Cloud user. Only the MongoDB Cloud user can update their password after it has been set from the MongoDB Cloud console.

        :schema: AtlasUser#Password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def roles(self) -> typing.Optional[typing.List[AtlasRole]]:
        '''List of objects that display the MongoDB Cloud user's roles and the corresponding organization or project to which that role applies.

        A role can apply to one organization or one project but not both.

        :schema: AtlasUser#Roles
        '''
        result = self._values.get("roles")
        return typing.cast(typing.Optional[typing.List[AtlasRole]], result)

    @builtins.property
    def team_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of unique 24-hexadecimal digit strings that identifies the teams to which this MongoDB Cloud user belongs.

        :schema: AtlasUser#TeamIds
        '''
        result = self._values.get("team_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Email address that represents the username of the MongoDB Cloud user.

        :schema: AtlasUser#Username
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AtlasUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.AuthConfig",
    jsii_struct_bases=[],
    name_mapping={"operation_type": "operationType", "providers": "providers"},
)
class AuthConfig:
    def __init__(
        self,
        *,
        operation_type: "AuthConfigOperationType",
        providers: typing.Sequence["AuthConfigProviders"],
    ) -> None:
        '''
        :param operation_type: The type of authentication event that the trigger listens for.
        :param providers: The type(s) of authentication provider that the trigger listens to.

        :schema: AuthConfig
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5226df9d8aa32f5d603a743768e2851f951f3da7c1954ac02c0e59a1a83b6261)
            check_type(argname="argument operation_type", value=operation_type, expected_type=type_hints["operation_type"])
            check_type(argname="argument providers", value=providers, expected_type=type_hints["providers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "operation_type": operation_type,
            "providers": providers,
        }

    @builtins.property
    def operation_type(self) -> "AuthConfigOperationType":
        '''The type of authentication event that the trigger listens for.

        :schema: AuthConfig#OperationType
        '''
        result = self._values.get("operation_type")
        assert result is not None, "Required property 'operation_type' is missing"
        return typing.cast("AuthConfigOperationType", result)

    @builtins.property
    def providers(self) -> typing.List["AuthConfigProviders"]:
        '''The type(s) of authentication provider that the trigger listens to.

        :schema: AuthConfig#Providers
        '''
        result = self._values.get("providers")
        assert result is not None, "Required property 'providers' is missing"
        return typing.cast(typing.List["AuthConfigProviders"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.AuthConfigOperationType")
class AuthConfigOperationType(enum.Enum):
    '''The type of authentication event that the trigger listens for.

    :schema: AuthConfigOperationType
    '''

    LOGIN = "LOGIN"
    '''LOGIN.'''
    CREATE = "CREATE"
    '''CREATE.'''
    DELETE = "DELETE"
    '''DELETE.'''


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.AuthConfigProviders")
class AuthConfigProviders(enum.Enum):
    '''
    :schema: AuthConfigProviders
    '''

    ANON_USER = "ANON_USER"
    '''anon-user.'''
    API_KEY = "API_KEY"
    '''api-key.'''
    CUSTOM_TOKEN = "CUSTOM_TOKEN"
    '''custom-token.'''
    CUSTOM_FUNCTION = "CUSTOM_FUNCTION"
    '''custom-function.'''
    LOCAL_USERPASS = "LOCAL_USERPASS"
    '''local-userpass.'''
    OAUTH2_APPLE = "OAUTH2_APPLE"
    '''oauth2-apple.'''
    OAUTH2_FACEBOOK = "OAUTH2_FACEBOOK"
    '''oauth2-facebook.'''
    OAUTH2_GOOGLE = "OAUTH2_GOOGLE"
    '''oauth2-google.'''


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.AwsKmsConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "customer_master_key_id": "customerMasterKeyId",
        "enabled": "enabled",
        "region": "region",
        "role_id": "roleId",
    },
)
class AwsKmsConfiguration:
    def __init__(
        self,
        *,
        customer_master_key_id: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
        region: typing.Optional[builtins.str] = None,
        role_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Specifies AWS KMS configuration details and whether Encryption at Rest is enabled for an Atlas project.

        :param customer_master_key_id: The AWS customer master key used to encrypt and decrypt the MongoDB master keys.
        :param enabled: Specifies whether Encryption at Rest is enabled for an Atlas project. To disable Encryption at Rest, pass only this parameter with a value of false. When you disable Encryption at Rest, Atlas also removes the configuration details.
        :param region: The AWS region in which the AWS customer master key exists.
        :param role_id: ID of an AWS IAM role authorized to manage an AWS customer master key.

        :schema: AwsKms
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7388feda47d948491eb9f6057d8e8d13c0fa2d221eed6e7ec474b0ae15fc00f)
            check_type(argname="argument customer_master_key_id", value=customer_master_key_id, expected_type=type_hints["customer_master_key_id"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument role_id", value=role_id, expected_type=type_hints["role_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if customer_master_key_id is not None:
            self._values["customer_master_key_id"] = customer_master_key_id
        if enabled is not None:
            self._values["enabled"] = enabled
        if region is not None:
            self._values["region"] = region
        if role_id is not None:
            self._values["role_id"] = role_id

    @builtins.property
    def customer_master_key_id(self) -> typing.Optional[builtins.str]:
        '''The AWS customer master key used to encrypt and decrypt the MongoDB master keys.

        :schema: AwsKms#CustomerMasterKeyID
        '''
        result = self._values.get("customer_master_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether Encryption at Rest is enabled for an Atlas project.

        To disable Encryption at Rest, pass only this parameter with a value of false. When you disable Encryption at Rest, Atlas also removes the configuration details.

        :schema: AwsKms#Enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The AWS region in which the AWS customer master key exists.

        :schema: AwsKms#Region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_id(self) -> typing.Optional[builtins.str]:
        '''ID of an AWS IAM role authorized to manage an AWS customer master key.

        :schema: AwsKms#RoleID
        '''
        result = self._values.get("role_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsKmsConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnAlertConfiguration(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnAlertConfiguration",
):
    '''A CloudFormation ``MongoDB::Atlas::AlertConfiguration``.

    :cloudformationResource: MongoDB::Atlas::AlertConfiguration
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        created: typing.Optional[builtins.str] = None,
        event_type_name: typing.Optional[builtins.str] = None,
        matchers: typing.Optional[typing.Sequence[typing.Union["Matcher", typing.Dict[builtins.str, typing.Any]]]] = None,
        metric_threshold: typing.Optional[typing.Union["MetricThresholdView", typing.Dict[builtins.str, typing.Any]]] = None,
        notifications: typing.Optional[typing.Sequence[typing.Union["NotificationView", typing.Dict[builtins.str, typing.Any]]]] = None,
        profile: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        threshold: typing.Optional[typing.Union["IntegerThresholdView", typing.Dict[builtins.str, typing.Any]]] = None,
        type_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::AlertConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param created: Date and time when MongoDB Cloud created the alert configuration. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
        :param event_type_name: Event type that triggers an alert.
        :param matchers: List of rules that determine whether MongoDB Cloud checks an object for the alert configuration. You can filter using the matchers array if the **eventTypeName** specifies an event for a host, replica set, or sharded cluster.
        :param metric_threshold: Threshold for the metric that, when exceeded, triggers an alert. The resource returns this parameter when '"eventTypeName" : "OUTSIDE_METRIC_THRESHOLD"'.
        :param notifications: List that contains the targets that MongoDB Cloud sends notifications.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param threshold: Limit that triggers an alert when exceeded. The resource returns this parameter when **eventTypeName** has not been set to 'OUTSIDE_METRIC_THRESHOLD'.
        :param type_name: Human-readable label that displays the alert type.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1da040dafccf3c31fc01d7d84650c82a95e60338eae23c0d0e0e264555272322)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAlertConfigurationProps(
            created=created,
            event_type_name=event_type_name,
            matchers=matchers,
            metric_threshold=metric_threshold,
            notifications=notifications,
            profile=profile,
            project_id=project_id,
            threshold=threshold,
            type_name=type_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrEnabled")
    def attr_enabled(self) -> _aws_cdk_ceddda9d.IResolvable:
        '''Attribute ``MongoDB::Atlas::AlertConfiguration.Enabled``.'''
        return typing.cast(_aws_cdk_ceddda9d.IResolvable, jsii.get(self, "attrEnabled"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::AlertConfiguration.Id``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdated")
    def attr_updated(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::AlertConfiguration.Updated``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdated"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnAlertConfigurationProps":
        '''Resource props.'''
        return typing.cast("CfnAlertConfigurationProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnAlertConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "created": "created",
        "event_type_name": "eventTypeName",
        "matchers": "matchers",
        "metric_threshold": "metricThreshold",
        "notifications": "notifications",
        "profile": "profile",
        "project_id": "projectId",
        "threshold": "threshold",
        "type_name": "typeName",
    },
)
class CfnAlertConfigurationProps:
    def __init__(
        self,
        *,
        created: typing.Optional[builtins.str] = None,
        event_type_name: typing.Optional[builtins.str] = None,
        matchers: typing.Optional[typing.Sequence[typing.Union["Matcher", typing.Dict[builtins.str, typing.Any]]]] = None,
        metric_threshold: typing.Optional[typing.Union["MetricThresholdView", typing.Dict[builtins.str, typing.Any]]] = None,
        notifications: typing.Optional[typing.Sequence[typing.Union["NotificationView", typing.Dict[builtins.str, typing.Any]]]] = None,
        profile: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        threshold: typing.Optional[typing.Union["IntegerThresholdView", typing.Dict[builtins.str, typing.Any]]] = None,
        type_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Returns and edits the conditions that trigger alerts and how MongoDB Cloud notifies users.

        This collection remains under revision and may change. Refer to the legacy documentation for this collection in the following link.

        :param created: Date and time when MongoDB Cloud created the alert configuration. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
        :param event_type_name: Event type that triggers an alert.
        :param matchers: List of rules that determine whether MongoDB Cloud checks an object for the alert configuration. You can filter using the matchers array if the **eventTypeName** specifies an event for a host, replica set, or sharded cluster.
        :param metric_threshold: Threshold for the metric that, when exceeded, triggers an alert. The resource returns this parameter when '"eventTypeName" : "OUTSIDE_METRIC_THRESHOLD"'.
        :param notifications: List that contains the targets that MongoDB Cloud sends notifications.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param threshold: Limit that triggers an alert when exceeded. The resource returns this parameter when **eventTypeName** has not been set to 'OUTSIDE_METRIC_THRESHOLD'.
        :param type_name: Human-readable label that displays the alert type.

        :schema: CfnAlertConfigurationProps
        '''
        if isinstance(metric_threshold, dict):
            metric_threshold = MetricThresholdView(**metric_threshold)
        if isinstance(threshold, dict):
            threshold = IntegerThresholdView(**threshold)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__124a8c3213791f916b7d88df4adbcca6ef1de224de7be7cd6a830df6113f4ef8)
            check_type(argname="argument created", value=created, expected_type=type_hints["created"])
            check_type(argname="argument event_type_name", value=event_type_name, expected_type=type_hints["event_type_name"])
            check_type(argname="argument matchers", value=matchers, expected_type=type_hints["matchers"])
            check_type(argname="argument metric_threshold", value=metric_threshold, expected_type=type_hints["metric_threshold"])
            check_type(argname="argument notifications", value=notifications, expected_type=type_hints["notifications"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if created is not None:
            self._values["created"] = created
        if event_type_name is not None:
            self._values["event_type_name"] = event_type_name
        if matchers is not None:
            self._values["matchers"] = matchers
        if metric_threshold is not None:
            self._values["metric_threshold"] = metric_threshold
        if notifications is not None:
            self._values["notifications"] = notifications
        if profile is not None:
            self._values["profile"] = profile
        if project_id is not None:
            self._values["project_id"] = project_id
        if threshold is not None:
            self._values["threshold"] = threshold
        if type_name is not None:
            self._values["type_name"] = type_name

    @builtins.property
    def created(self) -> typing.Optional[builtins.str]:
        '''Date and time when MongoDB Cloud created the alert configuration.

        This parameter expresses its value in the ISO 8601 timestamp format in UTC.

        :schema: CfnAlertConfigurationProps#Created
        '''
        result = self._values.get("created")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_type_name(self) -> typing.Optional[builtins.str]:
        '''Event type that triggers an alert.

        :schema: CfnAlertConfigurationProps#EventTypeName
        '''
        result = self._values.get("event_type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def matchers(self) -> typing.Optional[typing.List["Matcher"]]:
        '''List of rules that determine whether MongoDB Cloud checks an object for the alert configuration.

        You can filter using the matchers array if the **eventTypeName** specifies an event for a host, replica set, or sharded cluster.

        :schema: CfnAlertConfigurationProps#Matchers
        '''
        result = self._values.get("matchers")
        return typing.cast(typing.Optional[typing.List["Matcher"]], result)

    @builtins.property
    def metric_threshold(self) -> typing.Optional["MetricThresholdView"]:
        '''Threshold for the metric that, when exceeded, triggers an alert.

        The resource returns this parameter when '"eventTypeName" : "OUTSIDE_METRIC_THRESHOLD"'.

        :schema: CfnAlertConfigurationProps#MetricThreshold
        '''
        result = self._values.get("metric_threshold")
        return typing.cast(typing.Optional["MetricThresholdView"], result)

    @builtins.property
    def notifications(self) -> typing.Optional[typing.List["NotificationView"]]:
        '''List that contains the targets that MongoDB Cloud sends notifications.

        :schema: CfnAlertConfigurationProps#Notifications
        '''
        result = self._values.get("notifications")
        return typing.cast(typing.Optional[typing.List["NotificationView"]], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.

        :schema: CfnAlertConfigurationProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnAlertConfigurationProps#ProjectId
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def threshold(self) -> typing.Optional["IntegerThresholdView"]:
        '''Limit that triggers an alert when exceeded.

        The resource returns this parameter when **eventTypeName** has not been set to 'OUTSIDE_METRIC_THRESHOLD'.

        :schema: CfnAlertConfigurationProps#Threshold
        '''
        result = self._values.get("threshold")
        return typing.cast(typing.Optional["IntegerThresholdView"], result)

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that displays the alert type.

        :schema: CfnAlertConfigurationProps#TypeName
        '''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAlertConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnAuditing(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnAuditing",
):
    '''A CloudFormation ``MongoDB::Atlas::Auditing``.

    :cloudformationResource: MongoDB::Atlas::Auditing
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        group_id: builtins.str,
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::Auditing``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param group_id: Unique 24-hexadecimal digit string that identifies your project.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a26aea3c99c1ed5d3bb2bc42924ccb83bd9c0d582ab6564ad459d34982cb0a9b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAuditingProps(group_id=group_id, profile=profile)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAuditAuthorizationSuccess")
    def attr_audit_authorization_success(self) -> _aws_cdk_ceddda9d.IResolvable:
        '''Attribute ``MongoDB::Atlas::Auditing.AuditAuthorizationSuccess``.'''
        return typing.cast(_aws_cdk_ceddda9d.IResolvable, jsii.get(self, "attrAuditAuthorizationSuccess"))

    @builtins.property
    @jsii.member(jsii_name="attrAuditFilter")
    def attr_audit_filter(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Auditing.AuditFilter``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrAuditFilter"))

    @builtins.property
    @jsii.member(jsii_name="attrConfigurationType")
    def attr_configuration_type(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Auditing.ConfigurationType``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrConfigurationType"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnAuditingProps":
        '''Resource props.'''
        return typing.cast("CfnAuditingProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnAuditingProps",
    jsii_struct_bases=[],
    name_mapping={"group_id": "groupId", "profile": "profile"},
)
class CfnAuditingProps:
    def __init__(
        self,
        *,
        group_id: builtins.str,
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Returns and edits database auditing settings for MongoDB Cloud projects.

        :param group_id: Unique 24-hexadecimal digit string that identifies your project.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.

        :schema: CfnAuditingProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3478ad6f6a0f7e5f69e0f8e3efee5546775e0c04b0842546e587aee290cc4f1)
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_id": group_id,
        }
        if profile is not None:
            self._values["profile"] = profile

    @builtins.property
    def group_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnAuditingProps#GroupId
        '''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.

        :schema: CfnAuditingProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAuditingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnCloudBackUpRestoreJobs(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnCloudBackUpRestoreJobs",
):
    '''A CloudFormation ``MongoDB::Atlas::CloudBackUpRestoreJobs``.

    :cloudformationResource: MongoDB::Atlas::CloudBackUpRestoreJobs
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster_name: builtins.str,
        project_id: builtins.str,
        cancelled: typing.Optional[builtins.bool] = None,
        delivery_type: typing.Optional["CfnCloudBackUpRestoreJobsPropsDeliveryType"] = None,
        expired: typing.Optional[builtins.bool] = None,
        instance_name: typing.Optional[builtins.str] = None,
        op_log_inc: typing.Optional[builtins.str] = None,
        op_log_ts: typing.Optional[builtins.str] = None,
        point_in_time_utc_seconds: typing.Optional[jsii.Number] = None,
        profile: typing.Optional[builtins.str] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        target_cluster_name: typing.Optional[builtins.str] = None,
        target_project_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::CloudBackUpRestoreJobs``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cluster_name: The name of the Atlas cluster whose snapshot you want to restore or you want to retrieve restore jobs.
        :param project_id: The unique identifier of the project for the Atlas cluster.
        :param cancelled: Indicates whether the restore job was canceled.
        :param delivery_type: Type of restore job to create.The value can be any one of download,automated or point_in_time.
        :param expired: Indicates whether the restore job expired.
        :param instance_name: The instance name of the Serverless cluster whose snapshot you want to restore or you want to retrieve restore jobs.
        :param op_log_inc: Oplog operation number from which to you want to restore this snapshot. This is the second part of an Oplog timestamp.
        :param op_log_ts: Timestamp in the number of seconds that have elapsed since the UNIX epoch from which to you want to restore this snapshot. This is the first part of an Oplog timestamp.
        :param point_in_time_utc_seconds: If you performed a Point-in-Time restores at a time specified by a Unix time in seconds since epoch, pointInTimeUTCSeconds indicates the Unix time used.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param snapshot_id: Unique identifier of the source snapshot ID of the restore job.
        :param target_cluster_name: Name of the target Atlas cluster to which the restore job restores the snapshot. Only visible if deliveryType is automated.
        :param target_project_id: Name of the target Atlas project of the restore job. Only visible if deliveryType is automated.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d5a576b5b88e386d800cf2be9f8dd13676ca57ee8ff8653f832b0d7cc06b8cf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCloudBackUpRestoreJobsProps(
            cluster_name=cluster_name,
            project_id=project_id,
            cancelled=cancelled,
            delivery_type=delivery_type,
            expired=expired,
            instance_name=instance_name,
            op_log_inc=op_log_inc,
            op_log_ts=op_log_ts,
            point_in_time_utc_seconds=point_in_time_utc_seconds,
            profile=profile,
            snapshot_id=snapshot_id,
            target_cluster_name=target_cluster_name,
            target_project_id=target_project_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::CloudBackUpRestoreJobs.CreatedAt``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDeliveryUrl")
    def attr_delivery_url(self) -> typing.List[builtins.str]:
        '''Attribute ``MongoDB::Atlas::CloudBackUpRestoreJobs.DeliveryUrl``.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrDeliveryUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrExpiresAt")
    def attr_expires_at(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::CloudBackUpRestoreJobs.ExpiresAt``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrExpiresAt"))

    @builtins.property
    @jsii.member(jsii_name="attrFinishedAt")
    def attr_finished_at(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::CloudBackUpRestoreJobs.FinishedAt``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrFinishedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::CloudBackUpRestoreJobs.Id``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrTimestamp")
    def attr_timestamp(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::CloudBackUpRestoreJobs.Timestamp``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnCloudBackUpRestoreJobsProps":
        '''Resource props.'''
        return typing.cast("CfnCloudBackUpRestoreJobsProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnCloudBackUpRestoreJobsProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_name": "clusterName",
        "project_id": "projectId",
        "cancelled": "cancelled",
        "delivery_type": "deliveryType",
        "expired": "expired",
        "instance_name": "instanceName",
        "op_log_inc": "opLogInc",
        "op_log_ts": "opLogTs",
        "point_in_time_utc_seconds": "pointInTimeUtcSeconds",
        "profile": "profile",
        "snapshot_id": "snapshotId",
        "target_cluster_name": "targetClusterName",
        "target_project_id": "targetProjectId",
    },
)
class CfnCloudBackUpRestoreJobsProps:
    def __init__(
        self,
        *,
        cluster_name: builtins.str,
        project_id: builtins.str,
        cancelled: typing.Optional[builtins.bool] = None,
        delivery_type: typing.Optional["CfnCloudBackUpRestoreJobsPropsDeliveryType"] = None,
        expired: typing.Optional[builtins.bool] = None,
        instance_name: typing.Optional[builtins.str] = None,
        op_log_inc: typing.Optional[builtins.str] = None,
        op_log_ts: typing.Optional[builtins.str] = None,
        point_in_time_utc_seconds: typing.Optional[jsii.Number] = None,
        profile: typing.Optional[builtins.str] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        target_cluster_name: typing.Optional[builtins.str] = None,
        target_project_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Returns, starts, and cancels Cloud Backup restore jobs.

        :param cluster_name: The name of the Atlas cluster whose snapshot you want to restore or you want to retrieve restore jobs.
        :param project_id: The unique identifier of the project for the Atlas cluster.
        :param cancelled: Indicates whether the restore job was canceled.
        :param delivery_type: Type of restore job to create.The value can be any one of download,automated or point_in_time.
        :param expired: Indicates whether the restore job expired.
        :param instance_name: The instance name of the Serverless cluster whose snapshot you want to restore or you want to retrieve restore jobs.
        :param op_log_inc: Oplog operation number from which to you want to restore this snapshot. This is the second part of an Oplog timestamp.
        :param op_log_ts: Timestamp in the number of seconds that have elapsed since the UNIX epoch from which to you want to restore this snapshot. This is the first part of an Oplog timestamp.
        :param point_in_time_utc_seconds: If you performed a Point-in-Time restores at a time specified by a Unix time in seconds since epoch, pointInTimeUTCSeconds indicates the Unix time used.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param snapshot_id: Unique identifier of the source snapshot ID of the restore job.
        :param target_cluster_name: Name of the target Atlas cluster to which the restore job restores the snapshot. Only visible if deliveryType is automated.
        :param target_project_id: Name of the target Atlas project of the restore job. Only visible if deliveryType is automated.

        :schema: CfnCloudBackUpRestoreJobsProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c452f384c2684cd0393e2f443bac830ff55b9ea890ebb7fb44b8bd797fdda1a9)
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument cancelled", value=cancelled, expected_type=type_hints["cancelled"])
            check_type(argname="argument delivery_type", value=delivery_type, expected_type=type_hints["delivery_type"])
            check_type(argname="argument expired", value=expired, expected_type=type_hints["expired"])
            check_type(argname="argument instance_name", value=instance_name, expected_type=type_hints["instance_name"])
            check_type(argname="argument op_log_inc", value=op_log_inc, expected_type=type_hints["op_log_inc"])
            check_type(argname="argument op_log_ts", value=op_log_ts, expected_type=type_hints["op_log_ts"])
            check_type(argname="argument point_in_time_utc_seconds", value=point_in_time_utc_seconds, expected_type=type_hints["point_in_time_utc_seconds"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument snapshot_id", value=snapshot_id, expected_type=type_hints["snapshot_id"])
            check_type(argname="argument target_cluster_name", value=target_cluster_name, expected_type=type_hints["target_cluster_name"])
            check_type(argname="argument target_project_id", value=target_project_id, expected_type=type_hints["target_project_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_name": cluster_name,
            "project_id": project_id,
        }
        if cancelled is not None:
            self._values["cancelled"] = cancelled
        if delivery_type is not None:
            self._values["delivery_type"] = delivery_type
        if expired is not None:
            self._values["expired"] = expired
        if instance_name is not None:
            self._values["instance_name"] = instance_name
        if op_log_inc is not None:
            self._values["op_log_inc"] = op_log_inc
        if op_log_ts is not None:
            self._values["op_log_ts"] = op_log_ts
        if point_in_time_utc_seconds is not None:
            self._values["point_in_time_utc_seconds"] = point_in_time_utc_seconds
        if profile is not None:
            self._values["profile"] = profile
        if snapshot_id is not None:
            self._values["snapshot_id"] = snapshot_id
        if target_cluster_name is not None:
            self._values["target_cluster_name"] = target_cluster_name
        if target_project_id is not None:
            self._values["target_project_id"] = target_project_id

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''The name of the Atlas cluster whose snapshot you want to restore or you want to retrieve restore jobs.

        :schema: CfnCloudBackUpRestoreJobsProps#ClusterName
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The unique identifier of the project for the Atlas cluster.

        :schema: CfnCloudBackUpRestoreJobsProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cancelled(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether the restore job was canceled.

        :schema: CfnCloudBackUpRestoreJobsProps#Cancelled
        '''
        result = self._values.get("cancelled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def delivery_type(
        self,
    ) -> typing.Optional["CfnCloudBackUpRestoreJobsPropsDeliveryType"]:
        '''Type of restore job to create.The value can be any one of download,automated or point_in_time.

        :schema: CfnCloudBackUpRestoreJobsProps#DeliveryType
        '''
        result = self._values.get("delivery_type")
        return typing.cast(typing.Optional["CfnCloudBackUpRestoreJobsPropsDeliveryType"], result)

    @builtins.property
    def expired(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether the restore job expired.

        :schema: CfnCloudBackUpRestoreJobsProps#Expired
        '''
        result = self._values.get("expired")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def instance_name(self) -> typing.Optional[builtins.str]:
        '''The instance name of the Serverless cluster whose snapshot you want to restore or you want to retrieve restore jobs.

        :schema: CfnCloudBackUpRestoreJobsProps#InstanceName
        '''
        result = self._values.get("instance_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def op_log_inc(self) -> typing.Optional[builtins.str]:
        '''Oplog operation number from which to you want to restore this snapshot.

        This is the second part of an Oplog timestamp.

        :schema: CfnCloudBackUpRestoreJobsProps#OpLogInc
        '''
        result = self._values.get("op_log_inc")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def op_log_ts(self) -> typing.Optional[builtins.str]:
        '''Timestamp in the number of seconds that have elapsed since the UNIX epoch from which to you want to restore this snapshot.

        This is the first part of an Oplog timestamp.

        :schema: CfnCloudBackUpRestoreJobsProps#OpLogTs
        '''
        result = self._values.get("op_log_ts")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def point_in_time_utc_seconds(self) -> typing.Optional[jsii.Number]:
        '''If you performed a Point-in-Time restores at a time specified by a Unix time in seconds since epoch, pointInTimeUTCSeconds indicates the Unix time used.

        :schema: CfnCloudBackUpRestoreJobsProps#PointInTimeUtcSeconds
        '''
        result = self._values.get("point_in_time_utc_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.

        :schema: CfnCloudBackUpRestoreJobsProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier of the source snapshot ID of the restore job.

        :schema: CfnCloudBackUpRestoreJobsProps#SnapshotId
        '''
        result = self._values.get("snapshot_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_cluster_name(self) -> typing.Optional[builtins.str]:
        '''Name of the target Atlas cluster to which the restore job restores the snapshot.

        Only visible if deliveryType is automated.

        :schema: CfnCloudBackUpRestoreJobsProps#TargetClusterName
        '''
        result = self._values.get("target_cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_project_id(self) -> typing.Optional[builtins.str]:
        '''Name of the target Atlas project of the restore job.

        Only visible if deliveryType is automated.

        :schema: CfnCloudBackUpRestoreJobsProps#TargetProjectId
        '''
        result = self._values.get("target_project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudBackUpRestoreJobsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="awscdk-resources-mongodbatlas.CfnCloudBackUpRestoreJobsPropsDeliveryType"
)
class CfnCloudBackUpRestoreJobsPropsDeliveryType(enum.Enum):
    '''Type of restore job to create.The value can be any one of download,automated or point_in_time.

    :schema: CfnCloudBackUpRestoreJobsPropsDeliveryType
    '''

    DOWNLOAD = "DOWNLOAD"
    '''download.'''
    AUTOMATED = "AUTOMATED"
    '''automated.'''
    POINT_IN_TIME = "POINT_IN_TIME"
    '''pointInTime.'''


class CfnCloudBackupSchedule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnCloudBackupSchedule",
):
    '''A CloudFormation ``MongoDB::Atlas::CloudBackupSchedule``.

    :cloudformationResource: MongoDB::Atlas::CloudBackupSchedule
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        cluster_name: builtins.str,
        project_id: builtins.str,
        auto_export_enabled: typing.Optional[builtins.bool] = None,
        copy_settings: typing.Optional[typing.Sequence[typing.Union[ApiAtlasDiskBackupCopySettingView, typing.Dict[builtins.str, typing.Any]]]] = None,
        delete_copied_backups: typing.Optional[typing.Sequence[typing.Union[ApiDeleteCopiedBackupsView, typing.Dict[builtins.str, typing.Any]]]] = None,
        export: typing.Optional[typing.Union["Export", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        links: typing.Optional[typing.Sequence[typing.Union["Link", typing.Dict[builtins.str, typing.Any]]]] = None,
        policies: typing.Optional[typing.Sequence[typing.Union[ApiPolicyView, typing.Dict[builtins.str, typing.Any]]]] = None,
        profile: typing.Optional[builtins.str] = None,
        reference_hour_of_day: typing.Optional[jsii.Number] = None,
        reference_minute_of_hour: typing.Optional[jsii.Number] = None,
        restore_window_days: typing.Optional[jsii.Number] = None,
        update_snapshots: typing.Optional[builtins.bool] = None,
        use_org_and_group_names_in_export_prefix: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::CloudBackupSchedule``.

        :param scope: - scope in which this resource is defined.
        :param id_: - scoped id of the resource.
        :param cluster_name: The name of the Atlas cluster that contains the snapshots you want to retrieve.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param auto_export_enabled: Flag that indicates whether automatic export of cloud backup snapshots to the AWS bucket is enabled.
        :param copy_settings: List that contains a document for each copy setting item in the desired backup policy.
        :param delete_copied_backups: List that contains a document for each deleted copy setting whose backup copies you want to delete.
        :param export: Policy for automatically exporting cloud backup snapshots.
        :param id: Unique identifier of the snapshot.
        :param links: List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.
        :param policies: Rules set for this backup schedule.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param reference_hour_of_day: UTC Hour of day between 0 and 23 representing which hour of the day that Atlas takes a snapshot.
        :param reference_minute_of_hour: UTC Minute of day between 0 and 59 representing which minute of the referenceHourOfDay that Atlas takes the snapshot.
        :param restore_window_days: Number of days back in time you can restore to with Continuous Cloud Backup accuracy. Must be a positive, non-zero integer.
        :param update_snapshots: Flag indicating if updates to retention in the backup policy were applied to snapshots that Atlas took earlier.
        :param use_org_and_group_names_in_export_prefix: Specify true to use organization and project names instead of organization and project UUIDs in the path for the metadata files that Atlas uploads to your S3 bucket after it finishes exporting the snapshots.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bfdd674c8b0e499ab1f52cd281df10bf04b830fce65245beea7d06c6b570b57)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        props = CfnCloudBackupScheduleProps(
            cluster_name=cluster_name,
            project_id=project_id,
            auto_export_enabled=auto_export_enabled,
            copy_settings=copy_settings,
            delete_copied_backups=delete_copied_backups,
            export=export,
            id=id,
            links=links,
            policies=policies,
            profile=profile,
            reference_hour_of_day=reference_hour_of_day,
            reference_minute_of_hour=reference_minute_of_hour,
            restore_window_days=restore_window_days,
            update_snapshots=update_snapshots,
            use_org_and_group_names_in_export_prefix=use_org_and_group_names_in_export_prefix,
        )

        jsii.create(self.__class__, self, [scope, id_, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterId")
    def attr_cluster_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::CloudBackupSchedule.ClusterId``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrClusterId"))

    @builtins.property
    @jsii.member(jsii_name="attrNextSnapshot")
    def attr_next_snapshot(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::CloudBackupSchedule.NextSnapshot``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrNextSnapshot"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnCloudBackupScheduleProps":
        '''Resource props.'''
        return typing.cast("CfnCloudBackupScheduleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnCloudBackupScheduleProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_name": "clusterName",
        "project_id": "projectId",
        "auto_export_enabled": "autoExportEnabled",
        "copy_settings": "copySettings",
        "delete_copied_backups": "deleteCopiedBackups",
        "export": "export",
        "id": "id",
        "links": "links",
        "policies": "policies",
        "profile": "profile",
        "reference_hour_of_day": "referenceHourOfDay",
        "reference_minute_of_hour": "referenceMinuteOfHour",
        "restore_window_days": "restoreWindowDays",
        "update_snapshots": "updateSnapshots",
        "use_org_and_group_names_in_export_prefix": "useOrgAndGroupNamesInExportPrefix",
    },
)
class CfnCloudBackupScheduleProps:
    def __init__(
        self,
        *,
        cluster_name: builtins.str,
        project_id: builtins.str,
        auto_export_enabled: typing.Optional[builtins.bool] = None,
        copy_settings: typing.Optional[typing.Sequence[typing.Union[ApiAtlasDiskBackupCopySettingView, typing.Dict[builtins.str, typing.Any]]]] = None,
        delete_copied_backups: typing.Optional[typing.Sequence[typing.Union[ApiDeleteCopiedBackupsView, typing.Dict[builtins.str, typing.Any]]]] = None,
        export: typing.Optional[typing.Union["Export", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        links: typing.Optional[typing.Sequence[typing.Union["Link", typing.Dict[builtins.str, typing.Any]]]] = None,
        policies: typing.Optional[typing.Sequence[typing.Union[ApiPolicyView, typing.Dict[builtins.str, typing.Any]]]] = None,
        profile: typing.Optional[builtins.str] = None,
        reference_hour_of_day: typing.Optional[jsii.Number] = None,
        reference_minute_of_hour: typing.Optional[jsii.Number] = None,
        restore_window_days: typing.Optional[jsii.Number] = None,
        update_snapshots: typing.Optional[builtins.bool] = None,
        use_org_and_group_names_in_export_prefix: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''An example resource schema demonstrating some basic constructs and validation rules.

        :param cluster_name: The name of the Atlas cluster that contains the snapshots you want to retrieve.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param auto_export_enabled: Flag that indicates whether automatic export of cloud backup snapshots to the AWS bucket is enabled.
        :param copy_settings: List that contains a document for each copy setting item in the desired backup policy.
        :param delete_copied_backups: List that contains a document for each deleted copy setting whose backup copies you want to delete.
        :param export: Policy for automatically exporting cloud backup snapshots.
        :param id: Unique identifier of the snapshot.
        :param links: List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.
        :param policies: Rules set for this backup schedule.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param reference_hour_of_day: UTC Hour of day between 0 and 23 representing which hour of the day that Atlas takes a snapshot.
        :param reference_minute_of_hour: UTC Minute of day between 0 and 59 representing which minute of the referenceHourOfDay that Atlas takes the snapshot.
        :param restore_window_days: Number of days back in time you can restore to with Continuous Cloud Backup accuracy. Must be a positive, non-zero integer.
        :param update_snapshots: Flag indicating if updates to retention in the backup policy were applied to snapshots that Atlas took earlier.
        :param use_org_and_group_names_in_export_prefix: Specify true to use organization and project names instead of organization and project UUIDs in the path for the metadata files that Atlas uploads to your S3 bucket after it finishes exporting the snapshots.

        :schema: CfnCloudBackupScheduleProps
        '''
        if isinstance(export, dict):
            export = Export(**export)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2200bd53f19ffb8d78ee28d63e9f901d04707cca2ada01f3a1c4aa6c97d8aef)
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument auto_export_enabled", value=auto_export_enabled, expected_type=type_hints["auto_export_enabled"])
            check_type(argname="argument copy_settings", value=copy_settings, expected_type=type_hints["copy_settings"])
            check_type(argname="argument delete_copied_backups", value=delete_copied_backups, expected_type=type_hints["delete_copied_backups"])
            check_type(argname="argument export", value=export, expected_type=type_hints["export"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument links", value=links, expected_type=type_hints["links"])
            check_type(argname="argument policies", value=policies, expected_type=type_hints["policies"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument reference_hour_of_day", value=reference_hour_of_day, expected_type=type_hints["reference_hour_of_day"])
            check_type(argname="argument reference_minute_of_hour", value=reference_minute_of_hour, expected_type=type_hints["reference_minute_of_hour"])
            check_type(argname="argument restore_window_days", value=restore_window_days, expected_type=type_hints["restore_window_days"])
            check_type(argname="argument update_snapshots", value=update_snapshots, expected_type=type_hints["update_snapshots"])
            check_type(argname="argument use_org_and_group_names_in_export_prefix", value=use_org_and_group_names_in_export_prefix, expected_type=type_hints["use_org_and_group_names_in_export_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_name": cluster_name,
            "project_id": project_id,
        }
        if auto_export_enabled is not None:
            self._values["auto_export_enabled"] = auto_export_enabled
        if copy_settings is not None:
            self._values["copy_settings"] = copy_settings
        if delete_copied_backups is not None:
            self._values["delete_copied_backups"] = delete_copied_backups
        if export is not None:
            self._values["export"] = export
        if id is not None:
            self._values["id"] = id
        if links is not None:
            self._values["links"] = links
        if policies is not None:
            self._values["policies"] = policies
        if profile is not None:
            self._values["profile"] = profile
        if reference_hour_of_day is not None:
            self._values["reference_hour_of_day"] = reference_hour_of_day
        if reference_minute_of_hour is not None:
            self._values["reference_minute_of_hour"] = reference_minute_of_hour
        if restore_window_days is not None:
            self._values["restore_window_days"] = restore_window_days
        if update_snapshots is not None:
            self._values["update_snapshots"] = update_snapshots
        if use_org_and_group_names_in_export_prefix is not None:
            self._values["use_org_and_group_names_in_export_prefix"] = use_org_and_group_names_in_export_prefix

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''The name of the Atlas cluster that contains the snapshots you want to retrieve.

        :schema: CfnCloudBackupScheduleProps#ClusterName
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnCloudBackupScheduleProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_export_enabled(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether automatic export of cloud backup snapshots to the AWS bucket is enabled.

        :schema: CfnCloudBackupScheduleProps#AutoExportEnabled
        '''
        result = self._values.get("auto_export_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def copy_settings(
        self,
    ) -> typing.Optional[typing.List[ApiAtlasDiskBackupCopySettingView]]:
        '''List that contains a document for each copy setting item in the desired backup policy.

        :schema: CfnCloudBackupScheduleProps#CopySettings
        '''
        result = self._values.get("copy_settings")
        return typing.cast(typing.Optional[typing.List[ApiAtlasDiskBackupCopySettingView]], result)

    @builtins.property
    def delete_copied_backups(
        self,
    ) -> typing.Optional[typing.List[ApiDeleteCopiedBackupsView]]:
        '''List that contains a document for each deleted copy setting whose backup copies you want to delete.

        :schema: CfnCloudBackupScheduleProps#DeleteCopiedBackups
        '''
        result = self._values.get("delete_copied_backups")
        return typing.cast(typing.Optional[typing.List[ApiDeleteCopiedBackupsView]], result)

    @builtins.property
    def export(self) -> typing.Optional["Export"]:
        '''Policy for automatically exporting cloud backup snapshots.

        :schema: CfnCloudBackupScheduleProps#Export
        '''
        result = self._values.get("export")
        return typing.cast(typing.Optional["Export"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier of the snapshot.

        :schema: CfnCloudBackupScheduleProps#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def links(self) -> typing.Optional[typing.List["Link"]]:
        '''List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both.

        RFC 5988 outlines these relationships.

        :schema: CfnCloudBackupScheduleProps#Links
        '''
        result = self._values.get("links")
        return typing.cast(typing.Optional[typing.List["Link"]], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[ApiPolicyView]]:
        '''Rules set for this backup schedule.

        :schema: CfnCloudBackupScheduleProps#Policies
        '''
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[ApiPolicyView]], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.

        :schema: CfnCloudBackupScheduleProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reference_hour_of_day(self) -> typing.Optional[jsii.Number]:
        '''UTC Hour of day between 0 and 23 representing which hour of the day that Atlas takes a snapshot.

        :schema: CfnCloudBackupScheduleProps#ReferenceHourOfDay
        '''
        result = self._values.get("reference_hour_of_day")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def reference_minute_of_hour(self) -> typing.Optional[jsii.Number]:
        '''UTC Minute of day between 0 and 59 representing which minute of the referenceHourOfDay that Atlas takes the snapshot.

        :schema: CfnCloudBackupScheduleProps#ReferenceMinuteOfHour
        '''
        result = self._values.get("reference_minute_of_hour")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def restore_window_days(self) -> typing.Optional[jsii.Number]:
        '''Number of days back in time you can restore to with Continuous Cloud Backup accuracy.

        Must be a positive, non-zero integer.

        :schema: CfnCloudBackupScheduleProps#RestoreWindowDays
        '''
        result = self._values.get("restore_window_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def update_snapshots(self) -> typing.Optional[builtins.bool]:
        '''Flag indicating if updates to retention in the backup policy were applied to snapshots that Atlas took earlier.

        :schema: CfnCloudBackupScheduleProps#UpdateSnapshots
        '''
        result = self._values.get("update_snapshots")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def use_org_and_group_names_in_export_prefix(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Specify true to use organization and project names instead of organization and project UUIDs in the path for the metadata files that Atlas uploads to your S3 bucket after it finishes exporting the snapshots.

        :schema: CfnCloudBackupScheduleProps#UseOrgAndGroupNamesInExportPrefix
        '''
        result = self._values.get("use_org_and_group_names_in_export_prefix")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudBackupScheduleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnCloudBackupSnapshot(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnCloudBackupSnapshot",
):
    '''A CloudFormation ``MongoDB::Atlas::CloudBackupSnapshot``.

    :cloudformationResource: MongoDB::Atlas::CloudBackupSnapshot
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster_name: builtins.str,
        project_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        frequency_type: typing.Optional["CfnCloudBackupSnapshotPropsFrequencyType"] = None,
        include_count: typing.Optional[builtins.bool] = None,
        instance_name: typing.Optional[builtins.str] = None,
        items_per_page: typing.Optional[jsii.Number] = None,
        members: typing.Optional[typing.Sequence[typing.Union[ApiAtlasDiskBackupShardedClusterSnapshotMemberView, typing.Dict[builtins.str, typing.Any]]]] = None,
        page_num: typing.Optional[jsii.Number] = None,
        policy_items: typing.Optional[typing.Sequence[builtins.str]] = None,
        profile: typing.Optional[builtins.str] = None,
        results: typing.Optional[typing.Sequence[typing.Union[ApiAtlasDiskBackupShardedClusterSnapshotView, typing.Dict[builtins.str, typing.Any]]]] = None,
        retention_in_days: typing.Optional[jsii.Number] = None,
        snapshot_type: typing.Optional["CfnCloudBackupSnapshotPropsSnapshotType"] = None,
        total_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::CloudBackupSnapshot``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cluster_name: Human-readable label that identifies the cluster.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param description: Human-readable phrase or sentence that explains the purpose of the snapshot. The resource returns this parameter when ``"status": "onDemand"``.
        :param frequency_type: Human-readable label that identifies how often this snapshot triggers.
        :param include_count: Flag that indicates whether the response returns the total number of items (**totalCount**) in the response.
        :param instance_name: Human-readable label that identifies the serverless instance.
        :param items_per_page: Number of items that the response returns per page.
        :param members: List that includes the snapshots and the cloud provider that stores the snapshots. The resource returns this parameter when ``"type" : "SHARDED_CLUSTER"``.
        :param page_num: Number of the page that displays the current set of the total objects that the response returns.
        :param policy_items: List that contains unique identifiers for the policy items.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param results: List of returned documents that MongoDB Cloud provides when completing this request.
        :param retention_in_days: Number of days that MongoDB Cloud should retain the on-demand snapshot. Must be at least **1**
        :param snapshot_type: Human-readable label that identifies when this snapshot triggers.
        :param total_count: Number of documents returned in this response.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__529f49fdab044e02ca0bd055ed41fa8d7b5b244ba250907765c0fc282e21cd88)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCloudBackupSnapshotProps(
            cluster_name=cluster_name,
            project_id=project_id,
            description=description,
            frequency_type=frequency_type,
            include_count=include_count,
            instance_name=instance_name,
            items_per_page=items_per_page,
            members=members,
            page_num=page_num,
            policy_items=policy_items,
            profile=profile,
            results=results,
            retention_in_days=retention_in_days,
            snapshot_type=snapshot_type,
            total_count=total_count,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCloudProvider")
    def attr_cloud_provider(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::CloudBackupSnapshot.CloudProvider``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrCloudProvider"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::CloudBackupSnapshot.CreatedAt``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrExpiresAt")
    def attr_expires_at(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::CloudBackupSnapshot.ExpiresAt``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrExpiresAt"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::CloudBackupSnapshot.Id``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrMasterKeyUUID")
    def attr_master_key_uuid(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::CloudBackupSnapshot.MasterKeyUUID``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrMasterKeyUUID"))

    @builtins.property
    @jsii.member(jsii_name="attrMongodVersion")
    def attr_mongod_version(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::CloudBackupSnapshot.MongodVersion``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrMongodVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrReplicaSetName")
    def attr_replica_set_name(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::CloudBackupSnapshot.ReplicaSetName``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrReplicaSetName"))

    @builtins.property
    @jsii.member(jsii_name="attrSnapshotId")
    def attr_snapshot_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::CloudBackupSnapshot.SnapshotId``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrSnapshotId"))

    @builtins.property
    @jsii.member(jsii_name="attrSnapshotIds")
    def attr_snapshot_ids(self) -> typing.List[builtins.str]:
        '''Attribute ``MongoDB::Atlas::CloudBackupSnapshot.SnapshotIds``.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrSnapshotIds"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::CloudBackupSnapshot.Status``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStorageSizeBytes")
    def attr_storage_size_bytes(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::CloudBackupSnapshot.StorageSizeBytes``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrStorageSizeBytes"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::CloudBackupSnapshot.Type``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnCloudBackupSnapshotProps":
        '''Resource props.'''
        return typing.cast("CfnCloudBackupSnapshotProps", jsii.get(self, "props"))


class CfnCloudBackupSnapshotExportBucket(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnCloudBackupSnapshotExportBucket",
):
    '''A CloudFormation ``MongoDB::Atlas::CloudBackupSnapshotExportBucket``.

    :cloudformationResource: MongoDB::Atlas::CloudBackupSnapshotExportBucket
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        bucket_name: builtins.str,
        iam_role_id: builtins.str,
        project_id: builtins.str,
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::CloudBackupSnapshotExportBucket``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param bucket_name: Human-readable label that identifies the AWS bucket that the role is authorized to access.
        :param iam_role_id: Unique 24-hexadecimal character string that identifies the AWS IAM role that MongoDB Cloud uses to access the AWS S3 bucket.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d2cbf89a63594824b85f7bcf3bf165f87cb367057546423748ece0b111c26ff)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCloudBackupSnapshotExportBucketProps(
            bucket_name=bucket_name,
            iam_role_id=iam_role_id,
            project_id=project_id,
            profile=profile,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::CloudBackupSnapshotExportBucket.Id``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnCloudBackupSnapshotExportBucketProps":
        '''Resource props.'''
        return typing.cast("CfnCloudBackupSnapshotExportBucketProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnCloudBackupSnapshotExportBucketProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "iam_role_id": "iamRoleId",
        "project_id": "projectId",
        "profile": "profile",
    },
)
class CfnCloudBackupSnapshotExportBucketProps:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        iam_role_id: builtins.str,
        project_id: builtins.str,
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The exportBuckets resource allows you to grant Atlas access to the specified bucket for exporting backup snapshots.

        :param bucket_name: Human-readable label that identifies the AWS bucket that the role is authorized to access.
        :param iam_role_id: Unique 24-hexadecimal character string that identifies the AWS IAM role that MongoDB Cloud uses to access the AWS S3 bucket.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnCloudBackupSnapshotExportBucketProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bbf399890a7be0cef3c6995156840980718a18571938b035823d3ca4cf5afe7)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument iam_role_id", value=iam_role_id, expected_type=type_hints["iam_role_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
            "iam_role_id": iam_role_id,
            "project_id": project_id,
        }
        if profile is not None:
            self._values["profile"] = profile

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Human-readable label that identifies the AWS bucket that the role is authorized to access.

        :schema: CfnCloudBackupSnapshotExportBucketProps#BucketName
        '''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def iam_role_id(self) -> builtins.str:
        '''Unique 24-hexadecimal character string that identifies the AWS IAM role that MongoDB Cloud uses to access the AWS S3 bucket.

        :schema: CfnCloudBackupSnapshotExportBucketProps#IamRoleID
        '''
        result = self._values.get("iam_role_id")
        assert result is not None, "Required property 'iam_role_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnCloudBackupSnapshotExportBucketProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''The profile is defined in AWS Secret manager.

        See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnCloudBackupSnapshotExportBucketProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudBackupSnapshotExportBucketProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnCloudBackupSnapshotProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_name": "clusterName",
        "project_id": "projectId",
        "description": "description",
        "frequency_type": "frequencyType",
        "include_count": "includeCount",
        "instance_name": "instanceName",
        "items_per_page": "itemsPerPage",
        "members": "members",
        "page_num": "pageNum",
        "policy_items": "policyItems",
        "profile": "profile",
        "results": "results",
        "retention_in_days": "retentionInDays",
        "snapshot_type": "snapshotType",
        "total_count": "totalCount",
    },
)
class CfnCloudBackupSnapshotProps:
    def __init__(
        self,
        *,
        cluster_name: builtins.str,
        project_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        frequency_type: typing.Optional["CfnCloudBackupSnapshotPropsFrequencyType"] = None,
        include_count: typing.Optional[builtins.bool] = None,
        instance_name: typing.Optional[builtins.str] = None,
        items_per_page: typing.Optional[jsii.Number] = None,
        members: typing.Optional[typing.Sequence[typing.Union[ApiAtlasDiskBackupShardedClusterSnapshotMemberView, typing.Dict[builtins.str, typing.Any]]]] = None,
        page_num: typing.Optional[jsii.Number] = None,
        policy_items: typing.Optional[typing.Sequence[builtins.str]] = None,
        profile: typing.Optional[builtins.str] = None,
        results: typing.Optional[typing.Sequence[typing.Union[ApiAtlasDiskBackupShardedClusterSnapshotView, typing.Dict[builtins.str, typing.Any]]]] = None,
        retention_in_days: typing.Optional[jsii.Number] = None,
        snapshot_type: typing.Optional["CfnCloudBackupSnapshotPropsSnapshotType"] = None,
        total_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Returns, takes, and removes Cloud Backup snapshots.

        :param cluster_name: Human-readable label that identifies the cluster.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param description: Human-readable phrase or sentence that explains the purpose of the snapshot. The resource returns this parameter when ``"status": "onDemand"``.
        :param frequency_type: Human-readable label that identifies how often this snapshot triggers.
        :param include_count: Flag that indicates whether the response returns the total number of items (**totalCount**) in the response.
        :param instance_name: Human-readable label that identifies the serverless instance.
        :param items_per_page: Number of items that the response returns per page.
        :param members: List that includes the snapshots and the cloud provider that stores the snapshots. The resource returns this parameter when ``"type" : "SHARDED_CLUSTER"``.
        :param page_num: Number of the page that displays the current set of the total objects that the response returns.
        :param policy_items: List that contains unique identifiers for the policy items.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param results: List of returned documents that MongoDB Cloud provides when completing this request.
        :param retention_in_days: Number of days that MongoDB Cloud should retain the on-demand snapshot. Must be at least **1**
        :param snapshot_type: Human-readable label that identifies when this snapshot triggers.
        :param total_count: Number of documents returned in this response.

        :schema: CfnCloudBackupSnapshotProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a6774a317e39f3d32c18b6b78f8e6e5fb3dc632b6d633d27d87b2e7381a39b9)
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument frequency_type", value=frequency_type, expected_type=type_hints["frequency_type"])
            check_type(argname="argument include_count", value=include_count, expected_type=type_hints["include_count"])
            check_type(argname="argument instance_name", value=instance_name, expected_type=type_hints["instance_name"])
            check_type(argname="argument items_per_page", value=items_per_page, expected_type=type_hints["items_per_page"])
            check_type(argname="argument members", value=members, expected_type=type_hints["members"])
            check_type(argname="argument page_num", value=page_num, expected_type=type_hints["page_num"])
            check_type(argname="argument policy_items", value=policy_items, expected_type=type_hints["policy_items"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument results", value=results, expected_type=type_hints["results"])
            check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
            check_type(argname="argument snapshot_type", value=snapshot_type, expected_type=type_hints["snapshot_type"])
            check_type(argname="argument total_count", value=total_count, expected_type=type_hints["total_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_name": cluster_name,
            "project_id": project_id,
        }
        if description is not None:
            self._values["description"] = description
        if frequency_type is not None:
            self._values["frequency_type"] = frequency_type
        if include_count is not None:
            self._values["include_count"] = include_count
        if instance_name is not None:
            self._values["instance_name"] = instance_name
        if items_per_page is not None:
            self._values["items_per_page"] = items_per_page
        if members is not None:
            self._values["members"] = members
        if page_num is not None:
            self._values["page_num"] = page_num
        if policy_items is not None:
            self._values["policy_items"] = policy_items
        if profile is not None:
            self._values["profile"] = profile
        if results is not None:
            self._values["results"] = results
        if retention_in_days is not None:
            self._values["retention_in_days"] = retention_in_days
        if snapshot_type is not None:
            self._values["snapshot_type"] = snapshot_type
        if total_count is not None:
            self._values["total_count"] = total_count

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''Human-readable label that identifies the cluster.

        :schema: CfnCloudBackupSnapshotProps#ClusterName
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnCloudBackupSnapshotProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Human-readable phrase or sentence that explains the purpose of the snapshot.

        The resource returns this parameter when ``"status": "onDemand"``.

        :schema: CfnCloudBackupSnapshotProps#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def frequency_type(
        self,
    ) -> typing.Optional["CfnCloudBackupSnapshotPropsFrequencyType"]:
        '''Human-readable label that identifies how often this snapshot triggers.

        :schema: CfnCloudBackupSnapshotProps#FrequencyType
        '''
        result = self._values.get("frequency_type")
        return typing.cast(typing.Optional["CfnCloudBackupSnapshotPropsFrequencyType"], result)

    @builtins.property
    def include_count(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether the response returns the total number of items (**totalCount**) in the response.

        :schema: CfnCloudBackupSnapshotProps#IncludeCount
        '''
        result = self._values.get("include_count")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def instance_name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the serverless instance.

        :schema: CfnCloudBackupSnapshotProps#InstanceName
        '''
        result = self._values.get("instance_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def items_per_page(self) -> typing.Optional[jsii.Number]:
        '''Number of items that the response returns per page.

        :schema: CfnCloudBackupSnapshotProps#ItemsPerPage
        '''
        result = self._values.get("items_per_page")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def members(
        self,
    ) -> typing.Optional[typing.List[ApiAtlasDiskBackupShardedClusterSnapshotMemberView]]:
        '''List that includes the snapshots and the cloud provider that stores the snapshots.

        The resource returns this parameter when ``"type" : "SHARDED_CLUSTER"``.

        :schema: CfnCloudBackupSnapshotProps#Members
        '''
        result = self._values.get("members")
        return typing.cast(typing.Optional[typing.List[ApiAtlasDiskBackupShardedClusterSnapshotMemberView]], result)

    @builtins.property
    def page_num(self) -> typing.Optional[jsii.Number]:
        '''Number of the page that displays the current set of the total objects that the response returns.

        :schema: CfnCloudBackupSnapshotProps#PageNum
        '''
        result = self._values.get("page_num")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def policy_items(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List that contains unique identifiers for the policy items.

        :schema: CfnCloudBackupSnapshotProps#PolicyItems
        '''
        result = self._values.get("policy_items")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''The profile is defined in AWS Secret manager.

        See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnCloudBackupSnapshotProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def results(
        self,
    ) -> typing.Optional[typing.List[ApiAtlasDiskBackupShardedClusterSnapshotView]]:
        '''List of returned documents that MongoDB Cloud provides when completing this request.

        :schema: CfnCloudBackupSnapshotProps#Results
        '''
        result = self._values.get("results")
        return typing.cast(typing.Optional[typing.List[ApiAtlasDiskBackupShardedClusterSnapshotView]], result)

    @builtins.property
    def retention_in_days(self) -> typing.Optional[jsii.Number]:
        '''Number of days that MongoDB Cloud should retain the on-demand snapshot.

        Must be at least **1**

        :schema: CfnCloudBackupSnapshotProps#RetentionInDays
        '''
        result = self._values.get("retention_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def snapshot_type(
        self,
    ) -> typing.Optional["CfnCloudBackupSnapshotPropsSnapshotType"]:
        '''Human-readable label that identifies when this snapshot triggers.

        :schema: CfnCloudBackupSnapshotProps#SnapshotType
        '''
        result = self._values.get("snapshot_type")
        return typing.cast(typing.Optional["CfnCloudBackupSnapshotPropsSnapshotType"], result)

    @builtins.property
    def total_count(self) -> typing.Optional[jsii.Number]:
        '''Number of documents returned in this response.

        :schema: CfnCloudBackupSnapshotProps#TotalCount
        '''
        result = self._values.get("total_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudBackupSnapshotProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="awscdk-resources-mongodbatlas.CfnCloudBackupSnapshotPropsFrequencyType"
)
class CfnCloudBackupSnapshotPropsFrequencyType(enum.Enum):
    '''Human-readable label that identifies how often this snapshot triggers.

    :schema: CfnCloudBackupSnapshotPropsFrequencyType
    '''

    HOURLY = "HOURLY"
    '''hourly.'''
    DAILY = "DAILY"
    '''daily.'''
    WEEKLY = "WEEKLY"
    '''weekly.'''
    MONTHLY = "MONTHLY"
    '''monthly.'''


@jsii.enum(
    jsii_type="awscdk-resources-mongodbatlas.CfnCloudBackupSnapshotPropsSnapshotType"
)
class CfnCloudBackupSnapshotPropsSnapshotType(enum.Enum):
    '''Human-readable label that identifies when this snapshot triggers.

    :schema: CfnCloudBackupSnapshotPropsSnapshotType
    '''

    ON_DEMAND = "ON_DEMAND"
    '''onDemand.'''
    SCHEDULED = "SCHEDULED"
    '''scheduled.'''


class CfnCluster(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnCluster",
):
    '''A CloudFormation ``MongoDB::Atlas::Cluster``.

    :cloudformationResource: MongoDB::Atlas::Cluster
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        project_id: builtins.str,
        advanced_settings: typing.Optional[typing.Union["ProcessArgs", typing.Dict[builtins.str, typing.Any]]] = None,
        backup_enabled: typing.Optional[builtins.bool] = None,
        bi_connector: typing.Optional[typing.Union["CfnClusterPropsBiConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_type: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        encryption_at_rest_provider: typing.Optional["CfnClusterPropsEncryptionAtRestProvider"] = None,
        labels: typing.Optional[typing.Sequence[typing.Union["CfnClusterPropsLabels", typing.Dict[builtins.str, typing.Any]]]] = None,
        mongo_db_major_version: typing.Optional[builtins.str] = None,
        paused: typing.Optional[builtins.bool] = None,
        pit_enabled: typing.Optional[builtins.bool] = None,
        profile: typing.Optional[builtins.str] = None,
        replication_specs: typing.Optional[typing.Sequence[typing.Union[AdvancedReplicationSpec, typing.Dict[builtins.str, typing.Any]]]] = None,
        root_cert_type: typing.Optional[builtins.str] = None,
        termination_protection_enabled: typing.Optional[builtins.bool] = None,
        version_release_system: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::Cluster``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: Human-readable label that identifies the advanced cluster.
        :param project_id: Unique identifier of the project the cluster belongs to.
        :param advanced_settings: 
        :param backup_enabled: Flag that indicates whether the cluster can perform backups. If set to true, the cluster can perform backups. You must set this value to true for NVMe clusters. Backup uses Cloud Backups for dedicated clusters and Shared Cluster Backups for tenant clusters. If set to false, the cluster doesn't use backups.
        :param bi_connector: Settings needed to configure the MongoDB Connector for Business Intelligence for this cluster.
        :param cluster_type: Configuration of nodes that comprise the cluster.
        :param disk_size_gb: Storage capacity that the host's root volume possesses expressed in gigabytes. Increase this number to add capacity. MongoDB Cloud requires this parameter if you set replicationSpecs. If you specify a disk size below the minimum (10 GB), this parameter defaults to the minimum disk size value. Storage charge calculations depend on whether you choose the default value or a custom value. The maximum value for disk storage cannot exceed 50 times the maximum RAM for the selected cluster. If you require more storage space, consider upgrading your cluster to a higher tier.
        :param encryption_at_rest_provider: Cloud service provider that manages your customer keys to provide an additional layer of encryption at rest for the cluster. To enable customer key management for encryption at rest, the cluster replicationSpecs[n].regionConfigs[m].{type}Specs.instanceSize setting must be M10 or higher and "backupEnabled" : false or omitted entirely.
        :param labels: Collection of key-value pairs between 1 to 255 characters in length that tag and categorize the cluster. The MongoDB Cloud console doesn't display your labels.
        :param mongo_db_major_version: Major MongoDB version of the cluster. MongoDB Cloud deploys the cluster with the latest stable release of the specified version.
        :param paused: Flag that indicates whether the cluster is paused or not.
        :param pit_enabled: Flag that indicates whether the cluster uses continuous cloud backups.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param replication_specs: List of settings that configure your cluster regions. For Global Clusters, each object in the array represents a zone where your clusters nodes deploy. For non-Global replica sets and sharded clusters, this array has one object representing where your clusters nodes deploy.
        :param root_cert_type: Root Certificate Authority that MongoDB Cloud cluster uses. MongoDB Cloud supports Internet Security Research Group.
        :param termination_protection_enabled: Flag that indicates whether termination protection is enabled on the cluster. If set to true, MongoDB Cloud won't delete the cluster. If set to false, MongoDB Cloud will delete the cluster.
        :param version_release_system: Method by which the cluster maintains the MongoDB versions. If value is CONTINUOUS, you must not specify mongoDBMajorVersion
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bc5e075eab328219b963df173ff94d0a7cace489d75a5b5cb407bb5cc93bd2c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterProps(
            name=name,
            project_id=project_id,
            advanced_settings=advanced_settings,
            backup_enabled=backup_enabled,
            bi_connector=bi_connector,
            cluster_type=cluster_type,
            disk_size_gb=disk_size_gb,
            encryption_at_rest_provider=encryption_at_rest_provider,
            labels=labels,
            mongo_db_major_version=mongo_db_major_version,
            paused=paused,
            pit_enabled=pit_enabled,
            profile=profile,
            replication_specs=replication_specs,
            root_cert_type=root_cert_type,
            termination_protection_enabled=termination_protection_enabled,
            version_release_system=version_release_system,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedDate")
    def attr_created_date(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Cluster.CreatedDate``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedDate"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Cluster.Id``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrMongoDBVersion")
    def attr_mongo_db_version(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Cluster.MongoDBVersion``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrMongoDBVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrStateName")
    def attr_state_name(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Cluster.StateName``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrStateName"))

    @builtins.property
    @jsii.member(jsii_name="connectionStrings")
    def connection_strings(self) -> "ConnectionStrings":
        '''Attribute ``MongoDB::Atlas::Cluster.ConnectionStrings``.'''
        return typing.cast("ConnectionStrings", jsii.get(self, "connectionStrings"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnClusterProps":
        '''Resource props.'''
        return typing.cast("CfnClusterProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "project_id": "projectId",
        "advanced_settings": "advancedSettings",
        "backup_enabled": "backupEnabled",
        "bi_connector": "biConnector",
        "cluster_type": "clusterType",
        "disk_size_gb": "diskSizeGb",
        "encryption_at_rest_provider": "encryptionAtRestProvider",
        "labels": "labels",
        "mongo_db_major_version": "mongoDbMajorVersion",
        "paused": "paused",
        "pit_enabled": "pitEnabled",
        "profile": "profile",
        "replication_specs": "replicationSpecs",
        "root_cert_type": "rootCertType",
        "termination_protection_enabled": "terminationProtectionEnabled",
        "version_release_system": "versionReleaseSystem",
    },
)
class CfnClusterProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        project_id: builtins.str,
        advanced_settings: typing.Optional[typing.Union["ProcessArgs", typing.Dict[builtins.str, typing.Any]]] = None,
        backup_enabled: typing.Optional[builtins.bool] = None,
        bi_connector: typing.Optional[typing.Union["CfnClusterPropsBiConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_type: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        encryption_at_rest_provider: typing.Optional["CfnClusterPropsEncryptionAtRestProvider"] = None,
        labels: typing.Optional[typing.Sequence[typing.Union["CfnClusterPropsLabels", typing.Dict[builtins.str, typing.Any]]]] = None,
        mongo_db_major_version: typing.Optional[builtins.str] = None,
        paused: typing.Optional[builtins.bool] = None,
        pit_enabled: typing.Optional[builtins.bool] = None,
        profile: typing.Optional[builtins.str] = None,
        replication_specs: typing.Optional[typing.Sequence[typing.Union[AdvancedReplicationSpec, typing.Dict[builtins.str, typing.Any]]]] = None,
        root_cert_type: typing.Optional[builtins.str] = None,
        termination_protection_enabled: typing.Optional[builtins.bool] = None,
        version_release_system: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The cluster resource provides access to your cluster configurations.

        The resource lets you create, edit and delete clusters. The resource requires your Project ID.

        :param name: Human-readable label that identifies the advanced cluster.
        :param project_id: Unique identifier of the project the cluster belongs to.
        :param advanced_settings: 
        :param backup_enabled: Flag that indicates whether the cluster can perform backups. If set to true, the cluster can perform backups. You must set this value to true for NVMe clusters. Backup uses Cloud Backups for dedicated clusters and Shared Cluster Backups for tenant clusters. If set to false, the cluster doesn't use backups.
        :param bi_connector: Settings needed to configure the MongoDB Connector for Business Intelligence for this cluster.
        :param cluster_type: Configuration of nodes that comprise the cluster.
        :param disk_size_gb: Storage capacity that the host's root volume possesses expressed in gigabytes. Increase this number to add capacity. MongoDB Cloud requires this parameter if you set replicationSpecs. If you specify a disk size below the minimum (10 GB), this parameter defaults to the minimum disk size value. Storage charge calculations depend on whether you choose the default value or a custom value. The maximum value for disk storage cannot exceed 50 times the maximum RAM for the selected cluster. If you require more storage space, consider upgrading your cluster to a higher tier.
        :param encryption_at_rest_provider: Cloud service provider that manages your customer keys to provide an additional layer of encryption at rest for the cluster. To enable customer key management for encryption at rest, the cluster replicationSpecs[n].regionConfigs[m].{type}Specs.instanceSize setting must be M10 or higher and "backupEnabled" : false or omitted entirely.
        :param labels: Collection of key-value pairs between 1 to 255 characters in length that tag and categorize the cluster. The MongoDB Cloud console doesn't display your labels.
        :param mongo_db_major_version: Major MongoDB version of the cluster. MongoDB Cloud deploys the cluster with the latest stable release of the specified version.
        :param paused: Flag that indicates whether the cluster is paused or not.
        :param pit_enabled: Flag that indicates whether the cluster uses continuous cloud backups.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param replication_specs: List of settings that configure your cluster regions. For Global Clusters, each object in the array represents a zone where your clusters nodes deploy. For non-Global replica sets and sharded clusters, this array has one object representing where your clusters nodes deploy.
        :param root_cert_type: Root Certificate Authority that MongoDB Cloud cluster uses. MongoDB Cloud supports Internet Security Research Group.
        :param termination_protection_enabled: Flag that indicates whether termination protection is enabled on the cluster. If set to true, MongoDB Cloud won't delete the cluster. If set to false, MongoDB Cloud will delete the cluster.
        :param version_release_system: Method by which the cluster maintains the MongoDB versions. If value is CONTINUOUS, you must not specify mongoDBMajorVersion

        :schema: CfnClusterProps
        '''
        if isinstance(advanced_settings, dict):
            advanced_settings = ProcessArgs(**advanced_settings)
        if isinstance(bi_connector, dict):
            bi_connector = CfnClusterPropsBiConnector(**bi_connector)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1bc8a0a1d2a548e1055aa8d1afa8fe110f9e5280af17a15ff7166a8deb02fb8)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument advanced_settings", value=advanced_settings, expected_type=type_hints["advanced_settings"])
            check_type(argname="argument backup_enabled", value=backup_enabled, expected_type=type_hints["backup_enabled"])
            check_type(argname="argument bi_connector", value=bi_connector, expected_type=type_hints["bi_connector"])
            check_type(argname="argument cluster_type", value=cluster_type, expected_type=type_hints["cluster_type"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument encryption_at_rest_provider", value=encryption_at_rest_provider, expected_type=type_hints["encryption_at_rest_provider"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument mongo_db_major_version", value=mongo_db_major_version, expected_type=type_hints["mongo_db_major_version"])
            check_type(argname="argument paused", value=paused, expected_type=type_hints["paused"])
            check_type(argname="argument pit_enabled", value=pit_enabled, expected_type=type_hints["pit_enabled"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument replication_specs", value=replication_specs, expected_type=type_hints["replication_specs"])
            check_type(argname="argument root_cert_type", value=root_cert_type, expected_type=type_hints["root_cert_type"])
            check_type(argname="argument termination_protection_enabled", value=termination_protection_enabled, expected_type=type_hints["termination_protection_enabled"])
            check_type(argname="argument version_release_system", value=version_release_system, expected_type=type_hints["version_release_system"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "project_id": project_id,
        }
        if advanced_settings is not None:
            self._values["advanced_settings"] = advanced_settings
        if backup_enabled is not None:
            self._values["backup_enabled"] = backup_enabled
        if bi_connector is not None:
            self._values["bi_connector"] = bi_connector
        if cluster_type is not None:
            self._values["cluster_type"] = cluster_type
        if disk_size_gb is not None:
            self._values["disk_size_gb"] = disk_size_gb
        if encryption_at_rest_provider is not None:
            self._values["encryption_at_rest_provider"] = encryption_at_rest_provider
        if labels is not None:
            self._values["labels"] = labels
        if mongo_db_major_version is not None:
            self._values["mongo_db_major_version"] = mongo_db_major_version
        if paused is not None:
            self._values["paused"] = paused
        if pit_enabled is not None:
            self._values["pit_enabled"] = pit_enabled
        if profile is not None:
            self._values["profile"] = profile
        if replication_specs is not None:
            self._values["replication_specs"] = replication_specs
        if root_cert_type is not None:
            self._values["root_cert_type"] = root_cert_type
        if termination_protection_enabled is not None:
            self._values["termination_protection_enabled"] = termination_protection_enabled
        if version_release_system is not None:
            self._values["version_release_system"] = version_release_system

    @builtins.property
    def name(self) -> builtins.str:
        '''Human-readable label that identifies the advanced cluster.

        :schema: CfnClusterProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique identifier of the project the cluster belongs to.

        :schema: CfnClusterProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def advanced_settings(self) -> typing.Optional["ProcessArgs"]:
        '''
        :schema: CfnClusterProps#AdvancedSettings
        '''
        result = self._values.get("advanced_settings")
        return typing.cast(typing.Optional["ProcessArgs"], result)

    @builtins.property
    def backup_enabled(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether the cluster can perform backups.

        If set to true, the cluster can perform backups. You must set this value to true for NVMe clusters. Backup uses Cloud Backups for dedicated clusters and Shared Cluster Backups for tenant clusters. If set to false, the cluster doesn't use backups.

        :schema: CfnClusterProps#BackupEnabled
        '''
        result = self._values.get("backup_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def bi_connector(self) -> typing.Optional["CfnClusterPropsBiConnector"]:
        '''Settings needed to configure the MongoDB Connector for Business Intelligence for this cluster.

        :schema: CfnClusterProps#BiConnector
        '''
        result = self._values.get("bi_connector")
        return typing.cast(typing.Optional["CfnClusterPropsBiConnector"], result)

    @builtins.property
    def cluster_type(self) -> typing.Optional[builtins.str]:
        '''Configuration of nodes that comprise the cluster.

        :schema: CfnClusterProps#ClusterType
        '''
        result = self._values.get("cluster_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Storage capacity that the host's root volume possesses expressed in gigabytes.

        Increase this number to add capacity. MongoDB Cloud requires this parameter if you set replicationSpecs. If you specify a disk size below the minimum (10 GB), this parameter defaults to the minimum disk size value. Storage charge calculations depend on whether you choose the default value or a custom value. The maximum value for disk storage cannot exceed 50 times the maximum RAM for the selected cluster. If you require more storage space, consider upgrading your cluster to a higher tier.

        :schema: CfnClusterProps#DiskSizeGB
        '''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def encryption_at_rest_provider(
        self,
    ) -> typing.Optional["CfnClusterPropsEncryptionAtRestProvider"]:
        '''Cloud service provider that manages your customer keys to provide an additional layer of encryption at rest for the cluster.

        To enable customer key management for encryption at rest, the cluster replicationSpecs[n].regionConfigs[m].{type}Specs.instanceSize setting must be M10 or higher and "backupEnabled" : false or omitted entirely.

        :schema: CfnClusterProps#EncryptionAtRestProvider
        '''
        result = self._values.get("encryption_at_rest_provider")
        return typing.cast(typing.Optional["CfnClusterPropsEncryptionAtRestProvider"], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List["CfnClusterPropsLabels"]]:
        '''Collection of key-value pairs between 1 to 255 characters in length that tag and categorize the cluster.

        The MongoDB Cloud console doesn't display your labels.

        :schema: CfnClusterProps#Labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List["CfnClusterPropsLabels"]], result)

    @builtins.property
    def mongo_db_major_version(self) -> typing.Optional[builtins.str]:
        '''Major MongoDB version of the cluster.

        MongoDB Cloud deploys the cluster with the latest stable release of the specified version.

        :schema: CfnClusterProps#MongoDBMajorVersion
        '''
        result = self._values.get("mongo_db_major_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def paused(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether the cluster is paused or not.

        :schema: CfnClusterProps#Paused
        '''
        result = self._values.get("paused")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def pit_enabled(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether the cluster uses continuous cloud backups.

        :schema: CfnClusterProps#PitEnabled
        '''
        result = self._values.get("pit_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.

        :schema: CfnClusterProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_specs(
        self,
    ) -> typing.Optional[typing.List[AdvancedReplicationSpec]]:
        '''List of settings that configure your cluster regions.

        For Global Clusters, each object in the array represents a zone where your clusters nodes deploy. For non-Global replica sets and sharded clusters, this array has one object representing where your clusters nodes deploy.

        :schema: CfnClusterProps#ReplicationSpecs
        '''
        result = self._values.get("replication_specs")
        return typing.cast(typing.Optional[typing.List[AdvancedReplicationSpec]], result)

    @builtins.property
    def root_cert_type(self) -> typing.Optional[builtins.str]:
        '''Root Certificate Authority that MongoDB Cloud cluster uses.

        MongoDB Cloud supports Internet Security Research Group.

        :schema: CfnClusterProps#RootCertType
        '''
        result = self._values.get("root_cert_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def termination_protection_enabled(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether termination protection is enabled on the cluster.

        If set to true, MongoDB Cloud won't delete the cluster. If set to false, MongoDB Cloud will delete the cluster.

        :schema: CfnClusterProps#TerminationProtectionEnabled
        '''
        result = self._values.get("termination_protection_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def version_release_system(self) -> typing.Optional[builtins.str]:
        '''Method by which the cluster maintains the MongoDB versions.

        If value is CONTINUOUS, you must not specify mongoDBMajorVersion

        :schema: CfnClusterProps#VersionReleaseSystem
        '''
        result = self._values.get("version_release_system")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnClusterPropsBiConnector",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "read_preference": "readPreference"},
)
class CfnClusterPropsBiConnector:
    def __init__(
        self,
        *,
        enabled: typing.Optional[builtins.bool] = None,
        read_preference: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Settings needed to configure the MongoDB Connector for Business Intelligence for this cluster.

        :param enabled: Flag that indicates whether MongoDB Connector for Business Intelligence is enabled on the specified cluster.
        :param read_preference: Data source node designated for the MongoDB Connector for Business Intelligence on MongoDB Cloud. The MongoDB Connector for Business Intelligence on MongoDB Cloud reads data from the primary, secondary, or analytics node based on your read preferences. Defaults to ANALYTICS node, or SECONDARY if there are no ANALYTICS nodes. Default: ANALYTICS node, or SECONDARY if there are no ANALYTICS nodes.

        :schema: CfnClusterPropsBiConnector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2b38734bb7f9f3cc0507c7b2e3b52a5a5b9c79037624c47f3dac930e5ce4915)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument read_preference", value=read_preference, expected_type=type_hints["read_preference"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if read_preference is not None:
            self._values["read_preference"] = read_preference

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether MongoDB Connector for Business Intelligence is enabled on the specified cluster.

        :schema: CfnClusterPropsBiConnector#Enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def read_preference(self) -> typing.Optional[builtins.str]:
        '''Data source node designated for the MongoDB Connector for Business Intelligence on MongoDB Cloud.

        The MongoDB Connector for Business Intelligence on MongoDB Cloud reads data from the primary, secondary, or analytics node based on your read preferences. Defaults to ANALYTICS node, or SECONDARY if there are no ANALYTICS nodes.

        :default: ANALYTICS node, or SECONDARY if there are no ANALYTICS nodes.

        :schema: CfnClusterPropsBiConnector#ReadPreference
        '''
        result = self._values.get("read_preference")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterPropsBiConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="awscdk-resources-mongodbatlas.CfnClusterPropsEncryptionAtRestProvider"
)
class CfnClusterPropsEncryptionAtRestProvider(enum.Enum):
    '''Cloud service provider that manages your customer keys to provide an additional layer of encryption at rest for the cluster.

    To enable customer key management for encryption at rest, the cluster replicationSpecs[n].regionConfigs[m].{type}Specs.instanceSize setting must be M10 or higher and "backupEnabled" : false or omitted entirely.

    :schema: CfnClusterPropsEncryptionAtRestProvider
    '''

    AWS = "AWS"
    '''AWS.'''
    GCP = "GCP"
    '''GCP.'''
    AZURE = "AZURE"
    '''AZURE.'''
    NONE = "NONE"
    '''NONE.'''


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnClusterPropsLabels",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class CfnClusterPropsLabels:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: 
        :param value: 

        :schema: CfnClusterPropsLabels
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33e9c067ab8e3a2f0cafd43d6b7169c56c130a69745e771874e75f1649c24441)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnClusterPropsLabels#Key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnClusterPropsLabels#Value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterPropsLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnCustomDbRole(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnCustomDbRole",
):
    '''A CloudFormation ``MongoDB::Atlas::CustomDBRole``.

    :cloudformationResource: MongoDB::Atlas::CustomDBRole
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        project_id: builtins.str,
        role_name: builtins.str,
        actions: typing.Optional[typing.Sequence[typing.Union[Action, typing.Dict[builtins.str, typing.Any]]]] = None,
        inherited_roles: typing.Optional[typing.Sequence[typing.Union["InheritedRole", typing.Dict[builtins.str, typing.Any]]]] = None,
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::CustomDBRole``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param role_name: Human-readable label that identifies the role for the request. This name must be unique for this custom role in this project.
        :param actions: List of the individual privilege actions that the role grants.
        :param inherited_roles: List of the built-in roles that this custom role inherits.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a9ff921996dfab88be67df88221f112970c5268971a7c2a5f35106d61086898)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCustomDbRoleProps(
            project_id=project_id,
            role_name=role_name,
            actions=actions,
            inherited_roles=inherited_roles,
            profile=profile,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnCustomDbRoleProps":
        '''Resource props.'''
        return typing.cast("CfnCustomDbRoleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnCustomDbRoleProps",
    jsii_struct_bases=[],
    name_mapping={
        "project_id": "projectId",
        "role_name": "roleName",
        "actions": "actions",
        "inherited_roles": "inheritedRoles",
        "profile": "profile",
    },
)
class CfnCustomDbRoleProps:
    def __init__(
        self,
        *,
        project_id: builtins.str,
        role_name: builtins.str,
        actions: typing.Optional[typing.Sequence[typing.Union[Action, typing.Dict[builtins.str, typing.Any]]]] = None,
        inherited_roles: typing.Optional[typing.Sequence[typing.Union["InheritedRole", typing.Dict[builtins.str, typing.Any]]]] = None,
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Returns, adds, edits, and removes custom database user privilege roles.

        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param role_name: Human-readable label that identifies the role for the request. This name must be unique for this custom role in this project.
        :param actions: List of the individual privilege actions that the role grants.
        :param inherited_roles: List of the built-in roles that this custom role inherits.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnCustomDbRoleProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cfe2387200229b4088642580d5165b7db0ad0d54a7c635a501846f530e63ef8)
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument inherited_roles", value=inherited_roles, expected_type=type_hints["inherited_roles"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_id": project_id,
            "role_name": role_name,
        }
        if actions is not None:
            self._values["actions"] = actions
        if inherited_roles is not None:
            self._values["inherited_roles"] = inherited_roles
        if profile is not None:
            self._values["profile"] = profile

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnCustomDbRoleProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_name(self) -> builtins.str:
        '''Human-readable label that identifies the role for the request.

        This name must be unique for this custom role in this project.

        :schema: CfnCustomDbRoleProps#RoleName
        '''
        result = self._values.get("role_name")
        assert result is not None, "Required property 'role_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def actions(self) -> typing.Optional[typing.List[Action]]:
        '''List of the individual privilege actions that the role grants.

        :schema: CfnCustomDbRoleProps#Actions
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[typing.List[Action]], result)

    @builtins.property
    def inherited_roles(self) -> typing.Optional[typing.List["InheritedRole"]]:
        '''List of the built-in roles that this custom role inherits.

        :schema: CfnCustomDbRoleProps#InheritedRoles
        '''
        result = self._values.get("inherited_roles")
        return typing.cast(typing.Optional[typing.List["InheritedRole"]], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''The profile is defined in AWS Secret manager.

        See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnCustomDbRoleProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCustomDbRoleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnCustomDnsConfigurationClusterAws(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnCustomDnsConfigurationClusterAws",
):
    '''A CloudFormation ``MongoDB::Atlas::CustomDnsConfigurationClusterAws``.

    :cloudformationResource: MongoDB::Atlas::CustomDnsConfigurationClusterAws
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        project_id: builtins.str,
        enabled: typing.Optional[builtins.bool] = None,
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::CustomDnsConfigurationClusterAws``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param enabled: Flag that indicates whether the project's clusters deployed to Amazon Web Services (AWS) use a custom Domain Name System (DNS).
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0f88706de82c968034f862c67a677a4d3e6a276cc00f97836cc0d94795fa79f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCustomDnsConfigurationClusterAwsProps(
            project_id=project_id, enabled=enabled, profile=profile
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnCustomDnsConfigurationClusterAwsProps":
        '''Resource props.'''
        return typing.cast("CfnCustomDnsConfigurationClusterAwsProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnCustomDnsConfigurationClusterAwsProps",
    jsii_struct_bases=[],
    name_mapping={
        "project_id": "projectId",
        "enabled": "enabled",
        "profile": "profile",
    },
)
class CfnCustomDnsConfigurationClusterAwsProps:
    def __init__(
        self,
        *,
        project_id: builtins.str,
        enabled: typing.Optional[builtins.bool] = None,
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''An example resource schema demonstrating some basic constructs and validation rules.

        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param enabled: Flag that indicates whether the project's clusters deployed to Amazon Web Services (AWS) use a custom Domain Name System (DNS).
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnCustomDnsConfigurationClusterAwsProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbd42d5139b917f1ba7ff5f24d5756e205ae53489e0d73e76fb1959cb88b5e6a)
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_id": project_id,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if profile is not None:
            self._values["profile"] = profile

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnCustomDnsConfigurationClusterAwsProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether the project's clusters deployed to Amazon Web Services (AWS) use a custom Domain Name System (DNS).

        :schema: CfnCustomDnsConfigurationClusterAwsProps#Enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''The profile is defined in AWS Secret manager.

        See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnCustomDnsConfigurationClusterAwsProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCustomDnsConfigurationClusterAwsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnDataLakes(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnDataLakes",
):
    '''A CloudFormation ``MongoDB::Atlas::DataLakes``.

    :cloudformationResource: MongoDB::Atlas::DataLakes
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cloud_provider_config: typing.Optional[typing.Union["DataLakeCloudProviderConfigView", typing.Dict[builtins.str, typing.Any]]] = None,
        data_process_region: typing.Optional[typing.Union["DataLakeDataProcessRegionView", typing.Dict[builtins.str, typing.Any]]] = None,
        end_date: typing.Optional[jsii.Number] = None,
        profile: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        skip_role_validation: typing.Optional[builtins.bool] = None,
        storage: typing.Optional[typing.Union["DataLakeStorageView", typing.Dict[builtins.str, typing.Any]]] = None,
        tenant_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::DataLakes``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cloud_provider_config: Cloud provider linked to this data lake.
        :param data_process_region: Information about the cloud provider region to which the data lake routes client connections. MongoDB Cloud supports AWS only.
        :param end_date: Timestamp that specifies the end point for the range of log messages to download. MongoDB Cloud expresses this timestamp in the number of seconds that have elapsed since the UNIX epoch.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param skip_role_validation: Flag that indicates whether this request should check if the requesting IAM role can read from the S3 bucket. AWS checks if the role can list the objects in the bucket before writing to it. Some IAM roles only need write permissions. This flag allows you to skip that check.
        :param storage: Configuration information for each data store and its mapping to MongoDB Cloud databases.
        :param tenant_name: Human-readable label that identifies the Federated Database to remove.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__664ca025502c6690a88bf9d84e9fa20afda504cf270dfbe1bd90611bbd258a85)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataLakesProps(
            cloud_provider_config=cloud_provider_config,
            data_process_region=data_process_region,
            end_date=end_date,
            profile=profile,
            project_id=project_id,
            skip_role_validation=skip_role_validation,
            storage=storage,
            tenant_name=tenant_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrHostnames")
    def attr_hostnames(self) -> typing.List[builtins.str]:
        '''Attribute ``MongoDB::Atlas::DataLakes.Hostnames``.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrHostnames"))

    @builtins.property
    @jsii.member(jsii_name="attrStartDate")
    def attr_start_date(self) -> jsii.Number:
        '''Attribute ``MongoDB::Atlas::DataLakes.StartDate``.'''
        return typing.cast(jsii.Number, jsii.get(self, "attrStartDate"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::DataLakes.State``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnDataLakesProps":
        '''Resource props.'''
        return typing.cast("CfnDataLakesProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnDataLakesProps",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_provider_config": "cloudProviderConfig",
        "data_process_region": "dataProcessRegion",
        "end_date": "endDate",
        "profile": "profile",
        "project_id": "projectId",
        "skip_role_validation": "skipRoleValidation",
        "storage": "storage",
        "tenant_name": "tenantName",
    },
)
class CfnDataLakesProps:
    def __init__(
        self,
        *,
        cloud_provider_config: typing.Optional[typing.Union["DataLakeCloudProviderConfigView", typing.Dict[builtins.str, typing.Any]]] = None,
        data_process_region: typing.Optional[typing.Union["DataLakeDataProcessRegionView", typing.Dict[builtins.str, typing.Any]]] = None,
        end_date: typing.Optional[jsii.Number] = None,
        profile: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        skip_role_validation: typing.Optional[builtins.bool] = None,
        storage: typing.Optional[typing.Union["DataLakeStorageView", typing.Dict[builtins.str, typing.Any]]] = None,
        tenant_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Returns, adds, edits, and removes Federated Database Instances.

        :param cloud_provider_config: Cloud provider linked to this data lake.
        :param data_process_region: Information about the cloud provider region to which the data lake routes client connections. MongoDB Cloud supports AWS only.
        :param end_date: Timestamp that specifies the end point for the range of log messages to download. MongoDB Cloud expresses this timestamp in the number of seconds that have elapsed since the UNIX epoch.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param skip_role_validation: Flag that indicates whether this request should check if the requesting IAM role can read from the S3 bucket. AWS checks if the role can list the objects in the bucket before writing to it. Some IAM roles only need write permissions. This flag allows you to skip that check.
        :param storage: Configuration information for each data store and its mapping to MongoDB Cloud databases.
        :param tenant_name: Human-readable label that identifies the Federated Database to remove.

        :schema: CfnDataLakesProps
        '''
        if isinstance(cloud_provider_config, dict):
            cloud_provider_config = DataLakeCloudProviderConfigView(**cloud_provider_config)
        if isinstance(data_process_region, dict):
            data_process_region = DataLakeDataProcessRegionView(**data_process_region)
        if isinstance(storage, dict):
            storage = DataLakeStorageView(**storage)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06a68589750feeb65d350ba54a786ffc318e6300dc2af852a16fbfb9796ed9f4)
            check_type(argname="argument cloud_provider_config", value=cloud_provider_config, expected_type=type_hints["cloud_provider_config"])
            check_type(argname="argument data_process_region", value=data_process_region, expected_type=type_hints["data_process_region"])
            check_type(argname="argument end_date", value=end_date, expected_type=type_hints["end_date"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument skip_role_validation", value=skip_role_validation, expected_type=type_hints["skip_role_validation"])
            check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
            check_type(argname="argument tenant_name", value=tenant_name, expected_type=type_hints["tenant_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cloud_provider_config is not None:
            self._values["cloud_provider_config"] = cloud_provider_config
        if data_process_region is not None:
            self._values["data_process_region"] = data_process_region
        if end_date is not None:
            self._values["end_date"] = end_date
        if profile is not None:
            self._values["profile"] = profile
        if project_id is not None:
            self._values["project_id"] = project_id
        if skip_role_validation is not None:
            self._values["skip_role_validation"] = skip_role_validation
        if storage is not None:
            self._values["storage"] = storage
        if tenant_name is not None:
            self._values["tenant_name"] = tenant_name

    @builtins.property
    def cloud_provider_config(
        self,
    ) -> typing.Optional["DataLakeCloudProviderConfigView"]:
        '''Cloud provider linked to this data lake.

        :schema: CfnDataLakesProps#CloudProviderConfig
        '''
        result = self._values.get("cloud_provider_config")
        return typing.cast(typing.Optional["DataLakeCloudProviderConfigView"], result)

    @builtins.property
    def data_process_region(self) -> typing.Optional["DataLakeDataProcessRegionView"]:
        '''Information about the cloud provider region to which the data lake routes client connections.

        MongoDB Cloud supports AWS only.

        :schema: CfnDataLakesProps#DataProcessRegion
        '''
        result = self._values.get("data_process_region")
        return typing.cast(typing.Optional["DataLakeDataProcessRegionView"], result)

    @builtins.property
    def end_date(self) -> typing.Optional[jsii.Number]:
        '''Timestamp that specifies the end point for the range of log messages to download.

        MongoDB Cloud expresses this timestamp in the number of seconds that have elapsed since the UNIX epoch.

        :schema: CfnDataLakesProps#EndDate
        '''
        result = self._values.get("end_date")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''The profile is defined in AWS Secret manager.

        See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnDataLakesProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnDataLakesProps#ProjectId
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_role_validation(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether this request should check if the requesting IAM role can read from the S3 bucket.

        AWS checks if the role can list the objects in the bucket before writing to it. Some IAM roles only need write permissions. This flag allows you to skip that check.

        :schema: CfnDataLakesProps#SkipRoleValidation
        '''
        result = self._values.get("skip_role_validation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def storage(self) -> typing.Optional["DataLakeStorageView"]:
        '''Configuration information for each data store and its mapping to MongoDB Cloud databases.

        :schema: CfnDataLakesProps#Storage
        '''
        result = self._values.get("storage")
        return typing.cast(typing.Optional["DataLakeStorageView"], result)

    @builtins.property
    def tenant_name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the Federated Database to remove.

        :schema: CfnDataLakesProps#TenantName
        '''
        result = self._values.get("tenant_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataLakesProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnDatabaseUser(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnDatabaseUser",
):
    '''A CloudFormation ``MongoDB::Atlas::DatabaseUser``.

    :cloudformationResource: MongoDB::Atlas::DatabaseUser
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        database_name: builtins.str,
        project_id: builtins.str,
        roles: typing.Sequence[typing.Union["RoleDefinition", typing.Dict[builtins.str, typing.Any]]],
        username: builtins.str,
        awsiam_type: typing.Optional["CfnDatabaseUserPropsAwsiamType"] = None,
        delete_after_date: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Sequence[typing.Union["LabelDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        ldap_auth_type: typing.Optional["CfnDatabaseUserPropsLdapAuthType"] = None,
        password: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        scopes: typing.Optional[typing.Sequence[typing.Union["ScopeDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        x509_type: typing.Optional["CfnDatabaseUserPropsX509Type"] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::DatabaseUser``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param database_name: MongoDB database against which the MongoDB database user authenticates. MongoDB database users must provide both a username and authentication database to log into MongoDB. Default value is ``admin``.
        :param project_id: Unique 24-hexadecimal digit string that identifies your Atlas Project.
        :param roles: List that provides the pairings of one role with one applicable database.
        :param username: Human-readable label that represents the user that authenticates to MongoDB. The format of this label depends on the method of authentication. This will be USER_ARN or ROLE_ARN if AWSIAMType is USER or ROLE. Refer https://www.mongodb.com/docs/atlas/reference/api-resources-spec/#tag/Database-Users/operation/createDatabaseUser for details.
        :param awsiam_type: Human-readable label that indicates whether the new database user authenticates with the Amazon Web Services (AWS) Identity and Access Management (IAM) credentials associated with the user or the user's role. Default value is ``NONE``.
        :param delete_after_date: Date and time when MongoDB Cloud deletes the user. This parameter expresses its value in the ISO 8601 timestamp format in UTC and can include the time zone designation. You must specify a future date that falls within one week of making the Application Programming Interface (API) request.
        :param labels: List that contains the key-value pairs for tagging and categorizing the MongoDB database user. The labels that you define do not appear in the console.
        :param ldap_auth_type: Method by which the provided username is authenticated. Default value is ``NONE``.
        :param password: The user’s password. This field is not included in the entity returned from the server.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided ``default`` is used.
        :param scopes: List that contains clusters and MongoDB Atlas Data Lakes that this database user can access. If omitted, MongoDB Cloud grants the database user access to all the clusters and MongoDB Atlas Data Lakes in the project.
        :param x509_type: Method that briefs who owns the certificate provided. Default value is ``NONE``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8406f4354e90478b4bbd52a6ceff6a23c4965a2fc56673977d90dbd7ab8a3a40)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDatabaseUserProps(
            database_name=database_name,
            project_id=project_id,
            roles=roles,
            username=username,
            awsiam_type=awsiam_type,
            delete_after_date=delete_after_date,
            labels=labels,
            ldap_auth_type=ldap_auth_type,
            password=password,
            profile=profile,
            scopes=scopes,
            x509_type=x509_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrUserCFNIdentifier")
    def attr_user_cfn_identifier(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::DatabaseUser.UserCFNIdentifier``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrUserCFNIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnDatabaseUserProps":
        '''Resource props.'''
        return typing.cast("CfnDatabaseUserProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnDatabaseUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "project_id": "projectId",
        "roles": "roles",
        "username": "username",
        "awsiam_type": "awsiamType",
        "delete_after_date": "deleteAfterDate",
        "labels": "labels",
        "ldap_auth_type": "ldapAuthType",
        "password": "password",
        "profile": "profile",
        "scopes": "scopes",
        "x509_type": "x509Type",
    },
)
class CfnDatabaseUserProps:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        project_id: builtins.str,
        roles: typing.Sequence[typing.Union["RoleDefinition", typing.Dict[builtins.str, typing.Any]]],
        username: builtins.str,
        awsiam_type: typing.Optional["CfnDatabaseUserPropsAwsiamType"] = None,
        delete_after_date: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Sequence[typing.Union["LabelDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        ldap_auth_type: typing.Optional["CfnDatabaseUserPropsLdapAuthType"] = None,
        password: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        scopes: typing.Optional[typing.Sequence[typing.Union["ScopeDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        x509_type: typing.Optional["CfnDatabaseUserPropsX509Type"] = None,
    ) -> None:
        '''Returns, adds, edits, and removes database users.

        :param database_name: MongoDB database against which the MongoDB database user authenticates. MongoDB database users must provide both a username and authentication database to log into MongoDB. Default value is ``admin``.
        :param project_id: Unique 24-hexadecimal digit string that identifies your Atlas Project.
        :param roles: List that provides the pairings of one role with one applicable database.
        :param username: Human-readable label that represents the user that authenticates to MongoDB. The format of this label depends on the method of authentication. This will be USER_ARN or ROLE_ARN if AWSIAMType is USER or ROLE. Refer https://www.mongodb.com/docs/atlas/reference/api-resources-spec/#tag/Database-Users/operation/createDatabaseUser for details.
        :param awsiam_type: Human-readable label that indicates whether the new database user authenticates with the Amazon Web Services (AWS) Identity and Access Management (IAM) credentials associated with the user or the user's role. Default value is ``NONE``.
        :param delete_after_date: Date and time when MongoDB Cloud deletes the user. This parameter expresses its value in the ISO 8601 timestamp format in UTC and can include the time zone designation. You must specify a future date that falls within one week of making the Application Programming Interface (API) request.
        :param labels: List that contains the key-value pairs for tagging and categorizing the MongoDB database user. The labels that you define do not appear in the console.
        :param ldap_auth_type: Method by which the provided username is authenticated. Default value is ``NONE``.
        :param password: The user’s password. This field is not included in the entity returned from the server.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided ``default`` is used.
        :param scopes: List that contains clusters and MongoDB Atlas Data Lakes that this database user can access. If omitted, MongoDB Cloud grants the database user access to all the clusters and MongoDB Atlas Data Lakes in the project.
        :param x509_type: Method that briefs who owns the certificate provided. Default value is ``NONE``.

        :schema: CfnDatabaseUserProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b56b500507bd311917a33a9fbfa2f5edb8bae24b9fbd3dc38b4055df3f7c04c4)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument awsiam_type", value=awsiam_type, expected_type=type_hints["awsiam_type"])
            check_type(argname="argument delete_after_date", value=delete_after_date, expected_type=type_hints["delete_after_date"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument ldap_auth_type", value=ldap_auth_type, expected_type=type_hints["ldap_auth_type"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument scopes", value=scopes, expected_type=type_hints["scopes"])
            check_type(argname="argument x509_type", value=x509_type, expected_type=type_hints["x509_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
            "project_id": project_id,
            "roles": roles,
            "username": username,
        }
        if awsiam_type is not None:
            self._values["awsiam_type"] = awsiam_type
        if delete_after_date is not None:
            self._values["delete_after_date"] = delete_after_date
        if labels is not None:
            self._values["labels"] = labels
        if ldap_auth_type is not None:
            self._values["ldap_auth_type"] = ldap_auth_type
        if password is not None:
            self._values["password"] = password
        if profile is not None:
            self._values["profile"] = profile
        if scopes is not None:
            self._values["scopes"] = scopes
        if x509_type is not None:
            self._values["x509_type"] = x509_type

    @builtins.property
    def database_name(self) -> builtins.str:
        '''MongoDB database against which the MongoDB database user authenticates.

        MongoDB database users must provide both a username and authentication database to log into MongoDB.  Default value is ``admin``.

        :schema: CfnDatabaseUserProps#DatabaseName
        '''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies your Atlas Project.

        :schema: CfnDatabaseUserProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def roles(self) -> typing.List["RoleDefinition"]:
        '''List that provides the pairings of one role with one applicable database.

        :schema: CfnDatabaseUserProps#Roles
        '''
        result = self._values.get("roles")
        assert result is not None, "Required property 'roles' is missing"
        return typing.cast(typing.List["RoleDefinition"], result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Human-readable label that represents the user that authenticates to MongoDB.

        The format of this label depends on the method of authentication. This will be USER_ARN or ROLE_ARN if AWSIAMType is USER or ROLE. Refer https://www.mongodb.com/docs/atlas/reference/api-resources-spec/#tag/Database-Users/operation/createDatabaseUser for details.

        :schema: CfnDatabaseUserProps#Username
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def awsiam_type(self) -> typing.Optional["CfnDatabaseUserPropsAwsiamType"]:
        '''Human-readable label that indicates whether the new database user authenticates with the Amazon Web Services (AWS) Identity and Access Management (IAM) credentials associated with the user or the user's role.

        Default value is ``NONE``.

        :schema: CfnDatabaseUserProps#AWSIAMType
        '''
        result = self._values.get("awsiam_type")
        return typing.cast(typing.Optional["CfnDatabaseUserPropsAwsiamType"], result)

    @builtins.property
    def delete_after_date(self) -> typing.Optional[builtins.str]:
        '''Date and time when MongoDB Cloud deletes the user.

        This parameter expresses its value in the ISO 8601 timestamp format in UTC and can include the time zone designation. You must specify a future date that falls within one week of making the Application Programming Interface (API) request.

        :schema: CfnDatabaseUserProps#DeleteAfterDate
        '''
        result = self._values.get("delete_after_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List["LabelDefinition"]]:
        '''List that contains the key-value pairs for tagging and categorizing the MongoDB database user.

        The labels that you define do not appear in the console.

        :schema: CfnDatabaseUserProps#Labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List["LabelDefinition"]], result)

    @builtins.property
    def ldap_auth_type(self) -> typing.Optional["CfnDatabaseUserPropsLdapAuthType"]:
        '''Method by which the provided username is authenticated.

        Default value is ``NONE``.

        :schema: CfnDatabaseUserProps#LdapAuthType
        '''
        result = self._values.get("ldap_auth_type")
        return typing.cast(typing.Optional["CfnDatabaseUserPropsLdapAuthType"], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The user’s password.

        This field is not included in the entity returned from the server.

        :schema: CfnDatabaseUserProps#Password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided ``default`` is used.

        :schema: CfnDatabaseUserProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scopes(self) -> typing.Optional[typing.List["ScopeDefinition"]]:
        '''List that contains clusters and MongoDB Atlas Data Lakes that this database user can access.

        If omitted, MongoDB Cloud grants the database user access to all the clusters and MongoDB Atlas Data Lakes in the project.

        :schema: CfnDatabaseUserProps#Scopes
        '''
        result = self._values.get("scopes")
        return typing.cast(typing.Optional[typing.List["ScopeDefinition"]], result)

    @builtins.property
    def x509_type(self) -> typing.Optional["CfnDatabaseUserPropsX509Type"]:
        '''Method that briefs who owns the certificate provided.

        Default value is ``NONE``.

        :schema: CfnDatabaseUserProps#X509Type
        '''
        result = self._values.get("x509_type")
        return typing.cast(typing.Optional["CfnDatabaseUserPropsX509Type"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatabaseUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.CfnDatabaseUserPropsAwsiamType")
class CfnDatabaseUserPropsAwsiamType(enum.Enum):
    '''Human-readable label that indicates whether the new database user authenticates with the Amazon Web Services (AWS) Identity and Access Management (IAM) credentials associated with the user or the user's role.

    :schema: CfnDatabaseUserPropsAwsiamType
    '''

    NONE = "NONE"
    '''NONE.'''
    USER = "USER"
    '''USER.'''
    ROLE = "ROLE"
    '''ROLE.'''


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.CfnDatabaseUserPropsLdapAuthType")
class CfnDatabaseUserPropsLdapAuthType(enum.Enum):
    '''Method by which the provided username is authenticated.

    Default value is ``NONE``.

    :schema: CfnDatabaseUserPropsLdapAuthType
    '''

    NONE = "NONE"
    '''NONE.'''
    USER = "USER"
    '''USER.'''
    GROUP = "GROUP"
    '''GROUP.'''


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.CfnDatabaseUserPropsX509Type")
class CfnDatabaseUserPropsX509Type(enum.Enum):
    '''Method that briefs who owns the certificate provided.

    Default value is ``NONE``.

    :schema: CfnDatabaseUserPropsX509Type
    '''

    NONE = "NONE"
    '''NONE.'''
    MANAGED = "MANAGED"
    '''MANAGED.'''
    CUSTOMER = "CUSTOMER"
    '''CUSTOMER.'''


class CfnEncryptionAtRest(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnEncryptionAtRest",
):
    '''A CloudFormation ``MongoDB::Atlas::EncryptionAtRest``.

    :cloudformationResource: MongoDB::Atlas::EncryptionAtRest
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        aws_kms: typing.Union[AwsKmsConfiguration, typing.Dict[builtins.str, typing.Any]],
        project_id: builtins.str,
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::EncryptionAtRest``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param aws_kms: 
        :param project_id: Unique identifier of the Atlas project to which the user belongs.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c180750d8057b1363f69c973f8fccb55c27fd802c69977654436226f96f5a18)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEncryptionAtRestProps(
            aws_kms=aws_kms, project_id=project_id, profile=profile
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::EncryptionAtRest.Id``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnEncryptionAtRestProps":
        '''Resource props.'''
        return typing.cast("CfnEncryptionAtRestProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnEncryptionAtRestProps",
    jsii_struct_bases=[],
    name_mapping={
        "aws_kms": "awsKms",
        "project_id": "projectId",
        "profile": "profile",
    },
)
class CfnEncryptionAtRestProps:
    def __init__(
        self,
        *,
        aws_kms: typing.Union[AwsKmsConfiguration, typing.Dict[builtins.str, typing.Any]],
        project_id: builtins.str,
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Returns and edits the Encryption at Rest using Customer Key Management configuration.

        :param aws_kms: 
        :param project_id: Unique identifier of the Atlas project to which the user belongs.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnEncryptionAtRestProps
        '''
        if isinstance(aws_kms, dict):
            aws_kms = AwsKmsConfiguration(**aws_kms)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd94222cd7a5c427770775c9b15177a7efcab7ada166391b9cbe1c543d5c9b3c)
            check_type(argname="argument aws_kms", value=aws_kms, expected_type=type_hints["aws_kms"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_kms": aws_kms,
            "project_id": project_id,
        }
        if profile is not None:
            self._values["profile"] = profile

    @builtins.property
    def aws_kms(self) -> AwsKmsConfiguration:
        '''
        :schema: CfnEncryptionAtRestProps#AwsKms
        '''
        result = self._values.get("aws_kms")
        assert result is not None, "Required property 'aws_kms' is missing"
        return typing.cast(AwsKmsConfiguration, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique identifier of the Atlas project to which the user belongs.

        :schema: CfnEncryptionAtRestProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''The profile is defined in AWS Secret manager.

        See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnEncryptionAtRestProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEncryptionAtRestProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnFederatedSettingsOrgRoleMapping(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnFederatedSettingsOrgRoleMapping",
):
    '''A CloudFormation ``MongoDB::Atlas::FederatedSettingsOrgRoleMapping``.

    :cloudformationResource: MongoDB::Atlas::FederatedSettingsOrgRoleMapping
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        external_group_name: builtins.str,
        federation_settings_id: builtins.str,
        org_id: builtins.str,
        role_assignments: typing.Sequence[typing.Union["RoleAssignment", typing.Dict[builtins.str, typing.Any]]],
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::FederatedSettingsOrgRoleMapping``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param external_group_name: Unique human-readable label that identifies the identity provider group to whichthis role mapping applies.
        :param federation_settings_id: Unique 24-hexadecimal digit string that identifies your federation.
        :param org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects.
        :param role_assignments: Atlas roles and the unique identifiers of the groups and organizations associated with each role.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f167859158100888bcb0726ac79d0893ccc2bebaebcff902410f2693dc55077)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFederatedSettingsOrgRoleMappingProps(
            external_group_name=external_group_name,
            federation_settings_id=federation_settings_id,
            org_id=org_id,
            role_assignments=role_assignments,
            profile=profile,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::FederatedSettingsOrgRoleMapping.Id``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnFederatedSettingsOrgRoleMappingProps":
        '''Resource props.'''
        return typing.cast("CfnFederatedSettingsOrgRoleMappingProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnFederatedSettingsOrgRoleMappingProps",
    jsii_struct_bases=[],
    name_mapping={
        "external_group_name": "externalGroupName",
        "federation_settings_id": "federationSettingsId",
        "org_id": "orgId",
        "role_assignments": "roleAssignments",
        "profile": "profile",
    },
)
class CfnFederatedSettingsOrgRoleMappingProps:
    def __init__(
        self,
        *,
        external_group_name: builtins.str,
        federation_settings_id: builtins.str,
        org_id: builtins.str,
        role_assignments: typing.Sequence[typing.Union["RoleAssignment", typing.Dict[builtins.str, typing.Any]]],
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Returns, adds, edits, and removes federation-related features such as role mappings and connected organization configurations.

        :param external_group_name: Unique human-readable label that identifies the identity provider group to whichthis role mapping applies.
        :param federation_settings_id: Unique 24-hexadecimal digit string that identifies your federation.
        :param org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects.
        :param role_assignments: Atlas roles and the unique identifiers of the groups and organizations associated with each role.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnFederatedSettingsOrgRoleMappingProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c3839f13da84cc0789dea989620ab43857742ae7373d4038e286df38f05a3a1)
            check_type(argname="argument external_group_name", value=external_group_name, expected_type=type_hints["external_group_name"])
            check_type(argname="argument federation_settings_id", value=federation_settings_id, expected_type=type_hints["federation_settings_id"])
            check_type(argname="argument org_id", value=org_id, expected_type=type_hints["org_id"])
            check_type(argname="argument role_assignments", value=role_assignments, expected_type=type_hints["role_assignments"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "external_group_name": external_group_name,
            "federation_settings_id": federation_settings_id,
            "org_id": org_id,
            "role_assignments": role_assignments,
        }
        if profile is not None:
            self._values["profile"] = profile

    @builtins.property
    def external_group_name(self) -> builtins.str:
        '''Unique human-readable label that identifies the identity provider group to whichthis role mapping applies.

        :schema: CfnFederatedSettingsOrgRoleMappingProps#ExternalGroupName
        '''
        result = self._values.get("external_group_name")
        assert result is not None, "Required property 'external_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def federation_settings_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies your federation.

        :schema: CfnFederatedSettingsOrgRoleMappingProps#FederationSettingsId
        '''
        result = self._values.get("federation_settings_id")
        assert result is not None, "Required property 'federation_settings_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def org_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies the organization that contains your projects.

        :schema: CfnFederatedSettingsOrgRoleMappingProps#OrgId
        '''
        result = self._values.get("org_id")
        assert result is not None, "Required property 'org_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_assignments(self) -> typing.List["RoleAssignment"]:
        '''Atlas roles and the unique identifiers of the groups and organizations associated with each role.

        :schema: CfnFederatedSettingsOrgRoleMappingProps#RoleAssignments
        '''
        result = self._values.get("role_assignments")
        assert result is not None, "Required property 'role_assignments' is missing"
        return typing.cast(typing.List["RoleAssignment"], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''The profile is defined in AWS Secret manager.

        See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnFederatedSettingsOrgRoleMappingProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFederatedSettingsOrgRoleMappingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnGlobalClusterConfig(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnGlobalClusterConfig",
):
    '''A CloudFormation ``MongoDB::Atlas::GlobalClusterConfig``.

    :cloudformationResource: MongoDB::Atlas::GlobalClusterConfig
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster_name: builtins.str,
        project_id: builtins.str,
        custom_zone_mappings: typing.Optional[typing.Sequence[typing.Union["ZoneMapping", typing.Dict[builtins.str, typing.Any]]]] = None,
        managed_namespaces: typing.Optional[typing.Sequence[typing.Union["ManagedNamespace", typing.Dict[builtins.str, typing.Any]]]] = None,
        profile: typing.Optional[builtins.str] = None,
        remove_all_zone_mapping: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::GlobalClusterConfig``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cluster_name: The name of the Atlas cluster that contains the snapshots you want to retrieve.
        :param project_id: The unique identifier of the project for the Atlas cluster.
        :param custom_zone_mappings: List that contains comma-separated key value pairs to map zones to geographic regions. These pairs map an ISO 3166-1a2 location code, with an ISO 3166-2 subdivision code when possible, to the human-readable label for the desired custom zone. MongoDB Cloud maps the ISO 3166-1a2 code to the nearest geographical zone by default. Include this parameter to override the default mappings. This parameter returns an empty object if no custom zones exist.
        :param managed_namespaces: List that contains comma-separated key value pairs to map zones to geographic regions. These pairs map an ISO 3166-1a2 location code, with an ISO 3166-2 subdivision code when possible, to the human-readable label for the desired custom zone. MongoDB Cloud maps the ISO 3166-1a2 code to the nearest geographical zone by default. Include this parameter to override the default mappings. This parameter returns an empty object if no custom zones exist.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param remove_all_zone_mapping: Flag that indicates whether all custom zone mapping to be deleted during delete.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2437c69bb17314d4c89174a53a50594fb17919e17b6dc40fc3df6c906430422)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGlobalClusterConfigProps(
            cluster_name=cluster_name,
            project_id=project_id,
            custom_zone_mappings=custom_zone_mappings,
            managed_namespaces=managed_namespaces,
            profile=profile,
            remove_all_zone_mapping=remove_all_zone_mapping,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnGlobalClusterConfigProps":
        '''Resource props.'''
        return typing.cast("CfnGlobalClusterConfigProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnGlobalClusterConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_name": "clusterName",
        "project_id": "projectId",
        "custom_zone_mappings": "customZoneMappings",
        "managed_namespaces": "managedNamespaces",
        "profile": "profile",
        "remove_all_zone_mapping": "removeAllZoneMapping",
    },
)
class CfnGlobalClusterConfigProps:
    def __init__(
        self,
        *,
        cluster_name: builtins.str,
        project_id: builtins.str,
        custom_zone_mappings: typing.Optional[typing.Sequence[typing.Union["ZoneMapping", typing.Dict[builtins.str, typing.Any]]]] = None,
        managed_namespaces: typing.Optional[typing.Sequence[typing.Union["ManagedNamespace", typing.Dict[builtins.str, typing.Any]]]] = None,
        profile: typing.Optional[builtins.str] = None,
        remove_all_zone_mapping: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Returns, adds, and removes Global Cluster managed namespaces and custom zone mappings.

        :param cluster_name: The name of the Atlas cluster that contains the snapshots you want to retrieve.
        :param project_id: The unique identifier of the project for the Atlas cluster.
        :param custom_zone_mappings: List that contains comma-separated key value pairs to map zones to geographic regions. These pairs map an ISO 3166-1a2 location code, with an ISO 3166-2 subdivision code when possible, to the human-readable label for the desired custom zone. MongoDB Cloud maps the ISO 3166-1a2 code to the nearest geographical zone by default. Include this parameter to override the default mappings. This parameter returns an empty object if no custom zones exist.
        :param managed_namespaces: List that contains comma-separated key value pairs to map zones to geographic regions. These pairs map an ISO 3166-1a2 location code, with an ISO 3166-2 subdivision code when possible, to the human-readable label for the desired custom zone. MongoDB Cloud maps the ISO 3166-1a2 code to the nearest geographical zone by default. Include this parameter to override the default mappings. This parameter returns an empty object if no custom zones exist.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param remove_all_zone_mapping: Flag that indicates whether all custom zone mapping to be deleted during delete.

        :schema: CfnGlobalClusterConfigProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2abf09a412ab7492653aa5101a0106311ebaa3b5f1356b6df31145b1c366979f)
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument custom_zone_mappings", value=custom_zone_mappings, expected_type=type_hints["custom_zone_mappings"])
            check_type(argname="argument managed_namespaces", value=managed_namespaces, expected_type=type_hints["managed_namespaces"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument remove_all_zone_mapping", value=remove_all_zone_mapping, expected_type=type_hints["remove_all_zone_mapping"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_name": cluster_name,
            "project_id": project_id,
        }
        if custom_zone_mappings is not None:
            self._values["custom_zone_mappings"] = custom_zone_mappings
        if managed_namespaces is not None:
            self._values["managed_namespaces"] = managed_namespaces
        if profile is not None:
            self._values["profile"] = profile
        if remove_all_zone_mapping is not None:
            self._values["remove_all_zone_mapping"] = remove_all_zone_mapping

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''The name of the Atlas cluster that contains the snapshots you want to retrieve.

        :schema: CfnGlobalClusterConfigProps#ClusterName
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The unique identifier of the project for the Atlas cluster.

        :schema: CfnGlobalClusterConfigProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_zone_mappings(self) -> typing.Optional[typing.List["ZoneMapping"]]:
        '''List that contains comma-separated key value pairs to map zones to geographic regions.

        These pairs map an ISO 3166-1a2 location code, with an ISO 3166-2 subdivision code when possible, to the human-readable label for the desired custom zone. MongoDB Cloud maps the ISO 3166-1a2 code to the nearest geographical zone by default. Include this parameter to override the default mappings.

        This parameter returns an empty object if no custom zones exist.

        :schema: CfnGlobalClusterConfigProps#CustomZoneMappings
        '''
        result = self._values.get("custom_zone_mappings")
        return typing.cast(typing.Optional[typing.List["ZoneMapping"]], result)

    @builtins.property
    def managed_namespaces(self) -> typing.Optional[typing.List["ManagedNamespace"]]:
        '''List that contains comma-separated key value pairs to map zones to geographic regions.

        These pairs map an ISO 3166-1a2 location code, with an ISO 3166-2 subdivision code when possible, to the human-readable label for the desired custom zone. MongoDB Cloud maps the ISO 3166-1a2 code to the nearest geographical zone by default. Include this parameter to override the default mappings.

        This parameter returns an empty object if no custom zones exist.

        :schema: CfnGlobalClusterConfigProps#ManagedNamespaces
        '''
        result = self._values.get("managed_namespaces")
        return typing.cast(typing.Optional[typing.List["ManagedNamespace"]], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''The profile is defined in AWS Secret manager.

        See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnGlobalClusterConfigProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remove_all_zone_mapping(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether all custom zone mapping to be deleted during delete.

        :schema: CfnGlobalClusterConfigProps#RemoveAllZoneMapping
        '''
        result = self._values.get("remove_all_zone_mapping")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGlobalClusterConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnLdapConfiguration(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnLdapConfiguration",
):
    '''A CloudFormation ``MongoDB::Atlas::LDAPConfiguration``.

    :cloudformationResource: MongoDB::Atlas::LDAPConfiguration
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        bind_password: builtins.str,
        bind_username: builtins.str,
        hostname: builtins.str,
        port: jsii.Number,
        project_id: builtins.str,
        authentication_enabled: typing.Optional[builtins.bool] = None,
        authorization_enabled: typing.Optional[builtins.bool] = None,
        authz_query_template: typing.Optional[builtins.str] = None,
        ca_certificate: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        user_to_dn_mapping: typing.Optional[typing.Sequence[typing.Union[ApiAtlasNdsUserToDnMappingView, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::LDAPConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param bind_password: Password that MongoDB Cloud uses to authenticate the **bindUsername**.
        :param bind_username: Full Distinguished Name (DN) of the Lightweight Directory Access Protocol (LDAP) user that MongoDB Cloud uses to connect to the LDAP host. LDAP distinguished names must be formatted according to RFC 2253.
        :param hostname: Human-readable label that identifies the hostname or Internet Protocol (IP) address of the Lightweight Directory Access Protocol (LDAP) host. This host must have access to the internet or have a Virtual Private Cloud (VPC) peering connection to your cluster.
        :param port: Port to which the Lightweight Directory Access Protocol (LDAP) host listens for client connections.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param authentication_enabled: Flag that indicates whether users can authenticate using an Lightweight Directory Access Protocol (LDAP) host.
        :param authorization_enabled: Flag that indicates whether users can authorize access to MongoDB Cloud resources using an Lightweight Directory Access Protocol (LDAP) host.
        :param authz_query_template: Lightweight Directory Access Protocol (LDAP) query template that MongoDB Cloud runs to obtain the LDAP groups associated with the authenticated user. MongoDB Cloud uses this parameter only for user authorization. Use the ``{USER}`` placeholder in the Uniform Resource Locator (URL) to substitute the authenticated username. The query relates to the host specified with the hostname. Format this query according to `RFC 4515 <https://tools.ietf.org/search/rfc4515>`_ and `RFC 4516 <https://datatracker.ietf.org/doc/html/rfc4516>`_.
        :param ca_certificate: Certificate Authority (CA) certificate that MongoDB Cloud uses to verify the identity of the Lightweight Directory Access Protocol (LDAP) host. MongoDB Cloud allows self-signed certificates. To delete an assigned value, pass an empty string: ``"caCertificate": ""``
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param status: The current status of the LDAP over TLS/SSL configuration.
        :param user_to_dn_mapping: User-to-Distinguished Name (DN) map that MongoDB Cloud uses to transform a Lightweight Directory Access Protocol (LDAP) username into an LDAP DN.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64ba1f8429afaf86fe658100b8053a07f434a9162e0c336885568446454a3c23)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLdapConfigurationProps(
            bind_password=bind_password,
            bind_username=bind_username,
            hostname=hostname,
            port=port,
            project_id=project_id,
            authentication_enabled=authentication_enabled,
            authorization_enabled=authorization_enabled,
            authz_query_template=authz_query_template,
            ca_certificate=ca_certificate,
            profile=profile,
            status=status,
            user_to_dn_mapping=user_to_dn_mapping,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnLdapConfigurationProps":
        '''Resource props.'''
        return typing.cast("CfnLdapConfigurationProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnLdapConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "bind_password": "bindPassword",
        "bind_username": "bindUsername",
        "hostname": "hostname",
        "port": "port",
        "project_id": "projectId",
        "authentication_enabled": "authenticationEnabled",
        "authorization_enabled": "authorizationEnabled",
        "authz_query_template": "authzQueryTemplate",
        "ca_certificate": "caCertificate",
        "profile": "profile",
        "status": "status",
        "user_to_dn_mapping": "userToDnMapping",
    },
)
class CfnLdapConfigurationProps:
    def __init__(
        self,
        *,
        bind_password: builtins.str,
        bind_username: builtins.str,
        hostname: builtins.str,
        port: jsii.Number,
        project_id: builtins.str,
        authentication_enabled: typing.Optional[builtins.bool] = None,
        authorization_enabled: typing.Optional[builtins.bool] = None,
        authz_query_template: typing.Optional[builtins.str] = None,
        ca_certificate: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        user_to_dn_mapping: typing.Optional[typing.Sequence[typing.Union[ApiAtlasNdsUserToDnMappingView, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Returns, edits, verifies, and removes LDAP configurations.

        :param bind_password: Password that MongoDB Cloud uses to authenticate the **bindUsername**.
        :param bind_username: Full Distinguished Name (DN) of the Lightweight Directory Access Protocol (LDAP) user that MongoDB Cloud uses to connect to the LDAP host. LDAP distinguished names must be formatted according to RFC 2253.
        :param hostname: Human-readable label that identifies the hostname or Internet Protocol (IP) address of the Lightweight Directory Access Protocol (LDAP) host. This host must have access to the internet or have a Virtual Private Cloud (VPC) peering connection to your cluster.
        :param port: Port to which the Lightweight Directory Access Protocol (LDAP) host listens for client connections.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param authentication_enabled: Flag that indicates whether users can authenticate using an Lightweight Directory Access Protocol (LDAP) host.
        :param authorization_enabled: Flag that indicates whether users can authorize access to MongoDB Cloud resources using an Lightweight Directory Access Protocol (LDAP) host.
        :param authz_query_template: Lightweight Directory Access Protocol (LDAP) query template that MongoDB Cloud runs to obtain the LDAP groups associated with the authenticated user. MongoDB Cloud uses this parameter only for user authorization. Use the ``{USER}`` placeholder in the Uniform Resource Locator (URL) to substitute the authenticated username. The query relates to the host specified with the hostname. Format this query according to `RFC 4515 <https://tools.ietf.org/search/rfc4515>`_ and `RFC 4516 <https://datatracker.ietf.org/doc/html/rfc4516>`_.
        :param ca_certificate: Certificate Authority (CA) certificate that MongoDB Cloud uses to verify the identity of the Lightweight Directory Access Protocol (LDAP) host. MongoDB Cloud allows self-signed certificates. To delete an assigned value, pass an empty string: ``"caCertificate": ""``
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param status: The current status of the LDAP over TLS/SSL configuration.
        :param user_to_dn_mapping: User-to-Distinguished Name (DN) map that MongoDB Cloud uses to transform a Lightweight Directory Access Protocol (LDAP) username into an LDAP DN.

        :schema: CfnLdapConfigurationProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c3cc1347bf0066c86c262b5e05f16ab053181b08277183625438baf0e95d338)
            check_type(argname="argument bind_password", value=bind_password, expected_type=type_hints["bind_password"])
            check_type(argname="argument bind_username", value=bind_username, expected_type=type_hints["bind_username"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument authentication_enabled", value=authentication_enabled, expected_type=type_hints["authentication_enabled"])
            check_type(argname="argument authorization_enabled", value=authorization_enabled, expected_type=type_hints["authorization_enabled"])
            check_type(argname="argument authz_query_template", value=authz_query_template, expected_type=type_hints["authz_query_template"])
            check_type(argname="argument ca_certificate", value=ca_certificate, expected_type=type_hints["ca_certificate"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument user_to_dn_mapping", value=user_to_dn_mapping, expected_type=type_hints["user_to_dn_mapping"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bind_password": bind_password,
            "bind_username": bind_username,
            "hostname": hostname,
            "port": port,
            "project_id": project_id,
        }
        if authentication_enabled is not None:
            self._values["authentication_enabled"] = authentication_enabled
        if authorization_enabled is not None:
            self._values["authorization_enabled"] = authorization_enabled
        if authz_query_template is not None:
            self._values["authz_query_template"] = authz_query_template
        if ca_certificate is not None:
            self._values["ca_certificate"] = ca_certificate
        if profile is not None:
            self._values["profile"] = profile
        if status is not None:
            self._values["status"] = status
        if user_to_dn_mapping is not None:
            self._values["user_to_dn_mapping"] = user_to_dn_mapping

    @builtins.property
    def bind_password(self) -> builtins.str:
        '''Password that MongoDB Cloud uses to authenticate the **bindUsername**.

        :schema: CfnLdapConfigurationProps#BindPassword
        '''
        result = self._values.get("bind_password")
        assert result is not None, "Required property 'bind_password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bind_username(self) -> builtins.str:
        '''Full Distinguished Name (DN) of the Lightweight Directory Access Protocol (LDAP) user that MongoDB Cloud uses to connect to the LDAP host.

        LDAP distinguished names must be formatted according to RFC 2253.

        :schema: CfnLdapConfigurationProps#BindUsername
        '''
        result = self._values.get("bind_username")
        assert result is not None, "Required property 'bind_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hostname(self) -> builtins.str:
        '''Human-readable label that identifies the hostname or Internet Protocol (IP) address of the Lightweight Directory Access Protocol (LDAP) host.

        This host must have access to the internet or have a Virtual Private Cloud (VPC) peering connection to your cluster.

        :schema: CfnLdapConfigurationProps#Hostname
        '''
        result = self._values.get("hostname")
        assert result is not None, "Required property 'hostname' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Port to which the Lightweight Directory Access Protocol (LDAP) host listens for client connections.

        :schema: CfnLdapConfigurationProps#Port
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnLdapConfigurationProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authentication_enabled(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether users can authenticate using an Lightweight Directory Access Protocol (LDAP) host.

        :schema: CfnLdapConfigurationProps#AuthenticationEnabled
        '''
        result = self._values.get("authentication_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def authorization_enabled(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether users can authorize access to MongoDB Cloud resources using an Lightweight Directory Access Protocol (LDAP) host.

        :schema: CfnLdapConfigurationProps#AuthorizationEnabled
        '''
        result = self._values.get("authorization_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def authz_query_template(self) -> typing.Optional[builtins.str]:
        '''Lightweight Directory Access Protocol (LDAP) query template that MongoDB Cloud runs to obtain the LDAP groups associated with the authenticated user.

        MongoDB Cloud uses this parameter only for user authorization. Use the ``{USER}`` placeholder in the Uniform Resource Locator (URL) to substitute the authenticated username. The query relates to the host specified with the hostname. Format this query according to `RFC 4515 <https://tools.ietf.org/search/rfc4515>`_ and `RFC 4516 <https://datatracker.ietf.org/doc/html/rfc4516>`_.

        :schema: CfnLdapConfigurationProps#AuthzQueryTemplate
        '''
        result = self._values.get("authz_query_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ca_certificate(self) -> typing.Optional[builtins.str]:
        '''Certificate Authority (CA) certificate that MongoDB Cloud uses to verify the identity of the Lightweight Directory Access Protocol (LDAP) host.

        MongoDB Cloud allows self-signed certificates. To delete an assigned value, pass an empty string: ``"caCertificate": ""``

        :schema: CfnLdapConfigurationProps#CaCertificate
        '''
        result = self._values.get("ca_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.

        :schema: CfnLdapConfigurationProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The current status of the LDAP over TLS/SSL configuration.

        :schema: CfnLdapConfigurationProps#Status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_to_dn_mapping(
        self,
    ) -> typing.Optional[typing.List[ApiAtlasNdsUserToDnMappingView]]:
        '''User-to-Distinguished Name (DN) map that MongoDB Cloud uses to transform a Lightweight Directory Access Protocol (LDAP) username into an LDAP DN.

        :schema: CfnLdapConfigurationProps#UserToDNMapping
        '''
        result = self._values.get("user_to_dn_mapping")
        return typing.cast(typing.Optional[typing.List[ApiAtlasNdsUserToDnMappingView]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLdapConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnLdapVerify(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnLdapVerify",
):
    '''A CloudFormation ``MongoDB::Atlas::LDAPVerify``.

    :cloudformationResource: MongoDB::Atlas::LDAPVerify
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        bind_password: builtins.str,
        bind_username: builtins.str,
        host_name: builtins.str,
        port: jsii.Number,
        project_id: builtins.str,
        authz_query_template: typing.Optional[builtins.str] = None,
        ca_certificate: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        validations: typing.Optional[typing.Sequence[typing.Union["Validation", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::LDAPVerify``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param bind_password: Password that MongoDB Cloud uses to authenticate the **bindUsername**.
        :param bind_username: Full Distinguished Name (DN) of the Lightweight Directory Access Protocol (LDAP) user that MongoDB Cloud uses to connect to the LDAP host. LDAP distinguished names must be formatted according to RFC 2253.
        :param host_name: Human-readable label that identifies the hostname or Internet Protocol (IP) address of the Lightweight Directory Access Protocol (LDAP) host. This host must have access to the internet or have a Virtual Private Cloud (VPC) peering connection to your cluster.
        :param port: Port to which the Lightweight Directory Access Protocol (LDAP) host listens for client connections.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param authz_query_template: Lightweight Directory Access Protocol (LDAP) query template that MongoDB Cloud runs to obtain the LDAP groups associated with the authenticated user. MongoDB Cloud uses this parameter only for user authorization. Use the ``{USER}`` placeholder in the Uniform Resource Locator (URL) to substitute the authenticated username. The query relates to the host specified with the hostname. Format this query according to `RFC 4515 <https://tools.ietf.org/search/rfc4515>`_ and `RFC 4516 <https://datatracker.ietf.org/doc/html/rfc4516>`_.
        :param ca_certificate: Certificate Authority (CA) certificate that MongoDB Cloud uses to verify the identity of the Lightweight Directory Access Protocol (LDAP) host. MongoDB Cloud allows self-signed certificates. To delete an assigned value, pass an empty string: ``"caCertificate": ""``
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param validations: List of validation messages related to the verification of the provided LDAP over TLS configuration details. The array contains a document for each test that Atlas runs. Atlas stops running tests after the first failure.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de93db0c4570397a56ad2208f6f7c27ba66fa5f7ca40ed2393a5f3c43a35dba4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLdapVerifyProps(
            bind_password=bind_password,
            bind_username=bind_username,
            host_name=host_name,
            port=port,
            project_id=project_id,
            authz_query_template=authz_query_template,
            ca_certificate=ca_certificate,
            profile=profile,
            validations=validations,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRequestId")
    def attr_request_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::LDAPVerify.RequestId``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrRequestId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::LDAPVerify.Status``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnLdapVerifyProps":
        '''Resource props.'''
        return typing.cast("CfnLdapVerifyProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnLdapVerifyProps",
    jsii_struct_bases=[],
    name_mapping={
        "bind_password": "bindPassword",
        "bind_username": "bindUsername",
        "host_name": "hostName",
        "port": "port",
        "project_id": "projectId",
        "authz_query_template": "authzQueryTemplate",
        "ca_certificate": "caCertificate",
        "profile": "profile",
        "validations": "validations",
    },
)
class CfnLdapVerifyProps:
    def __init__(
        self,
        *,
        bind_password: builtins.str,
        bind_username: builtins.str,
        host_name: builtins.str,
        port: jsii.Number,
        project_id: builtins.str,
        authz_query_template: typing.Optional[builtins.str] = None,
        ca_certificate: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        validations: typing.Optional[typing.Sequence[typing.Union["Validation", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Requests a verification of an LDAP configuration over TLS for an Atlas project.

        Pass the requestId in the response object to the Verify |ldap| Configuration endpoint to get the status of a verification request. Atlas retains only the most recent request for each project.

        :param bind_password: Password that MongoDB Cloud uses to authenticate the **bindUsername**.
        :param bind_username: Full Distinguished Name (DN) of the Lightweight Directory Access Protocol (LDAP) user that MongoDB Cloud uses to connect to the LDAP host. LDAP distinguished names must be formatted according to RFC 2253.
        :param host_name: Human-readable label that identifies the hostname or Internet Protocol (IP) address of the Lightweight Directory Access Protocol (LDAP) host. This host must have access to the internet or have a Virtual Private Cloud (VPC) peering connection to your cluster.
        :param port: Port to which the Lightweight Directory Access Protocol (LDAP) host listens for client connections.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param authz_query_template: Lightweight Directory Access Protocol (LDAP) query template that MongoDB Cloud runs to obtain the LDAP groups associated with the authenticated user. MongoDB Cloud uses this parameter only for user authorization. Use the ``{USER}`` placeholder in the Uniform Resource Locator (URL) to substitute the authenticated username. The query relates to the host specified with the hostname. Format this query according to `RFC 4515 <https://tools.ietf.org/search/rfc4515>`_ and `RFC 4516 <https://datatracker.ietf.org/doc/html/rfc4516>`_.
        :param ca_certificate: Certificate Authority (CA) certificate that MongoDB Cloud uses to verify the identity of the Lightweight Directory Access Protocol (LDAP) host. MongoDB Cloud allows self-signed certificates. To delete an assigned value, pass an empty string: ``"caCertificate": ""``
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param validations: List of validation messages related to the verification of the provided LDAP over TLS configuration details. The array contains a document for each test that Atlas runs. Atlas stops running tests after the first failure.

        :schema: CfnLdapVerifyProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bb6ed957d2c446f2c47a1acae65ef2695e9d225c57a70e5b6a16dfd1f65b1e1)
            check_type(argname="argument bind_password", value=bind_password, expected_type=type_hints["bind_password"])
            check_type(argname="argument bind_username", value=bind_username, expected_type=type_hints["bind_username"])
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument authz_query_template", value=authz_query_template, expected_type=type_hints["authz_query_template"])
            check_type(argname="argument ca_certificate", value=ca_certificate, expected_type=type_hints["ca_certificate"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument validations", value=validations, expected_type=type_hints["validations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bind_password": bind_password,
            "bind_username": bind_username,
            "host_name": host_name,
            "port": port,
            "project_id": project_id,
        }
        if authz_query_template is not None:
            self._values["authz_query_template"] = authz_query_template
        if ca_certificate is not None:
            self._values["ca_certificate"] = ca_certificate
        if profile is not None:
            self._values["profile"] = profile
        if validations is not None:
            self._values["validations"] = validations

    @builtins.property
    def bind_password(self) -> builtins.str:
        '''Password that MongoDB Cloud uses to authenticate the **bindUsername**.

        :schema: CfnLdapVerifyProps#BindPassword
        '''
        result = self._values.get("bind_password")
        assert result is not None, "Required property 'bind_password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bind_username(self) -> builtins.str:
        '''Full Distinguished Name (DN) of the Lightweight Directory Access Protocol (LDAP) user that MongoDB Cloud uses to connect to the LDAP host.

        LDAP distinguished names must be formatted according to RFC 2253.

        :schema: CfnLdapVerifyProps#BindUsername
        '''
        result = self._values.get("bind_username")
        assert result is not None, "Required property 'bind_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host_name(self) -> builtins.str:
        '''Human-readable label that identifies the hostname or Internet Protocol (IP) address of the Lightweight Directory Access Protocol (LDAP) host.

        This host must have access to the internet or have a Virtual Private Cloud (VPC) peering connection to your cluster.

        :schema: CfnLdapVerifyProps#HostName
        '''
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Port to which the Lightweight Directory Access Protocol (LDAP) host listens for client connections.

        :schema: CfnLdapVerifyProps#Port
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnLdapVerifyProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authz_query_template(self) -> typing.Optional[builtins.str]:
        '''Lightweight Directory Access Protocol (LDAP) query template that MongoDB Cloud runs to obtain the LDAP groups associated with the authenticated user.

        MongoDB Cloud uses this parameter only for user authorization. Use the ``{USER}`` placeholder in the Uniform Resource Locator (URL) to substitute the authenticated username. The query relates to the host specified with the hostname. Format this query according to `RFC 4515 <https://tools.ietf.org/search/rfc4515>`_ and `RFC 4516 <https://datatracker.ietf.org/doc/html/rfc4516>`_.

        :schema: CfnLdapVerifyProps#AuthzQueryTemplate
        '''
        result = self._values.get("authz_query_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ca_certificate(self) -> typing.Optional[builtins.str]:
        '''Certificate Authority (CA) certificate that MongoDB Cloud uses to verify the identity of the Lightweight Directory Access Protocol (LDAP) host.

        MongoDB Cloud allows self-signed certificates. To delete an assigned value, pass an empty string: ``"caCertificate": ""``

        :schema: CfnLdapVerifyProps#CaCertificate
        '''
        result = self._values.get("ca_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.

        :schema: CfnLdapVerifyProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def validations(self) -> typing.Optional[typing.List["Validation"]]:
        '''List of validation messages related to the verification of the provided LDAP over TLS configuration details.

        The array contains a document for each test that Atlas runs. Atlas stops running tests after the first failure.

        :schema: CfnLdapVerifyProps#Validations
        '''
        result = self._values.get("validations")
        return typing.cast(typing.Optional[typing.List["Validation"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLdapVerifyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnMaintenanceWindow(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnMaintenanceWindow",
):
    '''A CloudFormation ``MongoDB::Atlas::MaintenanceWindow``.

    :cloudformationResource: MongoDB::Atlas::MaintenanceWindow
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        hour_of_day: jsii.Number,
        auto_defer_once_enabled: typing.Optional[builtins.bool] = None,
        day_of_week: typing.Optional[jsii.Number] = None,
        profile: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        start_asap: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::MaintenanceWindow``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param hour_of_day: Zero-based integer that represents the hour of the of the day that the maintenance window starts according to a 24-hour clock. Use ``0`` for midnight and ``12`` for noon.
        :param auto_defer_once_enabled: Flag that indicates whether MongoDB Cloud should defer all maintenance windows for one week after you enable them.
        :param day_of_week: One-based integer that represents the day of the week that the maintenance window starts. | Value | Day of Week | |---|---| | ``1`` | Sunday | | ``2`` | Monday | | ``3`` | Tuesday | | ``4`` | Wednesday | | ``5`` | Thursday | | ``6`` | Friday | | ``7`` | Saturday |
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param start_asap: Flag that indicates whether MongoDB Cloud starts the maintenance window immediately upon receiving this request. To start the maintenance window immediately for your project, MongoDB Cloud must have maintenance scheduled and you must set a maintenance window. This flag resets to ``false`` after MongoDB Cloud completes maintenance.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d709ba18cbc2813f625dfc983f1b51f0464eb8649a41db43931af94a23a82a3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMaintenanceWindowProps(
            hour_of_day=hour_of_day,
            auto_defer_once_enabled=auto_defer_once_enabled,
            day_of_week=day_of_week,
            profile=profile,
            project_id=project_id,
            start_asap=start_asap,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnMaintenanceWindowProps":
        '''Resource props.'''
        return typing.cast("CfnMaintenanceWindowProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnMaintenanceWindowProps",
    jsii_struct_bases=[],
    name_mapping={
        "hour_of_day": "hourOfDay",
        "auto_defer_once_enabled": "autoDeferOnceEnabled",
        "day_of_week": "dayOfWeek",
        "profile": "profile",
        "project_id": "projectId",
        "start_asap": "startAsap",
    },
)
class CfnMaintenanceWindowProps:
    def __init__(
        self,
        *,
        hour_of_day: jsii.Number,
        auto_defer_once_enabled: typing.Optional[builtins.bool] = None,
        day_of_week: typing.Optional[jsii.Number] = None,
        profile: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        start_asap: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''The maintenanceWindow resource provides access to retrieve or update the current Atlas project maintenance window.

        :param hour_of_day: Zero-based integer that represents the hour of the of the day that the maintenance window starts according to a 24-hour clock. Use ``0`` for midnight and ``12`` for noon.
        :param auto_defer_once_enabled: Flag that indicates whether MongoDB Cloud should defer all maintenance windows for one week after you enable them.
        :param day_of_week: One-based integer that represents the day of the week that the maintenance window starts. | Value | Day of Week | |---|---| | ``1`` | Sunday | | ``2`` | Monday | | ``3`` | Tuesday | | ``4`` | Wednesday | | ``5`` | Thursday | | ``6`` | Friday | | ``7`` | Saturday |
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param start_asap: Flag that indicates whether MongoDB Cloud starts the maintenance window immediately upon receiving this request. To start the maintenance window immediately for your project, MongoDB Cloud must have maintenance scheduled and you must set a maintenance window. This flag resets to ``false`` after MongoDB Cloud completes maintenance.

        :schema: CfnMaintenanceWindowProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23b64b93b716fc5c18498400d8d433073e8609bac008d6faf8110daea0f7c05a)
            check_type(argname="argument hour_of_day", value=hour_of_day, expected_type=type_hints["hour_of_day"])
            check_type(argname="argument auto_defer_once_enabled", value=auto_defer_once_enabled, expected_type=type_hints["auto_defer_once_enabled"])
            check_type(argname="argument day_of_week", value=day_of_week, expected_type=type_hints["day_of_week"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument start_asap", value=start_asap, expected_type=type_hints["start_asap"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hour_of_day": hour_of_day,
        }
        if auto_defer_once_enabled is not None:
            self._values["auto_defer_once_enabled"] = auto_defer_once_enabled
        if day_of_week is not None:
            self._values["day_of_week"] = day_of_week
        if profile is not None:
            self._values["profile"] = profile
        if project_id is not None:
            self._values["project_id"] = project_id
        if start_asap is not None:
            self._values["start_asap"] = start_asap

    @builtins.property
    def hour_of_day(self) -> jsii.Number:
        '''Zero-based integer that represents the hour of the of the day that the maintenance window starts according to a 24-hour clock.

        Use ``0`` for midnight and ``12`` for noon.

        :schema: CfnMaintenanceWindowProps#HourOfDay
        '''
        result = self._values.get("hour_of_day")
        assert result is not None, "Required property 'hour_of_day' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def auto_defer_once_enabled(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether MongoDB Cloud should defer all maintenance windows for one week after you enable them.

        :schema: CfnMaintenanceWindowProps#AutoDeferOnceEnabled
        '''
        result = self._values.get("auto_defer_once_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def day_of_week(self) -> typing.Optional[jsii.Number]:
        '''One-based integer that represents the day of the week that the maintenance window starts.

        | Value | Day of Week |
        |---|---|
        | ``1`` | Sunday |
        | ``2`` | Monday |
        | ``3`` | Tuesday |
        | ``4`` | Wednesday |
        | ``5`` | Thursday |
        | ``6`` | Friday |
        | ``7`` | Saturday |

        :schema: CfnMaintenanceWindowProps#DayOfWeek
        '''
        result = self._values.get("day_of_week")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''The profile is defined in AWS Secret manager.

        See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_

        :schema: CfnMaintenanceWindowProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnMaintenanceWindowProps#ProjectId
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_asap(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether MongoDB Cloud starts the maintenance window immediately upon receiving this request.

        To start the maintenance window immediately for your project, MongoDB Cloud must have maintenance scheduled and you must set a maintenance window. This flag resets to ``false`` after MongoDB Cloud completes maintenance.

        :schema: CfnMaintenanceWindowProps#StartASAP
        '''
        result = self._values.get("start_asap")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMaintenanceWindowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnNetworkContainer(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnNetworkContainer",
):
    '''A CloudFormation ``MongoDB::Atlas::NetworkContainer``.

    :cloudformationResource: MongoDB::Atlas::NetworkContainer
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        atlas_cidr_block: builtins.str,
        project_id: builtins.str,
        region_name: builtins.str,
        profile: typing.Optional[builtins.str] = None,
        provisioned: typing.Optional[builtins.bool] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::NetworkContainer``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param atlas_cidr_block: IP addresses expressed in Classless Inter-Domain Routing (CIDR) notation that MongoDB Cloud uses for the network peering containers in your project. MongoDB Cloud assigns all of the project's clusters deployed to this cloud provider an IP address from this range. MongoDB Cloud locks this value if an M10 or greater cluster or a network peering connection exists in this project. These CIDR blocks must fall within the ranges reserved per RFC 1918. AWS further limits the block to between the /24 and /21 ranges. To modify the CIDR block, the target project cannot have: - Any M10 or greater clusters - Any other VPC peering connections You can also create a new project and create a network peering connection to set the desired MongoDB Cloud network peering container CIDR block for that project. MongoDB Cloud limits the number of MongoDB nodes per network peering connection based on the CIDR block and the region selected for the project. Example: A project in an Amazon Web Services (AWS) region supporting three availability zones and an MongoDB CIDR network peering container block of limit of /24 equals 27 three-node replica sets.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param region_name: Geographic area that Amazon Web Services (AWS) defines to which MongoDB Cloud deployed this network peering container.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param provisioned: Boolean flag that indicates whether MongoDB Cloud clusters exist in the specified network peering container.
        :param vpc_id: Unique string that identifies the MongoDB Cloud VPC on AWS.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c9284447403a32509edf70d5f679ba1a327089973b2567a6f61cee465c831a3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNetworkContainerProps(
            atlas_cidr_block=atlas_cidr_block,
            project_id=project_id,
            region_name=region_name,
            profile=profile,
            provisioned=provisioned,
            vpc_id=vpc_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::NetworkContainer.Id``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnNetworkContainerProps":
        '''Resource props.'''
        return typing.cast("CfnNetworkContainerProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnNetworkContainerProps",
    jsii_struct_bases=[],
    name_mapping={
        "atlas_cidr_block": "atlasCidrBlock",
        "project_id": "projectId",
        "region_name": "regionName",
        "profile": "profile",
        "provisioned": "provisioned",
        "vpc_id": "vpcId",
    },
)
class CfnNetworkContainerProps:
    def __init__(
        self,
        *,
        atlas_cidr_block: builtins.str,
        project_id: builtins.str,
        region_name: builtins.str,
        profile: typing.Optional[builtins.str] = None,
        provisioned: typing.Optional[builtins.bool] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Returns, adds, edits, and removes network peering containers.

        :param atlas_cidr_block: IP addresses expressed in Classless Inter-Domain Routing (CIDR) notation that MongoDB Cloud uses for the network peering containers in your project. MongoDB Cloud assigns all of the project's clusters deployed to this cloud provider an IP address from this range. MongoDB Cloud locks this value if an M10 or greater cluster or a network peering connection exists in this project. These CIDR blocks must fall within the ranges reserved per RFC 1918. AWS further limits the block to between the /24 and /21 ranges. To modify the CIDR block, the target project cannot have: - Any M10 or greater clusters - Any other VPC peering connections You can also create a new project and create a network peering connection to set the desired MongoDB Cloud network peering container CIDR block for that project. MongoDB Cloud limits the number of MongoDB nodes per network peering connection based on the CIDR block and the region selected for the project. Example: A project in an Amazon Web Services (AWS) region supporting three availability zones and an MongoDB CIDR network peering container block of limit of /24 equals 27 three-node replica sets.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param region_name: Geographic area that Amazon Web Services (AWS) defines to which MongoDB Cloud deployed this network peering container.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param provisioned: Boolean flag that indicates whether MongoDB Cloud clusters exist in the specified network peering container.
        :param vpc_id: Unique string that identifies the MongoDB Cloud VPC on AWS.

        :schema: CfnNetworkContainerProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d55f15d0316fc413650d60ddc210fc38142413a4558f6b547d6a0546f9785ce1)
            check_type(argname="argument atlas_cidr_block", value=atlas_cidr_block, expected_type=type_hints["atlas_cidr_block"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument region_name", value=region_name, expected_type=type_hints["region_name"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument provisioned", value=provisioned, expected_type=type_hints["provisioned"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "atlas_cidr_block": atlas_cidr_block,
            "project_id": project_id,
            "region_name": region_name,
        }
        if profile is not None:
            self._values["profile"] = profile
        if provisioned is not None:
            self._values["provisioned"] = provisioned
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id

    @builtins.property
    def atlas_cidr_block(self) -> builtins.str:
        '''IP addresses expressed in Classless Inter-Domain Routing (CIDR) notation that MongoDB Cloud uses for the network peering containers in your project.

        MongoDB Cloud assigns all of the project's clusters deployed to this cloud provider an IP address from this range. MongoDB Cloud locks this value if an M10 or greater cluster or a network peering connection exists in this project.
        These CIDR blocks must fall within the ranges reserved per RFC 1918. AWS further limits the block to between the /24 and /21 ranges.
        To modify the CIDR block, the target project cannot have:

        - Any M10 or greater clusters
        - Any other VPC peering connections
          You can also create a new project and create a network peering connection to set the desired MongoDB Cloud network peering container CIDR block for that project. MongoDB Cloud limits the number of MongoDB nodes per network peering connection based on the CIDR block and the region selected for the project.
          Example: A project in an Amazon Web Services (AWS) region supporting three availability zones and an MongoDB CIDR network peering container block of limit of /24 equals 27 three-node replica sets.

        :schema: CfnNetworkContainerProps#AtlasCidrBlock
        '''
        result = self._values.get("atlas_cidr_block")
        assert result is not None, "Required property 'atlas_cidr_block' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnNetworkContainerProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region_name(self) -> builtins.str:
        '''Geographic area that Amazon Web Services (AWS) defines to which MongoDB Cloud deployed this network peering container.

        :schema: CfnNetworkContainerProps#RegionName
        '''
        result = self._values.get("region_name")
        assert result is not None, "Required property 'region_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''The profile is defined in AWS Secret manager.

        See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnNetworkContainerProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provisioned(self) -> typing.Optional[builtins.bool]:
        '''Boolean flag that indicates whether MongoDB Cloud clusters exist in the specified network peering container.

        :schema: CfnNetworkContainerProps#Provisioned
        '''
        result = self._values.get("provisioned")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional[builtins.str]:
        '''Unique string that identifies the MongoDB Cloud VPC on AWS.

        :schema: CfnNetworkContainerProps#VpcId
        '''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNetworkContainerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnNetworkPeering(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnNetworkPeering",
):
    '''A CloudFormation ``MongoDB::Atlas::NetworkPeering``.

    :cloudformationResource: MongoDB::Atlas::NetworkPeering
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        container_id: builtins.str,
        project_id: builtins.str,
        vpc_id: builtins.str,
        accepter_region_name: typing.Optional[builtins.str] = None,
        aws_account_id: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        route_table_cidr_block: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::NetworkPeering``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param container_id: Unique 24-hexadecimal digit string that identifies the MongoDB Cloud network container that contains the specified network peering connection.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param vpc_id: Unique string that identifies the VPC on Amazon Web Services (AWS) that you want to peer with the MongoDB Cloud VPC.
        :param accepter_region_name: Amazon Web Services (AWS) region where the Virtual Peering Connection (VPC) that you peered with the MongoDB Cloud VPC resides. The resource returns null if your VPC and the MongoDB Cloud VPC reside in the same region.
        :param aws_account_id: Unique twelve-digit string that identifies the Amazon Web Services (AWS) account that owns the VPC that you peered with the MongoDB Cloud VPC.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param route_table_cidr_block: Internet Protocol (IP) addresses expressed in Classless Inter-Domain Routing (CIDR) notation of the VPC's subnet that you want to peer with the MongoDB Cloud VPC.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dc613947bd4db1c6d883903dd838f6dd48daf92a78cc07faa959edc47dd394d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNetworkPeeringProps(
            container_id=container_id,
            project_id=project_id,
            vpc_id=vpc_id,
            accepter_region_name=accepter_region_name,
            aws_account_id=aws_account_id,
            profile=profile,
            route_table_cidr_block=route_table_cidr_block,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrConnectionId")
    def attr_connection_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::NetworkPeering.ConnectionId``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectionId"))

    @builtins.property
    @jsii.member(jsii_name="attrErrorStateName")
    def attr_error_state_name(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::NetworkPeering.ErrorStateName``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrErrorStateName"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::NetworkPeering.Id``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusName")
    def attr_status_name(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::NetworkPeering.StatusName``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusName"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnNetworkPeeringProps":
        '''Resource props.'''
        return typing.cast("CfnNetworkPeeringProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnNetworkPeeringProps",
    jsii_struct_bases=[],
    name_mapping={
        "container_id": "containerId",
        "project_id": "projectId",
        "vpc_id": "vpcId",
        "accepter_region_name": "accepterRegionName",
        "aws_account_id": "awsAccountId",
        "profile": "profile",
        "route_table_cidr_block": "routeTableCidrBlock",
    },
)
class CfnNetworkPeeringProps:
    def __init__(
        self,
        *,
        container_id: builtins.str,
        project_id: builtins.str,
        vpc_id: builtins.str,
        accepter_region_name: typing.Optional[builtins.str] = None,
        aws_account_id: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        route_table_cidr_block: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Returns, adds, edits, and removes network peering containers and peering connections.

        :param container_id: Unique 24-hexadecimal digit string that identifies the MongoDB Cloud network container that contains the specified network peering connection.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param vpc_id: Unique string that identifies the VPC on Amazon Web Services (AWS) that you want to peer with the MongoDB Cloud VPC.
        :param accepter_region_name: Amazon Web Services (AWS) region where the Virtual Peering Connection (VPC) that you peered with the MongoDB Cloud VPC resides. The resource returns null if your VPC and the MongoDB Cloud VPC reside in the same region.
        :param aws_account_id: Unique twelve-digit string that identifies the Amazon Web Services (AWS) account that owns the VPC that you peered with the MongoDB Cloud VPC.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param route_table_cidr_block: Internet Protocol (IP) addresses expressed in Classless Inter-Domain Routing (CIDR) notation of the VPC's subnet that you want to peer with the MongoDB Cloud VPC.

        :schema: CfnNetworkPeeringProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf187f1934d98a58159cf134a6c59635175a6c762f497b087153852b583c0a51)
            check_type(argname="argument container_id", value=container_id, expected_type=type_hints["container_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument accepter_region_name", value=accepter_region_name, expected_type=type_hints["accepter_region_name"])
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument route_table_cidr_block", value=route_table_cidr_block, expected_type=type_hints["route_table_cidr_block"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_id": container_id,
            "project_id": project_id,
            "vpc_id": vpc_id,
        }
        if accepter_region_name is not None:
            self._values["accepter_region_name"] = accepter_region_name
        if aws_account_id is not None:
            self._values["aws_account_id"] = aws_account_id
        if profile is not None:
            self._values["profile"] = profile
        if route_table_cidr_block is not None:
            self._values["route_table_cidr_block"] = route_table_cidr_block

    @builtins.property
    def container_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies the MongoDB Cloud network container that contains the specified network peering connection.

        :schema: CfnNetworkPeeringProps#ContainerId
        '''
        result = self._values.get("container_id")
        assert result is not None, "Required property 'container_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnNetworkPeeringProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''Unique string that identifies the VPC on Amazon Web Services (AWS) that you want to peer with the MongoDB Cloud VPC.

        :schema: CfnNetworkPeeringProps#VpcId
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accepter_region_name(self) -> typing.Optional[builtins.str]:
        '''Amazon Web Services (AWS) region where the Virtual Peering Connection (VPC) that you peered with the MongoDB Cloud VPC resides.

        The resource returns null if your VPC and the MongoDB Cloud VPC reside in the same region.

        :schema: CfnNetworkPeeringProps#AccepterRegionName
        '''
        result = self._values.get("accepter_region_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_account_id(self) -> typing.Optional[builtins.str]:
        '''Unique twelve-digit string that identifies the Amazon Web Services (AWS) account that owns the VPC that you peered with the MongoDB Cloud VPC.

        :schema: CfnNetworkPeeringProps#AwsAccountId
        '''
        result = self._values.get("aws_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''The profile is defined in AWS Secret manager.

        See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnNetworkPeeringProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def route_table_cidr_block(self) -> typing.Optional[builtins.str]:
        '''Internet Protocol (IP) addresses expressed in Classless Inter-Domain Routing (CIDR) notation of the VPC's subnet that you want to peer with the MongoDB Cloud VPC.

        :schema: CfnNetworkPeeringProps#RouteTableCIDRBlock
        '''
        result = self._values.get("route_table_cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNetworkPeeringProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnOnlineArchive(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnOnlineArchive",
):
    '''A CloudFormation ``MongoDB::Atlas::OnlineArchive``.

    :cloudformationResource: MongoDB::Atlas::OnlineArchive
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster_name: builtins.str,
        criteria: typing.Union["CriteriaView", typing.Dict[builtins.str, typing.Any]],
        collection_type: typing.Optional["CfnOnlineArchivePropsCollectionType"] = None,
        coll_name: typing.Optional[builtins.str] = None,
        db_name: typing.Optional[builtins.str] = None,
        include_count: typing.Optional[builtins.bool] = None,
        items_per_page: typing.Optional[jsii.Number] = None,
        page_num: typing.Optional[jsii.Number] = None,
        partition_fields: typing.Optional[typing.Sequence[typing.Union["PartitionFieldView", typing.Dict[builtins.str, typing.Any]]]] = None,
        profile: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[typing.Union["ScheduleView", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::OnlineArchive``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cluster_name: Human-readable label that identifies the cluster that contains the collection from which you want to remove an online archive.
        :param criteria: Rules by which MongoDB MongoDB Cloud archives data. Use the **criteria.type** field to choose how MongoDB Cloud selects data to archive. Choose data using the age of the data or a MongoDB query. **"criteria.type": "DATE"** selects documents to archive based on a date. **"criteria.type": "CUSTOM"** selects documents to archive based on a custom JSON query. MongoDB Cloud doesn't support **"criteria.type": "CUSTOM"** when **"collectionType": "TIMESERIES"**.
        :param collection_type: Classification of MongoDB database collection that you want to return. If you set this parameter to ``TIMESERIES``, set ``"criteria.type" : "date"`` and ``"criteria.dateFormat" : "ISODATE"``.
        :param coll_name: Human-readable label that identifies the collection for which you created the online archive.
        :param db_name: Human-readable label of the database that contains the collection that contains the online archive.
        :param include_count: Flag that indicates whether the response returns the total number of items (**totalCount**) in the response.
        :param items_per_page: Number of items that the response returns per page.
        :param page_num: Number of the page that displays the current set of the total objects that the response returns.
        :param partition_fields: List that contains document parameters to use to logically divide data within a collection. Partitions provide a coarse level of filtering of the underlying collection data. To divide your data, specify up to two parameters that you frequently query. Any queries that don't use these parameters result in a full collection scan of all archived documents. This takes more time and increase your costs.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param schedule: Regular frequency and duration when archiving process occurs.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25747c28460f7bc027e8af0fd1cda9b7810bca745f7c6a7796a795d2a50eda19)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOnlineArchiveProps(
            cluster_name=cluster_name,
            criteria=criteria,
            collection_type=collection_type,
            coll_name=coll_name,
            db_name=db_name,
            include_count=include_count,
            items_per_page=items_per_page,
            page_num=page_num,
            partition_fields=partition_fields,
            profile=profile,
            project_id=project_id,
            schedule=schedule,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArchiveId")
    def attr_archive_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::OnlineArchive.ArchiveId``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrArchiveId"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::OnlineArchive.State``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="attrTotalCount")
    def attr_total_count(self) -> jsii.Number:
        '''Attribute ``MongoDB::Atlas::OnlineArchive.TotalCount``.'''
        return typing.cast(jsii.Number, jsii.get(self, "attrTotalCount"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnOnlineArchiveProps":
        '''Resource props.'''
        return typing.cast("CfnOnlineArchiveProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnOnlineArchiveProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_name": "clusterName",
        "criteria": "criteria",
        "collection_type": "collectionType",
        "coll_name": "collName",
        "db_name": "dbName",
        "include_count": "includeCount",
        "items_per_page": "itemsPerPage",
        "page_num": "pageNum",
        "partition_fields": "partitionFields",
        "profile": "profile",
        "project_id": "projectId",
        "schedule": "schedule",
    },
)
class CfnOnlineArchiveProps:
    def __init__(
        self,
        *,
        cluster_name: builtins.str,
        criteria: typing.Union["CriteriaView", typing.Dict[builtins.str, typing.Any]],
        collection_type: typing.Optional["CfnOnlineArchivePropsCollectionType"] = None,
        coll_name: typing.Optional[builtins.str] = None,
        db_name: typing.Optional[builtins.str] = None,
        include_count: typing.Optional[builtins.bool] = None,
        items_per_page: typing.Optional[jsii.Number] = None,
        page_num: typing.Optional[jsii.Number] = None,
        partition_fields: typing.Optional[typing.Sequence[typing.Union["PartitionFieldView", typing.Dict[builtins.str, typing.Any]]]] = None,
        profile: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[typing.Union["ScheduleView", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Returns, adds, edits, or removes an online archive.

        :param cluster_name: Human-readable label that identifies the cluster that contains the collection from which you want to remove an online archive.
        :param criteria: Rules by which MongoDB MongoDB Cloud archives data. Use the **criteria.type** field to choose how MongoDB Cloud selects data to archive. Choose data using the age of the data or a MongoDB query. **"criteria.type": "DATE"** selects documents to archive based on a date. **"criteria.type": "CUSTOM"** selects documents to archive based on a custom JSON query. MongoDB Cloud doesn't support **"criteria.type": "CUSTOM"** when **"collectionType": "TIMESERIES"**.
        :param collection_type: Classification of MongoDB database collection that you want to return. If you set this parameter to ``TIMESERIES``, set ``"criteria.type" : "date"`` and ``"criteria.dateFormat" : "ISODATE"``.
        :param coll_name: Human-readable label that identifies the collection for which you created the online archive.
        :param db_name: Human-readable label of the database that contains the collection that contains the online archive.
        :param include_count: Flag that indicates whether the response returns the total number of items (**totalCount**) in the response.
        :param items_per_page: Number of items that the response returns per page.
        :param page_num: Number of the page that displays the current set of the total objects that the response returns.
        :param partition_fields: List that contains document parameters to use to logically divide data within a collection. Partitions provide a coarse level of filtering of the underlying collection data. To divide your data, specify up to two parameters that you frequently query. Any queries that don't use these parameters result in a full collection scan of all archived documents. This takes more time and increase your costs.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param schedule: Regular frequency and duration when archiving process occurs.

        :schema: CfnOnlineArchiveProps
        '''
        if isinstance(criteria, dict):
            criteria = CriteriaView(**criteria)
        if isinstance(schedule, dict):
            schedule = ScheduleView(**schedule)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dc840e142e8ce043b5b416cacb0e1a1607e1d4e5390581f081a08db637b0242)
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument criteria", value=criteria, expected_type=type_hints["criteria"])
            check_type(argname="argument collection_type", value=collection_type, expected_type=type_hints["collection_type"])
            check_type(argname="argument coll_name", value=coll_name, expected_type=type_hints["coll_name"])
            check_type(argname="argument db_name", value=db_name, expected_type=type_hints["db_name"])
            check_type(argname="argument include_count", value=include_count, expected_type=type_hints["include_count"])
            check_type(argname="argument items_per_page", value=items_per_page, expected_type=type_hints["items_per_page"])
            check_type(argname="argument page_num", value=page_num, expected_type=type_hints["page_num"])
            check_type(argname="argument partition_fields", value=partition_fields, expected_type=type_hints["partition_fields"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_name": cluster_name,
            "criteria": criteria,
        }
        if collection_type is not None:
            self._values["collection_type"] = collection_type
        if coll_name is not None:
            self._values["coll_name"] = coll_name
        if db_name is not None:
            self._values["db_name"] = db_name
        if include_count is not None:
            self._values["include_count"] = include_count
        if items_per_page is not None:
            self._values["items_per_page"] = items_per_page
        if page_num is not None:
            self._values["page_num"] = page_num
        if partition_fields is not None:
            self._values["partition_fields"] = partition_fields
        if profile is not None:
            self._values["profile"] = profile
        if project_id is not None:
            self._values["project_id"] = project_id
        if schedule is not None:
            self._values["schedule"] = schedule

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''Human-readable label that identifies the cluster that contains the collection from which you want to remove an online archive.

        :schema: CfnOnlineArchiveProps#ClusterName
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def criteria(self) -> "CriteriaView":
        '''Rules by which MongoDB MongoDB Cloud archives data.

        Use the **criteria.type** field to choose how MongoDB Cloud selects data to archive. Choose data using the age of the data or a MongoDB query.
        **"criteria.type": "DATE"** selects documents to archive based on a date.
        **"criteria.type": "CUSTOM"** selects documents to archive based on a custom JSON query. MongoDB Cloud doesn't support **"criteria.type": "CUSTOM"** when **"collectionType": "TIMESERIES"**.

        :schema: CfnOnlineArchiveProps#Criteria
        '''
        result = self._values.get("criteria")
        assert result is not None, "Required property 'criteria' is missing"
        return typing.cast("CriteriaView", result)

    @builtins.property
    def collection_type(self) -> typing.Optional["CfnOnlineArchivePropsCollectionType"]:
        '''Classification of MongoDB database collection that you want to return.

        If you set this parameter to ``TIMESERIES``, set ``"criteria.type" : "date"`` and ``"criteria.dateFormat" : "ISODATE"``.

        :schema: CfnOnlineArchiveProps#CollectionType
        '''
        result = self._values.get("collection_type")
        return typing.cast(typing.Optional["CfnOnlineArchivePropsCollectionType"], result)

    @builtins.property
    def coll_name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the collection for which you created the online archive.

        :schema: CfnOnlineArchiveProps#CollName
        '''
        result = self._values.get("coll_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label of the database that contains the collection that contains the online archive.

        :schema: CfnOnlineArchiveProps#DbName
        '''
        result = self._values.get("db_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def include_count(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether the response returns the total number of items (**totalCount**) in the response.

        :schema: CfnOnlineArchiveProps#IncludeCount
        '''
        result = self._values.get("include_count")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def items_per_page(self) -> typing.Optional[jsii.Number]:
        '''Number of items that the response returns per page.

        :schema: CfnOnlineArchiveProps#ItemsPerPage
        '''
        result = self._values.get("items_per_page")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def page_num(self) -> typing.Optional[jsii.Number]:
        '''Number of the page that displays the current set of the total objects that the response returns.

        :schema: CfnOnlineArchiveProps#PageNum
        '''
        result = self._values.get("page_num")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def partition_fields(self) -> typing.Optional[typing.List["PartitionFieldView"]]:
        '''List that contains document parameters to use to logically divide data within a collection.

        Partitions provide a coarse level of filtering of the underlying collection data. To divide your data, specify up to two parameters that you frequently query. Any queries that don't use these parameters result in a full collection scan of all archived documents. This takes more time and increase your costs.

        :schema: CfnOnlineArchiveProps#PartitionFields
        '''
        result = self._values.get("partition_fields")
        return typing.cast(typing.Optional[typing.List["PartitionFieldView"]], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''The profile is defined in AWS Secret manager.

        See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnOnlineArchiveProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnOnlineArchiveProps#ProjectId
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule(self) -> typing.Optional["ScheduleView"]:
        '''Regular frequency and duration when archiving process occurs.

        :schema: CfnOnlineArchiveProps#Schedule
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional["ScheduleView"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOnlineArchiveProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="awscdk-resources-mongodbatlas.CfnOnlineArchivePropsCollectionType"
)
class CfnOnlineArchivePropsCollectionType(enum.Enum):
    '''Classification of MongoDB database collection that you want to return.

    If you set this parameter to ``TIMESERIES``, set ``"criteria.type" : "date"`` and ``"criteria.dateFormat" : "ISODATE"``.

    :schema: CfnOnlineArchivePropsCollectionType
    '''

    STANDARD = "STANDARD"
    '''STANDARD.'''
    TIMESERIES = "TIMESERIES"
    '''TIMESERIES.'''


class CfnOrgInvitation(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnOrgInvitation",
):
    '''A CloudFormation ``MongoDB::Atlas::OrgInvitation``.

    :cloudformationResource: MongoDB::Atlas::OrgInvitation
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        profile: builtins.str,
        include_count: typing.Optional[builtins.bool] = None,
        invitation_id: typing.Optional[builtins.str] = None,
        items_per_page: typing.Optional[jsii.Number] = None,
        org_id: typing.Optional[builtins.str] = None,
        org_name: typing.Optional[builtins.str] = None,
        page_num: typing.Optional[jsii.Number] = None,
        roles: typing.Optional[typing.Sequence["CfnOrgInvitationPropsRoles"]] = None,
        team_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        total_count: typing.Optional[jsii.Number] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::OrgInvitation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param include_count: Flag that indicates whether the response returns the total number of items (**totalCount**) in the response.
        :param invitation_id: Unique 24-hexadecimal digit string that identifies the invitation.
        :param items_per_page: Number of items that the response returns per page.
        :param org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects.
        :param org_name: Human-readable label that identifies this organization.
        :param page_num: Number of the page that displays the current set of the total objects that the response returns.
        :param roles: One or more organization or project level roles to assign to the MongoDB Cloud user.
        :param team_ids: List of unique 24-hexadecimal digit strings that identifies each team.
        :param total_count: Number of documents returned in this response.
        :param username: Email address of the MongoDB Cloud user invited to join the organization.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b8ff8ce5f7a7ea00a66d0e978debe840bc4cbeceff0ce4d149b9417f22787a6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOrgInvitationProps(
            profile=profile,
            include_count=include_count,
            invitation_id=invitation_id,
            items_per_page=items_per_page,
            org_id=org_id,
            org_name=org_name,
            page_num=page_num,
            roles=roles,
            team_ids=team_ids,
            total_count=total_count,
            username=username,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::OrgInvitation.CreatedAt``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrExpiresAt")
    def attr_expires_at(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::OrgInvitation.ExpiresAt``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrExpiresAt"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::OrgInvitation.Id``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrInviterUsername")
    def attr_inviter_username(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::OrgInvitation.InviterUsername``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrInviterUsername"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnOrgInvitationProps":
        '''Resource props.'''
        return typing.cast("CfnOrgInvitationProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnOrgInvitationProps",
    jsii_struct_bases=[],
    name_mapping={
        "profile": "profile",
        "include_count": "includeCount",
        "invitation_id": "invitationId",
        "items_per_page": "itemsPerPage",
        "org_id": "orgId",
        "org_name": "orgName",
        "page_num": "pageNum",
        "roles": "roles",
        "team_ids": "teamIds",
        "total_count": "totalCount",
        "username": "username",
    },
)
class CfnOrgInvitationProps:
    def __init__(
        self,
        *,
        profile: builtins.str,
        include_count: typing.Optional[builtins.bool] = None,
        invitation_id: typing.Optional[builtins.str] = None,
        items_per_page: typing.Optional[jsii.Number] = None,
        org_id: typing.Optional[builtins.str] = None,
        org_name: typing.Optional[builtins.str] = None,
        page_num: typing.Optional[jsii.Number] = None,
        roles: typing.Optional[typing.Sequence["CfnOrgInvitationPropsRoles"]] = None,
        team_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        total_count: typing.Optional[jsii.Number] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Returns, adds, and edits organizational units in MongoDB Cloud.

        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param include_count: Flag that indicates whether the response returns the total number of items (**totalCount**) in the response.
        :param invitation_id: Unique 24-hexadecimal digit string that identifies the invitation.
        :param items_per_page: Number of items that the response returns per page.
        :param org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects.
        :param org_name: Human-readable label that identifies this organization.
        :param page_num: Number of the page that displays the current set of the total objects that the response returns.
        :param roles: One or more organization or project level roles to assign to the MongoDB Cloud user.
        :param team_ids: List of unique 24-hexadecimal digit strings that identifies each team.
        :param total_count: Number of documents returned in this response.
        :param username: Email address of the MongoDB Cloud user invited to join the organization.

        :schema: CfnOrgInvitationProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4debf5f8d3f86c022ce01796305d032e187d832088fee5bd7ccb6a59205e58c8)
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument include_count", value=include_count, expected_type=type_hints["include_count"])
            check_type(argname="argument invitation_id", value=invitation_id, expected_type=type_hints["invitation_id"])
            check_type(argname="argument items_per_page", value=items_per_page, expected_type=type_hints["items_per_page"])
            check_type(argname="argument org_id", value=org_id, expected_type=type_hints["org_id"])
            check_type(argname="argument org_name", value=org_name, expected_type=type_hints["org_name"])
            check_type(argname="argument page_num", value=page_num, expected_type=type_hints["page_num"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument team_ids", value=team_ids, expected_type=type_hints["team_ids"])
            check_type(argname="argument total_count", value=total_count, expected_type=type_hints["total_count"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "profile": profile,
        }
        if include_count is not None:
            self._values["include_count"] = include_count
        if invitation_id is not None:
            self._values["invitation_id"] = invitation_id
        if items_per_page is not None:
            self._values["items_per_page"] = items_per_page
        if org_id is not None:
            self._values["org_id"] = org_id
        if org_name is not None:
            self._values["org_name"] = org_name
        if page_num is not None:
            self._values["page_num"] = page_num
        if roles is not None:
            self._values["roles"] = roles
        if team_ids is not None:
            self._values["team_ids"] = team_ids
        if total_count is not None:
            self._values["total_count"] = total_count
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def profile(self) -> builtins.str:
        '''Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.

        :schema: CfnOrgInvitationProps#Profile
        '''
        result = self._values.get("profile")
        assert result is not None, "Required property 'profile' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def include_count(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether the response returns the total number of items (**totalCount**) in the response.

        :schema: CfnOrgInvitationProps#IncludeCount
        '''
        result = self._values.get("include_count")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def invitation_id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies the invitation.

        :schema: CfnOrgInvitationProps#InvitationId
        '''
        result = self._values.get("invitation_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def items_per_page(self) -> typing.Optional[jsii.Number]:
        '''Number of items that the response returns per page.

        :schema: CfnOrgInvitationProps#ItemsPerPage
        '''
        result = self._values.get("items_per_page")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def org_id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies the organization that contains your projects.

        :schema: CfnOrgInvitationProps#OrgId
        '''
        result = self._values.get("org_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def org_name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies this organization.

        :schema: CfnOrgInvitationProps#OrgName
        '''
        result = self._values.get("org_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def page_num(self) -> typing.Optional[jsii.Number]:
        '''Number of the page that displays the current set of the total objects that the response returns.

        :schema: CfnOrgInvitationProps#PageNum
        '''
        result = self._values.get("page_num")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def roles(self) -> typing.Optional[typing.List["CfnOrgInvitationPropsRoles"]]:
        '''One or more organization or project level roles to assign to the MongoDB Cloud user.

        :schema: CfnOrgInvitationProps#Roles
        '''
        result = self._values.get("roles")
        return typing.cast(typing.Optional[typing.List["CfnOrgInvitationPropsRoles"]], result)

    @builtins.property
    def team_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of unique 24-hexadecimal digit strings that identifies each team.

        :schema: CfnOrgInvitationProps#TeamIds
        '''
        result = self._values.get("team_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def total_count(self) -> typing.Optional[jsii.Number]:
        '''Number of documents returned in this response.

        :schema: CfnOrgInvitationProps#TotalCount
        '''
        result = self._values.get("total_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Email address of the MongoDB Cloud user invited to join the organization.

        :schema: CfnOrgInvitationProps#Username
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOrgInvitationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.CfnOrgInvitationPropsRoles")
class CfnOrgInvitationPropsRoles(enum.Enum):
    '''
    :schema: CfnOrgInvitationPropsRoles
    '''

    ORG_OWNER = "ORG_OWNER"
    '''ORG_OWNER.'''
    ORG_MEMBER = "ORG_MEMBER"
    '''ORG_MEMBER.'''
    ORG_GROUP_CREATOR = "ORG_GROUP_CREATOR"
    '''ORG_GROUP_CREATOR.'''
    ORG_BILLING_ADMIN = "ORG_BILLING_ADMIN"
    '''ORG_BILLING_ADMIN.'''
    ORG_READ_ONLY = "ORG_READ_ONLY"
    '''ORG_READ_ONLY.'''
    GROUP_CLUSTER_MANAGER = "GROUP_CLUSTER_MANAGER"
    '''GROUP_CLUSTER_MANAGER.'''
    GROUP_DATA_ACCESS_ADMIN = "GROUP_DATA_ACCESS_ADMIN"
    '''GROUP_DATA_ACCESS_ADMIN.'''
    GROUP_DATA_ACCESS_READ_ONLY = "GROUP_DATA_ACCESS_READ_ONLY"
    '''GROUP_DATA_ACCESS_READ_ONLY.'''
    GROUP_DATA_ACCESS_READ_WRITE = "GROUP_DATA_ACCESS_READ_WRITE"
    '''GROUP_DATA_ACCESS_READ_WRITE.'''
    GROUP_OWNER = "GROUP_OWNER"
    '''GROUP_OWNER.'''
    GROUP_READ_ONLY = "GROUP_READ_ONLY"
    '''GROUP_READ_ONLY.'''


class CfnPrivateEndPointRegionalMode(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnPrivateEndPointRegionalMode",
):
    '''A CloudFormation ``MongoDB::Atlas::PrivateEndPointRegionalMode``.

    :cloudformationResource: MongoDB::Atlas::PrivateEndPointRegionalMode
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        project_id: builtins.str,
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::PrivateEndPointRegionalMode``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd290a53b40e29a12f462b44c95c57ad20233cd8ec27bdbdc1fc106d01113bbb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPrivateEndPointRegionalModeProps(
            project_id=project_id, profile=profile
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnPrivateEndPointRegionalModeProps":
        '''Resource props.'''
        return typing.cast("CfnPrivateEndPointRegionalModeProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnPrivateEndPointRegionalModeProps",
    jsii_struct_bases=[],
    name_mapping={"project_id": "projectId", "profile": "profile"},
)
class CfnPrivateEndPointRegionalModeProps:
    def __init__(
        self,
        *,
        project_id: builtins.str,
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''An example resource schema demonstrating some basic constructs and validation rules.

        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.

        :schema: CfnPrivateEndPointRegionalModeProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5ff57abc06e2b5595ea609b4ae3ea8224a750d84b0f1dca9ec5bdfa5d2d0a73)
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_id": project_id,
        }
        if profile is not None:
            self._values["profile"] = profile

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnPrivateEndPointRegionalModeProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.

        :schema: CfnPrivateEndPointRegionalModeProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPrivateEndPointRegionalModeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnPrivateEndpoint(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnPrivateEndpoint",
):
    '''A CloudFormation ``MongoDB::Atlas::PrivateEndpoint``.

    :cloudformationResource: MongoDB::Atlas::PrivateEndpoint
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        group_id: builtins.str,
        region: builtins.str,
        endpoint_service_name: typing.Optional[builtins.str] = None,
        error_message: typing.Optional[builtins.str] = None,
        private_endpoints: typing.Optional[typing.Sequence[typing.Union["PrivateEndpoint", typing.Dict[builtins.str, typing.Any]]]] = None,
        profile: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::PrivateEndpoint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param group_id: Unique 24-hexadecimal digit string that identifies your project.
        :param region: Aws Region.
        :param endpoint_service_name: Name of the AWS PrivateLink endpoint service. Atlas returns null while it is creating the endpoint service.
        :param error_message: Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.
        :param private_endpoints: List of private endpoint associated to the service.
        :param profile: The profile is defined in AWS Secret manager. See [Secret Manager Profile setup (../../../examples/profile-secret.yaml)
        :param status: Status of the Atlas PrivateEndpoint service connection.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0dbda165f7b651d611d7156024f4f600cbf49239fe921d963641818d1bf4c19)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPrivateEndpointProps(
            group_id=group_id,
            region=region,
            endpoint_service_name=endpoint_service_name,
            error_message=error_message,
            private_endpoints=private_endpoints,
            profile=profile,
            status=status,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::PrivateEndpoint.Id``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrInterfaceEndpoints")
    def attr_interface_endpoints(self) -> typing.List[builtins.str]:
        '''Attribute ``MongoDB::Atlas::PrivateEndpoint.InterfaceEndpoints``.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrInterfaceEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnPrivateEndpointProps":
        '''Resource props.'''
        return typing.cast("CfnPrivateEndpointProps", jsii.get(self, "props"))


class CfnPrivateEndpointAdl(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnPrivateEndpointAdl",
):
    '''A CloudFormation ``MongoDB::Atlas::PrivateEndpointADL``.

    :cloudformationResource: MongoDB::Atlas::PrivateEndpointADL
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        project_id: builtins.str,
        provider: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        endpoint_id: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::PrivateEndpointADL``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param provider: Human-readable label that identifies the cloud service provider. Atlas Data Lake supports Amazon Web Services only.
        :param comment: Human-readable string to associate with this private endpoint.
        :param endpoint_id: Unique 22-character alphanumeric string that identifies the private endpoint.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param type: Human-readable label that identifies the resource type associated with this private endpoint.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93ffa99fc434f910a3dc07e98db360988b295acaf9b124a9debcdcb19ed5e568)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPrivateEndpointAdlProps(
            project_id=project_id,
            provider=provider,
            comment=comment,
            endpoint_id=endpoint_id,
            profile=profile,
            type=type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnPrivateEndpointAdlProps":
        '''Resource props.'''
        return typing.cast("CfnPrivateEndpointAdlProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnPrivateEndpointAdlProps",
    jsii_struct_bases=[],
    name_mapping={
        "project_id": "projectId",
        "provider": "provider",
        "comment": "comment",
        "endpoint_id": "endpointId",
        "profile": "profile",
        "type": "type",
    },
)
class CfnPrivateEndpointAdlProps:
    def __init__(
        self,
        *,
        project_id: builtins.str,
        provider: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        endpoint_id: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Adds one private endpoint for Federated Database Instances and Online Archives to the specified projects.

        To use this resource, the requesting API Key must have the Project Atlas Admin or Project Charts Admin roles. This resource doesn't require the API Key to have an Access List.

        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param provider: Human-readable label that identifies the cloud service provider. Atlas Data Lake supports Amazon Web Services only.
        :param comment: Human-readable string to associate with this private endpoint.
        :param endpoint_id: Unique 22-character alphanumeric string that identifies the private endpoint.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param type: Human-readable label that identifies the resource type associated with this private endpoint.

        :schema: CfnPrivateEndpointAdlProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef85df101cf97dd94f21606b0fa2a06158a450835b83d6a4b9a567769e27dfd1)
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument endpoint_id", value=endpoint_id, expected_type=type_hints["endpoint_id"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_id": project_id,
            "provider": provider,
        }
        if comment is not None:
            self._values["comment"] = comment
        if endpoint_id is not None:
            self._values["endpoint_id"] = endpoint_id
        if profile is not None:
            self._values["profile"] = profile
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnPrivateEndpointAdlProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def provider(self) -> builtins.str:
        '''Human-readable label that identifies the cloud service provider.

        Atlas Data Lake supports Amazon Web Services only.

        :schema: CfnPrivateEndpointAdlProps#Provider
        '''
        result = self._values.get("provider")
        assert result is not None, "Required property 'provider' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Human-readable string to associate with this private endpoint.

        :schema: CfnPrivateEndpointAdlProps#Comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint_id(self) -> typing.Optional[builtins.str]:
        '''Unique 22-character alphanumeric string that identifies the private endpoint.

        :schema: CfnPrivateEndpointAdlProps#EndpointId
        '''
        result = self._values.get("endpoint_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.

        :schema: CfnPrivateEndpointAdlProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the resource type associated with this private endpoint.

        :schema: CfnPrivateEndpointAdlProps#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPrivateEndpointAdlProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnPrivateEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "group_id": "groupId",
        "region": "region",
        "endpoint_service_name": "endpointServiceName",
        "error_message": "errorMessage",
        "private_endpoints": "privateEndpoints",
        "profile": "profile",
        "status": "status",
    },
)
class CfnPrivateEndpointProps:
    def __init__(
        self,
        *,
        group_id: builtins.str,
        region: builtins.str,
        endpoint_service_name: typing.Optional[builtins.str] = None,
        error_message: typing.Optional[builtins.str] = None,
        private_endpoints: typing.Optional[typing.Sequence[typing.Union["PrivateEndpoint", typing.Dict[builtins.str, typing.Any]]]] = None,
        profile: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The Private Endpoint creation flow consists of the creation of three related resources in the next order: 1.

        Atlas Private Endpoint Service 2. Aws VPC private Endpoint 3. Atlas Private Endpoint

        :param group_id: Unique 24-hexadecimal digit string that identifies your project.
        :param region: Aws Region.
        :param endpoint_service_name: Name of the AWS PrivateLink endpoint service. Atlas returns null while it is creating the endpoint service.
        :param error_message: Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.
        :param private_endpoints: List of private endpoint associated to the service.
        :param profile: The profile is defined in AWS Secret manager. See [Secret Manager Profile setup (../../../examples/profile-secret.yaml)
        :param status: Status of the Atlas PrivateEndpoint service connection.

        :schema: CfnPrivateEndpointProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46573598388bf535906c153a38c5e97b0d217854095d2c6e68527125ece7cde3)
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument endpoint_service_name", value=endpoint_service_name, expected_type=type_hints["endpoint_service_name"])
            check_type(argname="argument error_message", value=error_message, expected_type=type_hints["error_message"])
            check_type(argname="argument private_endpoints", value=private_endpoints, expected_type=type_hints["private_endpoints"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_id": group_id,
            "region": region,
        }
        if endpoint_service_name is not None:
            self._values["endpoint_service_name"] = endpoint_service_name
        if error_message is not None:
            self._values["error_message"] = error_message
        if private_endpoints is not None:
            self._values["private_endpoints"] = private_endpoints
        if profile is not None:
            self._values["profile"] = profile
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def group_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnPrivateEndpointProps#GroupId
        '''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Aws Region.

        :schema: CfnPrivateEndpointProps#Region
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_service_name(self) -> typing.Optional[builtins.str]:
        '''Name of the AWS PrivateLink endpoint service.

        Atlas returns null while it is creating the endpoint service.

        :schema: CfnPrivateEndpointProps#EndpointServiceName
        '''
        result = self._values.get("endpoint_service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error_message(self) -> typing.Optional[builtins.str]:
        '''Error message pertaining to the AWS PrivateLink connection.

        Returns null if there are no errors.

        :schema: CfnPrivateEndpointProps#ErrorMessage
        '''
        result = self._values.get("error_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_endpoints(self) -> typing.Optional[typing.List["PrivateEndpoint"]]:
        '''List of private endpoint associated to the service.

        :schema: CfnPrivateEndpointProps#PrivateEndpoints
        '''
        result = self._values.get("private_endpoints")
        return typing.cast(typing.Optional[typing.List["PrivateEndpoint"]], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''The profile is defined in AWS Secret manager.

        See [Secret Manager Profile setup (../../../examples/profile-secret.yaml)

        :schema: CfnPrivateEndpointProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Status of the Atlas PrivateEndpoint service connection.

        :schema: CfnPrivateEndpointProps#Status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPrivateEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnProject(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnProject",
):
    '''A CloudFormation ``MongoDB::Atlas::Project``.

    :cloudformationResource: MongoDB::Atlas::Project
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        org_id: builtins.str,
        profile: typing.Optional[builtins.str] = None,
        project_api_keys: typing.Optional[typing.Sequence[typing.Union["ProjectApiKey", typing.Dict[builtins.str, typing.Any]]]] = None,
        project_settings: typing.Optional[typing.Union["ProjectSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        project_teams: typing.Optional[typing.Sequence[typing.Union["ProjectTeam", typing.Dict[builtins.str, typing.Any]]]] = None,
        with_default_alerts_settings: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::Project``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: Name of the project to create.
        :param org_id: Unique identifier of the organization within which to create the project.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param project_api_keys: 
        :param project_settings: 
        :param project_teams: 
        :param with_default_alerts_settings: Flag that indicates whether to create the project with default alert settings.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd86e13237877e63b918eea83edf0a7eb5b7192a9299d3e126ca3b58578e33f0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProjectProps(
            name=name,
            org_id=org_id,
            profile=profile,
            project_api_keys=project_api_keys,
            project_settings=project_settings,
            project_teams=project_teams,
            with_default_alerts_settings=with_default_alerts_settings,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterCount")
    def attr_cluster_count(self) -> jsii.Number:
        '''Attribute ``MongoDB::Atlas::Project.ClusterCount``.'''
        return typing.cast(jsii.Number, jsii.get(self, "attrClusterCount"))

    @builtins.property
    @jsii.member(jsii_name="attrCreated")
    def attr_created(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Project.Created``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrCreated"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Project.Id``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrProjectOwnerId")
    def attr_project_owner_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Project.ProjectOwnerId``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectOwnerId"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnProjectProps":
        '''Resource props.'''
        return typing.cast("CfnProjectProps", jsii.get(self, "props"))


class CfnProjectInvitation(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnProjectInvitation",
):
    '''A CloudFormation ``MongoDB::Atlas::ProjectInvitation``.

    :cloudformationResource: MongoDB::Atlas::ProjectInvitation
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        invitation_id: typing.Optional[builtins.str] = None,
        page_num: typing.Optional[jsii.Number] = None,
        profile: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.Sequence["CfnProjectInvitationPropsRoles"]] = None,
        total_count: typing.Optional[jsii.Number] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::ProjectInvitation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param invitation_id: Unique 24-hexadecimal digit string that identifies the invitation.
        :param page_num: Number of the page that displays the current set of the total objects that the response returns.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param roles: One or more organization or project level roles to assign to the MongoDB Cloud user.
        :param total_count: Number of documents returned in this response.
        :param username: Email address of the user account invited to this project.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90fac7f9abc853c6415068d2b1ab6b61fd76f88b72c44d45a40492dd51a31c37)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProjectInvitationProps(
            invitation_id=invitation_id,
            page_num=page_num,
            profile=profile,
            project_id=project_id,
            roles=roles,
            total_count=total_count,
            username=username,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::ProjectInvitation.CreatedAt``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrExpiresAt")
    def attr_expires_at(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::ProjectInvitation.ExpiresAt``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrExpiresAt"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::ProjectInvitation.Id``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrInviterUsername")
    def attr_inviter_username(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::ProjectInvitation.InviterUsername``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrInviterUsername"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnProjectInvitationProps":
        '''Resource props.'''
        return typing.cast("CfnProjectInvitationProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnProjectInvitationProps",
    jsii_struct_bases=[],
    name_mapping={
        "invitation_id": "invitationId",
        "page_num": "pageNum",
        "profile": "profile",
        "project_id": "projectId",
        "roles": "roles",
        "total_count": "totalCount",
        "username": "username",
    },
)
class CfnProjectInvitationProps:
    def __init__(
        self,
        *,
        invitation_id: typing.Optional[builtins.str] = None,
        page_num: typing.Optional[jsii.Number] = None,
        profile: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.Sequence["CfnProjectInvitationPropsRoles"]] = None,
        total_count: typing.Optional[jsii.Number] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Returns, adds, and edits collections of clusters and users in MongoDB Cloud.

        :param invitation_id: Unique 24-hexadecimal digit string that identifies the invitation.
        :param page_num: Number of the page that displays the current set of the total objects that the response returns.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param roles: One or more organization or project level roles to assign to the MongoDB Cloud user.
        :param total_count: Number of documents returned in this response.
        :param username: Email address of the user account invited to this project.

        :schema: CfnProjectInvitationProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64950b750c4efa479cd1f86be0676ebda8c896441134de0602b875ece4fa2679)
            check_type(argname="argument invitation_id", value=invitation_id, expected_type=type_hints["invitation_id"])
            check_type(argname="argument page_num", value=page_num, expected_type=type_hints["page_num"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument total_count", value=total_count, expected_type=type_hints["total_count"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if invitation_id is not None:
            self._values["invitation_id"] = invitation_id
        if page_num is not None:
            self._values["page_num"] = page_num
        if profile is not None:
            self._values["profile"] = profile
        if project_id is not None:
            self._values["project_id"] = project_id
        if roles is not None:
            self._values["roles"] = roles
        if total_count is not None:
            self._values["total_count"] = total_count
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def invitation_id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies the invitation.

        :schema: CfnProjectInvitationProps#InvitationId
        '''
        result = self._values.get("invitation_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def page_num(self) -> typing.Optional[jsii.Number]:
        '''Number of the page that displays the current set of the total objects that the response returns.

        :schema: CfnProjectInvitationProps#PageNum
        '''
        result = self._values.get("page_num")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''The profile is defined in AWS Secret manager.

        See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnProjectInvitationProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnProjectInvitationProps#ProjectId
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def roles(self) -> typing.Optional[typing.List["CfnProjectInvitationPropsRoles"]]:
        '''One or more organization or project level roles to assign to the MongoDB Cloud user.

        :schema: CfnProjectInvitationProps#Roles
        '''
        result = self._values.get("roles")
        return typing.cast(typing.Optional[typing.List["CfnProjectInvitationPropsRoles"]], result)

    @builtins.property
    def total_count(self) -> typing.Optional[jsii.Number]:
        '''Number of documents returned in this response.

        :schema: CfnProjectInvitationProps#TotalCount
        '''
        result = self._values.get("total_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Email address of the user account invited to this project.

        :schema: CfnProjectInvitationProps#Username
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectInvitationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.CfnProjectInvitationPropsRoles")
class CfnProjectInvitationPropsRoles(enum.Enum):
    '''
    :schema: CfnProjectInvitationPropsRoles
    '''

    GROUP_CLUSTER_MANAGER = "GROUP_CLUSTER_MANAGER"
    '''GROUP_CLUSTER_MANAGER.'''
    GROUP_DATA_ACCESS_ADMIN = "GROUP_DATA_ACCESS_ADMIN"
    '''GROUP_DATA_ACCESS_ADMIN.'''
    GROUP_DATA_ACCESS_READ_ONLY = "GROUP_DATA_ACCESS_READ_ONLY"
    '''GROUP_DATA_ACCESS_READ_ONLY.'''
    GROUP_DATA_ACCESS_READ_WRITE = "GROUP_DATA_ACCESS_READ_WRITE"
    '''GROUP_DATA_ACCESS_READ_WRITE.'''
    GROUP_OWNER = "GROUP_OWNER"
    '''GROUP_OWNER.'''
    GROUP_READ_ONLY = "GROUP_READ_ONLY"
    '''GROUP_READ_ONLY.'''


class CfnProjectIpAccessList(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnProjectIpAccessList",
):
    '''A CloudFormation ``MongoDB::Atlas::ProjectIpAccessList``.

    :cloudformationResource: MongoDB::Atlas::ProjectIpAccessList
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        project_id: builtins.str,
        access_list: typing.Optional[typing.Sequence[typing.Union[AccessListDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
        list_options: typing.Optional[typing.Union["ListOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        profile: typing.Optional[builtins.str] = None,
        total_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::ProjectIpAccessList``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param access_list: 
        :param list_options: 
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param total_count: Number of documents returned in this response.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35c78432304d8ff29b8ff635279a10a18ae86da66b463c4be35eefb2b857aff3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProjectIpAccessListProps(
            project_id=project_id,
            access_list=access_list,
            list_options=list_options,
            profile=profile,
            total_count=total_count,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnProjectIpAccessListProps":
        '''Resource props.'''
        return typing.cast("CfnProjectIpAccessListProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnProjectIpAccessListProps",
    jsii_struct_bases=[],
    name_mapping={
        "project_id": "projectId",
        "access_list": "accessList",
        "list_options": "listOptions",
        "profile": "profile",
        "total_count": "totalCount",
    },
)
class CfnProjectIpAccessListProps:
    def __init__(
        self,
        *,
        project_id: builtins.str,
        access_list: typing.Optional[typing.Sequence[typing.Union[AccessListDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
        list_options: typing.Optional[typing.Union["ListOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        profile: typing.Optional[builtins.str] = None,
        total_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Returns, adds, edits, and removes network access limits to database deployments in MongoDB Cloud.

        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param access_list: 
        :param list_options: 
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param total_count: Number of documents returned in this response.

        :schema: CfnProjectIpAccessListProps
        '''
        if isinstance(list_options, dict):
            list_options = ListOptions(**list_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1967529b2e1355374728ffccdc38342d901bb46d7dbb4210cd964605a1cffd6)
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument access_list", value=access_list, expected_type=type_hints["access_list"])
            check_type(argname="argument list_options", value=list_options, expected_type=type_hints["list_options"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument total_count", value=total_count, expected_type=type_hints["total_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_id": project_id,
        }
        if access_list is not None:
            self._values["access_list"] = access_list
        if list_options is not None:
            self._values["list_options"] = list_options
        if profile is not None:
            self._values["profile"] = profile
        if total_count is not None:
            self._values["total_count"] = total_count

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnProjectIpAccessListProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_list(self) -> typing.Optional[typing.List[AccessListDefinition]]:
        '''
        :schema: CfnProjectIpAccessListProps#AccessList
        '''
        result = self._values.get("access_list")
        return typing.cast(typing.Optional[typing.List[AccessListDefinition]], result)

    @builtins.property
    def list_options(self) -> typing.Optional["ListOptions"]:
        '''
        :schema: CfnProjectIpAccessListProps#ListOptions
        '''
        result = self._values.get("list_options")
        return typing.cast(typing.Optional["ListOptions"], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.

        :schema: CfnProjectIpAccessListProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def total_count(self) -> typing.Optional[jsii.Number]:
        '''Number of documents returned in this response.

        :schema: CfnProjectIpAccessListProps#TotalCount
        '''
        result = self._values.get("total_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectIpAccessListProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnProjectProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "org_id": "orgId",
        "profile": "profile",
        "project_api_keys": "projectApiKeys",
        "project_settings": "projectSettings",
        "project_teams": "projectTeams",
        "with_default_alerts_settings": "withDefaultAlertsSettings",
    },
)
class CfnProjectProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        org_id: builtins.str,
        profile: typing.Optional[builtins.str] = None,
        project_api_keys: typing.Optional[typing.Sequence[typing.Union["ProjectApiKey", typing.Dict[builtins.str, typing.Any]]]] = None,
        project_settings: typing.Optional[typing.Union["ProjectSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        project_teams: typing.Optional[typing.Sequence[typing.Union["ProjectTeam", typing.Dict[builtins.str, typing.Any]]]] = None,
        with_default_alerts_settings: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Retrieves or creates projects in any given Atlas organization.

        :param name: Name of the project to create.
        :param org_id: Unique identifier of the organization within which to create the project.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param project_api_keys: 
        :param project_settings: 
        :param project_teams: 
        :param with_default_alerts_settings: Flag that indicates whether to create the project with default alert settings.

        :schema: CfnProjectProps
        '''
        if isinstance(project_settings, dict):
            project_settings = ProjectSettings(**project_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21510fd9984fce1826e8fccc145cf4e38e8554a29c5321d2960683f3d1851daf)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument org_id", value=org_id, expected_type=type_hints["org_id"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument project_api_keys", value=project_api_keys, expected_type=type_hints["project_api_keys"])
            check_type(argname="argument project_settings", value=project_settings, expected_type=type_hints["project_settings"])
            check_type(argname="argument project_teams", value=project_teams, expected_type=type_hints["project_teams"])
            check_type(argname="argument with_default_alerts_settings", value=with_default_alerts_settings, expected_type=type_hints["with_default_alerts_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "org_id": org_id,
        }
        if profile is not None:
            self._values["profile"] = profile
        if project_api_keys is not None:
            self._values["project_api_keys"] = project_api_keys
        if project_settings is not None:
            self._values["project_settings"] = project_settings
        if project_teams is not None:
            self._values["project_teams"] = project_teams
        if with_default_alerts_settings is not None:
            self._values["with_default_alerts_settings"] = with_default_alerts_settings

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the project to create.

        :schema: CfnProjectProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def org_id(self) -> builtins.str:
        '''Unique identifier of the organization within which to create the project.

        :schema: CfnProjectProps#OrgId
        '''
        result = self._values.get("org_id")
        assert result is not None, "Required property 'org_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.

        :schema: CfnProjectProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_api_keys(self) -> typing.Optional[typing.List["ProjectApiKey"]]:
        '''
        :schema: CfnProjectProps#ProjectApiKeys
        '''
        result = self._values.get("project_api_keys")
        return typing.cast(typing.Optional[typing.List["ProjectApiKey"]], result)

    @builtins.property
    def project_settings(self) -> typing.Optional["ProjectSettings"]:
        '''
        :schema: CfnProjectProps#ProjectSettings
        '''
        result = self._values.get("project_settings")
        return typing.cast(typing.Optional["ProjectSettings"], result)

    @builtins.property
    def project_teams(self) -> typing.Optional[typing.List["ProjectTeam"]]:
        '''
        :schema: CfnProjectProps#ProjectTeams
        '''
        result = self._values.get("project_teams")
        return typing.cast(typing.Optional[typing.List["ProjectTeam"]], result)

    @builtins.property
    def with_default_alerts_settings(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether to create the project with default alert settings.

        :schema: CfnProjectProps#WithDefaultAlertsSettings
        '''
        result = self._values.get("with_default_alerts_settings")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnSearchIndex(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnSearchIndex",
):
    '''A CloudFormation ``MongoDB::Atlas::SearchIndex``.

    :cloudformationResource: MongoDB::Atlas::SearchIndex
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster_name: builtins.str,
        collection_name: builtins.str,
        database: builtins.str,
        mappings: typing.Union[ApiAtlasFtsMappingsViewManual, typing.Dict[builtins.str, typing.Any]],
        analyzer: typing.Optional[builtins.str] = None,
        analyzers: typing.Optional[typing.Sequence[typing.Union[ApiAtlasFtsAnalyzersViewManual, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        search_analyzer: typing.Optional[builtins.str] = None,
        synonyms: typing.Optional[typing.Sequence[typing.Union[ApiAtlasFtsSynonymMappingDefinitionView, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::SearchIndex``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cluster_name: Name of the cluster that contains the database and collection with one or more Application Search indexes.
        :param collection_name: Human-readable label that identifies the collection that contains one or more Atlas Search indexes.
        :param database: Human-readable label that identifies the database that contains the collection with one or more Atlas Search indexes.
        :param mappings: Index specifications for the collection's fields.
        :param analyzer: Specific pre-defined method chosen to convert database field text into searchable words. This conversion reduces the text of fields into the smallest units of text. These units are called a **term** or **token**. This process, known as tokenization, involves a variety of changes made to the text in fields: - extracting words - removing punctuation - removing accents - changing to lowercase - removing common words - reducing words to their root form (stemming) - changing words to their base form (lemmatization) MongoDB Cloud uses the selected process to build the Atlas Search index.
        :param analyzers: List of user-defined methods to convert database field text into searchable words.
        :param name: Human-readable label that identifies this index. Within each namespace, names of all indexes in the namespace must be unique.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param search_analyzer: Method applied to identify words when searching this index.
        :param synonyms: Rule sets that map words to their synonyms in this index.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b13164dd11ebbec9ed7c892c14e8bbeddef284fe865e7f4b3f8b6cbb00703b99)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSearchIndexProps(
            cluster_name=cluster_name,
            collection_name=collection_name,
            database=database,
            mappings=mappings,
            analyzer=analyzer,
            analyzers=analyzers,
            name=name,
            profile=profile,
            project_id=project_id,
            search_analyzer=search_analyzer,
            synonyms=synonyms,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrIndexId")
    def attr_index_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::SearchIndex.IndexId``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrIndexId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::SearchIndex.Status``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnSearchIndexProps":
        '''Resource props.'''
        return typing.cast("CfnSearchIndexProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnSearchIndexProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_name": "clusterName",
        "collection_name": "collectionName",
        "database": "database",
        "mappings": "mappings",
        "analyzer": "analyzer",
        "analyzers": "analyzers",
        "name": "name",
        "profile": "profile",
        "project_id": "projectId",
        "search_analyzer": "searchAnalyzer",
        "synonyms": "synonyms",
    },
)
class CfnSearchIndexProps:
    def __init__(
        self,
        *,
        cluster_name: builtins.str,
        collection_name: builtins.str,
        database: builtins.str,
        mappings: typing.Union[ApiAtlasFtsMappingsViewManual, typing.Dict[builtins.str, typing.Any]],
        analyzer: typing.Optional[builtins.str] = None,
        analyzers: typing.Optional[typing.Sequence[typing.Union[ApiAtlasFtsAnalyzersViewManual, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        search_analyzer: typing.Optional[builtins.str] = None,
        synonyms: typing.Optional[typing.Sequence[typing.Union[ApiAtlasFtsSynonymMappingDefinitionView, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Returns, adds, edits, and removes Atlas Search indexes.

        Also returns and updates user-defined analyzers.

        :param cluster_name: Name of the cluster that contains the database and collection with one or more Application Search indexes.
        :param collection_name: Human-readable label that identifies the collection that contains one or more Atlas Search indexes.
        :param database: Human-readable label that identifies the database that contains the collection with one or more Atlas Search indexes.
        :param mappings: Index specifications for the collection's fields.
        :param analyzer: Specific pre-defined method chosen to convert database field text into searchable words. This conversion reduces the text of fields into the smallest units of text. These units are called a **term** or **token**. This process, known as tokenization, involves a variety of changes made to the text in fields: - extracting words - removing punctuation - removing accents - changing to lowercase - removing common words - reducing words to their root form (stemming) - changing words to their base form (lemmatization) MongoDB Cloud uses the selected process to build the Atlas Search index.
        :param analyzers: List of user-defined methods to convert database field text into searchable words.
        :param name: Human-readable label that identifies this index. Within each namespace, names of all indexes in the namespace must be unique.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param search_analyzer: Method applied to identify words when searching this index.
        :param synonyms: Rule sets that map words to their synonyms in this index.

        :schema: CfnSearchIndexProps
        '''
        if isinstance(mappings, dict):
            mappings = ApiAtlasFtsMappingsViewManual(**mappings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d4e976f5c6c5f42fe823f301f998aa27f79845058acebf22b666fb42a65238c)
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument collection_name", value=collection_name, expected_type=type_hints["collection_name"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument mappings", value=mappings, expected_type=type_hints["mappings"])
            check_type(argname="argument analyzer", value=analyzer, expected_type=type_hints["analyzer"])
            check_type(argname="argument analyzers", value=analyzers, expected_type=type_hints["analyzers"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument search_analyzer", value=search_analyzer, expected_type=type_hints["search_analyzer"])
            check_type(argname="argument synonyms", value=synonyms, expected_type=type_hints["synonyms"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_name": cluster_name,
            "collection_name": collection_name,
            "database": database,
            "mappings": mappings,
        }
        if analyzer is not None:
            self._values["analyzer"] = analyzer
        if analyzers is not None:
            self._values["analyzers"] = analyzers
        if name is not None:
            self._values["name"] = name
        if profile is not None:
            self._values["profile"] = profile
        if project_id is not None:
            self._values["project_id"] = project_id
        if search_analyzer is not None:
            self._values["search_analyzer"] = search_analyzer
        if synonyms is not None:
            self._values["synonyms"] = synonyms

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''Name of the cluster that contains the database and collection with one or more Application Search indexes.

        :schema: CfnSearchIndexProps#ClusterName
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def collection_name(self) -> builtins.str:
        '''Human-readable label that identifies the collection that contains one or more Atlas Search indexes.

        :schema: CfnSearchIndexProps#CollectionName
        '''
        result = self._values.get("collection_name")
        assert result is not None, "Required property 'collection_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database(self) -> builtins.str:
        '''Human-readable label that identifies the database that contains the collection with one or more Atlas Search indexes.

        :schema: CfnSearchIndexProps#Database
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mappings(self) -> ApiAtlasFtsMappingsViewManual:
        '''Index specifications for the collection's fields.

        :schema: CfnSearchIndexProps#Mappings
        '''
        result = self._values.get("mappings")
        assert result is not None, "Required property 'mappings' is missing"
        return typing.cast(ApiAtlasFtsMappingsViewManual, result)

    @builtins.property
    def analyzer(self) -> typing.Optional[builtins.str]:
        '''Specific pre-defined method chosen to convert database field text into searchable words.

        This conversion reduces the text of fields into the smallest units of text. These units are called a **term** or **token**. This process, known as tokenization, involves a variety of changes made to the text in fields:

        - extracting words
        - removing punctuation
        - removing accents
        - changing to lowercase
        - removing common words
        - reducing words to their root form (stemming)
        - changing words to their base form (lemmatization)
          MongoDB Cloud uses the selected process to build the Atlas Search index.

        :schema: CfnSearchIndexProps#Analyzer
        '''
        result = self._values.get("analyzer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def analyzers(self) -> typing.Optional[typing.List[ApiAtlasFtsAnalyzersViewManual]]:
        '''List of user-defined methods to convert database field text into searchable words.

        :schema: CfnSearchIndexProps#Analyzers
        '''
        result = self._values.get("analyzers")
        return typing.cast(typing.Optional[typing.List[ApiAtlasFtsAnalyzersViewManual]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies this index.

        Within each namespace, names of all indexes in the namespace must be unique.

        :schema: CfnSearchIndexProps#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''The profile is defined in AWS Secret manager.

        See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnSearchIndexProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnSearchIndexProps#ProjectId
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def search_analyzer(self) -> typing.Optional[builtins.str]:
        '''Method applied to identify words when searching this index.

        :schema: CfnSearchIndexProps#SearchAnalyzer
        '''
        result = self._values.get("search_analyzer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def synonyms(
        self,
    ) -> typing.Optional[typing.List[ApiAtlasFtsSynonymMappingDefinitionView]]:
        '''Rule sets that map words to their synonyms in this index.

        :schema: CfnSearchIndexProps#Synonyms
        '''
        result = self._values.get("synonyms")
        return typing.cast(typing.Optional[typing.List[ApiAtlasFtsSynonymMappingDefinitionView]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSearchIndexProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnServerlessInstance(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnServerlessInstance",
):
    '''A CloudFormation ``MongoDB::Atlas::ServerlessInstance``.

    :cloudformationResource: MongoDB::Atlas::ServerlessInstance
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        connection_strings: typing.Optional[typing.Union["ServerlessInstanceConnectionStrings", typing.Dict[builtins.str, typing.Any]]] = None,
        continuous_backup_enabled: typing.Optional[builtins.bool] = None,
        include_count: typing.Optional[builtins.bool] = None,
        items_per_page: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        page_num: typing.Optional[jsii.Number] = None,
        profile: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        provider_settings: typing.Optional[typing.Union["ServerlessInstanceProviderSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        termination_protection_enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::ServerlessInstance``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param connection_strings: Collection of Uniform Resource Locators that point to the MongoDB database.
        :param continuous_backup_enabled: Flag that indicates whether the serverless instances uses Serverless Continuous Backup. If this parameter is false, the serverless instance uses Basic Backup. | Option | Description | |---|---| | Serverless Continuous Backup | Atlas takes incremental snapshots of the data in your serverless instance every six hours and lets you restore the data from a selected point in time within the last 72 hours. Atlas also takes daily snapshots and retains these daily snapshots for 35 days. To learn more, see Serverless Instance Costs. | | Basic Backup | Atlas takes incremental snapshots of the data in your serverless instance every six hours and retains only the two most recent snapshots. You can use this option for free.
        :param include_count: Flag that indicates whether the response returns the total number of items (**totalCount**) in the response.
        :param items_per_page: Number of items that the response returns per page.
        :param name: Human-readable label that identifies the serverless instance.
        :param page_num: Number of the page that displays the current set of the total objects that the response returns.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param provider_settings: Group of settings that configure the provisioned MongoDB serverless instance. The options available relate to the cloud service provider.
        :param termination_protection_enabled: Flag that indicates whether termination protection is enabled on the serverless instance. If set to true, MongoDB Cloud won't delete the serverless instance. If set to false, MongoDB cloud will delete the serverless instance."
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71c2fac1e4b79aeb2fe8c14ae8952822335988c0afa9fbc18ab1bec25c7cc2b5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServerlessInstanceProps(
            connection_strings=connection_strings,
            continuous_backup_enabled=continuous_backup_enabled,
            include_count=include_count,
            items_per_page=items_per_page,
            name=name,
            page_num=page_num,
            profile=profile,
            project_id=project_id,
            provider_settings=provider_settings,
            termination_protection_enabled=termination_protection_enabled,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreateDate")
    def attr_create_date(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::ServerlessInstance.CreateDate``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrCreateDate"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::ServerlessInstance.Id``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrMongoDBVersion")
    def attr_mongo_db_version(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::ServerlessInstance.MongoDBVersion``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrMongoDBVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrStateName")
    def attr_state_name(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::ServerlessInstance.StateName``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrStateName"))

    @builtins.property
    @jsii.member(jsii_name="attrTotalCount")
    def attr_total_count(self) -> jsii.Number:
        '''Attribute ``MongoDB::Atlas::ServerlessInstance.TotalCount``.'''
        return typing.cast(jsii.Number, jsii.get(self, "attrTotalCount"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnServerlessInstanceProps":
        '''Resource props.'''
        return typing.cast("CfnServerlessInstanceProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnServerlessInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "connection_strings": "connectionStrings",
        "continuous_backup_enabled": "continuousBackupEnabled",
        "include_count": "includeCount",
        "items_per_page": "itemsPerPage",
        "name": "name",
        "page_num": "pageNum",
        "profile": "profile",
        "project_id": "projectId",
        "provider_settings": "providerSettings",
        "termination_protection_enabled": "terminationProtectionEnabled",
    },
)
class CfnServerlessInstanceProps:
    def __init__(
        self,
        *,
        connection_strings: typing.Optional[typing.Union["ServerlessInstanceConnectionStrings", typing.Dict[builtins.str, typing.Any]]] = None,
        continuous_backup_enabled: typing.Optional[builtins.bool] = None,
        include_count: typing.Optional[builtins.bool] = None,
        items_per_page: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        page_num: typing.Optional[jsii.Number] = None,
        profile: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        provider_settings: typing.Optional[typing.Union["ServerlessInstanceProviderSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        termination_protection_enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Returns, adds, edits, and removes serverless instances.

        :param connection_strings: Collection of Uniform Resource Locators that point to the MongoDB database.
        :param continuous_backup_enabled: Flag that indicates whether the serverless instances uses Serverless Continuous Backup. If this parameter is false, the serverless instance uses Basic Backup. | Option | Description | |---|---| | Serverless Continuous Backup | Atlas takes incremental snapshots of the data in your serverless instance every six hours and lets you restore the data from a selected point in time within the last 72 hours. Atlas also takes daily snapshots and retains these daily snapshots for 35 days. To learn more, see Serverless Instance Costs. | | Basic Backup | Atlas takes incremental snapshots of the data in your serverless instance every six hours and retains only the two most recent snapshots. You can use this option for free.
        :param include_count: Flag that indicates whether the response returns the total number of items (**totalCount**) in the response.
        :param items_per_page: Number of items that the response returns per page.
        :param name: Human-readable label that identifies the serverless instance.
        :param page_num: Number of the page that displays the current set of the total objects that the response returns.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param provider_settings: Group of settings that configure the provisioned MongoDB serverless instance. The options available relate to the cloud service provider.
        :param termination_protection_enabled: Flag that indicates whether termination protection is enabled on the serverless instance. If set to true, MongoDB Cloud won't delete the serverless instance. If set to false, MongoDB cloud will delete the serverless instance."

        :schema: CfnServerlessInstanceProps
        '''
        if isinstance(connection_strings, dict):
            connection_strings = ServerlessInstanceConnectionStrings(**connection_strings)
        if isinstance(provider_settings, dict):
            provider_settings = ServerlessInstanceProviderSettings(**provider_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d484760f72034dea11f0a7d6b1ec64440d35ec4867e3d0503e858340a4744b35)
            check_type(argname="argument connection_strings", value=connection_strings, expected_type=type_hints["connection_strings"])
            check_type(argname="argument continuous_backup_enabled", value=continuous_backup_enabled, expected_type=type_hints["continuous_backup_enabled"])
            check_type(argname="argument include_count", value=include_count, expected_type=type_hints["include_count"])
            check_type(argname="argument items_per_page", value=items_per_page, expected_type=type_hints["items_per_page"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument page_num", value=page_num, expected_type=type_hints["page_num"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument provider_settings", value=provider_settings, expected_type=type_hints["provider_settings"])
            check_type(argname="argument termination_protection_enabled", value=termination_protection_enabled, expected_type=type_hints["termination_protection_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_strings is not None:
            self._values["connection_strings"] = connection_strings
        if continuous_backup_enabled is not None:
            self._values["continuous_backup_enabled"] = continuous_backup_enabled
        if include_count is not None:
            self._values["include_count"] = include_count
        if items_per_page is not None:
            self._values["items_per_page"] = items_per_page
        if name is not None:
            self._values["name"] = name
        if page_num is not None:
            self._values["page_num"] = page_num
        if profile is not None:
            self._values["profile"] = profile
        if project_id is not None:
            self._values["project_id"] = project_id
        if provider_settings is not None:
            self._values["provider_settings"] = provider_settings
        if termination_protection_enabled is not None:
            self._values["termination_protection_enabled"] = termination_protection_enabled

    @builtins.property
    def connection_strings(
        self,
    ) -> typing.Optional["ServerlessInstanceConnectionStrings"]:
        '''Collection of Uniform Resource Locators that point to the MongoDB database.

        :schema: CfnServerlessInstanceProps#ConnectionStrings
        '''
        result = self._values.get("connection_strings")
        return typing.cast(typing.Optional["ServerlessInstanceConnectionStrings"], result)

    @builtins.property
    def continuous_backup_enabled(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether the serverless instances uses Serverless Continuous Backup.

        If this parameter is false, the serverless instance uses Basic Backup. | Option | Description | |---|---| | Serverless Continuous Backup | Atlas takes incremental snapshots of the data in your serverless instance every six hours and lets you restore the data from a selected point in time within the last 72 hours. Atlas also takes daily snapshots and retains these daily snapshots for 35 days. To learn more, see Serverless Instance Costs. | | Basic Backup | Atlas takes incremental snapshots of the data in your serverless instance every six hours and retains only the two most recent snapshots. You can use this option for free.

        :schema: CfnServerlessInstanceProps#ContinuousBackupEnabled
        '''
        result = self._values.get("continuous_backup_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def include_count(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether the response returns the total number of items (**totalCount**) in the response.

        :schema: CfnServerlessInstanceProps#IncludeCount
        '''
        result = self._values.get("include_count")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def items_per_page(self) -> typing.Optional[jsii.Number]:
        '''Number of items that the response returns per page.

        :schema: CfnServerlessInstanceProps#ItemsPerPage
        '''
        result = self._values.get("items_per_page")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the serverless instance.

        :schema: CfnServerlessInstanceProps#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def page_num(self) -> typing.Optional[jsii.Number]:
        '''Number of the page that displays the current set of the total objects that the response returns.

        :schema: CfnServerlessInstanceProps#PageNum
        '''
        result = self._values.get("page_num")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.

        :schema: CfnServerlessInstanceProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnServerlessInstanceProps#ProjectID
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider_settings(
        self,
    ) -> typing.Optional["ServerlessInstanceProviderSettings"]:
        '''Group of settings that configure the provisioned MongoDB serverless instance.

        The options available relate to the cloud service provider.

        :schema: CfnServerlessInstanceProps#ProviderSettings
        '''
        result = self._values.get("provider_settings")
        return typing.cast(typing.Optional["ServerlessInstanceProviderSettings"], result)

    @builtins.property
    def termination_protection_enabled(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether termination protection is enabled on the serverless instance.

        If set to true, MongoDB Cloud won't delete the serverless instance. If set to false, MongoDB cloud will delete the serverless instance."

        :schema: CfnServerlessInstanceProps#TerminationProtectionEnabled
        '''
        result = self._values.get("termination_protection_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServerlessInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnTeams(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnTeams",
):
    '''A CloudFormation ``MongoDB::Atlas::Teams``.

    :cloudformationResource: MongoDB::Atlas::Teams
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: typing.Optional[builtins.str] = None,
        org_id: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        role_names: typing.Optional[typing.Sequence["CfnTeamsPropsRoleNames"]] = None,
        usernames: typing.Optional[typing.Sequence[builtins.str]] = None,
        users: typing.Optional[typing.Sequence[typing.Union[AtlasUser, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::Teams``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: Unique 24-hexadecimal character string that identifies the team.
        :param org_id: Unique 24-hexadecimal character string that identifies the team.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param project_id: Unique 24-hexadecimal character string that identifies the project.
        :param role_names: One or more organization- or project-level roles to assign to the MongoDB Cloud user.
        :param usernames: One or more organization- or project-level roles to assign to the MongoDB Cloud user.
        :param users: List of returned documents that MongoDB Cloud provides when completing this request.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf5e9c70fe6389958baf6253e0662ec2c9d33390b067c6ad31b0899588d24378)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTeamsProps(
            name=name,
            org_id=org_id,
            profile=profile,
            project_id=project_id,
            role_names=role_names,
            usernames=usernames,
            users=users,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrTeamId")
    def attr_team_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Teams.TeamId``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrTeamId"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnTeamsProps":
        '''Resource props.'''
        return typing.cast("CfnTeamsProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnTeamsProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "org_id": "orgId",
        "profile": "profile",
        "project_id": "projectId",
        "role_names": "roleNames",
        "usernames": "usernames",
        "users": "users",
    },
)
class CfnTeamsProps:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        org_id: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        role_names: typing.Optional[typing.Sequence["CfnTeamsPropsRoleNames"]] = None,
        usernames: typing.Optional[typing.Sequence[builtins.str]] = None,
        users: typing.Optional[typing.Sequence[typing.Union[AtlasUser, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Adds one team to the specified project.

        All members of the team share the same project access. To use this resource, the requesting API Key must have the Project User Admin role. This resource doesn't require the API Key to have an Access List.

        :param name: Unique 24-hexadecimal character string that identifies the team.
        :param org_id: Unique 24-hexadecimal character string that identifies the team.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param project_id: Unique 24-hexadecimal character string that identifies the project.
        :param role_names: One or more organization- or project-level roles to assign to the MongoDB Cloud user.
        :param usernames: One or more organization- or project-level roles to assign to the MongoDB Cloud user.
        :param users: List of returned documents that MongoDB Cloud provides when completing this request.

        :schema: CfnTeamsProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a745e370f70f5b5f1354161322a7e239c35a2b265f58562ffb60e5564303102)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument org_id", value=org_id, expected_type=type_hints["org_id"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument role_names", value=role_names, expected_type=type_hints["role_names"])
            check_type(argname="argument usernames", value=usernames, expected_type=type_hints["usernames"])
            check_type(argname="argument users", value=users, expected_type=type_hints["users"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if org_id is not None:
            self._values["org_id"] = org_id
        if profile is not None:
            self._values["profile"] = profile
        if project_id is not None:
            self._values["project_id"] = project_id
        if role_names is not None:
            self._values["role_names"] = role_names
        if usernames is not None:
            self._values["usernames"] = usernames
        if users is not None:
            self._values["users"] = users

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal character string that identifies the team.

        :schema: CfnTeamsProps#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def org_id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal character string that identifies the team.

        :schema: CfnTeamsProps#OrgId
        '''
        result = self._values.get("org_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''The profile is defined in AWS Secret manager.

        See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnTeamsProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal character string that identifies the project.

        :schema: CfnTeamsProps#ProjectId
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_names(self) -> typing.Optional[typing.List["CfnTeamsPropsRoleNames"]]:
        '''One or more organization- or project-level roles to assign to the MongoDB Cloud user.

        :schema: CfnTeamsProps#RoleNames
        '''
        result = self._values.get("role_names")
        return typing.cast(typing.Optional[typing.List["CfnTeamsPropsRoleNames"]], result)

    @builtins.property
    def usernames(self) -> typing.Optional[typing.List[builtins.str]]:
        '''One or more organization- or project-level roles to assign to the MongoDB Cloud user.

        :schema: CfnTeamsProps#Usernames
        '''
        result = self._values.get("usernames")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def users(self) -> typing.Optional[typing.List[AtlasUser]]:
        '''List of returned documents that MongoDB Cloud provides when completing this request.

        :schema: CfnTeamsProps#Users
        '''
        result = self._values.get("users")
        return typing.cast(typing.Optional[typing.List[AtlasUser]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTeamsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.CfnTeamsPropsRoleNames")
class CfnTeamsPropsRoleNames(enum.Enum):
    '''
    :schema: CfnTeamsPropsRoleNames
    '''

    GROUP_CLUSTER_MANAGER = "GROUP_CLUSTER_MANAGER"
    '''GROUP_CLUSTER_MANAGER.'''
    GROUP_DATA_ACCESS_ADMIN = "GROUP_DATA_ACCESS_ADMIN"
    '''GROUP_DATA_ACCESS_ADMIN.'''
    GROUP_DATA_ACCESS_READ_ONLY = "GROUP_DATA_ACCESS_READ_ONLY"
    '''GROUP_DATA_ACCESS_READ_ONLY.'''
    GROUP_DATA_ACCESS_READ_WRITE = "GROUP_DATA_ACCESS_READ_WRITE"
    '''GROUP_DATA_ACCESS_READ_WRITE.'''
    GROUP_OWNER = "GROUP_OWNER"
    '''GROUP_OWNER.'''
    GROUP_READ_ONLY = "GROUP_READ_ONLY"
    '''GROUP_READ_ONLY.'''


class CfnThirdPartyIntegration(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnThirdPartyIntegration",
):
    '''A CloudFormation ``MongoDB::Atlas::ThirdPartyIntegration``.

    :cloudformationResource: MongoDB::Atlas::ThirdPartyIntegration
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_key: typing.Optional[builtins.str] = None,
        api_token: typing.Optional[builtins.str] = None,
        channel_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
        listen_address: typing.Optional[builtins.str] = None,
        microsoft_teams_webhook_url: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        routing_key: typing.Optional[builtins.str] = None,
        scheme: typing.Optional["CfnThirdPartyIntegrationPropsScheme"] = None,
        secret: typing.Optional[builtins.str] = None,
        service_discovery: typing.Optional["CfnThirdPartyIntegrationPropsServiceDiscovery"] = None,
        service_key: typing.Optional[builtins.str] = None,
        team_name: typing.Optional[builtins.str] = None,
        tls_pem_path: typing.Optional[builtins.str] = None,
        type: typing.Optional["CfnThirdPartyIntegrationPropsType"] = None,
        url: typing.Optional[builtins.str] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::ThirdPartyIntegration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_key: Key that allows MongoDB Cloud to access your Opsgenie/Datadog account.
        :param api_token: Key that allows MongoDB Cloud to access your Slack account.
        :param channel_name: Name of the Slack channel to which MongoDB Cloud sends alert notifications.
        :param enabled: Flag that indicates whether someone has activated the Prometheus integration.
        :param listen_address: Combination of IPv4 address and Internet Assigned Numbers Authority (IANA) port or the IANA port alone to which Prometheus binds to ingest MongoDB metrics.
        :param microsoft_teams_webhook_url: Endpoint web address of the Microsoft Teams webhook to which MongoDB Cloud sends notifications.
        :param password: Password required for your integration with Prometheus.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param region: Two-letter code that indicates which regional URL MongoDB uses to access the Opsgenie/Datadog API.
        :param routing_key: Routing key associated with your Splunk On-Call account.
        :param scheme: Security Scheme to apply to HyperText Transfer Protocol (HTTP) traffic between Prometheus and MongoDB Cloud.
        :param secret: Parameter returned if someone configure this webhook with a secret.
        :param service_discovery: Desired method to discover the Prometheus service.
        :param service_key: Service key associated with your PagerDuty account.
        :param team_name: Human-readable label that identifies your Slack team. Set this parameter when you configure a legacy Slack integration.
        :param tls_pem_path: Root-relative path to the Transport Layer Security (TLS) Privacy Enhanced Mail (PEM) key and certificate file on the host.
        :param type: Human-readable label that identifies the service to which you want to integrate with MongoDB Cloud. The value must match the third-party service integration type.
        :param url: Endpoint web address to which MongoDB Cloud sends notifications.
        :param user_name: Human-readable label that identifies your Prometheus incoming webhook.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5130cb31b4f4c657c02dff85f9317186b660fbbaa5e5e2a99aad6ebc444b618)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnThirdPartyIntegrationProps(
            api_key=api_key,
            api_token=api_token,
            channel_name=channel_name,
            enabled=enabled,
            listen_address=listen_address,
            microsoft_teams_webhook_url=microsoft_teams_webhook_url,
            password=password,
            profile=profile,
            project_id=project_id,
            region=region,
            routing_key=routing_key,
            scheme=scheme,
            secret=secret,
            service_discovery=service_discovery,
            service_key=service_key,
            team_name=team_name,
            tls_pem_path=tls_pem_path,
            type=type,
            url=url,
            user_name=user_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnThirdPartyIntegrationProps":
        '''Resource props.'''
        return typing.cast("CfnThirdPartyIntegrationProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnThirdPartyIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_key": "apiKey",
        "api_token": "apiToken",
        "channel_name": "channelName",
        "enabled": "enabled",
        "listen_address": "listenAddress",
        "microsoft_teams_webhook_url": "microsoftTeamsWebhookUrl",
        "password": "password",
        "profile": "profile",
        "project_id": "projectId",
        "region": "region",
        "routing_key": "routingKey",
        "scheme": "scheme",
        "secret": "secret",
        "service_discovery": "serviceDiscovery",
        "service_key": "serviceKey",
        "team_name": "teamName",
        "tls_pem_path": "tlsPemPath",
        "type": "type",
        "url": "url",
        "user_name": "userName",
    },
)
class CfnThirdPartyIntegrationProps:
    def __init__(
        self,
        *,
        api_key: typing.Optional[builtins.str] = None,
        api_token: typing.Optional[builtins.str] = None,
        channel_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
        listen_address: typing.Optional[builtins.str] = None,
        microsoft_teams_webhook_url: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        routing_key: typing.Optional[builtins.str] = None,
        scheme: typing.Optional["CfnThirdPartyIntegrationPropsScheme"] = None,
        secret: typing.Optional[builtins.str] = None,
        service_discovery: typing.Optional["CfnThirdPartyIntegrationPropsServiceDiscovery"] = None,
        service_key: typing.Optional[builtins.str] = None,
        team_name: typing.Optional[builtins.str] = None,
        tls_pem_path: typing.Optional[builtins.str] = None,
        type: typing.Optional["CfnThirdPartyIntegrationPropsType"] = None,
        url: typing.Optional[builtins.str] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Returns, adds, edits, and removes third-party service integration configurations.

        MongoDB Cloud sends alerts to each third-party service that you configure.

        :param api_key: Key that allows MongoDB Cloud to access your Opsgenie/Datadog account.
        :param api_token: Key that allows MongoDB Cloud to access your Slack account.
        :param channel_name: Name of the Slack channel to which MongoDB Cloud sends alert notifications.
        :param enabled: Flag that indicates whether someone has activated the Prometheus integration.
        :param listen_address: Combination of IPv4 address and Internet Assigned Numbers Authority (IANA) port or the IANA port alone to which Prometheus binds to ingest MongoDB metrics.
        :param microsoft_teams_webhook_url: Endpoint web address of the Microsoft Teams webhook to which MongoDB Cloud sends notifications.
        :param password: Password required for your integration with Prometheus.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param region: Two-letter code that indicates which regional URL MongoDB uses to access the Opsgenie/Datadog API.
        :param routing_key: Routing key associated with your Splunk On-Call account.
        :param scheme: Security Scheme to apply to HyperText Transfer Protocol (HTTP) traffic between Prometheus and MongoDB Cloud.
        :param secret: Parameter returned if someone configure this webhook with a secret.
        :param service_discovery: Desired method to discover the Prometheus service.
        :param service_key: Service key associated with your PagerDuty account.
        :param team_name: Human-readable label that identifies your Slack team. Set this parameter when you configure a legacy Slack integration.
        :param tls_pem_path: Root-relative path to the Transport Layer Security (TLS) Privacy Enhanced Mail (PEM) key and certificate file on the host.
        :param type: Human-readable label that identifies the service to which you want to integrate with MongoDB Cloud. The value must match the third-party service integration type.
        :param url: Endpoint web address to which MongoDB Cloud sends notifications.
        :param user_name: Human-readable label that identifies your Prometheus incoming webhook.

        :schema: CfnThirdPartyIntegrationProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be1439beaf06f53b34343a6c639a60c17b217e6a3a9b6d45d474ea3be41fa30d)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument api_token", value=api_token, expected_type=type_hints["api_token"])
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument listen_address", value=listen_address, expected_type=type_hints["listen_address"])
            check_type(argname="argument microsoft_teams_webhook_url", value=microsoft_teams_webhook_url, expected_type=type_hints["microsoft_teams_webhook_url"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument routing_key", value=routing_key, expected_type=type_hints["routing_key"])
            check_type(argname="argument scheme", value=scheme, expected_type=type_hints["scheme"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
            check_type(argname="argument service_discovery", value=service_discovery, expected_type=type_hints["service_discovery"])
            check_type(argname="argument service_key", value=service_key, expected_type=type_hints["service_key"])
            check_type(argname="argument team_name", value=team_name, expected_type=type_hints["team_name"])
            check_type(argname="argument tls_pem_path", value=tls_pem_path, expected_type=type_hints["tls_pem_path"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if api_key is not None:
            self._values["api_key"] = api_key
        if api_token is not None:
            self._values["api_token"] = api_token
        if channel_name is not None:
            self._values["channel_name"] = channel_name
        if enabled is not None:
            self._values["enabled"] = enabled
        if listen_address is not None:
            self._values["listen_address"] = listen_address
        if microsoft_teams_webhook_url is not None:
            self._values["microsoft_teams_webhook_url"] = microsoft_teams_webhook_url
        if password is not None:
            self._values["password"] = password
        if profile is not None:
            self._values["profile"] = profile
        if project_id is not None:
            self._values["project_id"] = project_id
        if region is not None:
            self._values["region"] = region
        if routing_key is not None:
            self._values["routing_key"] = routing_key
        if scheme is not None:
            self._values["scheme"] = scheme
        if secret is not None:
            self._values["secret"] = secret
        if service_discovery is not None:
            self._values["service_discovery"] = service_discovery
        if service_key is not None:
            self._values["service_key"] = service_key
        if team_name is not None:
            self._values["team_name"] = team_name
        if tls_pem_path is not None:
            self._values["tls_pem_path"] = tls_pem_path
        if type is not None:
            self._values["type"] = type
        if url is not None:
            self._values["url"] = url
        if user_name is not None:
            self._values["user_name"] = user_name

    @builtins.property
    def api_key(self) -> typing.Optional[builtins.str]:
        '''Key that allows MongoDB Cloud to access your Opsgenie/Datadog account.

        :schema: CfnThirdPartyIntegrationProps#ApiKey
        '''
        result = self._values.get("api_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_token(self) -> typing.Optional[builtins.str]:
        '''Key that allows MongoDB Cloud to access your Slack account.

        :schema: CfnThirdPartyIntegrationProps#ApiToken
        '''
        result = self._values.get("api_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def channel_name(self) -> typing.Optional[builtins.str]:
        '''Name of the Slack channel to which MongoDB Cloud sends alert notifications.

        :schema: CfnThirdPartyIntegrationProps#ChannelName
        '''
        result = self._values.get("channel_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether someone has activated the Prometheus integration.

        :schema: CfnThirdPartyIntegrationProps#Enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def listen_address(self) -> typing.Optional[builtins.str]:
        '''Combination of IPv4 address and Internet Assigned Numbers Authority (IANA) port or the IANA port alone to which Prometheus binds to ingest MongoDB metrics.

        :schema: CfnThirdPartyIntegrationProps#ListenAddress
        '''
        result = self._values.get("listen_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def microsoft_teams_webhook_url(self) -> typing.Optional[builtins.str]:
        '''Endpoint web address of the Microsoft Teams webhook to which MongoDB Cloud sends notifications.

        :schema: CfnThirdPartyIntegrationProps#MicrosoftTeamsWebhookUrl
        '''
        result = self._values.get("microsoft_teams_webhook_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Password required for your integration with Prometheus.

        :schema: CfnThirdPartyIntegrationProps#Password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''The profile is defined in AWS Secret manager.

        See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnThirdPartyIntegrationProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies your project.

        :schema: CfnThirdPartyIntegrationProps#ProjectId
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Two-letter code that indicates which regional URL MongoDB uses to access the Opsgenie/Datadog API.

        :schema: CfnThirdPartyIntegrationProps#Region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def routing_key(self) -> typing.Optional[builtins.str]:
        '''Routing key associated with your Splunk On-Call account.

        :schema: CfnThirdPartyIntegrationProps#RoutingKey
        '''
        result = self._values.get("routing_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheme(self) -> typing.Optional["CfnThirdPartyIntegrationPropsScheme"]:
        '''Security Scheme to apply to HyperText Transfer Protocol (HTTP) traffic between Prometheus and MongoDB Cloud.

        :schema: CfnThirdPartyIntegrationProps#Scheme
        '''
        result = self._values.get("scheme")
        return typing.cast(typing.Optional["CfnThirdPartyIntegrationPropsScheme"], result)

    @builtins.property
    def secret(self) -> typing.Optional[builtins.str]:
        '''Parameter returned if someone configure this webhook with a secret.

        :schema: CfnThirdPartyIntegrationProps#Secret
        '''
        result = self._values.get("secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_discovery(
        self,
    ) -> typing.Optional["CfnThirdPartyIntegrationPropsServiceDiscovery"]:
        '''Desired method to discover the Prometheus service.

        :schema: CfnThirdPartyIntegrationProps#ServiceDiscovery
        '''
        result = self._values.get("service_discovery")
        return typing.cast(typing.Optional["CfnThirdPartyIntegrationPropsServiceDiscovery"], result)

    @builtins.property
    def service_key(self) -> typing.Optional[builtins.str]:
        '''Service key associated with your PagerDuty account.

        :schema: CfnThirdPartyIntegrationProps#ServiceKey
        '''
        result = self._values.get("service_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def team_name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies your Slack team.

        Set this parameter when you configure a legacy Slack integration.

        :schema: CfnThirdPartyIntegrationProps#TeamName
        '''
        result = self._values.get("team_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_pem_path(self) -> typing.Optional[builtins.str]:
        '''Root-relative path to the Transport Layer Security (TLS) Privacy Enhanced Mail (PEM) key and certificate file on the host.

        :schema: CfnThirdPartyIntegrationProps#TlsPemPath
        '''
        result = self._values.get("tls_pem_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional["CfnThirdPartyIntegrationPropsType"]:
        '''Human-readable label that identifies the service to which you want to integrate with MongoDB Cloud.

        The value must match the third-party service integration type.

        :schema: CfnThirdPartyIntegrationProps#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["CfnThirdPartyIntegrationPropsType"], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''Endpoint web address to which MongoDB Cloud sends notifications.

        :schema: CfnThirdPartyIntegrationProps#Url
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies your Prometheus incoming webhook.

        :schema: CfnThirdPartyIntegrationProps#UserName
        '''
        result = self._values.get("user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnThirdPartyIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="awscdk-resources-mongodbatlas.CfnThirdPartyIntegrationPropsScheme"
)
class CfnThirdPartyIntegrationPropsScheme(enum.Enum):
    '''Security Scheme to apply to HyperText Transfer Protocol (HTTP) traffic between Prometheus and MongoDB Cloud.

    :schema: CfnThirdPartyIntegrationPropsScheme
    '''

    HTTP = "HTTP"
    '''http.'''
    HTTPS = "HTTPS"
    '''https.'''


@jsii.enum(
    jsii_type="awscdk-resources-mongodbatlas.CfnThirdPartyIntegrationPropsServiceDiscovery"
)
class CfnThirdPartyIntegrationPropsServiceDiscovery(enum.Enum):
    '''Desired method to discover the Prometheus service.

    :schema: CfnThirdPartyIntegrationPropsServiceDiscovery
    '''

    HTTP = "HTTP"
    '''http.'''
    FILE = "FILE"
    '''file.'''


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.CfnThirdPartyIntegrationPropsType")
class CfnThirdPartyIntegrationPropsType(enum.Enum):
    '''Human-readable label that identifies the service to which you want to integrate with MongoDB Cloud.

    The value must match the third-party service integration type.

    :schema: CfnThirdPartyIntegrationPropsType
    '''

    PAGER_DUTY = "PAGER_DUTY"
    '''PAGER_DUTY.'''
    MICROSOFT_TEAMS = "MICROSOFT_TEAMS"
    '''MICROSOFT_TEAMS.'''
    SLACK = "SLACK"
    '''SLACK.'''
    DATADOG = "DATADOG"
    '''DATADOG.'''
    OPS_GENIE = "OPS_GENIE"
    '''OPS_GENIE.'''
    VICTOR_OPS = "VICTOR_OPS"
    '''VICTOR_OPS.'''
    WEBHOOK = "WEBHOOK"
    '''WEBHOOK.'''
    PROMETHEUS = "PROMETHEUS"
    '''PROMETHEUS.'''


class CfnTrigger(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnTrigger",
):
    '''A CloudFormation ``MongoDB::Atlas::Trigger``.

    :cloudformationResource: MongoDB::Atlas::Trigger
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        app_id: builtins.str,
        project_id: builtins.str,
        auth_trigger: typing.Optional[typing.Union[AuthConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        database_trigger: typing.Optional[typing.Union["DatabaseConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        disabled: typing.Optional[builtins.bool] = None,
        event_processors: typing.Optional[typing.Union["Event", typing.Dict[builtins.str, typing.Any]]] = None,
        function_id: typing.Optional[builtins.str] = None,
        function_name: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        schedule_trigger: typing.Optional[typing.Union["ScheduleConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::Trigger``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param app_id: App Services Application ID.
        :param project_id: Project Id for application services.
        :param auth_trigger: 
        :param database_trigger: 
        :param disabled: If ``true``, the trigger is disabled and does not listen for events or execute.
        :param event_processors: An object where each field name is an event processor ID and each value is an object that configures its corresponding event processor. For an example configuration object, see `Send Trigger Events to AWS EventBridge <https://www.mongodb.com/docs/realm/triggers/examples/send-events-aws-eventbridge#std-label-event_processor_example>`_.
        :param function_id: The ID of the function that the trigger calls when it fires. This value is the same as ``event_processors.FUNCTION.function_id``. You can either define the value here or in ``event_processors.FUNCTION.function_id``. The App Services backend duplicates the value to the configuration location where you did not define it. For example, if you define ``function_id``, the backend duplicates it to ``event_processors.FUNCTION.function_id``.
        :param function_name: The name of the function that the trigger calls when it fires, i.e. the function described by ``function_id``. This value is the same as ``event_processors.FUNCTION.function_name``. You can either define the value here or in ``event_processors.FUNCTION.function_name``. The App Services backend duplicates the value to the configuration location where you did not define it. For example, if you define ``function_name``, the backend duplicates it to ``event_processors.FUNCTION.function_name``.
        :param name: The trigger's name.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param schedule_trigger: 
        :param type: The trigger's type.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6bdbf471d26e0ad87a81655e01a9beddf96f71e5232ef55c13171c50b162c02)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTriggerProps(
            app_id=app_id,
            project_id=project_id,
            auth_trigger=auth_trigger,
            database_trigger=database_trigger,
            disabled=disabled,
            event_processors=event_processors,
            function_id=function_id,
            function_name=function_name,
            name=name,
            profile=profile,
            schedule_trigger=schedule_trigger,
            type=type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Trigger.Id``.'''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnTriggerProps":
        '''Resource props.'''
        return typing.cast("CfnTriggerProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnTriggerProps",
    jsii_struct_bases=[],
    name_mapping={
        "app_id": "appId",
        "project_id": "projectId",
        "auth_trigger": "authTrigger",
        "database_trigger": "databaseTrigger",
        "disabled": "disabled",
        "event_processors": "eventProcessors",
        "function_id": "functionId",
        "function_name": "functionName",
        "name": "name",
        "profile": "profile",
        "schedule_trigger": "scheduleTrigger",
        "type": "type",
    },
)
class CfnTriggerProps:
    def __init__(
        self,
        *,
        app_id: builtins.str,
        project_id: builtins.str,
        auth_trigger: typing.Optional[typing.Union[AuthConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        database_trigger: typing.Optional[typing.Union["DatabaseConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        disabled: typing.Optional[builtins.bool] = None,
        event_processors: typing.Optional[typing.Union["Event", typing.Dict[builtins.str, typing.Any]]] = None,
        function_id: typing.Optional[builtins.str] = None,
        function_name: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        schedule_trigger: typing.Optional[typing.Union["ScheduleConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''View and manage your application's `triggers <https://www.mongodb.com/docs/atlas/app-services/triggers/overview/>`_.

        :param app_id: App Services Application ID.
        :param project_id: Project Id for application services.
        :param auth_trigger: 
        :param database_trigger: 
        :param disabled: If ``true``, the trigger is disabled and does not listen for events or execute.
        :param event_processors: An object where each field name is an event processor ID and each value is an object that configures its corresponding event processor. For an example configuration object, see `Send Trigger Events to AWS EventBridge <https://www.mongodb.com/docs/realm/triggers/examples/send-events-aws-eventbridge#std-label-event_processor_example>`_.
        :param function_id: The ID of the function that the trigger calls when it fires. This value is the same as ``event_processors.FUNCTION.function_id``. You can either define the value here or in ``event_processors.FUNCTION.function_id``. The App Services backend duplicates the value to the configuration location where you did not define it. For example, if you define ``function_id``, the backend duplicates it to ``event_processors.FUNCTION.function_id``.
        :param function_name: The name of the function that the trigger calls when it fires, i.e. the function described by ``function_id``. This value is the same as ``event_processors.FUNCTION.function_name``. You can either define the value here or in ``event_processors.FUNCTION.function_name``. The App Services backend duplicates the value to the configuration location where you did not define it. For example, if you define ``function_name``, the backend duplicates it to ``event_processors.FUNCTION.function_name``.
        :param name: The trigger's name.
        :param profile: The profile is defined in AWS Secret manager. See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.
        :param schedule_trigger: 
        :param type: The trigger's type.

        :schema: CfnTriggerProps
        '''
        if isinstance(auth_trigger, dict):
            auth_trigger = AuthConfig(**auth_trigger)
        if isinstance(database_trigger, dict):
            database_trigger = DatabaseConfig(**database_trigger)
        if isinstance(event_processors, dict):
            event_processors = Event(**event_processors)
        if isinstance(schedule_trigger, dict):
            schedule_trigger = ScheduleConfig(**schedule_trigger)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7db6e39c2f2c99b7eb0bc2548c65b47123dfba34574ee5f34fe937ef4416aef5)
            check_type(argname="argument app_id", value=app_id, expected_type=type_hints["app_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument auth_trigger", value=auth_trigger, expected_type=type_hints["auth_trigger"])
            check_type(argname="argument database_trigger", value=database_trigger, expected_type=type_hints["database_trigger"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument event_processors", value=event_processors, expected_type=type_hints["event_processors"])
            check_type(argname="argument function_id", value=function_id, expected_type=type_hints["function_id"])
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument schedule_trigger", value=schedule_trigger, expected_type=type_hints["schedule_trigger"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_id": app_id,
            "project_id": project_id,
        }
        if auth_trigger is not None:
            self._values["auth_trigger"] = auth_trigger
        if database_trigger is not None:
            self._values["database_trigger"] = database_trigger
        if disabled is not None:
            self._values["disabled"] = disabled
        if event_processors is not None:
            self._values["event_processors"] = event_processors
        if function_id is not None:
            self._values["function_id"] = function_id
        if function_name is not None:
            self._values["function_name"] = function_name
        if name is not None:
            self._values["name"] = name
        if profile is not None:
            self._values["profile"] = profile
        if schedule_trigger is not None:
            self._values["schedule_trigger"] = schedule_trigger
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def app_id(self) -> builtins.str:
        '''App Services Application ID.

        :schema: CfnTriggerProps#AppId
        '''
        result = self._values.get("app_id")
        assert result is not None, "Required property 'app_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Project Id for application services.

        :schema: CfnTriggerProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth_trigger(self) -> typing.Optional[AuthConfig]:
        '''
        :schema: CfnTriggerProps#AuthTrigger
        '''
        result = self._values.get("auth_trigger")
        return typing.cast(typing.Optional[AuthConfig], result)

    @builtins.property
    def database_trigger(self) -> typing.Optional["DatabaseConfig"]:
        '''
        :schema: CfnTriggerProps#DatabaseTrigger
        '''
        result = self._values.get("database_trigger")
        return typing.cast(typing.Optional["DatabaseConfig"], result)

    @builtins.property
    def disabled(self) -> typing.Optional[builtins.bool]:
        '''If ``true``, the trigger is disabled and does not listen for events or execute.

        :schema: CfnTriggerProps#Disabled
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def event_processors(self) -> typing.Optional["Event"]:
        '''An object where each field name is an event processor ID and each value is an object that configures its corresponding event processor.

        For an example configuration object, see
        `Send Trigger Events to AWS
        EventBridge <https://www.mongodb.com/docs/realm/triggers/examples/send-events-aws-eventbridge#std-label-event_processor_example>`_.

        :schema: CfnTriggerProps#EventProcessors
        '''
        result = self._values.get("event_processors")
        return typing.cast(typing.Optional["Event"], result)

    @builtins.property
    def function_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the function that the trigger calls when it fires.

        This value is the same as ``event_processors.FUNCTION.function_id``.
        You can either define the value here or in ``event_processors.FUNCTION.function_id``.
        The App Services backend duplicates the value to the configuration location where you did not define it.

        For example, if you define ``function_id``, the backend duplicates it to ``event_processors.FUNCTION.function_id``.

        :schema: CfnTriggerProps#FunctionId
        '''
        result = self._values.get("function_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def function_name(self) -> typing.Optional[builtins.str]:
        '''The name of the function that the trigger calls when it fires, i.e. the function described by ``function_id``.

        This value is the same as ``event_processors.FUNCTION.function_name``.
        You can either define the value here or in ``event_processors.FUNCTION.function_name``.
        The App Services backend duplicates the value to the configuration location where you did not define it.

        For example, if you define ``function_name``, the backend duplicates it to ``event_processors.FUNCTION.function_name``.

        :schema: CfnTriggerProps#FunctionName
        '''
        result = self._values.get("function_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The trigger's name.

        :schema: CfnTriggerProps#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''The profile is defined in AWS Secret manager.

        See `Secret Manager Profile setup <../../../examples/profile-secret.yaml>`_.

        :schema: CfnTriggerProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule_trigger(self) -> typing.Optional["ScheduleConfig"]:
        '''
        :schema: CfnTriggerProps#ScheduleTrigger
        '''
        result = self._values.get("schedule_trigger")
        return typing.cast(typing.Optional["ScheduleConfig"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The trigger's type.

        :schema: CfnTriggerProps#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTriggerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnX509AuthenticationDatabaseUser(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.CfnX509AuthenticationDatabaseUser",
):
    '''A CloudFormation ``MongoDB::Atlas::X509AuthenticationDatabaseUser``.

    :cloudformationResource: MongoDB::Atlas::X509AuthenticationDatabaseUser
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        customer_x509: typing.Optional[typing.Union["CustomerX509", typing.Dict[builtins.str, typing.Any]]] = None,
        months_until_expiration: typing.Optional[jsii.Number] = None,
        profile: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        total_count: typing.Optional[jsii.Number] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::X509AuthenticationDatabaseUser``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param customer_x509: CustomerX509 represents Customer-managed X.509 configuration for an Atlas project.
        :param months_until_expiration: A number of months that the created certificate is valid for before expiry, up to 24 months.default 3.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param project_id: The unique identifier for the project .
        :param total_count: Total number of unexpired certificates returned in this response.
        :param user_name: Username of the database user to create a certificate for.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13b9b050ae1c7a9ab6d780c0f2c1a0409182aa3712dd04020715b8aef6c02048)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnX509AuthenticationDatabaseUserProps(
            customer_x509=customer_x509,
            months_until_expiration=months_until_expiration,
            profile=profile,
            project_id=project_id,
            total_count=total_count,
            user_name=user_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnX509AuthenticationDatabaseUserProps":
        '''Resource props.'''
        return typing.cast("CfnX509AuthenticationDatabaseUserProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CfnX509AuthenticationDatabaseUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "customer_x509": "customerX509",
        "months_until_expiration": "monthsUntilExpiration",
        "profile": "profile",
        "project_id": "projectId",
        "total_count": "totalCount",
        "user_name": "userName",
    },
)
class CfnX509AuthenticationDatabaseUserProps:
    def __init__(
        self,
        *,
        customer_x509: typing.Optional[typing.Union["CustomerX509", typing.Dict[builtins.str, typing.Any]]] = None,
        months_until_expiration: typing.Optional[jsii.Number] = None,
        profile: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        total_count: typing.Optional[jsii.Number] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Generates one X.509 certificate for the specified MongoDB user. Atlas manages the certificate and MongoDB user that belong to one project. To use this resource, the requesting API Key must have the Project Atlas Admin role. This resource doesn't require the API Key to have an Access List.

        To get MongoDB Cloud to generate a managed certificate for a database user, set ``"x509Type" : "MANAGED"`` on the desired MongoDB Database User.

        If you are managing your own Certificate Authority (CA) in Self-Managed X.509 mode, you must generate certificates for database users using your own CA.

        :param customer_x509: CustomerX509 represents Customer-managed X.509 configuration for an Atlas project.
        :param months_until_expiration: A number of months that the created certificate is valid for before expiry, up to 24 months.default 3.
        :param profile: Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.
        :param project_id: The unique identifier for the project .
        :param total_count: Total number of unexpired certificates returned in this response.
        :param user_name: Username of the database user to create a certificate for.

        :schema: CfnX509AuthenticationDatabaseUserProps
        '''
        if isinstance(customer_x509, dict):
            customer_x509 = CustomerX509(**customer_x509)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce69c30cea79a8a0148655e04b8eb82131c7a4b60f382199c9085a21b5729936)
            check_type(argname="argument customer_x509", value=customer_x509, expected_type=type_hints["customer_x509"])
            check_type(argname="argument months_until_expiration", value=months_until_expiration, expected_type=type_hints["months_until_expiration"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument total_count", value=total_count, expected_type=type_hints["total_count"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if customer_x509 is not None:
            self._values["customer_x509"] = customer_x509
        if months_until_expiration is not None:
            self._values["months_until_expiration"] = months_until_expiration
        if profile is not None:
            self._values["profile"] = profile
        if project_id is not None:
            self._values["project_id"] = project_id
        if total_count is not None:
            self._values["total_count"] = total_count
        if user_name is not None:
            self._values["user_name"] = user_name

    @builtins.property
    def customer_x509(self) -> typing.Optional["CustomerX509"]:
        '''CustomerX509 represents Customer-managed X.509 configuration for an Atlas project.

        :schema: CfnX509AuthenticationDatabaseUserProps#CustomerX509
        '''
        result = self._values.get("customer_x509")
        return typing.cast(typing.Optional["CustomerX509"], result)

    @builtins.property
    def months_until_expiration(self) -> typing.Optional[jsii.Number]:
        '''A number of months that the created certificate is valid for before expiry, up to 24 months.default 3.

        :schema: CfnX509AuthenticationDatabaseUserProps#MonthsUntilExpiration
        '''
        result = self._values.get("months_until_expiration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Profile used to provide credentials information, (a secret with the cfn/atlas/profile/{Profile}, is required), if not provided default is used.

        :schema: CfnX509AuthenticationDatabaseUserProps#Profile
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier for the project .

        :schema: CfnX509AuthenticationDatabaseUserProps#ProjectId
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def total_count(self) -> typing.Optional[jsii.Number]:
        '''Total number of unexpired certificates returned in this response.

        :schema: CfnX509AuthenticationDatabaseUserProps#TotalCount
        '''
        result = self._values.get("total_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def user_name(self) -> typing.Optional[builtins.str]:
        '''Username of the database user to create a certificate for.

        :schema: CfnX509AuthenticationDatabaseUserProps#UserName
        '''
        result = self._values.get("user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnX509AuthenticationDatabaseUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "advanced_settings": "advancedSettings",
        "backup_enabled": "backupEnabled",
        "bi_connector": "biConnector",
        "cluster_type": "clusterType",
        "connection_strings": "connectionStrings",
        "disk_size_gb": "diskSizeGb",
        "encryption_at_rest_provider": "encryptionAtRestProvider",
        "labels": "labels",
        "mongo_db_major_version": "mongoDbMajorVersion",
        "name": "name",
        "paused": "paused",
        "pit_enabled": "pitEnabled",
        "project_id": "projectId",
        "replication_specs": "replicationSpecs",
        "root_cert_type": "rootCertType",
        "termination_protection_enabled": "terminationProtectionEnabled",
        "version_release_system": "versionReleaseSystem",
    },
)
class ClusterProps:
    def __init__(
        self,
        *,
        advanced_settings: typing.Optional[typing.Union["ProcessArgs", typing.Dict[builtins.str, typing.Any]]] = None,
        backup_enabled: typing.Optional[builtins.bool] = None,
        bi_connector: typing.Optional[typing.Union[CfnClusterPropsBiConnector, typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_type: typing.Optional[builtins.str] = None,
        connection_strings: typing.Optional[typing.Union["ConnectionStrings", typing.Dict[builtins.str, typing.Any]]] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        encryption_at_rest_provider: typing.Optional[CfnClusterPropsEncryptionAtRestProvider] = None,
        labels: typing.Optional[typing.Sequence[typing.Union[CfnClusterPropsLabels, typing.Dict[builtins.str, typing.Any]]]] = None,
        mongo_db_major_version: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        paused: typing.Optional[builtins.bool] = None,
        pit_enabled: typing.Optional[builtins.bool] = None,
        project_id: typing.Optional[builtins.str] = None,
        replication_specs: typing.Optional[typing.Sequence[typing.Union[AdvancedReplicationSpec, typing.Dict[builtins.str, typing.Any]]]] = None,
        root_cert_type: typing.Optional[builtins.str] = None,
        termination_protection_enabled: typing.Optional[builtins.bool] = None,
        version_release_system: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param advanced_settings: 
        :param backup_enabled: 
        :param bi_connector: 
        :param cluster_type: 
        :param connection_strings: Default: REPLICASET
        :param disk_size_gb: 
        :param encryption_at_rest_provider: 
        :param labels: 
        :param mongo_db_major_version: 
        :param name: 
        :param paused: Default: auto-generated
        :param pit_enabled: 
        :param project_id: 
        :param replication_specs: 
        :param root_cert_type: 
        :param termination_protection_enabled: 
        :param version_release_system: 

        :description: true
        :export: true
        :interface: ClusterProps
        '''
        if isinstance(advanced_settings, dict):
            advanced_settings = ProcessArgs(**advanced_settings)
        if isinstance(bi_connector, dict):
            bi_connector = CfnClusterPropsBiConnector(**bi_connector)
        if isinstance(connection_strings, dict):
            connection_strings = ConnectionStrings(**connection_strings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aa8d6bf21c97655b6cbb7136f7ee1cbd527d1d9246da810f82ed4420d0456e9)
            check_type(argname="argument advanced_settings", value=advanced_settings, expected_type=type_hints["advanced_settings"])
            check_type(argname="argument backup_enabled", value=backup_enabled, expected_type=type_hints["backup_enabled"])
            check_type(argname="argument bi_connector", value=bi_connector, expected_type=type_hints["bi_connector"])
            check_type(argname="argument cluster_type", value=cluster_type, expected_type=type_hints["cluster_type"])
            check_type(argname="argument connection_strings", value=connection_strings, expected_type=type_hints["connection_strings"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument encryption_at_rest_provider", value=encryption_at_rest_provider, expected_type=type_hints["encryption_at_rest_provider"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument mongo_db_major_version", value=mongo_db_major_version, expected_type=type_hints["mongo_db_major_version"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument paused", value=paused, expected_type=type_hints["paused"])
            check_type(argname="argument pit_enabled", value=pit_enabled, expected_type=type_hints["pit_enabled"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument replication_specs", value=replication_specs, expected_type=type_hints["replication_specs"])
            check_type(argname="argument root_cert_type", value=root_cert_type, expected_type=type_hints["root_cert_type"])
            check_type(argname="argument termination_protection_enabled", value=termination_protection_enabled, expected_type=type_hints["termination_protection_enabled"])
            check_type(argname="argument version_release_system", value=version_release_system, expected_type=type_hints["version_release_system"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if advanced_settings is not None:
            self._values["advanced_settings"] = advanced_settings
        if backup_enabled is not None:
            self._values["backup_enabled"] = backup_enabled
        if bi_connector is not None:
            self._values["bi_connector"] = bi_connector
        if cluster_type is not None:
            self._values["cluster_type"] = cluster_type
        if connection_strings is not None:
            self._values["connection_strings"] = connection_strings
        if disk_size_gb is not None:
            self._values["disk_size_gb"] = disk_size_gb
        if encryption_at_rest_provider is not None:
            self._values["encryption_at_rest_provider"] = encryption_at_rest_provider
        if labels is not None:
            self._values["labels"] = labels
        if mongo_db_major_version is not None:
            self._values["mongo_db_major_version"] = mongo_db_major_version
        if name is not None:
            self._values["name"] = name
        if paused is not None:
            self._values["paused"] = paused
        if pit_enabled is not None:
            self._values["pit_enabled"] = pit_enabled
        if project_id is not None:
            self._values["project_id"] = project_id
        if replication_specs is not None:
            self._values["replication_specs"] = replication_specs
        if root_cert_type is not None:
            self._values["root_cert_type"] = root_cert_type
        if termination_protection_enabled is not None:
            self._values["termination_protection_enabled"] = termination_protection_enabled
        if version_release_system is not None:
            self._values["version_release_system"] = version_release_system

    @builtins.property
    def advanced_settings(self) -> typing.Optional["ProcessArgs"]:
        '''
        :description: Advanced configuration details to add for one cluster in the specified project.
        :memberof: ClusterProps
        :type: {atlas.ProcessArgs}
        '''
        result = self._values.get("advanced_settings")
        return typing.cast(typing.Optional["ProcessArgs"], result)

    @builtins.property
    def backup_enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :description: Flag that indicates whether the cluster can perform backups. If set to true, the cluster can perform backups. You must set this value to true for NVMe clusters. Backup uses Cloud Backups for dedicated clusters and Shared Cluster Backups for tenant clusters. If set to false, the cluster doesn't use backups.
        :memberof: ClusterProps
        :type: {boolean}
        '''
        result = self._values.get("backup_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def bi_connector(self) -> typing.Optional[CfnClusterPropsBiConnector]:
        '''
        :description: Settings needed to configure the MongoDB Connector for Business Intelligence for this cluster.
        :memberof: ClusterProps
        :type: {atlas.CfnClusterPropsBiConnector}
        '''
        result = self._values.get("bi_connector")
        return typing.cast(typing.Optional[CfnClusterPropsBiConnector], result)

    @builtins.property
    def cluster_type(self) -> typing.Optional[builtins.str]:
        '''
        :description: Configuration of nodes that comprise the cluster. Atlas accepts: ``REPLICASET``, ``SHARDED``, ``GEOSHARDED``.
        :memberof: ClusterProps
        :type: {string}
        '''
        result = self._values.get("cluster_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_strings(self) -> typing.Optional["ConnectionStrings"]:
        '''
        :default: REPLICASET

        :description: Set of connection strings that your applications use to connect to this cluster. Use the parameters in this object to connect your applications to this cluster. See the MongoDB `Connection String URI Format <https://docs.mongodb.com/manual/reference/connection-string/>`_ reference for further details.
        :memberof: ClusterProps
        :type: {atlas.ConnectionStrings}
        '''
        result = self._values.get("connection_strings")
        return typing.cast(typing.Optional["ConnectionStrings"], result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''
        :description: Storage capacity that the host's root volume possesses expressed in gigabytes. Increase this number to add capacity. MongoDB Cloud requires this parameter if you set replicationSpecs. If you specify a disk size below the minimum (10 GB), this parameter defaults to the minimum disk size value. Storage charge calculations depend on whether you choose the default value or a custom value. The maximum value for disk storage cannot exceed 50 times the maximum RAM for the selected cluster. If you require more storage space, consider upgrading your cluster to a higher tier.
        :memberof: ClusterProps
        :type: {number}
        '''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def encryption_at_rest_provider(
        self,
    ) -> typing.Optional[CfnClusterPropsEncryptionAtRestProvider]:
        '''
        :description: Cloud service provider that manages your customer keys to provide an additional layer of encryption at rest for the cluster. To enable customer key management for encryption at rest, the cluster replicationSpecs[n].regionConfigs[m].{type}Specs.instanceSize setting must be M10 or higher and "backupEnabled" : false or omitted entirely.
        :memberof: ClusterProps
        :type: {atlas.CfnClusterPropsEncryptionAtRestProvider}
        '''
        result = self._values.get("encryption_at_rest_provider")
        return typing.cast(typing.Optional[CfnClusterPropsEncryptionAtRestProvider], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List[CfnClusterPropsLabels]]:
        '''
        :description: Collection of key-value pairs between 1 and 255 characters in length that tag and categorize the cluster. The MongoDB Cloud console doesn't display your labels.
        :memberof: ClusterProps
        :type: {atlas.CfnClusterPropsLabels[]}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List[CfnClusterPropsLabels]], result)

    @builtins.property
    def mongo_db_major_version(self) -> typing.Optional[builtins.str]:
        '''
        :description: Major MongoDB version of the cluster. MongoDB Cloud deploys the cluster with the latest stable release of the specified version.
        :memberof: ClusterProps
        :type: {string}
        '''
        result = self._values.get("mongo_db_major_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :description: Human-readable label that identifies the advanced cluster.
        :memberof: ClusterProps
        :type: {string}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def paused(self) -> typing.Optional[builtins.bool]:
        '''
        :default: auto-generated

        :description: Flag that indicates whether the cluster is paused or not.
        :memberof: ClusterProps
        :type: {boolean}
        '''
        result = self._values.get("paused")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def pit_enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :description: Flag that indicates whether the cluster uses continuous cloud backups.
        :memberof: ClusterProps
        :type: {boolean}
        '''
        result = self._values.get("pit_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''
        :description: true
        :memberof: ClusterProps
        :type: {string}
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_specs(
        self,
    ) -> typing.Optional[typing.List[AdvancedReplicationSpec]]:
        '''
        :description: List of settings that configure your cluster regions. For Global Clusters, each object in the array represents a zone where your clusters nodes deploy. For non-Global replica sets and sharded clusters, this array has one object representing where your clusters nodes deploy.
        :memberof: ClusterProps
        :type: {atlas.AdvancedReplicationSpec[]}
        '''
        result = self._values.get("replication_specs")
        return typing.cast(typing.Optional[typing.List[AdvancedReplicationSpec]], result)

    @builtins.property
    def root_cert_type(self) -> typing.Optional[builtins.str]:
        '''
        :description: Root Certificate Authority that MongoDB Cloud cluster uses. MongoDB Cloud supports Internet Security Research Group.
        :memberof: ClusterProps
        :type: {string}
        '''
        result = self._values.get("root_cert_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def termination_protection_enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :description: Flag that indicates whether termination protection is enabled on the cluster. If set to true, MongoDB Cloud won't delete the cluster. If set to false, MongoDB Cloud will delete the cluster.
        :memberof: ClusterProps
        :type: {boolean}
        '''
        result = self._values.get("termination_protection_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def version_release_system(self) -> typing.Optional[builtins.str]:
        '''
        :description: Method by which the cluster maintains the MongoDB versions. If value is CONTINUOUS, you must not specify mongoDBMajorVersion
        :memberof: ClusterProps
        :type: {string}
        '''
        result = self._values.get("version_release_system")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.Compute",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "max_instance_size": "maxInstanceSize",
        "min_instance_size": "minInstanceSize",
        "scale_down_enabled": "scaleDownEnabled",
    },
)
class Compute:
    def __init__(
        self,
        *,
        enabled: typing.Optional[builtins.bool] = None,
        max_instance_size: typing.Optional[builtins.str] = None,
        min_instance_size: typing.Optional[builtins.str] = None,
        scale_down_enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Automatic Compute Scaling.

        :param enabled: Flag that indicates whether someone enabled instance size auto-scaling. Set to true to enable instance size auto-scaling. If enabled, you must specify a value for replicationSpecs[n].regionConfigs[m].autoScaling.compute.maxInstanceSize. Set to false to disable instance size automatic scaling.
        :param max_instance_size: Maximum instance size to which your cluster can automatically scale. MongoDB Cloud requires this parameter if "replicationSpecs[n].regionConfigs[m].autoScaling.compute.enabled" : true.
        :param min_instance_size: Minimum instance size to which your cluster can automatically scale. MongoDB Cloud requires this parameter if "replicationSpecs[n].regionConfigs[m].autoScaling.compute.enabled" : true.
        :param scale_down_enabled: Flag that indicates whether the instance size may scale down. MongoDB Cloud requires this parameter if "replicationSpecs[n].regionConfigs[m].autoScaling.compute.enabled" : true. If you enable this option, specify a value for replicationSpecs[n].regionConfigs[m].autoScaling.compute.minInstanceSize.

        :schema: compute
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fc92953d030e14f8e475637fe710ef24fa4306fc84ca82ab7017b88af8b5076)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument max_instance_size", value=max_instance_size, expected_type=type_hints["max_instance_size"])
            check_type(argname="argument min_instance_size", value=min_instance_size, expected_type=type_hints["min_instance_size"])
            check_type(argname="argument scale_down_enabled", value=scale_down_enabled, expected_type=type_hints["scale_down_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if max_instance_size is not None:
            self._values["max_instance_size"] = max_instance_size
        if min_instance_size is not None:
            self._values["min_instance_size"] = min_instance_size
        if scale_down_enabled is not None:
            self._values["scale_down_enabled"] = scale_down_enabled

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether someone enabled instance size auto-scaling.

        Set to true to enable instance size auto-scaling. If enabled, you must specify a value for replicationSpecs[n].regionConfigs[m].autoScaling.compute.maxInstanceSize.
        Set to false to disable instance size automatic scaling.

        :schema: compute#Enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def max_instance_size(self) -> typing.Optional[builtins.str]:
        '''Maximum instance size to which your cluster can automatically scale.

        MongoDB Cloud requires this parameter if "replicationSpecs[n].regionConfigs[m].autoScaling.compute.enabled" : true.

        :schema: compute#MaxInstanceSize
        '''
        result = self._values.get("max_instance_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_instance_size(self) -> typing.Optional[builtins.str]:
        '''Minimum instance size to which your cluster can automatically scale.

        MongoDB Cloud requires this parameter if "replicationSpecs[n].regionConfigs[m].autoScaling.compute.enabled" : true.

        :schema: compute#MinInstanceSize
        '''
        result = self._values.get("min_instance_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_down_enabled(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether the instance size may scale down.

        MongoDB Cloud requires this parameter if "replicationSpecs[n].regionConfigs[m].autoScaling.compute.enabled" : true. If you enable this option, specify a value for replicationSpecs[n].regionConfigs[m].autoScaling.compute.minInstanceSize.

        :schema: compute#ScaleDownEnabled
        '''
        result = self._values.get("scale_down_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Compute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ConnectionStrings",
    jsii_struct_bases=[],
    name_mapping={
        "aws_private_link": "awsPrivateLink",
        "aws_private_link_srv": "awsPrivateLinkSrv",
        "private": "private",
        "private_endpoint": "privateEndpoint",
        "private_srv": "privateSrv",
        "standard": "standard",
        "standard_srv": "standardSrv",
    },
)
class ConnectionStrings:
    def __init__(
        self,
        *,
        aws_private_link: typing.Optional[builtins.str] = None,
        aws_private_link_srv: typing.Optional[builtins.str] = None,
        private: typing.Optional[builtins.str] = None,
        private_endpoint: typing.Optional[typing.Sequence[typing.Union["PrivateEndpoint", typing.Dict[builtins.str, typing.Any]]]] = None,
        private_srv: typing.Optional[builtins.str] = None,
        standard: typing.Optional[builtins.str] = None,
        standard_srv: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Collection of Uniform Resource Locators that point to the MongoDB database.

        :param aws_private_link: Private endpoint-aware connection strings that use AWS-hosted clusters with Amazon Web Services (AWS) PrivateLink. Each key identifies an Amazon Web Services (AWS) interface endpoint. Each value identifies the related mongodb:// connection string that you use to connect to MongoDB Cloud through the interface endpoint that the key names.
        :param aws_private_link_srv: Private endpoint-aware connection strings that use AWS-hosted clusters with Amazon Web Services (AWS) PrivateLink. Each key identifies an Amazon Web Services (AWS) interface endpoint. Each value identifies the related mongodb:// connection string that you use to connect to Atlas through the interface endpoint that the key names.
        :param private: Network peering connection strings for each interface Virtual Private Cloud (VPC) endpoint that you configured to connect to this cluster. This connection string uses the mongodb+srv:// protocol. The resource returns this parameter once someone creates a network peering connection to this cluster. This protocol tells the application to look up the host seed list in the Domain Name System (DNS). This list synchronizes with the nodes in a cluster. If the connection string uses this Uniform Resource Identifier (URI) format, you don't need to append the seed list or change the URI if the nodes change. Use this URI format if your driver supports it. If it doesn't, use connectionStrings.private. For Amazon Web Services (AWS) clusters, this resource returns this parameter only if you enable custom DNS.
        :param private_endpoint: List of private endpoint connection strings that you can use to connect to this cluster through a private endpoint. This parameter returns only if you deployed a private endpoint to all regions to which you deployed this clusters' nodes.
        :param private_srv: Network peering connection strings for each interface Virtual Private Cloud (VPC) endpoint that you configured to connect to this cluster. This connection string uses the mongodb+srv:// protocol. The resource returns this parameter when someone creates a network peering connection to this cluster. This protocol tells the application to look up the host seed list in the Domain Name System (DNS). This list synchronizes with the nodes in a cluster. If the connection string uses this Uniform Resource Identifier (URI) format, you don't need to append the seed list or change the Uniform Resource Identifier (URI) if the nodes change. Use this Uniform Resource Identifier (URI) format if your driver supports it. If it doesn't, use connectionStrings.private. For Amazon Web Services (AWS) clusters, this parameter returns only if you enable custom DNS.
        :param standard: Public connection string that you can use to connect to this cluster. This connection string uses the mongodb:// protocol.
        :param standard_srv: Public connection string that you can use to connect to this cluster. This connection string uses the mongodb+srv:// protocol.

        :schema: connectionStrings
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__597338f96c3a4d62d6939ce0f092a5160cae79412897f58a15ddfb72d6f47d80)
            check_type(argname="argument aws_private_link", value=aws_private_link, expected_type=type_hints["aws_private_link"])
            check_type(argname="argument aws_private_link_srv", value=aws_private_link_srv, expected_type=type_hints["aws_private_link_srv"])
            check_type(argname="argument private", value=private, expected_type=type_hints["private"])
            check_type(argname="argument private_endpoint", value=private_endpoint, expected_type=type_hints["private_endpoint"])
            check_type(argname="argument private_srv", value=private_srv, expected_type=type_hints["private_srv"])
            check_type(argname="argument standard", value=standard, expected_type=type_hints["standard"])
            check_type(argname="argument standard_srv", value=standard_srv, expected_type=type_hints["standard_srv"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_private_link is not None:
            self._values["aws_private_link"] = aws_private_link
        if aws_private_link_srv is not None:
            self._values["aws_private_link_srv"] = aws_private_link_srv
        if private is not None:
            self._values["private"] = private
        if private_endpoint is not None:
            self._values["private_endpoint"] = private_endpoint
        if private_srv is not None:
            self._values["private_srv"] = private_srv
        if standard is not None:
            self._values["standard"] = standard
        if standard_srv is not None:
            self._values["standard_srv"] = standard_srv

    @builtins.property
    def aws_private_link(self) -> typing.Optional[builtins.str]:
        '''Private endpoint-aware connection strings that use AWS-hosted clusters with Amazon Web Services (AWS) PrivateLink.

        Each key identifies an Amazon Web Services (AWS) interface endpoint. Each value identifies the related mongodb:// connection string that you use to connect to MongoDB Cloud through the interface endpoint that the key names.

        :schema: connectionStrings#AwsPrivateLink
        '''
        result = self._values.get("aws_private_link")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_private_link_srv(self) -> typing.Optional[builtins.str]:
        '''Private endpoint-aware connection strings that use AWS-hosted clusters with Amazon Web Services (AWS) PrivateLink.

        Each key identifies an Amazon Web Services (AWS) interface endpoint. Each value identifies the related mongodb:// connection string that you use to connect to Atlas through the interface endpoint that the key names.

        :schema: connectionStrings#AwsPrivateLinkSrv
        '''
        result = self._values.get("aws_private_link_srv")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private(self) -> typing.Optional[builtins.str]:
        '''Network peering connection strings for each interface Virtual Private Cloud (VPC) endpoint that you configured to connect to this cluster.

        This connection string uses the mongodb+srv:// protocol. The resource returns this parameter once someone creates a network peering connection to this cluster. This protocol tells the application to look up the host seed list in the Domain Name System (DNS). This list synchronizes with the nodes in a cluster. If the connection string uses this Uniform Resource Identifier (URI) format, you don't need to append the seed list or change the URI if the nodes change. Use this URI format if your driver supports it. If it doesn't, use connectionStrings.private. For Amazon Web Services (AWS) clusters, this resource returns this parameter only if you enable custom DNS.

        :schema: connectionStrings#Private
        '''
        result = self._values.get("private")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_endpoint(self) -> typing.Optional[typing.List["PrivateEndpoint"]]:
        '''List of private endpoint connection strings that you can use to connect to this cluster through a private endpoint.

        This parameter returns only if you deployed a private endpoint to all regions to which you deployed this clusters' nodes.

        :schema: connectionStrings#PrivateEndpoint
        '''
        result = self._values.get("private_endpoint")
        return typing.cast(typing.Optional[typing.List["PrivateEndpoint"]], result)

    @builtins.property
    def private_srv(self) -> typing.Optional[builtins.str]:
        '''Network peering connection strings for each interface Virtual Private Cloud (VPC) endpoint that you configured to connect to this cluster.

        This connection string uses the mongodb+srv:// protocol. The resource returns this parameter when someone creates a network peering connection to this cluster. This protocol tells the application to look up the host seed list in the Domain Name System (DNS). This list synchronizes with the nodes in a cluster. If the connection string uses this Uniform Resource Identifier (URI) format, you don't need to append the seed list or change the Uniform Resource Identifier (URI) if the nodes change. Use this Uniform Resource Identifier (URI) format if your driver supports it. If it doesn't, use connectionStrings.private. For Amazon Web Services (AWS) clusters, this parameter returns only if you enable custom DNS.

        :schema: connectionStrings#PrivateSrv
        '''
        result = self._values.get("private_srv")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def standard(self) -> typing.Optional[builtins.str]:
        '''Public connection string that you can use to connect to this cluster.

        This connection string uses the mongodb:// protocol.

        :schema: connectionStrings#Standard
        '''
        result = self._values.get("standard")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def standard_srv(self) -> typing.Optional[builtins.str]:
        '''Public connection string that you can use to connect to this cluster.

        This connection string uses the mongodb+srv:// protocol.

        :schema: connectionStrings#StandardSrv
        '''
        result = self._values.get("standard_srv")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectionStrings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CriteriaView",
    jsii_struct_bases=[],
    name_mapping={
        "date_field": "dateField",
        "date_format": "dateFormat",
        "expire_after_days": "expireAfterDays",
        "query": "query",
        "type": "type",
    },
)
class CriteriaView:
    def __init__(
        self,
        *,
        date_field: typing.Optional[builtins.str] = None,
        date_format: typing.Optional["CriteriaViewDateFormat"] = None,
        expire_after_days: typing.Optional[jsii.Number] = None,
        query: typing.Optional[builtins.str] = None,
        type: typing.Optional["CriteriaViewType"] = None,
    ) -> None:
        '''
        :param date_field: Indexed database parameter that stores the date that determines when data moves to the online archive. MongoDB Cloud archives the data when the current date exceeds the date in this database parameter plus the number of days specified through the expireAfterDays parameter. Set this parameter when you set "criteria.type" : "DATE".
        :param date_format: Syntax used to write the date after which data moves to the online archive. Date can be expressed as ISO 8601 or Epoch timestamps. The Epoch timestamp can be expressed as nanoseconds, milliseconds, or seconds. Set this parameter when "criteria.type" : "DATE". You must set "criteria.type" : "DATE" if "collectionType": "TIMESERIES".
        :param expire_after_days: Number of days after the value in the criteria.dateField when MongoDB Cloud archives data in the specified cluster. Set this parameter when you set "criteria.type" : "DATE".
        :param query: MongoDB find query that selects documents to archive. The specified query follows the syntax of the db.collection.find(query) command. This query can't use the empty document ({}) to return all documents. Set this parameter when "criteria.type" : "CUSTOM".
        :param type: Means by which MongoDB Cloud selects data to archive. Data can be chosen using the age of the data or a MongoDB query. **DATE** selects documents to archive based on a date. **CUSTOM** selects documents to archive based on a custom JSON query. MongoDB Cloud doesn't support **CUSTOM** when ``"collectionType": "TIMESERIES"``.

        :schema: CriteriaView
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9178a762a9d17a97c4394e06788cc6c7cefffda2394f9af1cc3375a2f0e0cedf)
            check_type(argname="argument date_field", value=date_field, expected_type=type_hints["date_field"])
            check_type(argname="argument date_format", value=date_format, expected_type=type_hints["date_format"])
            check_type(argname="argument expire_after_days", value=expire_after_days, expected_type=type_hints["expire_after_days"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if date_field is not None:
            self._values["date_field"] = date_field
        if date_format is not None:
            self._values["date_format"] = date_format
        if expire_after_days is not None:
            self._values["expire_after_days"] = expire_after_days
        if query is not None:
            self._values["query"] = query
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def date_field(self) -> typing.Optional[builtins.str]:
        '''Indexed database parameter that stores the date that determines when data moves to the online archive.

        MongoDB Cloud archives the data when the current date exceeds the date in this database parameter plus the number of days specified through the expireAfterDays parameter. Set this parameter when you set "criteria.type" : "DATE".

        :schema: CriteriaView#DateField
        '''
        result = self._values.get("date_field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def date_format(self) -> typing.Optional["CriteriaViewDateFormat"]:
        '''Syntax used to write the date after which data moves to the online archive.

        Date can be expressed as ISO 8601 or Epoch timestamps. The Epoch timestamp can be expressed as nanoseconds, milliseconds, or seconds. Set this parameter when "criteria.type" : "DATE". You must set "criteria.type" : "DATE" if "collectionType": "TIMESERIES".

        :schema: CriteriaView#DateFormat
        '''
        result = self._values.get("date_format")
        return typing.cast(typing.Optional["CriteriaViewDateFormat"], result)

    @builtins.property
    def expire_after_days(self) -> typing.Optional[jsii.Number]:
        '''Number of days after the value in the criteria.dateField when MongoDB Cloud archives data in the specified cluster. Set this parameter when you set "criteria.type" : "DATE".

        :schema: CriteriaView#ExpireAfterDays
        '''
        result = self._values.get("expire_after_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def query(self) -> typing.Optional[builtins.str]:
        '''MongoDB find query that selects documents to archive.

        The specified query follows the syntax of the db.collection.find(query) command. This query can't use the empty document ({}) to return all documents. Set this parameter when "criteria.type" : "CUSTOM".

        :schema: CriteriaView#Query
        '''
        result = self._values.get("query")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional["CriteriaViewType"]:
        '''Means by which MongoDB Cloud selects data to archive.

        Data can be chosen using the age of the data or a MongoDB query.
        **DATE** selects documents to archive based on a date.
        **CUSTOM** selects documents to archive based on a custom JSON query. MongoDB Cloud doesn't support **CUSTOM** when ``"collectionType": "TIMESERIES"``.

        :schema: CriteriaView#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["CriteriaViewType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CriteriaView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.CriteriaViewDateFormat")
class CriteriaViewDateFormat(enum.Enum):
    '''Syntax used to write the date after which data moves to the online archive.

    Date can be expressed as ISO 8601 or Epoch timestamps. The Epoch timestamp can be expressed as nanoseconds, milliseconds, or seconds. Set this parameter when "criteria.type" : "DATE". You must set "criteria.type" : "DATE" if "collectionType": "TIMESERIES".

    :schema: CriteriaViewDateFormat
    '''

    ISODATE = "ISODATE"
    '''ISODATE.'''
    EPOCH_SECONDS = "EPOCH_SECONDS"
    '''EPOCH_SECONDS.'''
    EPOCH_MILLIS = "EPOCH_MILLIS"
    '''EPOCH_MILLIS.'''
    EPOCH_NANOSECONDS = "EPOCH_NANOSECONDS"
    '''EPOCH_NANOSECONDS.'''


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.CriteriaViewType")
class CriteriaViewType(enum.Enum):
    '''Means by which MongoDB Cloud selects data to archive.

    Data can be chosen using the age of the data or a MongoDB query.
    **DATE** selects documents to archive based on a date.
    **CUSTOM** selects documents to archive based on a custom JSON query. MongoDB Cloud doesn't support **CUSTOM** when ``"collectionType": "TIMESERIES"``.

    :schema: CriteriaViewType
    '''

    DATE = "DATE"
    '''DATE.'''
    CUSTOM = "CUSTOM"
    '''CUSTOM.'''


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.CustomerX509",
    jsii_struct_bases=[],
    name_mapping={"cas": "cas"},
)
class CustomerX509:
    def __init__(self, *, cas: typing.Optional[builtins.str] = None) -> None:
        '''
        :param cas: PEM string containing one or more customer CAs for database user authentication.

        :schema: customerX509
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8955783ba140d2d218b792195af3b8f839d43594be8ad7cb1b77dd1d80fc1fcf)
            check_type(argname="argument cas", value=cas, expected_type=type_hints["cas"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cas is not None:
            self._values["cas"] = cas

    @builtins.property
    def cas(self) -> typing.Optional[builtins.str]:
        '''PEM string containing one or more customer CAs for database user authentication.

        :schema: customerX509#Cas
        '''
        result = self._values.get("cas")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomerX509(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.DataLakeAwsCloudProviderConfigView",
    jsii_struct_bases=[],
    name_mapping={
        "external_id": "externalId",
        "iam_assumed_role_arn": "iamAssumedRoleArn",
        "iam_user_arn": "iamUserArn",
        "role_id": "roleId",
        "test_s3_bucket": "testS3Bucket",
    },
)
class DataLakeAwsCloudProviderConfigView:
    def __init__(
        self,
        *,
        external_id: typing.Optional[builtins.str] = None,
        iam_assumed_role_arn: typing.Optional[builtins.str] = None,
        iam_user_arn: typing.Optional[builtins.str] = None,
        role_id: typing.Optional[builtins.str] = None,
        test_s3_bucket: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param external_id: Unique identifier associated with the Identity and Access Management (IAM) role that the data lake assumes when accessing the data stores.
        :param iam_assumed_role_arn: Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that the data lake assumes when accessing data stores.
        :param iam_user_arn: Amazon Resource Name (ARN) of the user that the data lake assumes when accessing data stores.
        :param role_id: Unique identifier of the role that the data lake can use to access the data stores.Required if specifying cloudProviderConfig.
        :param test_s3_bucket: Name of the S3 data bucket that the provided role ID is authorized to access.Required if specifying cloudProviderConfig.

        :schema: DataLakeAWSCloudProviderConfigView
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64dae4bb023041c371e115c80ad9c19c45f3d9fe02e856c6300a224b0db099d9)
            check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
            check_type(argname="argument iam_assumed_role_arn", value=iam_assumed_role_arn, expected_type=type_hints["iam_assumed_role_arn"])
            check_type(argname="argument iam_user_arn", value=iam_user_arn, expected_type=type_hints["iam_user_arn"])
            check_type(argname="argument role_id", value=role_id, expected_type=type_hints["role_id"])
            check_type(argname="argument test_s3_bucket", value=test_s3_bucket, expected_type=type_hints["test_s3_bucket"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if external_id is not None:
            self._values["external_id"] = external_id
        if iam_assumed_role_arn is not None:
            self._values["iam_assumed_role_arn"] = iam_assumed_role_arn
        if iam_user_arn is not None:
            self._values["iam_user_arn"] = iam_user_arn
        if role_id is not None:
            self._values["role_id"] = role_id
        if test_s3_bucket is not None:
            self._values["test_s3_bucket"] = test_s3_bucket

    @builtins.property
    def external_id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier associated with the Identity and Access Management (IAM) role that the data lake assumes when accessing the data stores.

        :schema: DataLakeAWSCloudProviderConfigView#ExternalId
        '''
        result = self._values.get("external_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_assumed_role_arn(self) -> typing.Optional[builtins.str]:
        '''Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that the data lake assumes when accessing data stores.

        :schema: DataLakeAWSCloudProviderConfigView#IamAssumedRoleARN
        '''
        result = self._values.get("iam_assumed_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_user_arn(self) -> typing.Optional[builtins.str]:
        '''Amazon Resource Name (ARN) of the user that the data lake assumes when accessing data stores.

        :schema: DataLakeAWSCloudProviderConfigView#IamUserARN
        '''
        result = self._values.get("iam_user_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier of the role that the data lake can use to access the data stores.Required if specifying cloudProviderConfig.

        :schema: DataLakeAWSCloudProviderConfigView#RoleId
        '''
        result = self._values.get("role_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def test_s3_bucket(self) -> typing.Optional[builtins.str]:
        '''Name of the S3 data bucket that the provided role ID is authorized to access.Required if specifying cloudProviderConfig.

        :schema: DataLakeAWSCloudProviderConfigView#TestS3Bucket
        '''
        result = self._values.get("test_s3_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataLakeAwsCloudProviderConfigView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.DataLakeCloudProviderConfigView",
    jsii_struct_bases=[],
    name_mapping={"aws": "aws"},
)
class DataLakeCloudProviderConfigView:
    def __init__(
        self,
        *,
        aws: typing.Optional[typing.Union[DataLakeAwsCloudProviderConfigView, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aws: Name of the cloud service that hosts the data lake's data stores.

        :schema: DataLakeCloudProviderConfigView
        '''
        if isinstance(aws, dict):
            aws = DataLakeAwsCloudProviderConfigView(**aws)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7917368b756c11887541463887ec1b21b43fa1fe5cab7730a08caf1a0da47cd6)
            check_type(argname="argument aws", value=aws, expected_type=type_hints["aws"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws is not None:
            self._values["aws"] = aws

    @builtins.property
    def aws(self) -> typing.Optional[DataLakeAwsCloudProviderConfigView]:
        '''Name of the cloud service that hosts the data lake's data stores.

        :schema: DataLakeCloudProviderConfigView#Aws
        '''
        result = self._values.get("aws")
        return typing.cast(typing.Optional[DataLakeAwsCloudProviderConfigView], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataLakeCloudProviderConfigView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.DataLakeDataProcessRegionView",
    jsii_struct_bases=[],
    name_mapping={"cloud_provider": "cloudProvider", "region": "region"},
)
class DataLakeDataProcessRegionView:
    def __init__(
        self,
        *,
        cloud_provider: typing.Optional["DataLakeDataProcessRegionViewCloudProvider"] = None,
        region: typing.Optional["DataLakeDataProcessRegionViewRegion"] = None,
    ) -> None:
        '''
        :param cloud_provider: Name of the cloud service that hosts the data lake's data stores.
        :param region: Name of the region to which the data lake routes client connections.

        :schema: DataLakeDataProcessRegionView
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__446e9a05d8da528c995e54b7696432dabaf21c2c6d09fa3a6638fdafcbe9f7f3)
            check_type(argname="argument cloud_provider", value=cloud_provider, expected_type=type_hints["cloud_provider"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cloud_provider is not None:
            self._values["cloud_provider"] = cloud_provider
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def cloud_provider(
        self,
    ) -> typing.Optional["DataLakeDataProcessRegionViewCloudProvider"]:
        '''Name of the cloud service that hosts the data lake's data stores.

        :schema: DataLakeDataProcessRegionView#CloudProvider
        '''
        result = self._values.get("cloud_provider")
        return typing.cast(typing.Optional["DataLakeDataProcessRegionViewCloudProvider"], result)

    @builtins.property
    def region(self) -> typing.Optional["DataLakeDataProcessRegionViewRegion"]:
        '''Name of the region to which the data lake routes client connections.

        :schema: DataLakeDataProcessRegionView#Region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional["DataLakeDataProcessRegionViewRegion"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataLakeDataProcessRegionView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="awscdk-resources-mongodbatlas.DataLakeDataProcessRegionViewCloudProvider"
)
class DataLakeDataProcessRegionViewCloudProvider(enum.Enum):
    '''Name of the cloud service that hosts the data lake's data stores.

    :schema: DataLakeDataProcessRegionViewCloudProvider
    '''

    AWS = "AWS"
    '''AWS.'''
    GCP = "GCP"
    '''GCP.'''
    AZURE = "AZURE"
    '''AZURE.'''
    TENANT = "TENANT"
    '''TENANT.'''
    SERVERLESS = "SERVERLESS"
    '''SERVERLESS.'''


@jsii.enum(
    jsii_type="awscdk-resources-mongodbatlas.DataLakeDataProcessRegionViewRegion"
)
class DataLakeDataProcessRegionViewRegion(enum.Enum):
    '''Name of the region to which the data lake routes client connections.

    :schema: DataLakeDataProcessRegionViewRegion
    '''

    DUBLIN_IRL = "DUBLIN_IRL"
    '''DUBLIN_IRL.'''
    FRANKFURT_DEU = "FRANKFURT_DEU"
    '''FRANKFURT_DEU.'''
    LONDON_GBR = "LONDON_GBR"
    '''LONDON_GBR.'''
    MUMBAI_IND = "MUMBAI_IND"
    '''MUMBAI_IND.'''
    OREGON_USA = "OREGON_USA"
    '''OREGON_USA.'''
    SYDNEY_AUS = "SYDNEY_AUS"
    '''SYDNEY_AUS.'''
    VIRGINIA_USA = "VIRGINIA_USA"
    '''VIRGINIA_USA.'''


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.DataLakeDatabaseCollectionView",
    jsii_struct_bases=[],
    name_mapping={"data_sources": "dataSources", "name": "name"},
)
class DataLakeDatabaseCollectionView:
    def __init__(
        self,
        *,
        data_sources: typing.Optional[typing.Sequence[typing.Union["DataLakeDatabaseDataSourceView", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param data_sources: Array that contains the data stores that map to a collection for this data lake.
        :param name: Human-readable label that identifies the collection to which MongoDB Cloud maps the data in the data stores.

        :schema: DataLakeDatabaseCollectionView
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b48e2673acdeedad71f44b9523bd52f699c40277e2249f516c67ce3085455630)
            check_type(argname="argument data_sources", value=data_sources, expected_type=type_hints["data_sources"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if data_sources is not None:
            self._values["data_sources"] = data_sources
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def data_sources(
        self,
    ) -> typing.Optional[typing.List["DataLakeDatabaseDataSourceView"]]:
        '''Array that contains the data stores that map to a collection for this data lake.

        :schema: DataLakeDatabaseCollectionView#DataSources
        '''
        result = self._values.get("data_sources")
        return typing.cast(typing.Optional[typing.List["DataLakeDatabaseDataSourceView"]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the collection to which MongoDB Cloud maps the data in the data stores.

        :schema: DataLakeDatabaseCollectionView#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataLakeDatabaseCollectionView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.DataLakeDatabaseDataSourceView",
    jsii_struct_bases=[],
    name_mapping={
        "allow_insecure": "allowInsecure",
        "collection": "collection",
        "collection_regex": "collectionRegex",
        "database": "database",
        "default_format": "defaultFormat",
        "path": "path",
        "store_name": "storeName",
        "urls": "urls",
    },
)
class DataLakeDatabaseDataSourceView:
    def __init__(
        self,
        *,
        allow_insecure: typing.Optional[builtins.bool] = None,
        collection: typing.Optional[builtins.str] = None,
        collection_regex: typing.Optional[builtins.str] = None,
        database: typing.Optional[builtins.str] = None,
        default_format: typing.Optional["DataLakeDatabaseDataSourceViewDefaultFormat"] = None,
        path: typing.Optional[builtins.str] = None,
        store_name: typing.Optional[builtins.str] = None,
        urls: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param allow_insecure: Flag that validates the scheme in the specified URLs. If ``true``, allows insecure ``HTTP`` scheme, doesn't verify the server's certificate chain and hostname, and accepts any certificate with any hostname presented by the server. If ``false``, allows secure ``HTTPS`` scheme only.
        :param collection: Human-readable label that identifies the collection in the database. For creating a wildcard (``*``) collection, you must omit this parameter.
        :param collection_regex: Regex pattern to use for creating the wildcard (*) collection. To learn more about the regex syntax, see `Go programming language <https://pkg.go.dev/regexp>`_.
        :param database: Human-readable label that identifies the database, which contains the collection in the cluster. You must omit this parameter to generate wildcard (``*``) collections for dynamically generated databases.
        :param default_format: File format that MongoDB Cloud uses if it encounters a file without a file extension while searching **storeName**.
        :param path: File path that controls how MongoDB Cloud searches for and parses files in the **storeName** before mapping them to a collection.Specify ``/`` to capture all files and folders from the ``prefix`` path.
        :param store_name: Human-readable label that identifies the data store that MongoDB Cloud maps to the collection.
        :param urls: URLs of the publicly accessible data files. You can't specify URLs that require authentication. Atlas Data Lake creates a partition for each URL. If empty or omitted, Data Lake uses the URLs from the store specified in the **dataSources.storeName** parameter.

        :schema: DataLakeDatabaseDataSourceView
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dc74245ff120308aa3a02abf2de5307f8184271fca6b0b9ab5930c7d926163b)
            check_type(argname="argument allow_insecure", value=allow_insecure, expected_type=type_hints["allow_insecure"])
            check_type(argname="argument collection", value=collection, expected_type=type_hints["collection"])
            check_type(argname="argument collection_regex", value=collection_regex, expected_type=type_hints["collection_regex"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument default_format", value=default_format, expected_type=type_hints["default_format"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument store_name", value=store_name, expected_type=type_hints["store_name"])
            check_type(argname="argument urls", value=urls, expected_type=type_hints["urls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allow_insecure is not None:
            self._values["allow_insecure"] = allow_insecure
        if collection is not None:
            self._values["collection"] = collection
        if collection_regex is not None:
            self._values["collection_regex"] = collection_regex
        if database is not None:
            self._values["database"] = database
        if default_format is not None:
            self._values["default_format"] = default_format
        if path is not None:
            self._values["path"] = path
        if store_name is not None:
            self._values["store_name"] = store_name
        if urls is not None:
            self._values["urls"] = urls

    @builtins.property
    def allow_insecure(self) -> typing.Optional[builtins.bool]:
        '''Flag that validates the scheme in the specified URLs.

        If ``true``, allows insecure ``HTTP`` scheme, doesn't verify the server's certificate chain and hostname, and accepts any certificate with any hostname presented by the server. If ``false``, allows secure ``HTTPS`` scheme only.

        :schema: DataLakeDatabaseDataSourceView#AllowInsecure
        '''
        result = self._values.get("allow_insecure")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def collection(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the collection in the database.

        For creating a wildcard (``*``) collection, you must omit this parameter.

        :schema: DataLakeDatabaseDataSourceView#Collection
        '''
        result = self._values.get("collection")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def collection_regex(self) -> typing.Optional[builtins.str]:
        '''Regex pattern to use for creating the wildcard (*) collection.

        To learn more about the regex syntax, see `Go programming language <https://pkg.go.dev/regexp>`_.

        :schema: DataLakeDatabaseDataSourceView#CollectionRegex
        '''
        result = self._values.get("collection_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the database, which contains the collection in the cluster.

        You must omit this parameter to generate wildcard (``*``) collections for dynamically generated databases.

        :schema: DataLakeDatabaseDataSourceView#Database
        '''
        result = self._values.get("database")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_format(
        self,
    ) -> typing.Optional["DataLakeDatabaseDataSourceViewDefaultFormat"]:
        '''File format that MongoDB Cloud uses if it encounters a file without a file extension while searching **storeName**.

        :schema: DataLakeDatabaseDataSourceView#DefaultFormat
        '''
        result = self._values.get("default_format")
        return typing.cast(typing.Optional["DataLakeDatabaseDataSourceViewDefaultFormat"], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''File path that controls how MongoDB Cloud searches for and parses files in the **storeName** before mapping them to a collection.Specify ``/`` to capture all files and folders from the ``prefix`` path.

        :schema: DataLakeDatabaseDataSourceView#Path
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def store_name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the data store that MongoDB Cloud maps to the collection.

        :schema: DataLakeDatabaseDataSourceView#StoreName
        '''
        result = self._values.get("store_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def urls(self) -> typing.Optional[typing.List[builtins.str]]:
        '''URLs of the publicly accessible data files.

        You can't specify URLs that require authentication. Atlas Data Lake creates a partition for each URL. If empty or omitted, Data Lake uses the URLs from the store specified in the **dataSources.storeName** parameter.

        :schema: DataLakeDatabaseDataSourceView#Urls
        '''
        result = self._values.get("urls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataLakeDatabaseDataSourceView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="awscdk-resources-mongodbatlas.DataLakeDatabaseDataSourceViewDefaultFormat"
)
class DataLakeDatabaseDataSourceViewDefaultFormat(enum.Enum):
    '''File format that MongoDB Cloud uses if it encounters a file without a file extension while searching **storeName**.

    :schema: DataLakeDatabaseDataSourceViewDefaultFormat
    '''

    AVRO = "AVRO"
    '''.avro.'''
    AVRO_GZ = "AVRO_GZ"
    '''.avro.gz.'''
    BSON = "BSON"
    '''.bson.'''
    BSON_GZ = "BSON_GZ"
    '''.bson.gz.'''
    CSV = "CSV"
    '''.csv.'''
    JSON = "JSON"
    '''.json.'''
    JSON_GZ = "JSON_GZ"
    '''.json.gz.'''
    ORC = "ORC"
    '''.orc.'''
    TSV = "TSV"
    '''.tsv.'''
    TSV_GZ = "TSV_GZ"
    '''.tsv.gz.'''


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.DataLakeDatabaseView",
    jsii_struct_bases=[],
    name_mapping={
        "collections": "collections",
        "max_wildcard_collections": "maxWildcardCollections",
        "name": "name",
        "views": "views",
    },
)
class DataLakeDatabaseView:
    def __init__(
        self,
        *,
        collections: typing.Optional[typing.Sequence[typing.Union[DataLakeDatabaseCollectionView, typing.Dict[builtins.str, typing.Any]]]] = None,
        max_wildcard_collections: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        views: typing.Optional[typing.Sequence[typing.Union["DataLakeViewView", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param collections: Array of collections and data sources that map to a ``stores`` data store.
        :param max_wildcard_collections: Maximum number of wildcard collections in the database. This only applies to S3 data sources.
        :param name: Human-readable label that identifies the database to which the data lake maps data.
        :param views: Array of aggregation pipelines that apply to the collection. This only applies to S3 data sources.

        :schema: DataLakeDatabaseView
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb7c74972eb221456a5310f41795e50b4a9f95119db53ad880587aaa365a5c70)
            check_type(argname="argument collections", value=collections, expected_type=type_hints["collections"])
            check_type(argname="argument max_wildcard_collections", value=max_wildcard_collections, expected_type=type_hints["max_wildcard_collections"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument views", value=views, expected_type=type_hints["views"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if collections is not None:
            self._values["collections"] = collections
        if max_wildcard_collections is not None:
            self._values["max_wildcard_collections"] = max_wildcard_collections
        if name is not None:
            self._values["name"] = name
        if views is not None:
            self._values["views"] = views

    @builtins.property
    def collections(
        self,
    ) -> typing.Optional[typing.List[DataLakeDatabaseCollectionView]]:
        '''Array of collections and data sources that map to a ``stores`` data store.

        :schema: DataLakeDatabaseView#Collections
        '''
        result = self._values.get("collections")
        return typing.cast(typing.Optional[typing.List[DataLakeDatabaseCollectionView]], result)

    @builtins.property
    def max_wildcard_collections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of wildcard collections in the database.

        This only applies to S3 data sources.

        :schema: DataLakeDatabaseView#MaxWildcardCollections
        '''
        result = self._values.get("max_wildcard_collections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the database to which the data lake maps data.

        :schema: DataLakeDatabaseView#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def views(self) -> typing.Optional[typing.List["DataLakeViewView"]]:
        '''Array of aggregation pipelines that apply to the collection.

        This only applies to S3 data sources.

        :schema: DataLakeDatabaseView#Views
        '''
        result = self._values.get("views")
        return typing.cast(typing.Optional[typing.List["DataLakeViewView"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataLakeDatabaseView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.DataLakeStorageView",
    jsii_struct_bases=[],
    name_mapping={"databases": "databases", "stores": "stores"},
)
class DataLakeStorageView:
    def __init__(
        self,
        *,
        databases: typing.Optional[typing.Sequence[typing.Union[DataLakeDatabaseView, typing.Dict[builtins.str, typing.Any]]]] = None,
        stores: typing.Optional[typing.Sequence[typing.Union["StoreDetail", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param databases: Array that contains the queryable databases and collections for this data lake.
        :param stores: Array that contains the data stores for the data lake.

        :schema: DataLakeStorageView
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__491fe317a24ece5d6ac226c05284632fcbce71ac270d33bd6c7e52adeeeabed7)
            check_type(argname="argument databases", value=databases, expected_type=type_hints["databases"])
            check_type(argname="argument stores", value=stores, expected_type=type_hints["stores"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if databases is not None:
            self._values["databases"] = databases
        if stores is not None:
            self._values["stores"] = stores

    @builtins.property
    def databases(self) -> typing.Optional[typing.List[DataLakeDatabaseView]]:
        '''Array that contains the queryable databases and collections for this data lake.

        :schema: DataLakeStorageView#Databases
        '''
        result = self._values.get("databases")
        return typing.cast(typing.Optional[typing.List[DataLakeDatabaseView]], result)

    @builtins.property
    def stores(self) -> typing.Optional[typing.List["StoreDetail"]]:
        '''Array that contains the data stores for the data lake.

        :schema: DataLakeStorageView#Stores
        '''
        result = self._values.get("stores")
        return typing.cast(typing.Optional[typing.List["StoreDetail"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataLakeStorageView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.DataLakeViewView",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "pipeline": "pipeline", "source": "source"},
)
class DataLakeViewView:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        pipeline: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Human-readable label that identifies the view, which corresponds to an aggregation pipeline on a collection.
        :param pipeline: Aggregation pipeline stages to apply to the source collection.
        :param source: Human-readable label that identifies the source collection for the view.

        :schema: DataLakeViewView
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b23815afaae89643b0bf0689d6cd80752628bf73c49a1f2bd336360124c40886)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument pipeline", value=pipeline, expected_type=type_hints["pipeline"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if pipeline is not None:
            self._values["pipeline"] = pipeline
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the view, which corresponds to an aggregation pipeline on a collection.

        :schema: DataLakeViewView#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pipeline(self) -> typing.Optional[builtins.str]:
        '''Aggregation pipeline stages to apply to the source collection.

        :schema: DataLakeViewView#Pipeline
        '''
        result = self._values.get("pipeline")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the source collection for the view.

        :schema: DataLakeViewView#Source
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataLakeViewView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.DatabaseConfig",
    jsii_struct_bases=[],
    name_mapping={
        "collection": "collection",
        "database": "database",
        "full_document": "fullDocument",
        "full_document_before_change": "fullDocumentBeforeChange",
        "match": "match",
        "operation_types": "operationTypes",
        "project": "project",
        "service_id": "serviceId",
        "skip_catchup_events": "skipCatchupEvents",
        "tolerate_resume_errors": "tolerateResumeErrors",
        "unordered": "unordered",
    },
)
class DatabaseConfig:
    def __init__(
        self,
        *,
        collection: typing.Optional[builtins.str] = None,
        database: typing.Optional[builtins.str] = None,
        full_document: typing.Optional[builtins.bool] = None,
        full_document_before_change: typing.Optional[builtins.bool] = None,
        match: typing.Optional[builtins.str] = None,
        operation_types: typing.Optional[typing.Sequence["DatabaseConfigOperationTypes"]] = None,
        project: typing.Optional[builtins.str] = None,
        service_id: typing.Optional[builtins.str] = None,
        skip_catchup_events: typing.Optional[builtins.bool] = None,
        tolerate_resume_errors: typing.Optional[builtins.bool] = None,
        unordered: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param collection: The name of a collection in the specified database. The trigger listens to events from this collection.
        :param database: The name of a database in the linked data source.
        :param full_document: If ``true``, indicates that ``UPDATE`` change events should include the most current `majority-committed <https://www.mongodb.com/docs/manual/reference/read-concern-majority/>`_ version of the modified document in the ``fullDocument`` field.
        :param full_document_before_change: If true, indicates that ``UPDATE`` change events should include a snapshot of the modified document from immediately before the update was applied. You must enable `document preimages <https://www.mongodb.com/docs/atlas/app-services/mongodb/preimages/>`_ for your cluster to include these snapshots.
        :param match: stringify version of a `$match <https://www.mongodb.com/docs/manual/reference/operator/aggregation/match>`_ expression filters change events. The trigger will only fire if the expression evaluates to true for a given change event.
        :param operation_types: The type(s) of MongoDB change event that the trigger listens for.
        :param project: stringify version of a `$project <https://www.mongodb.com/docs/manual/reference/operator/aggregation/project/>`_ expressions to limit the data included in each event.
        :param service_id: The _id value of a linked MongoDB data source. See `Get a Data Source <#operation/adminGetService>`_.
        :param skip_catchup_events: If ``true``, enabling the Trigger after it was disabled will not invoke events that occurred while the Trigger was disabled.
        :param tolerate_resume_errors: If ``true``, when this Trigger's resume token cannot be found in the cluster's oplog, the Trigger automatically resumes processing events at the next relevant change stream event. All change stream events from when the Trigger was suspended until the Trigger resumes execution do not have the Trigger fire for them.
        :param unordered: If ``true``, event ordering is disabled and this Trigger can process events in parallel. If ``false``, event ordering is enabled and the Trigger executes events serially.

        :schema: DatabaseConfig
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c596fa3d50439f8375e9aa957e6ae339cc4ef295e632b62bcd5147d6a908f38d)
            check_type(argname="argument collection", value=collection, expected_type=type_hints["collection"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument full_document", value=full_document, expected_type=type_hints["full_document"])
            check_type(argname="argument full_document_before_change", value=full_document_before_change, expected_type=type_hints["full_document_before_change"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
            check_type(argname="argument operation_types", value=operation_types, expected_type=type_hints["operation_types"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument service_id", value=service_id, expected_type=type_hints["service_id"])
            check_type(argname="argument skip_catchup_events", value=skip_catchup_events, expected_type=type_hints["skip_catchup_events"])
            check_type(argname="argument tolerate_resume_errors", value=tolerate_resume_errors, expected_type=type_hints["tolerate_resume_errors"])
            check_type(argname="argument unordered", value=unordered, expected_type=type_hints["unordered"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if collection is not None:
            self._values["collection"] = collection
        if database is not None:
            self._values["database"] = database
        if full_document is not None:
            self._values["full_document"] = full_document
        if full_document_before_change is not None:
            self._values["full_document_before_change"] = full_document_before_change
        if match is not None:
            self._values["match"] = match
        if operation_types is not None:
            self._values["operation_types"] = operation_types
        if project is not None:
            self._values["project"] = project
        if service_id is not None:
            self._values["service_id"] = service_id
        if skip_catchup_events is not None:
            self._values["skip_catchup_events"] = skip_catchup_events
        if tolerate_resume_errors is not None:
            self._values["tolerate_resume_errors"] = tolerate_resume_errors
        if unordered is not None:
            self._values["unordered"] = unordered

    @builtins.property
    def collection(self) -> typing.Optional[builtins.str]:
        '''The name of a collection in the specified database.

        The
        trigger listens to events from this collection.

        :schema: DatabaseConfig#Collection
        '''
        result = self._values.get("collection")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database(self) -> typing.Optional[builtins.str]:
        '''The name of a database in the linked data source.

        :schema: DatabaseConfig#Database
        '''
        result = self._values.get("database")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def full_document(self) -> typing.Optional[builtins.bool]:
        '''If ``true``, indicates that ``UPDATE`` change events should include the most current `majority-committed <https://www.mongodb.com/docs/manual/reference/read-concern-majority/>`_ version of the modified document in the ``fullDocument`` field.

        :schema: DatabaseConfig#FullDocument
        '''
        result = self._values.get("full_document")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def full_document_before_change(self) -> typing.Optional[builtins.bool]:
        '''If true, indicates that ``UPDATE`` change events should include a snapshot of the modified document from immediately before the update was applied.

        You must enable `document
        preimages <https://www.mongodb.com/docs/atlas/app-services/mongodb/preimages/>`_
        for your cluster to include these snapshots.

        :schema: DatabaseConfig#FullDocumentBeforeChange
        '''
        result = self._values.get("full_document_before_change")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def match(self) -> typing.Optional[builtins.str]:
        '''stringify version of a `$match <https://www.mongodb.com/docs/manual/reference/operator/aggregation/match>`_ expression filters change events. The trigger will only fire if the expression evaluates to true for a given change event.

        :schema: DatabaseConfig#Match
        '''
        result = self._values.get("match")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operation_types(
        self,
    ) -> typing.Optional[typing.List["DatabaseConfigOperationTypes"]]:
        '''The type(s) of MongoDB change event that the trigger listens for.

        :schema: DatabaseConfig#OperationTypes
        '''
        result = self._values.get("operation_types")
        return typing.cast(typing.Optional[typing.List["DatabaseConfigOperationTypes"]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''stringify version of a `$project <https://www.mongodb.com/docs/manual/reference/operator/aggregation/project/>`_ expressions to limit the data included in each event.

        :schema: DatabaseConfig#Project
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_id(self) -> typing.Optional[builtins.str]:
        '''The _id value of a linked MongoDB data source.

        See `Get a Data Source <#operation/adminGetService>`_.

        :schema: DatabaseConfig#ServiceId
        '''
        result = self._values.get("service_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_catchup_events(self) -> typing.Optional[builtins.bool]:
        '''If ``true``, enabling the Trigger after it was disabled will not invoke events that occurred while the Trigger was disabled.

        :schema: DatabaseConfig#SkipCatchupEvents
        '''
        result = self._values.get("skip_catchup_events")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tolerate_resume_errors(self) -> typing.Optional[builtins.bool]:
        '''If ``true``, when this Trigger's resume token cannot be found in the cluster's oplog, the Trigger automatically resumes processing events at the next relevant change stream event.

        All change stream events from when the Trigger was suspended until the Trigger
        resumes execution do not have the Trigger fire for them.

        :schema: DatabaseConfig#TolerateResumeErrors
        '''
        result = self._values.get("tolerate_resume_errors")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def unordered(self) -> typing.Optional[builtins.bool]:
        '''If ``true``, event ordering is disabled and this Trigger can process events in parallel.

        If ``false``, event
        ordering is enabled and the Trigger executes events
        serially.

        :schema: DatabaseConfig#Unordered
        '''
        result = self._values.get("unordered")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.DatabaseConfigOperationTypes")
class DatabaseConfigOperationTypes(enum.Enum):
    '''
    :schema: DatabaseConfigOperationTypes
    '''

    INSERT = "INSERT"
    '''INSERT.'''
    UPDATE = "UPDATE"
    '''UPDATE.'''
    REPLACE = "REPLACE"
    '''REPLACE.'''
    DELETE = "DELETE"
    '''DELETE.'''


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.DatabaseUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "awsiam_type": "awsiamType",
        "database_name": "databaseName",
        "delete_after_date": "deleteAfterDate",
        "labels": "labels",
        "ldap_auth_type": "ldapAuthType",
        "password": "password",
        "project_id": "projectId",
        "roles": "roles",
        "scopes": "scopes",
        "username": "username",
        "x509_type": "x509Type",
    },
)
class DatabaseUserProps:
    def __init__(
        self,
        *,
        awsiam_type: typing.Optional[CfnDatabaseUserPropsAwsiamType] = None,
        database_name: typing.Optional[builtins.str] = None,
        delete_after_date: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Sequence[typing.Union["LabelDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        ldap_auth_type: typing.Optional[CfnDatabaseUserPropsLdapAuthType] = None,
        password: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.Sequence[typing.Union["RoleDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        scopes: typing.Optional[typing.Sequence[typing.Union["ScopeDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        username: typing.Optional[builtins.str] = None,
        x509_type: typing.Optional[CfnDatabaseUserPropsX509Type] = None,
    ) -> None:
        '''
        :param awsiam_type: 
        :param database_name: 
        :param delete_after_date: 
        :param labels: Default: admin
        :param ldap_auth_type: 
        :param password: 
        :param project_id: Default: cdk-pwd
        :param roles: 
        :param scopes: 
        :param username: Default: cdk-user
        :param x509_type: 

        :description: true
        :export: true
        :interface: DatabaseUserProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f89b9e37c1287f462039a624c6fa1c72740a2fa064ed0647aea56514a661a69)
            check_type(argname="argument awsiam_type", value=awsiam_type, expected_type=type_hints["awsiam_type"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument delete_after_date", value=delete_after_date, expected_type=type_hints["delete_after_date"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument ldap_auth_type", value=ldap_auth_type, expected_type=type_hints["ldap_auth_type"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument scopes", value=scopes, expected_type=type_hints["scopes"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument x509_type", value=x509_type, expected_type=type_hints["x509_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if awsiam_type is not None:
            self._values["awsiam_type"] = awsiam_type
        if database_name is not None:
            self._values["database_name"] = database_name
        if delete_after_date is not None:
            self._values["delete_after_date"] = delete_after_date
        if labels is not None:
            self._values["labels"] = labels
        if ldap_auth_type is not None:
            self._values["ldap_auth_type"] = ldap_auth_type
        if password is not None:
            self._values["password"] = password
        if project_id is not None:
            self._values["project_id"] = project_id
        if roles is not None:
            self._values["roles"] = roles
        if scopes is not None:
            self._values["scopes"] = scopes
        if username is not None:
            self._values["username"] = username
        if x509_type is not None:
            self._values["x509_type"] = x509_type

    @builtins.property
    def awsiam_type(self) -> typing.Optional[CfnDatabaseUserPropsAwsiamType]:
        '''
        :description: Human-readable label that indicates whether the new database user authenticates with the Amazon Web Services (AWS) Identity and Access Management (IAM) credentials associated with the user or the user's role. Default value is ``NONE``.
        :memberof: DatabaseUserProps
        :type: {user.CfnDatabaseUserPropsAwsiamType}
        '''
        result = self._values.get("awsiam_type")
        return typing.cast(typing.Optional[CfnDatabaseUserPropsAwsiamType], result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''
        :description: MongoDB database against which the MongoDB database user authenticates. MongoDB database users must provide both a username and authentication database to log into MongoDB.  Default value is ``admin``.
        :memberof: DatabaseUserProps
        :type: {string}
        '''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_after_date(self) -> typing.Optional[builtins.str]:
        '''
        :description: Date and time when MongoDB Cloud deletes the user. This parameter expresses its value in the ISO 8601 timestamp format in UTC and can include the time zone designation. You must specify a future date that falls within one week of making the Application Programming Interface (API) request.
        :memberof: DatabaseUserProps
        :type: {string}
        '''
        result = self._values.get("delete_after_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List["LabelDefinition"]]:
        '''
        :default: admin

        :description: List that contains the key-value pairs for tagging and categorizing the MongoDB database user. The labels that you define do not appear in the console.
        :memberof: DatabaseUserProps
        :type: {user.LabelDefinition[]}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List["LabelDefinition"]], result)

    @builtins.property
    def ldap_auth_type(self) -> typing.Optional[CfnDatabaseUserPropsLdapAuthType]:
        '''
        :description: Method by which the provided username is authenticated. Default value is ``NONE``.
        :memberof: DatabaseUserProps
        :type: {user.CfnDatabaseUserPropsLdapAuthType}
        '''
        result = self._values.get("ldap_auth_type")
        return typing.cast(typing.Optional[CfnDatabaseUserPropsLdapAuthType], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''
        :description: The user’s password. This field is not included in the entity returned from the server.
        :memberof: DatabaseUserProps
        :type: {string}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''
        :default: cdk-pwd

        :description: Unique 24-hexadecimal digit string that identifies your Atlas Project.
        :memberof: DatabaseUserProps
        :type: {string}
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def roles(self) -> typing.Optional[typing.List["RoleDefinition"]]:
        '''
        :description: List that provides the pairings of one role with one applicable database.
        :memberof: DatabaseUserProps
        :type: {user.RoleDefinition[]}
        '''
        result = self._values.get("roles")
        return typing.cast(typing.Optional[typing.List["RoleDefinition"]], result)

    @builtins.property
    def scopes(self) -> typing.Optional[typing.List["ScopeDefinition"]]:
        '''
        :description: List that contains clusters and MongoDB Atlas Data Lakes that this database user can access. If omitted, MongoDB Cloud grants the database user access to all the clusters and MongoDB Atlas Data Lakes in the project.
        :memberof: DatabaseUserProps
        :type: {user.ScopeDefinition[]}
        '''
        result = self._values.get("scopes")
        return typing.cast(typing.Optional[typing.List["ScopeDefinition"]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''
        :default: cdk-user

        :description: Human-readable label that represents the user that authenticates to MongoDB. The format of this label depends on the method of authentication. This will be USER_ARN or ROLE_ARN if AWSIAMType is USER or ROLE. Refer https://www.mongodb.com/docs/atlas/reference/api-resources-spec/#tag/Database-Users/operation/createDatabaseUser for details.
        :memberof: DatabaseUserProps
        :type: {string}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def x509_type(self) -> typing.Optional[CfnDatabaseUserPropsX509Type]:
        '''
        :description: Method that briefs who owns the certificate provided. Default value is ``NONE``.
        :memberof: DatabaseUserProps
        :type: {user.CfnDatabaseUserPropsX509Type}
        '''
        result = self._values.get("x509_type")
        return typing.cast(typing.Optional[CfnDatabaseUserPropsX509Type], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatadogIntegration(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.DatadogIntegration",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_key: builtins.str,
        region: "DatadogRegion",
        project_id: builtins.str,
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param api_key: Key that allows MongoDB Cloud to access your Datadog account.
        :param region: Two-letter code that indicates which regional URL MongoDB uses to access the Datadog API.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param profile: Atlas API keys.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56eba705c7c584194b1cc1f13195601f403c2566fc48adba8efd0fdd059a6dfd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DatadogIntegrationProps(
            api_key=api_key, region=region, project_id=project_id, profile=profile
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="cfnThirdPartyIntegration")
    def cfn_third_party_integration(self) -> CfnThirdPartyIntegration:
        return typing.cast(CfnThirdPartyIntegration, jsii.get(self, "cfnThirdPartyIntegration"))


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.DatadogRegion")
class DatadogRegion(enum.Enum):
    US = "US"
    EU = "EU"
    US3 = "US3"
    US5 = "US5"


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.DiskGb",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class DiskGb:
    def __init__(self, *, enabled: typing.Optional[builtins.bool] = None) -> None:
        '''Automatic cluster storage settings that apply to this cluster.

        :param enabled: Flag that indicates whether this cluster enables disk auto-scaling. The maximum memory allowed for the selected cluster tier and the oplog size can limit storage auto-scaling.

        :schema: diskGB
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10fcd199c44bba3157e152dd42a416da985ab6b1b0cc94062bd34e86ef8e4a85)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether this cluster enables disk auto-scaling.

        The maximum memory allowed for the selected cluster tier and the oplog size can limit storage auto-scaling.

        :schema: diskGB#Enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DiskGb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.EncryptionAtRestProps",
    jsii_struct_bases=[],
    name_mapping={
        "customer_master_key_id": "customerMasterKeyId",
        "role_id": "roleId",
        "enabled_encryption_at_rest": "enabledEncryptionAtRest",
        "region": "region",
    },
)
class EncryptionAtRestProps:
    def __init__(
        self,
        *,
        customer_master_key_id: builtins.str,
        role_id: builtins.str,
        enabled_encryption_at_rest: typing.Optional[builtins.bool] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param customer_master_key_id: The AWS customer master key used to encrypt and decrypt the MongoDB master keys.
        :param role_id: ID of an AWS IAM role authorized to manage an AWS customer master key.
        :param enabled_encryption_at_rest: Specifies whether Encryption at Rest is enabled for an Atlas project. To disable Encryption at Rest, pass only this parameter with a value of false. When you disable Encryption at Rest, Atlas also removes the configuration details. Default Value: true
        :param region: The AWS region in which the AWS customer master key exists.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__253978e3e3456c45cbc4a9c6cf2c9245ed80da206221d014db914b2702a7574b)
            check_type(argname="argument customer_master_key_id", value=customer_master_key_id, expected_type=type_hints["customer_master_key_id"])
            check_type(argname="argument role_id", value=role_id, expected_type=type_hints["role_id"])
            check_type(argname="argument enabled_encryption_at_rest", value=enabled_encryption_at_rest, expected_type=type_hints["enabled_encryption_at_rest"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "customer_master_key_id": customer_master_key_id,
            "role_id": role_id,
        }
        if enabled_encryption_at_rest is not None:
            self._values["enabled_encryption_at_rest"] = enabled_encryption_at_rest
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def customer_master_key_id(self) -> builtins.str:
        '''The AWS customer master key used to encrypt and decrypt the MongoDB master keys.

        :schema: AwsKms#CustomerMasterKeyID
        '''
        result = self._values.get("customer_master_key_id")
        assert result is not None, "Required property 'customer_master_key_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_id(self) -> builtins.str:
        '''ID of an AWS IAM role authorized to manage an AWS customer master key.

        :schema: AwsKms#RoleID
        '''
        result = self._values.get("role_id")
        assert result is not None, "Required property 'role_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled_encryption_at_rest(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether Encryption at Rest is enabled for an Atlas project.

        To disable Encryption at Rest, pass only this parameter with a value of false. When you disable Encryption at Rest, Atlas also removes the configuration details.
        Default Value: true

        :schema: AwsKms#Enabled
        '''
        result = self._values.get("enabled_encryption_at_rest")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The AWS region in which the AWS customer master key exists.

        :schema: AwsKms#Region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EncryptionAtRestProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.Endpoint",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_id": "endpointId",
        "provider_name": "providerName",
        "region": "region",
    },
)
class Endpoint:
    def __init__(
        self,
        *,
        endpoint_id: typing.Optional[builtins.str] = None,
        provider_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint_id: Unique string that the cloud provider uses to identify the private endpoint.
        :param provider_name: Cloud provider in which MongoDB Cloud deploys the private endpoint.
        :param region: Region in which MongoDB Cloud deploys the private endpoint.

        :schema: endpoint
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccae3eff9124ff17212ad0fbcb5515d1b4300cc0911df3d2086c1774127cdd03)
            check_type(argname="argument endpoint_id", value=endpoint_id, expected_type=type_hints["endpoint_id"])
            check_type(argname="argument provider_name", value=provider_name, expected_type=type_hints["provider_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if endpoint_id is not None:
            self._values["endpoint_id"] = endpoint_id
        if provider_name is not None:
            self._values["provider_name"] = provider_name
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def endpoint_id(self) -> typing.Optional[builtins.str]:
        '''Unique string that the cloud provider uses to identify the private endpoint.

        :schema: endpoint#EndpointID
        '''
        result = self._values.get("endpoint_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider_name(self) -> typing.Optional[builtins.str]:
        '''Cloud provider in which MongoDB Cloud deploys the private endpoint.

        :schema: endpoint#ProviderName
        '''
        result = self._values.get("provider_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Region in which MongoDB Cloud deploys the private endpoint.

        :schema: endpoint#Region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Endpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.Event",
    jsii_struct_bases=[],
    name_mapping={"awseventbridge": "awseventbridge", "function": "function"},
)
class Event:
    def __init__(
        self,
        *,
        awseventbridge: typing.Optional[typing.Union["EventAwseventbridge", typing.Dict[builtins.str, typing.Any]]] = None,
        function: typing.Optional[typing.Union["EventFunction", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param awseventbridge: 
        :param function: 

        :schema: Event
        '''
        if isinstance(awseventbridge, dict):
            awseventbridge = EventAwseventbridge(**awseventbridge)
        if isinstance(function, dict):
            function = EventFunction(**function)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0dc245443948b2ecc2b90f9696d91c16d5b80819be3878518bc91675db9ea50)
            check_type(argname="argument awseventbridge", value=awseventbridge, expected_type=type_hints["awseventbridge"])
            check_type(argname="argument function", value=function, expected_type=type_hints["function"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if awseventbridge is not None:
            self._values["awseventbridge"] = awseventbridge
        if function is not None:
            self._values["function"] = function

    @builtins.property
    def awseventbridge(self) -> typing.Optional["EventAwseventbridge"]:
        '''
        :schema: Event#AWSEVENTBRIDGE
        '''
        result = self._values.get("awseventbridge")
        return typing.cast(typing.Optional["EventAwseventbridge"], result)

    @builtins.property
    def function(self) -> typing.Optional["EventFunction"]:
        '''
        :schema: Event#FUNCTION
        '''
        result = self._values.get("function")
        return typing.cast(typing.Optional["EventFunction"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Event(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.EventAwseventbridge",
    jsii_struct_bases=[],
    name_mapping={"aws_config": "awsConfig"},
)
class EventAwseventbridge:
    def __init__(
        self,
        *,
        aws_config: typing.Optional[typing.Union["EventAwseventbridgeAwsConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aws_config: 

        :schema: EventAwseventbridge
        '''
        if isinstance(aws_config, dict):
            aws_config = EventAwseventbridgeAwsConfig(**aws_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccb20a14bea734882010cbf52775743642365eeb4a04d7727b7f9bc8eabf5341)
            check_type(argname="argument aws_config", value=aws_config, expected_type=type_hints["aws_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_config is not None:
            self._values["aws_config"] = aws_config

    @builtins.property
    def aws_config(self) -> typing.Optional["EventAwseventbridgeAwsConfig"]:
        '''
        :schema: EventAwseventbridge#AWSConfig
        '''
        result = self._values.get("aws_config")
        return typing.cast(typing.Optional["EventAwseventbridgeAwsConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventAwseventbridge(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.EventAwseventbridgeAwsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "extended_json_enabled": "extendedJsonEnabled",
        "region": "region",
    },
)
class EventAwseventbridgeAwsConfig:
    def __init__(
        self,
        *,
        account_id: typing.Optional[builtins.str] = None,
        extended_json_enabled: typing.Optional[builtins.bool] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account_id: An AWS Account ID.
        :param extended_json_enabled: If ``true``, event objects are serialized using EJSON.
        :param region: An AWS region.

        :schema: EventAwseventbridgeAwsConfig
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__171cb758e4fd8eadf647fb131f3f029d40f7d0aca69e5223c23803a0bc1000a8)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument extended_json_enabled", value=extended_json_enabled, expected_type=type_hints["extended_json_enabled"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if account_id is not None:
            self._values["account_id"] = account_id
        if extended_json_enabled is not None:
            self._values["extended_json_enabled"] = extended_json_enabled
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''An AWS Account ID.

        :schema: EventAwseventbridgeAwsConfig#AccountId
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extended_json_enabled(self) -> typing.Optional[builtins.bool]:
        '''If ``true``, event objects are serialized using EJSON.

        :schema: EventAwseventbridgeAwsConfig#ExtendedJsonEnabled
        '''
        result = self._values.get("extended_json_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''An AWS region.

        :schema: EventAwseventbridgeAwsConfig#Region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventAwseventbridgeAwsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.EventFunction",
    jsii_struct_bases=[],
    name_mapping={"func_config": "funcConfig"},
)
class EventFunction:
    def __init__(
        self,
        *,
        func_config: typing.Optional[typing.Union["EventFunctionFuncConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param func_config: 

        :schema: EventFunction
        '''
        if isinstance(func_config, dict):
            func_config = EventFunctionFuncConfig(**func_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29a68d656e22e4e69d8e52f1162ca3bacb251ab920f753a5799d04e6c2aed37a)
            check_type(argname="argument func_config", value=func_config, expected_type=type_hints["func_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if func_config is not None:
            self._values["func_config"] = func_config

    @builtins.property
    def func_config(self) -> typing.Optional["EventFunctionFuncConfig"]:
        '''
        :schema: EventFunction#FuncConfig
        '''
        result = self._values.get("func_config")
        return typing.cast(typing.Optional["EventFunctionFuncConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventFunction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.EventFunctionFuncConfig",
    jsii_struct_bases=[],
    name_mapping={"function_id": "functionId", "function_name": "functionName"},
)
class EventFunctionFuncConfig:
    def __init__(
        self,
        *,
        function_id: typing.Optional[builtins.str] = None,
        function_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param function_id: The ID of the function that the trigger calls when it fires. This value is the same as the root-level ``function_id``. You can either define the value here or in ``function_id``. The App Services backend duplicates the value to the configuration location where you did not define it. For example, if you define ``event_processors.FUNCTION.function_id``, the backend duplicates it to ``function_id``.
        :param function_name: The name of the function that the trigger calls when it fires, i.e. the function described by ``function_id``. This value is the same as the root-level ``function_name``. You can either define the value here or in ``function_name``. The App Services backend duplicates the value to the configuration location where you did not define it. For example, if you define ``event_processors.FUNCTION.function_name``, the backend duplicates it to ``function_name``.

        :schema: EventFunctionFuncConfig
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c938d24f56144895cdf1463b758f168301b2c657fd5bc09eda286bde4135f38)
            check_type(argname="argument function_id", value=function_id, expected_type=type_hints["function_id"])
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if function_id is not None:
            self._values["function_id"] = function_id
        if function_name is not None:
            self._values["function_name"] = function_name

    @builtins.property
    def function_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the function that the trigger calls when it fires.

        This value is the same as the root-level ``function_id``.
        You can either define the value here or in ``function_id``.
        The App Services backend duplicates the value to the configuration location where you did not define it.

        For example, if you define ``event_processors.FUNCTION.function_id``, the backend duplicates it to ``function_id``.

        :schema: EventFunctionFuncConfig#FunctionId
        '''
        result = self._values.get("function_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def function_name(self) -> typing.Optional[builtins.str]:
        '''The name of the function that the trigger calls when it fires, i.e. the function described by ``function_id``.

        This value is the same as the root-level ``function_name``.
        You can either define the value here or in ``function_name``.
        The App Services backend duplicates the value to the configuration location where you did not define it.

        For example, if you define ``event_processors.FUNCTION.function_name``, the backend duplicates it to ``function_name``.

        :schema: EventFunctionFuncConfig#FunctionName
        '''
        result = self._values.get("function_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventFunctionFuncConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.Export",
    jsii_struct_bases=[],
    name_mapping={
        "export_bucket_id": "exportBucketId",
        "frequency_type": "frequencyType",
    },
)
class Export:
    def __init__(
        self,
        *,
        export_bucket_id: typing.Optional[builtins.str] = None,
        frequency_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param export_bucket_id: Unique identifier of the AWS bucket to export the cloud backup snapshot to.
        :param frequency_type: Frequency associated with the export policy. Value can be daily, weekly, or monthly.

        :schema: Export
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7332b18961cc042f9a0c566841cf2685eece9e1b8ac11fa81944688826e6a42f)
            check_type(argname="argument export_bucket_id", value=export_bucket_id, expected_type=type_hints["export_bucket_id"])
            check_type(argname="argument frequency_type", value=frequency_type, expected_type=type_hints["frequency_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if export_bucket_id is not None:
            self._values["export_bucket_id"] = export_bucket_id
        if frequency_type is not None:
            self._values["frequency_type"] = frequency_type

    @builtins.property
    def export_bucket_id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier of the AWS bucket to export the cloud backup snapshot to.

        :schema: Export#ExportBucketId
        '''
        result = self._values.get("export_bucket_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def frequency_type(self) -> typing.Optional[builtins.str]:
        '''Frequency associated with the export policy.

        Value can be daily, weekly, or monthly.

        :schema: Export#FrequencyType
        '''
        result = self._values.get("frequency_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Export(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.InheritedRole",
    jsii_struct_bases=[],
    name_mapping={"db": "db", "role": "role"},
)
class InheritedRole:
    def __init__(
        self,
        *,
        db: typing.Optional[builtins.str] = None,
        role: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param db: 
        :param role: 

        :schema: InheritedRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffb58f5e14a6c6202ae6a247485c1a771bdbcf4faf4f5127281018096ec7ea7e)
            check_type(argname="argument db", value=db, expected_type=type_hints["db"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if db is not None:
            self._values["db"] = db
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def db(self) -> typing.Optional[builtins.str]:
        '''
        :schema: InheritedRole#Db
        '''
        result = self._values.get("db")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''
        :schema: InheritedRole#Role
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InheritedRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.IntegerThresholdView",
    jsii_struct_bases=[],
    name_mapping={"operator": "operator", "threshold": "threshold", "units": "units"},
)
class IntegerThresholdView:
    def __init__(
        self,
        *,
        operator: typing.Optional["IntegerThresholdViewOperator"] = None,
        threshold: typing.Optional[jsii.Number] = None,
        units: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param operator: Comparison operator to apply when checking the current metric value.
        :param threshold: Value of metric that, when exceeded, triggers an alert.
        :param units: Element used to express the quantity. This can be an element of time, storage capacity, and the like.

        :schema: IntegerThresholdView
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce5e7db4624f7765b99e64e51ce61c9491658bd0e6e96f4dfa31f550e4d3e43b)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument units", value=units, expected_type=type_hints["units"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if operator is not None:
            self._values["operator"] = operator
        if threshold is not None:
            self._values["threshold"] = threshold
        if units is not None:
            self._values["units"] = units

    @builtins.property
    def operator(self) -> typing.Optional["IntegerThresholdViewOperator"]:
        '''Comparison operator to apply when checking the current metric value.

        :schema: IntegerThresholdView#Operator
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional["IntegerThresholdViewOperator"], result)

    @builtins.property
    def threshold(self) -> typing.Optional[jsii.Number]:
        '''Value of metric that, when exceeded, triggers an alert.

        :schema: IntegerThresholdView#Threshold
        '''
        result = self._values.get("threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def units(self) -> typing.Optional[builtins.str]:
        '''Element used to express the quantity.

        This can be an element of time, storage capacity, and the like.

        :schema: IntegerThresholdView#Units
        '''
        result = self._values.get("units")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IntegerThresholdView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.IntegerThresholdViewOperator")
class IntegerThresholdViewOperator(enum.Enum):
    '''Comparison operator to apply when checking the current metric value.

    :schema: IntegerThresholdViewOperator
    '''

    GREATER_THAN = "GREATER_THAN"
    '''GREATER_THAN.'''
    LESS_THAN = "LESS_THAN"
    '''LESS_THAN.'''


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.IpAccessListProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_list": "accessList",
        "list_options": "listOptions",
        "project_id": "projectId",
        "total_count": "totalCount",
    },
)
class IpAccessListProps:
    def __init__(
        self,
        *,
        access_list: typing.Sequence[typing.Union[AccessListDefinition, typing.Dict[builtins.str, typing.Any]]],
        list_options: typing.Optional[typing.Union["ListOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        project_id: typing.Optional[builtins.str] = None,
        total_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param access_list: 
        :param list_options: 
        :param project_id: Default: allow-all
        :param total_count: 

        :description: Returns, adds, edits, and removes network access limits to database deployments in MongoDB Cloud.
        :export: true
        :interface: IpAccessListProps
        '''
        if isinstance(list_options, dict):
            list_options = ListOptions(**list_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f7d63d578a57067631a2a1db8a32af1ddfa54c5ea6ddeb8a83d8fccd180b69a)
            check_type(argname="argument access_list", value=access_list, expected_type=type_hints["access_list"])
            check_type(argname="argument list_options", value=list_options, expected_type=type_hints["list_options"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument total_count", value=total_count, expected_type=type_hints["total_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_list": access_list,
        }
        if list_options is not None:
            self._values["list_options"] = list_options
        if project_id is not None:
            self._values["project_id"] = project_id
        if total_count is not None:
            self._values["total_count"] = total_count

    @builtins.property
    def access_list(self) -> typing.List[AccessListDefinition]:
        '''
        :description: true
        :memberof: IpAccessListProps
        :type: {ipAccessList.AccessListDefinition[]}
        '''
        result = self._values.get("access_list")
        assert result is not None, "Required property 'access_list' is missing"
        return typing.cast(typing.List[AccessListDefinition], result)

    @builtins.property
    def list_options(self) -> typing.Optional["ListOptions"]:
        '''
        :description: true
        :memberof: IpAccessListProps
        :type: {ipAccessList.ListOptions}
        '''
        result = self._values.get("list_options")
        return typing.cast(typing.Optional["ListOptions"], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''
        :default: allow-all

        :description: Unique 24-hexadecimal digit string that identifies your project.
        :memberof: IpAccessListProps
        :type: {string}
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def total_count(self) -> typing.Optional[jsii.Number]:
        '''
        :description: Number of documents returned in this response.
        :memberof: IpAccessListProps
        :type: {number}
        '''
        result = self._values.get("total_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IpAccessListProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.LabelDefinition",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class LabelDefinition:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: 
        :param value: 

        :schema: labelDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8c031af21c2cdb4b9e1a18fd37d89f994af7a0789480328d6defe09a75e8ce6)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: labelDefinition#Key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''
        :schema: labelDefinition#Value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LabelDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.Link",
    jsii_struct_bases=[],
    name_mapping={"href": "href", "rel": "rel"},
)
class Link:
    def __init__(
        self,
        *,
        href: typing.Optional[builtins.str] = None,
        rel: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param href: Uniform Resource Locator (URL) that points another API resource to which this response has some relationship. This URL often begins with ``https://mms.mongodb.com``.
        :param rel: Uniform Resource Locator (URL) that defines the semantic relationship between this resource and another API resource. This URL often begins with ``https://mms.mongodb.com``.

        :schema: Link
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c52915f0b0cda2d2fc193f5a02edc121c5cddb3ed21a4241f3cbabffec1b4ced)
            check_type(argname="argument href", value=href, expected_type=type_hints["href"])
            check_type(argname="argument rel", value=rel, expected_type=type_hints["rel"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if href is not None:
            self._values["href"] = href
        if rel is not None:
            self._values["rel"] = rel

    @builtins.property
    def href(self) -> typing.Optional[builtins.str]:
        '''Uniform Resource Locator (URL) that points another API resource to which this response has some relationship.

        This URL often begins with ``https://mms.mongodb.com``.

        :schema: Link#Href
        '''
        result = self._values.get("href")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rel(self) -> typing.Optional[builtins.str]:
        '''Uniform Resource Locator (URL) that defines the semantic relationship between this resource and another API resource.

        This URL often begins with ``https://mms.mongodb.com``.

        :schema: Link#Rel
        '''
        result = self._values.get("rel")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Link(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ListOptions",
    jsii_struct_bases=[],
    name_mapping={
        "include_count": "includeCount",
        "items_per_page": "itemsPerPage",
        "page_num": "pageNum",
    },
)
class ListOptions:
    def __init__(
        self,
        *,
        include_count: typing.Optional[builtins.bool] = None,
        items_per_page: typing.Optional[jsii.Number] = None,
        page_num: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param include_count: Flag that indicates whether the response returns the total number of items (totalCount) in the response.
        :param items_per_page: Number of items that the response returns per page.
        :param page_num: Number of the page that displays the current set of the total objects that the response returns.

        :schema: listOptions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37f570e907501747a6f0a9537110ff2c160b28ece28a9bc456a39b023474ec39)
            check_type(argname="argument include_count", value=include_count, expected_type=type_hints["include_count"])
            check_type(argname="argument items_per_page", value=items_per_page, expected_type=type_hints["items_per_page"])
            check_type(argname="argument page_num", value=page_num, expected_type=type_hints["page_num"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if include_count is not None:
            self._values["include_count"] = include_count
        if items_per_page is not None:
            self._values["items_per_page"] = items_per_page
        if page_num is not None:
            self._values["page_num"] = page_num

    @builtins.property
    def include_count(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether the response returns the total number of items (totalCount) in the response.

        :schema: listOptions#IncludeCount
        '''
        result = self._values.get("include_count")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def items_per_page(self) -> typing.Optional[jsii.Number]:
        '''Number of items that the response returns per page.

        :schema: listOptions#ItemsPerPage
        '''
        result = self._values.get("items_per_page")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def page_num(self) -> typing.Optional[jsii.Number]:
        '''Number of the page that displays the current set of the total objects that the response returns.

        :schema: listOptions#PageNum
        '''
        result = self._values.get("page_num")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ManagedNamespace",
    jsii_struct_bases=[],
    name_mapping={
        "collection": "collection",
        "custom_shard_key": "customShardKey",
        "db": "db",
        "is_custom_shard_key_hashed": "isCustomShardKeyHashed",
        "is_shard_key_unique": "isShardKeyUnique",
    },
)
class ManagedNamespace:
    def __init__(
        self,
        *,
        collection: typing.Optional[builtins.str] = None,
        custom_shard_key: typing.Optional[builtins.str] = None,
        db: typing.Optional[builtins.str] = None,
        is_custom_shard_key_hashed: typing.Optional[builtins.bool] = None,
        is_shard_key_unique: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param collection: Human-readable label of the collection to manage for this Global Cluster.
        :param custom_shard_key: Database parameter used to divide the *collection* into shards. Global clusters require a compound shard key. This compound shard key combines the location parameter and the user-selected custom key.
        :param db: Human-readable label of the database to manage for this Global Cluster.
        :param is_custom_shard_key_hashed: Flag that indicates whether someone hashed the custom shard key for the specified collection. If you set this value to ``false``, MongoDB Cloud uses ranged sharding.
        :param is_shard_key_unique: Flag that indicates whether someone `hashed <https://www.mongodb.com/docs/manual/reference/method/sh.shardCollection/#hashed-shard-keys>`_ the custom shard key. If this parameter returns ``false``, this cluster uses `ranged sharding <https://www.mongodb.com/docs/manual/core/ranged-sharding/>`_.

        :schema: managedNamespace
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54680a11e9c3c9531eb236189cac739387e25736004725511d1445883cc1f274)
            check_type(argname="argument collection", value=collection, expected_type=type_hints["collection"])
            check_type(argname="argument custom_shard_key", value=custom_shard_key, expected_type=type_hints["custom_shard_key"])
            check_type(argname="argument db", value=db, expected_type=type_hints["db"])
            check_type(argname="argument is_custom_shard_key_hashed", value=is_custom_shard_key_hashed, expected_type=type_hints["is_custom_shard_key_hashed"])
            check_type(argname="argument is_shard_key_unique", value=is_shard_key_unique, expected_type=type_hints["is_shard_key_unique"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if collection is not None:
            self._values["collection"] = collection
        if custom_shard_key is not None:
            self._values["custom_shard_key"] = custom_shard_key
        if db is not None:
            self._values["db"] = db
        if is_custom_shard_key_hashed is not None:
            self._values["is_custom_shard_key_hashed"] = is_custom_shard_key_hashed
        if is_shard_key_unique is not None:
            self._values["is_shard_key_unique"] = is_shard_key_unique

    @builtins.property
    def collection(self) -> typing.Optional[builtins.str]:
        '''Human-readable label of the collection to manage for this Global Cluster.

        :schema: managedNamespace#Collection
        '''
        result = self._values.get("collection")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_shard_key(self) -> typing.Optional[builtins.str]:
        '''Database parameter used to divide the *collection* into shards.

        Global clusters require a compound shard key. This compound shard key combines the location parameter and the user-selected custom key.

        :schema: managedNamespace#CustomShardKey
        '''
        result = self._values.get("custom_shard_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db(self) -> typing.Optional[builtins.str]:
        '''Human-readable label of the database to manage for this Global Cluster.

        :schema: managedNamespace#Db
        '''
        result = self._values.get("db")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_custom_shard_key_hashed(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether someone hashed the custom shard key for the specified collection.

        If you set this value to ``false``, MongoDB Cloud uses ranged sharding.

        :schema: managedNamespace#IsCustomShardKeyHashed
        '''
        result = self._values.get("is_custom_shard_key_hashed")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def is_shard_key_unique(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether someone `hashed <https://www.mongodb.com/docs/manual/reference/method/sh.shardCollection/#hashed-shard-keys>`_ the custom shard key. If this parameter returns ``false``, this cluster uses `ranged sharding <https://www.mongodb.com/docs/manual/core/ranged-sharding/>`_.

        :schema: managedNamespace#IsShardKeyUnique
        '''
        result = self._values.get("is_shard_key_unique")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedNamespace(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.Matcher",
    jsii_struct_bases=[],
    name_mapping={"field_name": "fieldName", "operator": "operator", "value": "value"},
)
class Matcher:
    def __init__(
        self,
        *,
        field_name: typing.Optional["MatcherFieldName"] = None,
        operator: typing.Optional["MatcherOperator"] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param field_name: Name of the parameter in the target object that MongoDB Cloud checks. The parameter must match all rules for MongoDB Cloud to check for alert configurations.
        :param operator: Comparison operator to apply when checking the current metric value against **matcher[n].value**.
        :param value: Value to match or exceed using the specified **matchers.operator**.

        :schema: Matcher
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32b2259b94ea91c87f55ce869b3a735b3844213b5d13c282ad53f024b95395ab)
            check_type(argname="argument field_name", value=field_name, expected_type=type_hints["field_name"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if field_name is not None:
            self._values["field_name"] = field_name
        if operator is not None:
            self._values["operator"] = operator
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def field_name(self) -> typing.Optional["MatcherFieldName"]:
        '''Name of the parameter in the target object that MongoDB Cloud checks.

        The parameter must match all rules for MongoDB Cloud to check for alert configurations.

        :schema: Matcher#FieldName
        '''
        result = self._values.get("field_name")
        return typing.cast(typing.Optional["MatcherFieldName"], result)

    @builtins.property
    def operator(self) -> typing.Optional["MatcherOperator"]:
        '''Comparison operator to apply when checking the current metric value against **matcher[n].value**.

        :schema: Matcher#Operator
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional["MatcherOperator"], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Value to match or exceed using the specified **matchers.operator**.

        :schema: Matcher#Value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Matcher(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.MatcherFieldName")
class MatcherFieldName(enum.Enum):
    '''Name of the parameter in the target object that MongoDB Cloud checks.

    The parameter must match all rules for MongoDB Cloud to check for alert configurations.

    :schema: MatcherFieldName
    '''

    CLUSTER_NAME = "CLUSTER_NAME"
    '''CLUSTER_NAME.'''
    HOSTNAME = "HOSTNAME"
    '''HOSTNAME.'''
    HOSTNAME_AND_PORT = "HOSTNAME_AND_PORT"
    '''HOSTNAME_AND_PORT.'''
    PORT = "PORT"
    '''PORT.'''
    REPLICA_SET_NAME = "REPLICA_SET_NAME"
    '''REPLICA_SET_NAME.'''
    SHARD_NAME = "SHARD_NAME"
    '''SHARD_NAME.'''
    TYPE_NAME = "TYPE_NAME"
    '''TYPE_NAME.'''


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.MatcherOperator")
class MatcherOperator(enum.Enum):
    '''Comparison operator to apply when checking the current metric value against **matcher[n].value**.

    :schema: MatcherOperator
    '''

    EQUALS = "EQUALS"
    '''EQUALS.'''
    CONTAINS = "CONTAINS"
    '''CONTAINS.'''
    STARTS_WITH = "STARTS_WITH"
    '''STARTS_WITH.'''
    ENDS_WITH = "ENDS_WITH"
    '''ENDS_WITH.'''
    NOT_EQUALS = "NOT_EQUALS"
    '''NOT_EQUALS.'''
    NOT_CONTAINS = "NOT_CONTAINS"
    '''NOT_CONTAINS.'''
    REGEX = "REGEX"
    '''REGEX.'''


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.MetricThresholdView",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "mode": "mode",
        "operator": "operator",
        "threshold": "threshold",
        "units": "units",
    },
)
class MetricThresholdView:
    def __init__(
        self,
        *,
        metric_name: typing.Optional[builtins.str] = None,
        mode: typing.Optional["MetricThresholdViewMode"] = None,
        operator: typing.Optional["MetricThresholdViewOperator"] = None,
        threshold: typing.Optional[jsii.Number] = None,
        units: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Human-readable label that identifies the metric against which MongoDB Cloud checks the configured **metricThreshold.threshold**.
        :param mode: MongoDB Cloud computes the current metric value as an average.
        :param operator: Comparison operator to apply when checking the current metric value.
        :param threshold: Value of metric that, when exceeded, triggers an alert.
        :param units: Element used to express the quantity. This can be an element of time, storage capacity, and the like.

        :schema: MetricThresholdView
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c291ccce2257cf6fd490c747b0093b22db3ae35f9b19ed83014f2205fbeee58)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument units", value=units, expected_type=type_hints["units"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metric_name is not None:
            self._values["metric_name"] = metric_name
        if mode is not None:
            self._values["mode"] = mode
        if operator is not None:
            self._values["operator"] = operator
        if threshold is not None:
            self._values["threshold"] = threshold
        if units is not None:
            self._values["units"] = units

    @builtins.property
    def metric_name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the metric against which MongoDB Cloud checks the configured **metricThreshold.threshold**.

        :schema: MetricThresholdView#MetricName
        '''
        result = self._values.get("metric_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mode(self) -> typing.Optional["MetricThresholdViewMode"]:
        '''MongoDB Cloud computes the current metric value as an average.

        :schema: MetricThresholdView#Mode
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional["MetricThresholdViewMode"], result)

    @builtins.property
    def operator(self) -> typing.Optional["MetricThresholdViewOperator"]:
        '''Comparison operator to apply when checking the current metric value.

        :schema: MetricThresholdView#Operator
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional["MetricThresholdViewOperator"], result)

    @builtins.property
    def threshold(self) -> typing.Optional[jsii.Number]:
        '''Value of metric that, when exceeded, triggers an alert.

        :schema: MetricThresholdView#Threshold
        '''
        result = self._values.get("threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def units(self) -> typing.Optional[builtins.str]:
        '''Element used to express the quantity.

        This can be an element of time, storage capacity, and the like.

        :schema: MetricThresholdView#Units
        '''
        result = self._values.get("units")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricThresholdView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.MetricThresholdViewMode")
class MetricThresholdViewMode(enum.Enum):
    '''MongoDB Cloud computes the current metric value as an average.

    :schema: MetricThresholdViewMode
    '''

    AVERAGE = "AVERAGE"
    '''AVERAGE.'''


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.MetricThresholdViewOperator")
class MetricThresholdViewOperator(enum.Enum):
    '''Comparison operator to apply when checking the current metric value.

    :schema: MetricThresholdViewOperator
    '''

    GREATER_THAN = "GREATER_THAN"
    '''GREATER_THAN.'''
    LESS_THAN = "LESS_THAN"
    '''LESS_THAN.'''


class MicrosoftTeamsIntegration(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.MicrosoftTeamsIntegration",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        microsoft_teams_webhook_url: builtins.str,
        project_id: builtins.str,
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param microsoft_teams_webhook_url: Endpoint web address of the Microsoft Teams webhook to which MongoDB Cloud sends notifications.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param profile: Atlas API keys.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73e18f91e94120d8c86aeb405540116b113fb0abc1dee76b3bd19a5a1046ecb3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = MicrosoftTeamsIntegrationProps(
            microsoft_teams_webhook_url=microsoft_teams_webhook_url,
            project_id=project_id,
            profile=profile,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="cfnThirdPartyIntegration")
    def cfn_third_party_integration(self) -> CfnThirdPartyIntegration:
        return typing.cast(CfnThirdPartyIntegration, jsii.get(self, "cfnThirdPartyIntegration"))


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.NotificationView",
    jsii_struct_bases=[],
    name_mapping={
        "api_token": "apiToken",
        "channel_name": "channelName",
        "datadog_api_key": "datadogApiKey",
        "datadog_region": "datadogRegion",
        "delay_min": "delayMin",
        "email_address": "emailAddress",
        "email_enabled": "emailEnabled",
        "flowdock_api_token": "flowdockApiToken",
        "flow_name": "flowName",
        "interval_min": "intervalMin",
        "microsoft_teams_webhook_url": "microsoftTeamsWebhookUrl",
        "mobile_number": "mobileNumber",
        "notification_token": "notificationToken",
        "ops_genie_api_key": "opsGenieApiKey",
        "ops_genie_region": "opsGenieRegion",
        "org_name": "orgName",
        "roles": "roles",
        "room_name": "roomName",
        "service_key": "serviceKey",
        "severity": "severity",
        "sms_enabled": "smsEnabled",
        "team_id": "teamId",
        "team_name": "teamName",
        "type_name": "typeName",
        "username": "username",
        "victor_ops_api_key": "victorOpsApiKey",
        "victor_ops_routing_key": "victorOpsRoutingKey",
        "webhook_secret": "webhookSecret",
        "webhook_url": "webhookUrl",
    },
)
class NotificationView:
    def __init__(
        self,
        *,
        api_token: typing.Optional[builtins.str] = None,
        channel_name: typing.Optional[builtins.str] = None,
        datadog_api_key: typing.Optional[builtins.str] = None,
        datadog_region: typing.Optional["NotificationViewDatadogRegion"] = None,
        delay_min: typing.Optional[jsii.Number] = None,
        email_address: typing.Optional[builtins.str] = None,
        email_enabled: typing.Optional[builtins.bool] = None,
        flowdock_api_token: typing.Optional[builtins.str] = None,
        flow_name: typing.Optional[builtins.str] = None,
        interval_min: typing.Optional[jsii.Number] = None,
        microsoft_teams_webhook_url: typing.Optional[builtins.str] = None,
        mobile_number: typing.Optional[builtins.str] = None,
        notification_token: typing.Optional[builtins.str] = None,
        ops_genie_api_key: typing.Optional[builtins.str] = None,
        ops_genie_region: typing.Optional["NotificationViewOpsGenieRegion"] = None,
        org_name: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.Sequence["NotificationViewRoles"]] = None,
        room_name: typing.Optional[builtins.str] = None,
        service_key: typing.Optional[builtins.str] = None,
        severity: typing.Optional["NotificationViewSeverity"] = None,
        sms_enabled: typing.Optional[builtins.bool] = None,
        team_id: typing.Optional[builtins.str] = None,
        team_name: typing.Optional[builtins.str] = None,
        type_name: typing.Optional["NotificationViewTypeName"] = None,
        username: typing.Optional[builtins.str] = None,
        victor_ops_api_key: typing.Optional[builtins.str] = None,
        victor_ops_routing_key: typing.Optional[builtins.str] = None,
        webhook_secret: typing.Optional[builtins.str] = None,
        webhook_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_token: Slack API token or Bot token that MongoDB Cloud needs to send alert notifications via Slack. The resource requires this parameter when '"notifications.typeName" : "SLACK"'. If the token later becomes invalid, MongoDB Cloud sends an email to the project owners. If the token remains invalid, MongoDB Cloud removes the token.
        :param channel_name: Name of the Slack channel to which MongoDB Cloud sends alert notifications. The resource requires this parameter when '"notifications.typeName" : "SLACK"'.
        :param datadog_api_key: Datadog API Key that MongoDB Cloud needs to send alert notifications to Datadog. You can find this API key in the Datadog dashboard. The resource requires this parameter when '"notifications.typeName" : "DATADOG"'.
        :param datadog_region: Datadog region that indicates which API Uniform Resource Locator (URL) to use. The resource requires this parameter when '"notifications.typeName" : "DATADOG"'.
        :param delay_min: Number of minutes that MongoDB Cloud waits after detecting an alert condition before it sends out the first notification.
        :param email_address: Email address to which MongoDB Cloud sends alert notifications. The resource requires this parameter when '"notifications.typeName" : "EMAIL"'. You don't need to set this value to send emails to individual or groups of MongoDB Cloud users including: - specific MongoDB Cloud users ('"notifications.typeName" : "USER"') - MongoDB Cloud users with specific project roles ('"notifications.typeName" : "GROUP"') - MongoDB Cloud users with specific organization roles ('"notifications.typeName" : "ORG"') - MongoDB Cloud teams ('"notifications.typeName" : "TEAM"') To send emails to one MongoDB Cloud user or grouping of users, set the **notifications.emailEnabled** parameter.
        :param email_enabled: Flag that indicates whether MongoDB Cloud should send email notifications. The resource requires this parameter when one of the following values have been set: - '"notifications.typeName" : "ORG"' - '"notifications.typeName" : "GROUP"' - '"notifications.typeName" : "USER"'
        :param flowdock_api_token: Flowdock API token that MongoDB Cloud needs to send alert notifications to Flowdock. The resource requires this parameter when '"notifications.typeName" : "FLOWDOCK"'. If the token later becomes invalid, MongoDB Cloud sends an email to the project owners. If the token remains invalid, MongoDB Cloud removes the token.
        :param flow_name: Flowdock flow name to which MongoDB Cloud sends alert notifications. This name appears after the organization name in the Uniform Resource Locator (URL) path: 'www.flowdock.com/app//'. The resource requires this parameter when '"notifications.typeName" : "FLOWDOCK"'.
        :param interval_min: Number of minutes to wait between successive notifications. MongoDB Cloud sends notifications until someone acknowledges the unacknowledged alert. PagerDuty, VictorOps, and OpsGenie notifications don't return this element. Configure and manage the notification interval within each of those services.
        :param microsoft_teams_webhook_url: Microsoft Teams Webhook Uniform Resource Locator (URL) that MongoDB Cloud needs to send this notification via Microsoft Teams. The resource requires this parameter when '"notifications.typeName" : "MICROSOFT_TEAMS"'. If the URL later becomes invalid, MongoDB Cloud sends an email to the project owners. If the key remains invalid, MongoDB Cloud removes it.
        :param mobile_number: Mobile phone number to which MongoDB Cloud sends alert notifications. The resource requires this parameter when '"notifications.typeName" : "SMS"'.
        :param notification_token: HipChat API token that MongoDB Cloud needs to send alert notifications to HipChat. The resource requires this parameter when '"notifications.typeName" : "HIP_CHAT"'". If the token later becomes invalid, MongoDB Cloud sends an email to the project owners. If the token remains invalid, MongoDB Cloud removes it.
        :param ops_genie_api_key: API Key that MongoDB Cloud needs to send this notification via Opsgenie. The resource requires this parameter when '"notifications.typeName" : "OPS_GENIE"'. If the key later becomes invalid, MongoDB Cloud sends an email to the project owners. If the key remains invalid, MongoDB Cloud removes it.
        :param ops_genie_region: Opsgenie region that indicates which API Uniform Resource Locator (URL) to use.
        :param org_name: Flowdock organization name to which MongoDB Cloud sends alert notifications. This name appears after 'www.flowdock.com/app/' in the Uniform Resource Locator (URL) path. The resource requires this parameter when '"notifications.typeName" : "FLOWDOCK"'.
        :param roles: List that contains the one or more organization or project roles that receive the configured alert. The resource requires this parameter when '"notifications.typeName" : "GROUP"' or '"notifications.typeName" : "ORG"'. If you include this parameter, MongoDB Cloud sends alerts only to users assigned the roles you specify in the array. If you omit this parameter, MongoDB Cloud sends alerts to users assigned any role.
        :param room_name: HipChat API room name to which MongoDB Cloud sends alert notifications. The resource requires this parameter when '"notifications.typeName" : "HIP_CHAT"'".
        :param service_key: PagerDuty service key that MongoDB Cloud needs to send notifications via PagerDuty. The resource requires this parameter when '"notifications.typeName" : "PAGER_DUTY"'. If the key later becomes invalid, MongoDB Cloud sends an email to the project owners. If the key remains invalid, MongoDB Cloud removes it.
        :param severity: Degree of seriousness given to this notification.
        :param sms_enabled: Flag that indicates whether MongoDB Cloud should send text message notifications. The resource requires this parameter when one of the following values have been set: - '"notifications.typeName" : "ORG"' - '"notifications.typeName" : "GROUP"' - '"notifications.typeName" : "USER"'
        :param team_id: Unique 24-hexadecimal digit string that identifies one MongoDB Cloud team. The resource requires this parameter when '"notifications.typeName" : "TEAM"'.
        :param team_name: Name of the MongoDB Cloud team that receives this notification. The resource requires this parameter when '"notifications.typeName" : "TEAM"'.
        :param type_name: Human-readable label that displays the alert notification type.
        :param username: MongoDB Cloud username of the person to whom MongoDB Cloud sends notifications. Specify only MongoDB Cloud users who belong to the project that owns the alert configuration. The resource requires this parameter when '"notifications.typeName" : "USER"'.
        :param victor_ops_api_key: API key that MongoDB Cloud needs to send alert notifications to Splunk On-Call. The resource requires this parameter when '"notifications.typeName" : "VICTOR_OPS"'. If the key later becomes invalid, MongoDB Cloud sends an email to the project owners. If the key remains invalid, MongoDB Cloud removes it.
        :param victor_ops_routing_key: Routing key that MongoDB Cloud needs to send alert notifications to Splunk On-Call. The resource requires this parameter when '"notifications.typeName" : "VICTOR_OPS"'. If the key later becomes invalid, MongoDB Cloud sends an email to the project owners. If the key remains invalid, MongoDB Cloud removes it.
        :param webhook_secret: An optional field for your webhook secret.
        :param webhook_url: Your webhook URL.

        :schema: NotificationView
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18ce630edcb8981a87f2402df2cecd72fb5a7a174629deea172a99f905404141)
            check_type(argname="argument api_token", value=api_token, expected_type=type_hints["api_token"])
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
            check_type(argname="argument datadog_api_key", value=datadog_api_key, expected_type=type_hints["datadog_api_key"])
            check_type(argname="argument datadog_region", value=datadog_region, expected_type=type_hints["datadog_region"])
            check_type(argname="argument delay_min", value=delay_min, expected_type=type_hints["delay_min"])
            check_type(argname="argument email_address", value=email_address, expected_type=type_hints["email_address"])
            check_type(argname="argument email_enabled", value=email_enabled, expected_type=type_hints["email_enabled"])
            check_type(argname="argument flowdock_api_token", value=flowdock_api_token, expected_type=type_hints["flowdock_api_token"])
            check_type(argname="argument flow_name", value=flow_name, expected_type=type_hints["flow_name"])
            check_type(argname="argument interval_min", value=interval_min, expected_type=type_hints["interval_min"])
            check_type(argname="argument microsoft_teams_webhook_url", value=microsoft_teams_webhook_url, expected_type=type_hints["microsoft_teams_webhook_url"])
            check_type(argname="argument mobile_number", value=mobile_number, expected_type=type_hints["mobile_number"])
            check_type(argname="argument notification_token", value=notification_token, expected_type=type_hints["notification_token"])
            check_type(argname="argument ops_genie_api_key", value=ops_genie_api_key, expected_type=type_hints["ops_genie_api_key"])
            check_type(argname="argument ops_genie_region", value=ops_genie_region, expected_type=type_hints["ops_genie_region"])
            check_type(argname="argument org_name", value=org_name, expected_type=type_hints["org_name"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument room_name", value=room_name, expected_type=type_hints["room_name"])
            check_type(argname="argument service_key", value=service_key, expected_type=type_hints["service_key"])
            check_type(argname="argument severity", value=severity, expected_type=type_hints["severity"])
            check_type(argname="argument sms_enabled", value=sms_enabled, expected_type=type_hints["sms_enabled"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
            check_type(argname="argument team_name", value=team_name, expected_type=type_hints["team_name"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument victor_ops_api_key", value=victor_ops_api_key, expected_type=type_hints["victor_ops_api_key"])
            check_type(argname="argument victor_ops_routing_key", value=victor_ops_routing_key, expected_type=type_hints["victor_ops_routing_key"])
            check_type(argname="argument webhook_secret", value=webhook_secret, expected_type=type_hints["webhook_secret"])
            check_type(argname="argument webhook_url", value=webhook_url, expected_type=type_hints["webhook_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if api_token is not None:
            self._values["api_token"] = api_token
        if channel_name is not None:
            self._values["channel_name"] = channel_name
        if datadog_api_key is not None:
            self._values["datadog_api_key"] = datadog_api_key
        if datadog_region is not None:
            self._values["datadog_region"] = datadog_region
        if delay_min is not None:
            self._values["delay_min"] = delay_min
        if email_address is not None:
            self._values["email_address"] = email_address
        if email_enabled is not None:
            self._values["email_enabled"] = email_enabled
        if flowdock_api_token is not None:
            self._values["flowdock_api_token"] = flowdock_api_token
        if flow_name is not None:
            self._values["flow_name"] = flow_name
        if interval_min is not None:
            self._values["interval_min"] = interval_min
        if microsoft_teams_webhook_url is not None:
            self._values["microsoft_teams_webhook_url"] = microsoft_teams_webhook_url
        if mobile_number is not None:
            self._values["mobile_number"] = mobile_number
        if notification_token is not None:
            self._values["notification_token"] = notification_token
        if ops_genie_api_key is not None:
            self._values["ops_genie_api_key"] = ops_genie_api_key
        if ops_genie_region is not None:
            self._values["ops_genie_region"] = ops_genie_region
        if org_name is not None:
            self._values["org_name"] = org_name
        if roles is not None:
            self._values["roles"] = roles
        if room_name is not None:
            self._values["room_name"] = room_name
        if service_key is not None:
            self._values["service_key"] = service_key
        if severity is not None:
            self._values["severity"] = severity
        if sms_enabled is not None:
            self._values["sms_enabled"] = sms_enabled
        if team_id is not None:
            self._values["team_id"] = team_id
        if team_name is not None:
            self._values["team_name"] = team_name
        if type_name is not None:
            self._values["type_name"] = type_name
        if username is not None:
            self._values["username"] = username
        if victor_ops_api_key is not None:
            self._values["victor_ops_api_key"] = victor_ops_api_key
        if victor_ops_routing_key is not None:
            self._values["victor_ops_routing_key"] = victor_ops_routing_key
        if webhook_secret is not None:
            self._values["webhook_secret"] = webhook_secret
        if webhook_url is not None:
            self._values["webhook_url"] = webhook_url

    @builtins.property
    def api_token(self) -> typing.Optional[builtins.str]:
        '''Slack API token or Bot token that MongoDB Cloud needs to send alert notifications via Slack.

        The resource requires this parameter when '"notifications.typeName" : "SLACK"'. If the token later becomes invalid, MongoDB Cloud sends an email to the project owners. If the token remains invalid, MongoDB Cloud removes the token.

        :schema: NotificationView#ApiToken
        '''
        result = self._values.get("api_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def channel_name(self) -> typing.Optional[builtins.str]:
        '''Name of the Slack channel to which MongoDB Cloud sends alert notifications.

        The resource requires this parameter when '"notifications.typeName" : "SLACK"'.

        :schema: NotificationView#ChannelName
        '''
        result = self._values.get("channel_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def datadog_api_key(self) -> typing.Optional[builtins.str]:
        '''Datadog API Key that MongoDB Cloud needs to send alert notifications to Datadog.

        You can find this API key in the Datadog dashboard. The resource requires this parameter when '"notifications.typeName" : "DATADOG"'.

        :schema: NotificationView#DatadogApiKey
        '''
        result = self._values.get("datadog_api_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def datadog_region(self) -> typing.Optional["NotificationViewDatadogRegion"]:
        '''Datadog region that indicates which API Uniform Resource Locator (URL) to use.

        The resource requires this parameter when '"notifications.typeName" : "DATADOG"'.

        :schema: NotificationView#DatadogRegion
        '''
        result = self._values.get("datadog_region")
        return typing.cast(typing.Optional["NotificationViewDatadogRegion"], result)

    @builtins.property
    def delay_min(self) -> typing.Optional[jsii.Number]:
        '''Number of minutes that MongoDB Cloud waits after detecting an alert condition before it sends out the first notification.

        :schema: NotificationView#DelayMin
        '''
        result = self._values.get("delay_min")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def email_address(self) -> typing.Optional[builtins.str]:
        '''Email address to which MongoDB Cloud sends alert notifications.

        The resource requires this parameter when '"notifications.typeName" : "EMAIL"'. You don't need to set this value to send emails to individual or groups of MongoDB Cloud users including:

        - specific MongoDB Cloud users ('"notifications.typeName" : "USER"')
        - MongoDB Cloud users with specific project roles ('"notifications.typeName" : "GROUP"')
        - MongoDB Cloud users with specific organization roles ('"notifications.typeName" : "ORG"')
        - MongoDB Cloud teams ('"notifications.typeName" : "TEAM"')

        To send emails to one MongoDB Cloud user or grouping of users, set the **notifications.emailEnabled** parameter.

        :schema: NotificationView#EmailAddress
        '''
        result = self._values.get("email_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_enabled(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether MongoDB Cloud should send email notifications.

        The resource requires this parameter when one of the following values have been set:

        - '"notifications.typeName" : "ORG"'
        - '"notifications.typeName" : "GROUP"'
        - '"notifications.typeName" : "USER"'

        :schema: NotificationView#EmailEnabled
        '''
        result = self._values.get("email_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def flowdock_api_token(self) -> typing.Optional[builtins.str]:
        '''Flowdock API token that MongoDB Cloud needs to send alert notifications to Flowdock.

        The resource requires this parameter when '"notifications.typeName" : "FLOWDOCK"'. If the token later becomes invalid, MongoDB Cloud sends an email to the project owners. If the token remains invalid, MongoDB Cloud removes the token.

        :schema: NotificationView#FlowdockApiToken
        '''
        result = self._values.get("flowdock_api_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flow_name(self) -> typing.Optional[builtins.str]:
        '''Flowdock flow name to which MongoDB Cloud sends alert notifications.

        This name appears after the organization name in the Uniform Resource Locator (URL) path: 'www.flowdock.com/app//'. The resource requires this parameter when '"notifications.typeName" : "FLOWDOCK"'.

        :schema: NotificationView#FlowName
        '''
        result = self._values.get("flow_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def interval_min(self) -> typing.Optional[jsii.Number]:
        '''Number of minutes to wait between successive notifications. MongoDB Cloud sends notifications until someone acknowledges the unacknowledged alert.

        PagerDuty, VictorOps, and OpsGenie notifications don't return this element. Configure and manage the notification interval within each of those services.

        :schema: NotificationView#IntervalMin
        '''
        result = self._values.get("interval_min")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def microsoft_teams_webhook_url(self) -> typing.Optional[builtins.str]:
        '''Microsoft Teams Webhook Uniform Resource Locator (URL) that MongoDB Cloud needs to send this notification via Microsoft Teams.

        The resource requires this parameter when '"notifications.typeName" : "MICROSOFT_TEAMS"'. If the URL later becomes invalid, MongoDB Cloud sends an email to the project owners. If the key remains invalid, MongoDB Cloud removes it.

        :schema: NotificationView#MicrosoftTeamsWebhookUrl
        '''
        result = self._values.get("microsoft_teams_webhook_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mobile_number(self) -> typing.Optional[builtins.str]:
        '''Mobile phone number to which MongoDB Cloud sends alert notifications.

        The resource requires this parameter when '"notifications.typeName" : "SMS"'.

        :schema: NotificationView#MobileNumber
        '''
        result = self._values.get("mobile_number")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_token(self) -> typing.Optional[builtins.str]:
        '''HipChat API token that MongoDB Cloud needs to send alert notifications to HipChat.

        The resource requires this parameter when '"notifications.typeName" : "HIP_CHAT"'". If the token later becomes invalid, MongoDB Cloud sends an email to the project owners. If the token remains invalid, MongoDB Cloud removes it.

        :schema: NotificationView#NotificationToken
        '''
        result = self._values.get("notification_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ops_genie_api_key(self) -> typing.Optional[builtins.str]:
        '''API Key that MongoDB Cloud needs to send this notification via Opsgenie.

        The resource requires this parameter when '"notifications.typeName" : "OPS_GENIE"'. If the key later becomes invalid, MongoDB Cloud sends an email to the project owners. If the key remains invalid, MongoDB Cloud removes it.

        :schema: NotificationView#OpsGenieApiKey
        '''
        result = self._values.get("ops_genie_api_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ops_genie_region(self) -> typing.Optional["NotificationViewOpsGenieRegion"]:
        '''Opsgenie region that indicates which API Uniform Resource Locator (URL) to use.

        :schema: NotificationView#OpsGenieRegion
        '''
        result = self._values.get("ops_genie_region")
        return typing.cast(typing.Optional["NotificationViewOpsGenieRegion"], result)

    @builtins.property
    def org_name(self) -> typing.Optional[builtins.str]:
        '''Flowdock organization name to which MongoDB Cloud sends alert notifications.

        This name appears after 'www.flowdock.com/app/' in the Uniform Resource Locator (URL) path. The resource requires this parameter when '"notifications.typeName" : "FLOWDOCK"'.

        :schema: NotificationView#OrgName
        '''
        result = self._values.get("org_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def roles(self) -> typing.Optional[typing.List["NotificationViewRoles"]]:
        '''List that contains the one or more organization or project roles that receive the configured alert.

        The resource requires this parameter when '"notifications.typeName" : "GROUP"' or '"notifications.typeName" : "ORG"'. If you include this parameter, MongoDB Cloud sends alerts only to users assigned the roles you specify in the array. If you omit this parameter, MongoDB Cloud sends alerts to users assigned any role.

        :schema: NotificationView#Roles
        '''
        result = self._values.get("roles")
        return typing.cast(typing.Optional[typing.List["NotificationViewRoles"]], result)

    @builtins.property
    def room_name(self) -> typing.Optional[builtins.str]:
        '''HipChat API room name to which MongoDB Cloud sends alert notifications.

        The resource requires this parameter when '"notifications.typeName" : "HIP_CHAT"'".

        :schema: NotificationView#RoomName
        '''
        result = self._values.get("room_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_key(self) -> typing.Optional[builtins.str]:
        '''PagerDuty service key that MongoDB Cloud needs to send notifications via PagerDuty.

        The resource requires this parameter when '"notifications.typeName" : "PAGER_DUTY"'. If the key later becomes invalid, MongoDB Cloud sends an email to the project owners. If the key remains invalid, MongoDB Cloud removes it.

        :schema: NotificationView#ServiceKey
        '''
        result = self._values.get("service_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def severity(self) -> typing.Optional["NotificationViewSeverity"]:
        '''Degree of seriousness given to this notification.

        :schema: NotificationView#Severity
        '''
        result = self._values.get("severity")
        return typing.cast(typing.Optional["NotificationViewSeverity"], result)

    @builtins.property
    def sms_enabled(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether MongoDB Cloud should send text message notifications.

        The resource requires this parameter when one of the following values have been set:

        - '"notifications.typeName" : "ORG"'
        - '"notifications.typeName" : "GROUP"'
        - '"notifications.typeName" : "USER"'

        :schema: NotificationView#SmsEnabled
        '''
        result = self._values.get("sms_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def team_id(self) -> typing.Optional[builtins.str]:
        '''Unique 24-hexadecimal digit string that identifies one MongoDB Cloud team.

        The resource requires this parameter when '"notifications.typeName" : "TEAM"'.

        :schema: NotificationView#TeamId
        '''
        result = self._values.get("team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def team_name(self) -> typing.Optional[builtins.str]:
        '''Name of the MongoDB Cloud team that receives this notification.

        The resource requires this parameter when '"notifications.typeName" : "TEAM"'.

        :schema: NotificationView#TeamName
        '''
        result = self._values.get("team_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name(self) -> typing.Optional["NotificationViewTypeName"]:
        '''Human-readable label that displays the alert notification type.

        :schema: NotificationView#TypeName
        '''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional["NotificationViewTypeName"], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''MongoDB Cloud username of the person to whom MongoDB Cloud sends notifications.

        Specify only MongoDB Cloud users who belong to the project that owns the alert configuration. The resource requires this parameter when '"notifications.typeName" : "USER"'.

        :schema: NotificationView#Username
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def victor_ops_api_key(self) -> typing.Optional[builtins.str]:
        '''API key that MongoDB Cloud needs to send alert notifications to Splunk On-Call.

        The resource requires this parameter when '"notifications.typeName" : "VICTOR_OPS"'. If the key later becomes invalid, MongoDB Cloud sends an email to the project owners. If the key remains invalid, MongoDB Cloud removes it.

        :schema: NotificationView#VictorOpsApiKey
        '''
        result = self._values.get("victor_ops_api_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def victor_ops_routing_key(self) -> typing.Optional[builtins.str]:
        '''Routing key that MongoDB Cloud needs to send alert notifications to Splunk On-Call.

        The resource requires this parameter when '"notifications.typeName" : "VICTOR_OPS"'. If the key later becomes invalid, MongoDB Cloud sends an email to the project owners. If the key remains invalid, MongoDB Cloud removes it.

        :schema: NotificationView#VictorOpsRoutingKey
        '''
        result = self._values.get("victor_ops_routing_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def webhook_secret(self) -> typing.Optional[builtins.str]:
        '''An optional field for your webhook secret.

        :schema: NotificationView#WebhookSecret
        '''
        result = self._values.get("webhook_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def webhook_url(self) -> typing.Optional[builtins.str]:
        '''Your webhook URL.

        :schema: NotificationView#WebhookUrl
        '''
        result = self._values.get("webhook_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.NotificationViewDatadogRegion")
class NotificationViewDatadogRegion(enum.Enum):
    '''Datadog region that indicates which API Uniform Resource Locator (URL) to use.

    The resource requires this parameter when '"notifications.typeName" : "DATADOG"'.

    :schema: NotificationViewDatadogRegion
    '''

    EU = "EU"
    '''EU.'''
    US = "US"
    '''US.'''


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.NotificationViewOpsGenieRegion")
class NotificationViewOpsGenieRegion(enum.Enum):
    '''Opsgenie region that indicates which API Uniform Resource Locator (URL) to use.

    :schema: NotificationViewOpsGenieRegion
    '''

    EU = "EU"
    '''EU.'''
    US = "US"
    '''US.'''


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.NotificationViewRoles")
class NotificationViewRoles(enum.Enum):
    '''
    :schema: NotificationViewRoles
    '''

    GROUP_CLUSTER_MANAGER = "GROUP_CLUSTER_MANAGER"
    '''GROUP_CLUSTER_MANAGER.'''
    GROUP_DATA_ACCESS_ADMIN = "GROUP_DATA_ACCESS_ADMIN"
    '''GROUP_DATA_ACCESS_ADMIN.'''
    GROUP_DATA_ACCESS_READ_ONLY = "GROUP_DATA_ACCESS_READ_ONLY"
    '''GROUP_DATA_ACCESS_READ_ONLY.'''
    GROUP_DATA_ACCESS_READ_WRITE = "GROUP_DATA_ACCESS_READ_WRITE"
    '''GROUP_DATA_ACCESS_READ_WRITE.'''
    GROUP_OWNER = "GROUP_OWNER"
    '''GROUP_OWNER.'''
    GROUP_READ_WRITE = "GROUP_READ_WRITE"
    '''GROUP_READ_WRITE.'''
    ORG_OWNER = "ORG_OWNER"
    '''ORG_OWNER.'''
    ORG_MEMBER = "ORG_MEMBER"
    '''ORG_MEMBER.'''
    ORG_GROUP_CREATOR = "ORG_GROUP_CREATOR"
    '''ORG_GROUP_CREATOR.'''
    ORG_BILLING_ADMIN = "ORG_BILLING_ADMIN"
    '''ORG_BILLING_ADMIN.'''
    ORG_READ_ONLY = "ORG_READ_ONLY"
    '''ORG_READ_ONLY.'''


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.NotificationViewSeverity")
class NotificationViewSeverity(enum.Enum):
    '''Degree of seriousness given to this notification.

    :schema: NotificationViewSeverity
    '''

    CRITICAL = "CRITICAL"
    '''CRITICAL.'''
    ERROR = "ERROR"
    '''ERROR.'''
    WARNING = "WARNING"
    '''WARNING.'''


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.NotificationViewTypeName")
class NotificationViewTypeName(enum.Enum):
    '''Human-readable label that displays the alert notification type.

    :schema: NotificationViewTypeName
    '''

    DATADOG = "DATADOG"
    '''DATADOG.'''
    EMAIL = "EMAIL"
    '''EMAIL.'''
    FLOWDOCK = "FLOWDOCK"
    '''FLOWDOCK.'''
    GROUP = "GROUP"
    '''GROUP.'''
    MICROSOFT_TEAMS = "MICROSOFT_TEAMS"
    '''MICROSOFT_TEAMS.'''
    OPS_GENIE = "OPS_GENIE"
    '''OPS_GENIE.'''
    ORG = "ORG"
    '''ORG.'''
    PAGER_DUTY = "PAGER_DUTY"
    '''PAGER_DUTY.'''
    PROMETHEUS = "PROMETHEUS"
    '''PROMETHEUS.'''
    SLACK = "SLACK"
    '''SLACK.'''
    SMS = "SMS"
    '''SMS.'''
    TEAM = "TEAM"
    '''TEAM.'''
    USER = "USER"
    '''USER.'''
    VICTOR_OPS = "VICTOR_OPS"
    '''VICTOR_OPS.'''
    WEBHOOK = "WEBHOOK"
    '''WEBHOOK.'''


class PagerDutyIntegration(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="awscdk-resources-mongodbatlas.PagerDutyIntegration",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        region: "PagerDutyRegion",
        service_key: builtins.str,
        project_id: builtins.str,
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param region: PagerDuty region that indicates the API Uniform Resource Locator (URL) to use.
        :param service_key: Service key associated with your PagerDuty account.
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param profile: Atlas API keys.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0947dfb5400d003085185a98017709c7ac8199d73096c8b71a8790a3a95f7d61)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = PagerDutyIntegrationProps(
            region=region,
            service_key=service_key,
            project_id=project_id,
            profile=profile,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="cfnThirdPartyIntegration")
    def cfn_third_party_integration(self) -> CfnThirdPartyIntegration:
        return typing.cast(CfnThirdPartyIntegration, jsii.get(self, "cfnThirdPartyIntegration"))


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.PagerDutyRegion")
class PagerDutyRegion(enum.Enum):
    US = "US"
    EU = "EU"


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.PartitionFieldView",
    jsii_struct_bases=[],
    name_mapping={
        "field_name": "fieldName",
        "field_type": "fieldType",
        "order": "order",
    },
)
class PartitionFieldView:
    def __init__(
        self,
        *,
        field_name: typing.Optional[builtins.str] = None,
        field_type: typing.Optional["PartitionFieldViewFieldType"] = None,
        order: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param field_name: Human-readable label that identifies the parameter that MongoDB Cloud uses to partition data. To specify a nested parameter, use the dot notation.
        :param field_type: Data type of the parameter that that MongoDB Cloud uses to partition data. Partition parameters of type `UUID <http://bsonspec.org/spec.html>`_ must be of binary subtype 4. MongoDB Cloud skips partition parameters of type UUID with subtype 3.
        :param order: Sequence in which MongoDB Cloud slices the collection data to create partitions. The resource expresses this sequence starting with zero. The value of the **criteria.dateField** parameter defaults as the first item in the partition sequence.

        :schema: PartitionFieldView
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8e23aeb1d228b2b98874cd221e4205b7c6c6bafcff0c2c2340206323db86463)
            check_type(argname="argument field_name", value=field_name, expected_type=type_hints["field_name"])
            check_type(argname="argument field_type", value=field_type, expected_type=type_hints["field_type"])
            check_type(argname="argument order", value=order, expected_type=type_hints["order"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if field_name is not None:
            self._values["field_name"] = field_name
        if field_type is not None:
            self._values["field_type"] = field_type
        if order is not None:
            self._values["order"] = order

    @builtins.property
    def field_name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the parameter that MongoDB Cloud uses to partition data.

        To specify a nested parameter, use the dot notation.

        :schema: PartitionFieldView#FieldName
        '''
        result = self._values.get("field_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def field_type(self) -> typing.Optional["PartitionFieldViewFieldType"]:
        '''Data type of the parameter that that MongoDB Cloud uses to partition data.

        Partition parameters of type `UUID <http://bsonspec.org/spec.html>`_ must be of binary subtype 4. MongoDB Cloud skips partition parameters of type UUID with subtype 3.

        :schema: PartitionFieldView#FieldType
        '''
        result = self._values.get("field_type")
        return typing.cast(typing.Optional["PartitionFieldViewFieldType"], result)

    @builtins.property
    def order(self) -> typing.Optional[jsii.Number]:
        '''Sequence in which MongoDB Cloud slices the collection data to create partitions.

        The resource expresses this sequence starting with zero. The value of the **criteria.dateField** parameter defaults as the first item in the partition sequence.

        :schema: PartitionFieldView#Order
        '''
        result = self._values.get("order")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PartitionFieldView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.PartitionFieldViewFieldType")
class PartitionFieldViewFieldType(enum.Enum):
    '''Data type of the parameter that that MongoDB Cloud uses to partition data.

    Partition parameters of type `UUID <http://bsonspec.org/spec.html>`_ must be of binary subtype 4. MongoDB Cloud skips partition parameters of type UUID with subtype 3.

    :schema: PartitionFieldViewFieldType
    '''

    DATE = "DATE"
    '''date.'''
    INT = "INT"
    '''int.'''
    LONG = "LONG"
    '''long.'''
    OBJECT_ID = "OBJECT_ID"
    '''objectId.'''
    STRING = "STRING"
    '''string.'''
    UUID = "UUID"
    '''uuid.'''


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.PrivateEndpoint",
    jsii_struct_bases=[],
    name_mapping={
        "atlas_private_endpoint_status": "atlasPrivateEndpointStatus",
        "aws_private_endpoint_status": "awsPrivateEndpointStatus",
        "interface_endpoint_id": "interfaceEndpointId",
        "subnet_ids": "subnetIds",
        "vpc_id": "vpcId",
    },
)
class PrivateEndpoint:
    def __init__(
        self,
        *,
        atlas_private_endpoint_status: typing.Optional[builtins.str] = None,
        aws_private_endpoint_status: typing.Optional[builtins.str] = None,
        interface_endpoint_id: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param atlas_private_endpoint_status: Status of the Atlas PrivateEndpoint connection.
        :param aws_private_endpoint_status: Status of the AWS PrivateEndpoint connection.
        :param interface_endpoint_id: Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.
        :param subnet_ids: List of string representing the AWS VPC Subnet ID (like: subnet-xxxxxxxxxxxxxxxxx) (Used For Creating the AWS VPC Endpoint).
        :param vpc_id: String Representing the AWS VPC ID (like: vpc-xxxxxxxxxxxxxxxx) (Used For Creating the AWS VPC Endpoint).

        :schema: PrivateEndpoint
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe378b6ecf361d53088f4dcb74bbbd22a1efc46e97cfe68ce0de004545a34cdb)
            check_type(argname="argument atlas_private_endpoint_status", value=atlas_private_endpoint_status, expected_type=type_hints["atlas_private_endpoint_status"])
            check_type(argname="argument aws_private_endpoint_status", value=aws_private_endpoint_status, expected_type=type_hints["aws_private_endpoint_status"])
            check_type(argname="argument interface_endpoint_id", value=interface_endpoint_id, expected_type=type_hints["interface_endpoint_id"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if atlas_private_endpoint_status is not None:
            self._values["atlas_private_endpoint_status"] = atlas_private_endpoint_status
        if aws_private_endpoint_status is not None:
            self._values["aws_private_endpoint_status"] = aws_private_endpoint_status
        if interface_endpoint_id is not None:
            self._values["interface_endpoint_id"] = interface_endpoint_id
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id

    @builtins.property
    def atlas_private_endpoint_status(self) -> typing.Optional[builtins.str]:
        '''Status of the Atlas PrivateEndpoint connection.

        :schema: PrivateEndpoint#AtlasPrivateEndpointStatus
        '''
        result = self._values.get("atlas_private_endpoint_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_private_endpoint_status(self) -> typing.Optional[builtins.str]:
        '''Status of the AWS PrivateEndpoint connection.

        :schema: PrivateEndpoint#AWSPrivateEndpointStatus
        '''
        result = self._values.get("aws_private_endpoint_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def interface_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.

        :schema: PrivateEndpoint#InterfaceEndpointId
        '''
        result = self._values.get("interface_endpoint_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of string representing the AWS VPC Subnet ID (like: subnet-xxxxxxxxxxxxxxxxx) (Used For Creating the AWS VPC Endpoint).

        :schema: PrivateEndpoint#SubnetIds
        '''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional[builtins.str]:
        '''String Representing the AWS VPC ID (like: vpc-xxxxxxxxxxxxxxxx) (Used For Creating the AWS VPC Endpoint).

        :schema: PrivateEndpoint#VpcId
        '''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.PrivateEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_service_name": "endpointServiceName",
        "error_message": "errorMessage",
        "group_id": "groupId",
        "private_endpoints": "privateEndpoints",
        "region": "region",
        "status": "status",
    },
)
class PrivateEndpointProps:
    def __init__(
        self,
        *,
        endpoint_service_name: typing.Optional[builtins.str] = None,
        error_message: typing.Optional[builtins.str] = None,
        group_id: typing.Optional[builtins.str] = None,
        private_endpoints: typing.Optional[typing.Sequence[typing.Union[PrivateEndpoint, typing.Dict[builtins.str, typing.Any]]]] = None,
        region: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint_service_name: 
        :param error_message: 
        :param group_id: 
        :param private_endpoints: 
        :param region: 
        :param status: 

        :description: true
        :export: true
        :interface: PrivateEndpointProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb5c702819b6ee32bef8ed1262e84c3dec760c7a2e7bfeaef3fffcc5819b070c)
            check_type(argname="argument endpoint_service_name", value=endpoint_service_name, expected_type=type_hints["endpoint_service_name"])
            check_type(argname="argument error_message", value=error_message, expected_type=type_hints["error_message"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument private_endpoints", value=private_endpoints, expected_type=type_hints["private_endpoints"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if endpoint_service_name is not None:
            self._values["endpoint_service_name"] = endpoint_service_name
        if error_message is not None:
            self._values["error_message"] = error_message
        if group_id is not None:
            self._values["group_id"] = group_id
        if private_endpoints is not None:
            self._values["private_endpoints"] = private_endpoints
        if region is not None:
            self._values["region"] = region
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def endpoint_service_name(self) -> typing.Optional[builtins.str]:
        '''
        :description: Name of the AWS PrivateLink endpoint service. Atlas returns null while it is creating the endpoint service.
        :memberof: PrivateEndpointProps
        :type: {string}
        '''
        result = self._values.get("endpoint_service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error_message(self) -> typing.Optional[builtins.str]:
        '''
        :description: Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.
        :memberof: PrivateEndpointProps
        :type: {string}
        '''
        result = self._values.get("error_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_id(self) -> typing.Optional[builtins.str]:
        '''
        :description: Unique 24-hexadecimal digit string that identifies your project.
        :memberof: PrivateEndpointProps
        :type: {string}
        '''
        result = self._values.get("group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_endpoints(self) -> typing.Optional[typing.List[PrivateEndpoint]]:
        '''
        :description: true
        :memberof: PrivateEndpointProps
        :type: {PrivateEndpoint[]}
        '''
        result = self._values.get("private_endpoints")
        return typing.cast(typing.Optional[typing.List[PrivateEndpoint]], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''
        :description: true
        :memberof: PrivateEndpointProps
        :type: {string}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''
        :description: Status of the Atlas PrivateEndpoint service connection
        :memberof: PrivateEndpointProps
        :type: {string}
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ProcessArgs",
    jsii_struct_bases=[],
    name_mapping={
        "default_read_concern": "defaultReadConcern",
        "default_write_concern": "defaultWriteConcern",
        "fail_index_key_too_long": "failIndexKeyTooLong",
        "javascript_enabled": "javascriptEnabled",
        "minimum_enabled_tls_protocol": "minimumEnabledTlsProtocol",
        "no_table_scan": "noTableScan",
        "oplog_min_retention_hours": "oplogMinRetentionHours",
        "oplog_size_mb": "oplogSizeMb",
        "sample_refresh_interval_bi_connector": "sampleRefreshIntervalBiConnector",
        "sample_size_bi_connector": "sampleSizeBiConnector",
    },
)
class ProcessArgs:
    def __init__(
        self,
        *,
        default_read_concern: typing.Optional[builtins.str] = None,
        default_write_concern: typing.Optional[builtins.str] = None,
        fail_index_key_too_long: typing.Optional[builtins.bool] = None,
        javascript_enabled: typing.Optional[builtins.bool] = None,
        minimum_enabled_tls_protocol: typing.Optional[builtins.str] = None,
        no_table_scan: typing.Optional[builtins.bool] = None,
        oplog_min_retention_hours: typing.Optional[jsii.Number] = None,
        oplog_size_mb: typing.Optional[jsii.Number] = None,
        sample_refresh_interval_bi_connector: typing.Optional[jsii.Number] = None,
        sample_size_bi_connector: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Advanced configuration details to add for one cluster in the specified project.

        :param default_read_concern: Default level of acknowledgment requested from MongoDB for read operations set for this cluster.
        :param default_write_concern: Default level of acknowledgment requested from MongoDB for write operations set for this cluster.
        :param fail_index_key_too_long: Flag that indicates whether you can insert or update documents where all indexed entries don't exceed 1024 bytes. If you set this to false, mongod writes documents that exceed this limit but doesn't index them.
        :param javascript_enabled: Flag that indicates whether the cluster allows execution of operations that perform server-side executions of JavaScript.
        :param minimum_enabled_tls_protocol: Minimum Transport Layer Security (TLS) version that the cluster accepts for incoming connections. Clusters using TLS 1.0 or 1.1 should consider setting TLS 1.2 as the minimum TLS protocol version.
        :param no_table_scan: Flag that indicates whether the cluster disables executing any query that requires a collection scan to return results.
        :param oplog_min_retention_hours: Minimum retention window for cluster's oplog expressed in hours. A value of null indicates that the cluster uses the default minimum oplog window that MongoDB Cloud calculates.
        :param oplog_size_mb: Storage limit of cluster's oplog expressed in megabytes. A value of null indicates that the cluster uses the default oplog size that MongoDB Cloud calculates.
        :param sample_refresh_interval_bi_connector: Number of documents per database to sample when gathering schema information.
        :param sample_size_bi_connector: Interval in seconds at which the mongosqld process re-samples data to create its relational schema.

        :schema: processArgs
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27eeb5507fb2bc60736ccb27da8ac7a1b3ab43c84cb503f6d94a89b50115f391)
            check_type(argname="argument default_read_concern", value=default_read_concern, expected_type=type_hints["default_read_concern"])
            check_type(argname="argument default_write_concern", value=default_write_concern, expected_type=type_hints["default_write_concern"])
            check_type(argname="argument fail_index_key_too_long", value=fail_index_key_too_long, expected_type=type_hints["fail_index_key_too_long"])
            check_type(argname="argument javascript_enabled", value=javascript_enabled, expected_type=type_hints["javascript_enabled"])
            check_type(argname="argument minimum_enabled_tls_protocol", value=minimum_enabled_tls_protocol, expected_type=type_hints["minimum_enabled_tls_protocol"])
            check_type(argname="argument no_table_scan", value=no_table_scan, expected_type=type_hints["no_table_scan"])
            check_type(argname="argument oplog_min_retention_hours", value=oplog_min_retention_hours, expected_type=type_hints["oplog_min_retention_hours"])
            check_type(argname="argument oplog_size_mb", value=oplog_size_mb, expected_type=type_hints["oplog_size_mb"])
            check_type(argname="argument sample_refresh_interval_bi_connector", value=sample_refresh_interval_bi_connector, expected_type=type_hints["sample_refresh_interval_bi_connector"])
            check_type(argname="argument sample_size_bi_connector", value=sample_size_bi_connector, expected_type=type_hints["sample_size_bi_connector"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default_read_concern is not None:
            self._values["default_read_concern"] = default_read_concern
        if default_write_concern is not None:
            self._values["default_write_concern"] = default_write_concern
        if fail_index_key_too_long is not None:
            self._values["fail_index_key_too_long"] = fail_index_key_too_long
        if javascript_enabled is not None:
            self._values["javascript_enabled"] = javascript_enabled
        if minimum_enabled_tls_protocol is not None:
            self._values["minimum_enabled_tls_protocol"] = minimum_enabled_tls_protocol
        if no_table_scan is not None:
            self._values["no_table_scan"] = no_table_scan
        if oplog_min_retention_hours is not None:
            self._values["oplog_min_retention_hours"] = oplog_min_retention_hours
        if oplog_size_mb is not None:
            self._values["oplog_size_mb"] = oplog_size_mb
        if sample_refresh_interval_bi_connector is not None:
            self._values["sample_refresh_interval_bi_connector"] = sample_refresh_interval_bi_connector
        if sample_size_bi_connector is not None:
            self._values["sample_size_bi_connector"] = sample_size_bi_connector

    @builtins.property
    def default_read_concern(self) -> typing.Optional[builtins.str]:
        '''Default level of acknowledgment requested from MongoDB for read operations set for this cluster.

        :schema: processArgs#DefaultReadConcern
        '''
        result = self._values.get("default_read_concern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_write_concern(self) -> typing.Optional[builtins.str]:
        '''Default level of acknowledgment requested from MongoDB for write operations set for this cluster.

        :schema: processArgs#DefaultWriteConcern
        '''
        result = self._values.get("default_write_concern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fail_index_key_too_long(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether you can insert or update documents where all indexed entries don't exceed 1024 bytes.

        If you set this to false, mongod writes documents that exceed this limit but doesn't index them.

        :schema: processArgs#FailIndexKeyTooLong
        '''
        result = self._values.get("fail_index_key_too_long")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def javascript_enabled(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether the cluster allows execution of operations that perform server-side executions of JavaScript.

        :schema: processArgs#JavascriptEnabled
        '''
        result = self._values.get("javascript_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def minimum_enabled_tls_protocol(self) -> typing.Optional[builtins.str]:
        '''Minimum Transport Layer Security (TLS) version that the cluster accepts for incoming connections.

        Clusters using TLS 1.0 or 1.1 should consider setting TLS 1.2 as the minimum TLS protocol version.

        :schema: processArgs#MinimumEnabledTLSProtocol
        '''
        result = self._values.get("minimum_enabled_tls_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def no_table_scan(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether the cluster disables executing any query that requires a collection scan to return results.

        :schema: processArgs#NoTableScan
        '''
        result = self._values.get("no_table_scan")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def oplog_min_retention_hours(self) -> typing.Optional[jsii.Number]:
        '''Minimum retention window for cluster's oplog expressed in hours.

        A value of null indicates that the cluster uses the default minimum oplog window that MongoDB Cloud calculates.

        :schema: processArgs#OplogMinRetentionHours
        '''
        result = self._values.get("oplog_min_retention_hours")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def oplog_size_mb(self) -> typing.Optional[jsii.Number]:
        '''Storage limit of cluster's oplog expressed in megabytes.

        A value of null indicates that the cluster uses the default oplog size that MongoDB Cloud calculates.

        :schema: processArgs#OplogSizeMB
        '''
        result = self._values.get("oplog_size_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sample_refresh_interval_bi_connector(self) -> typing.Optional[jsii.Number]:
        '''Number of documents per database to sample when gathering schema information.

        :schema: processArgs#SampleRefreshIntervalBIConnector
        '''
        result = self._values.get("sample_refresh_interval_bi_connector")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sample_size_bi_connector(self) -> typing.Optional[jsii.Number]:
        '''Interval in seconds at which the mongosqld process re-samples data to create its relational schema.

        :schema: processArgs#SampleSizeBIConnector
        '''
        result = self._values.get("sample_size_bi_connector")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProcessArgs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ProjectApiKey",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "role_names": "roleNames"},
)
class ProjectApiKey:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        role_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: 
        :param role_names: 

        :schema: projectApiKey
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91daed197f501b7fd9f92d1d7731074280b321ae722ebf63b85a29b93b007a1c)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument role_names", value=role_names, expected_type=type_hints["role_names"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if role_names is not None:
            self._values["role_names"] = role_names

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: projectApiKey#Key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: projectApiKey#RoleNames
        '''
        result = self._values.get("role_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectApiKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ProjectProps",
    jsii_struct_bases=[],
    name_mapping={
        "org_id": "orgId",
        "cluster_count": "clusterCount",
        "name": "name",
        "project_api_keys": "projectApiKeys",
        "project_owner_id": "projectOwnerId",
        "project_settings": "projectSettings",
        "project_teams": "projectTeams",
        "with_default_alerts_settings": "withDefaultAlertsSettings",
    },
)
class ProjectProps:
    def __init__(
        self,
        *,
        org_id: builtins.str,
        cluster_count: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        project_api_keys: typing.Optional[typing.Sequence[typing.Union[ProjectApiKey, typing.Dict[builtins.str, typing.Any]]]] = None,
        project_owner_id: typing.Optional[builtins.str] = None,
        project_settings: typing.Optional[typing.Union["ProjectSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        project_teams: typing.Optional[typing.Sequence[typing.Union["ProjectTeam", typing.Dict[builtins.str, typing.Any]]]] = None,
        with_default_alerts_settings: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param org_id: Default: auto-generated
        :param cluster_count: 
        :param name: 
        :param project_api_keys: 
        :param project_owner_id: 
        :param project_settings: 
        :param project_teams: 
        :param with_default_alerts_settings: 

        :description: true
        :export: true
        :interface: ProjectProps
        '''
        if isinstance(project_settings, dict):
            project_settings = ProjectSettings(**project_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18cb6c98d5bad22aef897af56a5ba523c7eb8616b58bf4c75bb719ac53e1b889)
            check_type(argname="argument org_id", value=org_id, expected_type=type_hints["org_id"])
            check_type(argname="argument cluster_count", value=cluster_count, expected_type=type_hints["cluster_count"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project_api_keys", value=project_api_keys, expected_type=type_hints["project_api_keys"])
            check_type(argname="argument project_owner_id", value=project_owner_id, expected_type=type_hints["project_owner_id"])
            check_type(argname="argument project_settings", value=project_settings, expected_type=type_hints["project_settings"])
            check_type(argname="argument project_teams", value=project_teams, expected_type=type_hints["project_teams"])
            check_type(argname="argument with_default_alerts_settings", value=with_default_alerts_settings, expected_type=type_hints["with_default_alerts_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "org_id": org_id,
        }
        if cluster_count is not None:
            self._values["cluster_count"] = cluster_count
        if name is not None:
            self._values["name"] = name
        if project_api_keys is not None:
            self._values["project_api_keys"] = project_api_keys
        if project_owner_id is not None:
            self._values["project_owner_id"] = project_owner_id
        if project_settings is not None:
            self._values["project_settings"] = project_settings
        if project_teams is not None:
            self._values["project_teams"] = project_teams
        if with_default_alerts_settings is not None:
            self._values["with_default_alerts_settings"] = with_default_alerts_settings

    @builtins.property
    def org_id(self) -> builtins.str:
        '''
        :default: auto-generated

        :description: Unique identifier of the organization within which to create the project.
        :memberof: ProjectProps
        :type: {string}
        '''
        result = self._values.get("org_id")
        assert result is not None, "Required property 'org_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_count(self) -> typing.Optional[jsii.Number]:
        '''
        :description: The number of Atlas clusters deployed in the project.
        :memberof: ProjectProps
        :type: {number}
        '''
        result = self._values.get("cluster_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :description: Name of the project to create.
        :memberof: ProjectProps
        :type: {string}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_api_keys(self) -> typing.Optional[typing.List[ProjectApiKey]]:
        '''
        :description: true
        :memberof: ProjectProps
        :type: {project.ProjectApiKey[]}
        '''
        result = self._values.get("project_api_keys")
        return typing.cast(typing.Optional[typing.List[ProjectApiKey]], result)

    @builtins.property
    def project_owner_id(self) -> typing.Optional[builtins.str]:
        '''
        :description: Unique 24-hexadecimal digit string that identifies the Atlas user account to be granted the ``Project Owner`` role on the specified project. If you set this parameter, it overrides the default value of the oldest ``Organization Owner``.
        :memberof: ProjectProps
        :type: {string}
        '''
        result = self._values.get("project_owner_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_settings(self) -> typing.Optional["ProjectSettings"]:
        '''
        :description: true
        :memberof: ProjectProps
        :type: {project.ProjectSettings}
        '''
        result = self._values.get("project_settings")
        return typing.cast(typing.Optional["ProjectSettings"], result)

    @builtins.property
    def project_teams(self) -> typing.Optional[typing.List["ProjectTeam"]]:
        '''
        :description: true
        :memberof: ProjectProps
        :type: {project.ProjectTeam[]}
        '''
        result = self._values.get("project_teams")
        return typing.cast(typing.Optional[typing.List["ProjectTeam"]], result)

    @builtins.property
    def with_default_alerts_settings(self) -> typing.Optional[builtins.bool]:
        '''
        :description: Flag that indicates whether to create the project with default alert settings.
        :memberof: ProjectProps
        :type: {boolean}
        '''
        result = self._values.get("with_default_alerts_settings")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ProjectSettings",
    jsii_struct_bases=[],
    name_mapping={
        "is_collect_database_specifics_statistics_enabled": "isCollectDatabaseSpecificsStatisticsEnabled",
        "is_data_explorer_enabled": "isDataExplorerEnabled",
        "is_performance_advisor_enabled": "isPerformanceAdvisorEnabled",
        "is_realtime_performance_panel_enabled": "isRealtimePerformancePanelEnabled",
        "is_schema_advisor_enabled": "isSchemaAdvisorEnabled",
    },
)
class ProjectSettings:
    def __init__(
        self,
        *,
        is_collect_database_specifics_statistics_enabled: typing.Optional[builtins.bool] = None,
        is_data_explorer_enabled: typing.Optional[builtins.bool] = None,
        is_performance_advisor_enabled: typing.Optional[builtins.bool] = None,
        is_realtime_performance_panel_enabled: typing.Optional[builtins.bool] = None,
        is_schema_advisor_enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param is_collect_database_specifics_statistics_enabled: 
        :param is_data_explorer_enabled: 
        :param is_performance_advisor_enabled: 
        :param is_realtime_performance_panel_enabled: 
        :param is_schema_advisor_enabled: 

        :schema: projectSettings
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__507a4ab615a966f162caf3cbd9e8cb3a69fdb875a77c88eb53283cdb14bc7784)
            check_type(argname="argument is_collect_database_specifics_statistics_enabled", value=is_collect_database_specifics_statistics_enabled, expected_type=type_hints["is_collect_database_specifics_statistics_enabled"])
            check_type(argname="argument is_data_explorer_enabled", value=is_data_explorer_enabled, expected_type=type_hints["is_data_explorer_enabled"])
            check_type(argname="argument is_performance_advisor_enabled", value=is_performance_advisor_enabled, expected_type=type_hints["is_performance_advisor_enabled"])
            check_type(argname="argument is_realtime_performance_panel_enabled", value=is_realtime_performance_panel_enabled, expected_type=type_hints["is_realtime_performance_panel_enabled"])
            check_type(argname="argument is_schema_advisor_enabled", value=is_schema_advisor_enabled, expected_type=type_hints["is_schema_advisor_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if is_collect_database_specifics_statistics_enabled is not None:
            self._values["is_collect_database_specifics_statistics_enabled"] = is_collect_database_specifics_statistics_enabled
        if is_data_explorer_enabled is not None:
            self._values["is_data_explorer_enabled"] = is_data_explorer_enabled
        if is_performance_advisor_enabled is not None:
            self._values["is_performance_advisor_enabled"] = is_performance_advisor_enabled
        if is_realtime_performance_panel_enabled is not None:
            self._values["is_realtime_performance_panel_enabled"] = is_realtime_performance_panel_enabled
        if is_schema_advisor_enabled is not None:
            self._values["is_schema_advisor_enabled"] = is_schema_advisor_enabled

    @builtins.property
    def is_collect_database_specifics_statistics_enabled(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''
        :schema: projectSettings#IsCollectDatabaseSpecificsStatisticsEnabled
        '''
        result = self._values.get("is_collect_database_specifics_statistics_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def is_data_explorer_enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: projectSettings#IsDataExplorerEnabled
        '''
        result = self._values.get("is_data_explorer_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def is_performance_advisor_enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: projectSettings#IsPerformanceAdvisorEnabled
        '''
        result = self._values.get("is_performance_advisor_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def is_realtime_performance_panel_enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: projectSettings#IsRealtimePerformancePanelEnabled
        '''
        result = self._values.get("is_realtime_performance_panel_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def is_schema_advisor_enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: projectSettings#IsSchemaAdvisorEnabled
        '''
        result = self._values.get("is_schema_advisor_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ProjectTeam",
    jsii_struct_bases=[],
    name_mapping={"role_names": "roleNames", "team_id": "teamId"},
)
class ProjectTeam:
    def __init__(
        self,
        *,
        role_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        team_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param role_names: 
        :param team_id: 

        :schema: projectTeam
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82fae69953a2a39be1284fe9158aeef8885c67726b3e35cdec3e8819d704fd32)
            check_type(argname="argument role_names", value=role_names, expected_type=type_hints["role_names"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if role_names is not None:
            self._values["role_names"] = role_names
        if team_id is not None:
            self._values["team_id"] = team_id

    @builtins.property
    def role_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: projectTeam#RoleNames
        '''
        result = self._values.get("role_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def team_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: projectTeam#TeamId
        '''
        result = self._values.get("team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectTeam(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.Resource",
    jsii_struct_bases=[],
    name_mapping={"cluster": "cluster", "collection": "collection", "db": "db"},
)
class Resource:
    def __init__(
        self,
        *,
        cluster: typing.Optional[builtins.bool] = None,
        collection: typing.Optional[builtins.str] = None,
        db: typing.Optional[builtins.str] = None,
    ) -> None:
        '''List of resources on which you grant the action.

        :param cluster: Flag that indicates whether to grant the action on the cluster resource. If true, MongoDB Cloud ignores the actions.resources.collection and actions.resources.db parameters.
        :param collection: Human-readable label that identifies the collection on which you grant the action to one MongoDB user. If you don't set this parameter, you grant the action to all collections in the database specified in the actions.resources.db parameter. If you set "actions.resources.cluster" : true, MongoDB Cloud ignores this parameter.
        :param db: Human-readable label that identifies the database on which you grant the action to one MongoDB user. If you set "actions.resources.cluster" : true, MongoDB Cloud ignores this parameter.

        :schema: Resource
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cda0ca68d66524a23a9186fd3afdf8b3d7b4ce9c02ceb5f2ca293f0ab24b268)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument collection", value=collection, expected_type=type_hints["collection"])
            check_type(argname="argument db", value=db, expected_type=type_hints["db"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cluster is not None:
            self._values["cluster"] = cluster
        if collection is not None:
            self._values["collection"] = collection
        if db is not None:
            self._values["db"] = db

    @builtins.property
    def cluster(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether to grant the action on the cluster resource.

        If true, MongoDB Cloud ignores the actions.resources.collection and actions.resources.db parameters.

        :schema: Resource#Cluster
        '''
        result = self._values.get("cluster")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def collection(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the collection on which you grant the action to one MongoDB user.

        If you don't set this parameter, you grant the action to all collections in the database specified in the actions.resources.db parameter. If you set "actions.resources.cluster" : true, MongoDB Cloud ignores this parameter.

        :schema: Resource#Collection
        '''
        result = self._values.get("collection")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the database on which you grant the action to one MongoDB user.

        If you set "actions.resources.cluster" : true, MongoDB Cloud ignores this parameter.

        :schema: Resource#DB
        '''
        result = self._values.get("db")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Resource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.RoleAssignment",
    jsii_struct_bases=[],
    name_mapping={"org_id": "orgId", "project_id": "projectId", "role": "role"},
)
class RoleAssignment:
    def __init__(
        self,
        *,
        org_id: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        role: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param org_id: List that contains comma-separated key value pairs to map zones to geographic regions. These pairs map an ISO 3166-1a2 location code, with an ISO 3166-2 subdivision code when possible, to a unique 24-hexadecimal string that identifies the custom zone. This parameter returns an empty object if no custom zones exist.
        :param project_id: List that contains comma-separated key value pairs to map zones to geographic regions. These pairs map an ISO 3166-1a2 location code, with an ISO 3166-2 subdivision code when possible, to a unique 24-hexadecimal string that identifies the custom zone. This parameter returns an empty object if no custom zones exist.
        :param role: 

        :schema: RoleAssignment
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72371f97531e42912048f6782cab67619ac5520a56a158d50a2a201f543f15a0)
            check_type(argname="argument org_id", value=org_id, expected_type=type_hints["org_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if org_id is not None:
            self._values["org_id"] = org_id
        if project_id is not None:
            self._values["project_id"] = project_id
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def org_id(self) -> typing.Optional[builtins.str]:
        '''List that contains comma-separated key value pairs to map zones to geographic regions.

        These pairs map an ISO 3166-1a2 location code, with an ISO 3166-2 subdivision code when possible, to a unique 24-hexadecimal string that identifies the custom zone.

        This parameter returns an empty object if no custom zones exist.

        :schema: RoleAssignment#OrgId
        '''
        result = self._values.get("org_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''List that contains comma-separated key value pairs to map zones to geographic regions.

        These pairs map an ISO 3166-1a2 location code, with an ISO 3166-2 subdivision code when possible, to a unique 24-hexadecimal string that identifies the custom zone.

        This parameter returns an empty object if no custom zones exist.

        :schema: RoleAssignment#ProjectId
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''
        :schema: RoleAssignment#Role
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RoleAssignment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.RoleDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "collection_name": "collectionName",
        "database_name": "databaseName",
        "role_name": "roleName",
    },
)
class RoleDefinition:
    def __init__(
        self,
        *,
        collection_name: typing.Optional[builtins.str] = None,
        database_name: typing.Optional[builtins.str] = None,
        role_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param collection_name: 
        :param database_name: 
        :param role_name: 

        :schema: roleDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__529daedbf89ca5908579cea08ccd15f9eafe0971359fe062d851868734b98576)
            check_type(argname="argument collection_name", value=collection_name, expected_type=type_hints["collection_name"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if collection_name is not None:
            self._values["collection_name"] = collection_name
        if database_name is not None:
            self._values["database_name"] = database_name
        if role_name is not None:
            self._values["role_name"] = role_name

    @builtins.property
    def collection_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: roleDefinition#CollectionName
        '''
        result = self._values.get("collection_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: roleDefinition#DatabaseName
        '''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: roleDefinition#RoleName
        '''
        result = self._values.get("role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RoleDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ScheduleConfig",
    jsii_struct_bases=[],
    name_mapping={"schedule": "schedule", "skipcatchup_events": "skipcatchupEvents"},
)
class ScheduleConfig:
    def __init__(
        self,
        *,
        schedule: typing.Optional[builtins.str] = None,
        skipcatchup_events: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param schedule: A `cron expression <https://www.mongodb.com/docs/atlas/app-services/triggers/scheduled-triggers/#cron-expressions>`_ that specifies when the trigger executes.
        :param skipcatchup_events: If ``true``, enabling the trigger after it was disabled will not invoke events that occurred while the trigger was disabled.

        :schema: ScheduleConfig
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__843802625c48ab9b6849df3c2e0baede76ea75e1e0b66ce231db2295f73d74ea)
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument skipcatchup_events", value=skipcatchup_events, expected_type=type_hints["skipcatchup_events"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if schedule is not None:
            self._values["schedule"] = schedule
        if skipcatchup_events is not None:
            self._values["skipcatchup_events"] = skipcatchup_events

    @builtins.property
    def schedule(self) -> typing.Optional[builtins.str]:
        '''A `cron expression <https://www.mongodb.com/docs/atlas/app-services/triggers/scheduled-triggers/#cron-expressions>`_ that specifies when the trigger executes.

        :schema: ScheduleConfig#Schedule
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skipcatchup_events(self) -> typing.Optional[builtins.bool]:
        '''If ``true``, enabling the trigger after it was disabled will not invoke events that occurred while the trigger was disabled.

        :schema: ScheduleConfig#SkipcatchupEvents
        '''
        result = self._values.get("skipcatchup_events")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScheduleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ScheduleView",
    jsii_struct_bases=[],
    name_mapping={
        "day_of_month": "dayOfMonth",
        "day_of_week": "dayOfWeek",
        "end_hour": "endHour",
        "end_minute": "endMinute",
        "start_hour": "startHour",
        "start_minute": "startMinute",
        "type": "type",
    },
)
class ScheduleView:
    def __init__(
        self,
        *,
        day_of_month: typing.Optional[jsii.Number] = None,
        day_of_week: typing.Optional[jsii.Number] = None,
        end_hour: typing.Optional[jsii.Number] = None,
        end_minute: typing.Optional[jsii.Number] = None,
        start_hour: typing.Optional[jsii.Number] = None,
        start_minute: typing.Optional[jsii.Number] = None,
        type: typing.Optional["ScheduleViewType"] = None,
    ) -> None:
        '''
        :param day_of_month: Day of the month when the scheduled archive starts.
        :param day_of_week: Day of the month when the scheduled archive starts.
        :param end_hour: Hour of the day when the scheduled window to run one online archive ends.
        :param end_minute: Minute of the hour when the scheduled window to run one online archive ends.
        :param start_hour: Hour of the day when the when the scheduled window to run one online archive starts.
        :param start_minute: Minute of the hour when the scheduled window to run one online archive starts.
        :param type: 

        :schema: ScheduleView
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cc397c278727b04c15dbb5da033aa1b05323068a00cc34118b971ff6c456d3b)
            check_type(argname="argument day_of_month", value=day_of_month, expected_type=type_hints["day_of_month"])
            check_type(argname="argument day_of_week", value=day_of_week, expected_type=type_hints["day_of_week"])
            check_type(argname="argument end_hour", value=end_hour, expected_type=type_hints["end_hour"])
            check_type(argname="argument end_minute", value=end_minute, expected_type=type_hints["end_minute"])
            check_type(argname="argument start_hour", value=start_hour, expected_type=type_hints["start_hour"])
            check_type(argname="argument start_minute", value=start_minute, expected_type=type_hints["start_minute"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if day_of_month is not None:
            self._values["day_of_month"] = day_of_month
        if day_of_week is not None:
            self._values["day_of_week"] = day_of_week
        if end_hour is not None:
            self._values["end_hour"] = end_hour
        if end_minute is not None:
            self._values["end_minute"] = end_minute
        if start_hour is not None:
            self._values["start_hour"] = start_hour
        if start_minute is not None:
            self._values["start_minute"] = start_minute
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def day_of_month(self) -> typing.Optional[jsii.Number]:
        '''Day of the month when the scheduled archive starts.

        :schema: ScheduleView#DayOfMonth
        '''
        result = self._values.get("day_of_month")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def day_of_week(self) -> typing.Optional[jsii.Number]:
        '''Day of the month when the scheduled archive starts.

        :schema: ScheduleView#DayOfWeek
        '''
        result = self._values.get("day_of_week")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def end_hour(self) -> typing.Optional[jsii.Number]:
        '''Hour of the day when the scheduled window to run one online archive ends.

        :schema: ScheduleView#EndHour
        '''
        result = self._values.get("end_hour")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def end_minute(self) -> typing.Optional[jsii.Number]:
        '''Minute of the hour when the scheduled window to run one online archive ends.

        :schema: ScheduleView#EndMinute
        '''
        result = self._values.get("end_minute")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start_hour(self) -> typing.Optional[jsii.Number]:
        '''Hour of the day when the when the scheduled window to run one online archive starts.

        :schema: ScheduleView#StartHour
        '''
        result = self._values.get("start_hour")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start_minute(self) -> typing.Optional[jsii.Number]:
        '''Minute of the hour when the scheduled window to run one online archive starts.

        :schema: ScheduleView#StartMinute
        '''
        result = self._values.get("start_minute")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional["ScheduleViewType"]:
        '''
        :schema: ScheduleView#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["ScheduleViewType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScheduleView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.ScheduleViewType")
class ScheduleViewType(enum.Enum):
    '''
    :schema: ScheduleViewType
    '''

    DAILY = "DAILY"
    '''DAILY.'''
    MONTHLY = "MONTHLY"
    '''MONTHLY.'''
    DEFAULT = "DEFAULT"
    '''DEFAULT.'''
    WEEKLY = "WEEKLY"
    '''WEEKLY.'''


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ScopeDefinition",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class ScopeDefinition:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional["ScopeDefinitionType"] = None,
    ) -> None:
        '''
        :param name: 
        :param type: 

        :schema: scopeDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33863fef557cc51b9b5fdfc6e05962108c9253ac9a133d92d211b1fc2f87c2d2)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: scopeDefinition#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional["ScopeDefinitionType"]:
        '''
        :schema: scopeDefinition#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["ScopeDefinitionType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScopeDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="awscdk-resources-mongodbatlas.ScopeDefinitionType")
class ScopeDefinitionType(enum.Enum):
    '''
    :schema: ScopeDefinitionType
    '''

    CLUSTER = "CLUSTER"
    '''CLUSTER.'''
    DATA_LAKE = "DATA_LAKE"
    '''DATA_LAKE.'''


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ServerlessInstanceConnectionStrings",
    jsii_struct_bases=[],
    name_mapping={
        "private_endpoint": "privateEndpoint",
        "standard_srv": "standardSrv",
    },
)
class ServerlessInstanceConnectionStrings:
    def __init__(
        self,
        *,
        private_endpoint: typing.Optional[typing.Sequence[typing.Union["ServerlessInstancePrivateEndpoint", typing.Dict[builtins.str, typing.Any]]]] = None,
        standard_srv: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param private_endpoint: List of private endpoint connection strings that you can use to connect to this serverless instance through a private endpoint. This parameter returns only if you created a private endpoint for this serverless instance and it is AVAILABLE.
        :param standard_srv: Public connection string that you can use to connect to this serverless instance. This connection string uses the ``mongodb+srv://`` protocol.

        :schema: ServerlessInstanceConnectionStrings
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__233f155335ccb1a613f2dc06a72ed7e43a897b210fe3ae1a7f4dead54585bb74)
            check_type(argname="argument private_endpoint", value=private_endpoint, expected_type=type_hints["private_endpoint"])
            check_type(argname="argument standard_srv", value=standard_srv, expected_type=type_hints["standard_srv"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if private_endpoint is not None:
            self._values["private_endpoint"] = private_endpoint
        if standard_srv is not None:
            self._values["standard_srv"] = standard_srv

    @builtins.property
    def private_endpoint(
        self,
    ) -> typing.Optional[typing.List["ServerlessInstancePrivateEndpoint"]]:
        '''List of private endpoint connection strings that you can use to connect to this serverless instance through a private endpoint.

        This parameter returns only if you created a private endpoint for this serverless instance and it is AVAILABLE.

        :schema: ServerlessInstanceConnectionStrings#PrivateEndpoint
        '''
        result = self._values.get("private_endpoint")
        return typing.cast(typing.Optional[typing.List["ServerlessInstancePrivateEndpoint"]], result)

    @builtins.property
    def standard_srv(self) -> typing.Optional[builtins.str]:
        '''Public connection string that you can use to connect to this serverless instance.

        This connection string uses the ``mongodb+srv://`` protocol.

        :schema: ServerlessInstanceConnectionStrings#StandardSrv
        '''
        result = self._values.get("standard_srv")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerlessInstanceConnectionStrings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ServerlessInstancePrivateEndpoint",
    jsii_struct_bases=[],
    name_mapping={
        "endpoints": "endpoints",
        "srv_connection_string": "srvConnectionString",
        "type": "type",
    },
)
class ServerlessInstancePrivateEndpoint:
    def __init__(
        self,
        *,
        endpoints: typing.Optional[typing.Sequence[typing.Union["ServerlessInstancePrivateEndpointEndpoint", typing.Dict[builtins.str, typing.Any]]]] = None,
        srv_connection_string: typing.Optional[builtins.str] = None,
        type: typing.Optional["ServerlessInstancePrivateEndpointType"] = None,
    ) -> None:
        '''
        :param endpoints: List that contains the private endpoints through which you connect to MongoDB Cloud when you use **connectionStrings.privateEndpoint[n].srvConnectionString**.
        :param srv_connection_string: Private endpoint-aware connection string that uses the ``mongodb+srv://`` protocol to connect to MongoDB Cloud through a private endpoint. The ``mongodb+srv`` protocol tells the driver to look up the seed list of hosts in the Domain Name System (DNS).
        :param type: MongoDB process type to which your application connects.

        :schema: ServerlessInstancePrivateEndpoint
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__958247bcbc9a391c48d0f6a979e76086abb9df4cf214cbe24cd943d1a969e320)
            check_type(argname="argument endpoints", value=endpoints, expected_type=type_hints["endpoints"])
            check_type(argname="argument srv_connection_string", value=srv_connection_string, expected_type=type_hints["srv_connection_string"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if endpoints is not None:
            self._values["endpoints"] = endpoints
        if srv_connection_string is not None:
            self._values["srv_connection_string"] = srv_connection_string
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def endpoints(
        self,
    ) -> typing.Optional[typing.List["ServerlessInstancePrivateEndpointEndpoint"]]:
        '''List that contains the private endpoints through which you connect to MongoDB Cloud when you use **connectionStrings.privateEndpoint[n].srvConnectionString**.

        :schema: ServerlessInstancePrivateEndpoint#Endpoints
        '''
        result = self._values.get("endpoints")
        return typing.cast(typing.Optional[typing.List["ServerlessInstancePrivateEndpointEndpoint"]], result)

    @builtins.property
    def srv_connection_string(self) -> typing.Optional[builtins.str]:
        '''Private endpoint-aware connection string that uses the ``mongodb+srv://`` protocol to connect to MongoDB Cloud through a private endpoint.

        The ``mongodb+srv`` protocol tells the driver to look up the seed list of hosts in the Domain Name System (DNS).

        :schema: ServerlessInstancePrivateEndpoint#SrvConnectionString
        '''
        result = self._values.get("srv_connection_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional["ServerlessInstancePrivateEndpointType"]:
        '''MongoDB process type to which your application connects.

        :schema: ServerlessInstancePrivateEndpoint#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["ServerlessInstancePrivateEndpointType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerlessInstancePrivateEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ServerlessInstancePrivateEndpointEndpoint",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_id": "endpointId",
        "provider_name": "providerName",
        "region": "region",
    },
)
class ServerlessInstancePrivateEndpointEndpoint:
    def __init__(
        self,
        *,
        endpoint_id: typing.Optional[builtins.str] = None,
        provider_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint_id: Unique provider identifier of the private endpoint.
        :param provider_name: Cloud provider where the private endpoint is deployed.
        :param region: Region where the private endpoint is deployed.

        :schema: ServerlessInstancePrivateEndpointEndpoint
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1328265175dc11efbfc92ac3a4a35f4478033611ff57e7fec38e7349829f0b41)
            check_type(argname="argument endpoint_id", value=endpoint_id, expected_type=type_hints["endpoint_id"])
            check_type(argname="argument provider_name", value=provider_name, expected_type=type_hints["provider_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if endpoint_id is not None:
            self._values["endpoint_id"] = endpoint_id
        if provider_name is not None:
            self._values["provider_name"] = provider_name
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def endpoint_id(self) -> typing.Optional[builtins.str]:
        '''Unique provider identifier of the private endpoint.

        :schema: ServerlessInstancePrivateEndpointEndpoint#EndpointId
        '''
        result = self._values.get("endpoint_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider_name(self) -> typing.Optional[builtins.str]:
        '''Cloud provider where the private endpoint is deployed.

        :schema: ServerlessInstancePrivateEndpointEndpoint#ProviderName
        '''
        result = self._values.get("provider_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Region where the private endpoint is deployed.

        :schema: ServerlessInstancePrivateEndpointEndpoint#Region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerlessInstancePrivateEndpointEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="awscdk-resources-mongodbatlas.ServerlessInstancePrivateEndpointType"
)
class ServerlessInstancePrivateEndpointType(enum.Enum):
    '''MongoDB process type to which your application connects.

    :schema: ServerlessInstancePrivateEndpointType
    '''

    MONGOS = "MONGOS"
    '''MONGOS.'''


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ServerlessInstanceProviderSettings",
    jsii_struct_bases=[],
    name_mapping={"provider_name": "providerName", "region_name": "regionName"},
)
class ServerlessInstanceProviderSettings:
    def __init__(
        self,
        *,
        provider_name: typing.Optional["ServerlessInstanceProviderSettingsProviderName"] = None,
        region_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param provider_name: Human-readable label that identifies the cloud service provider.
        :param region_name: Human-readable label that identifies the geographic location of your MongoDB serverless instance. The region you choose can affect network latency for clients accessing your databases. For a complete list of region names, see `AWS <https://docs.atlas.mongodb.com/reference/amazon-aws/#std-label-amazon-aws>`_, `GCP <https://docs.atlas.mongodb.com/reference/google-gcp/>`_, and `Azure <https://docs.atlas.mongodb.com/reference/microsoft-azure/>`_.

        :schema: ServerlessInstanceProviderSettings
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab7d13f61158c6dc5e7248221fdd372bc869a6caf5c8645c35d51293406b5159)
            check_type(argname="argument provider_name", value=provider_name, expected_type=type_hints["provider_name"])
            check_type(argname="argument region_name", value=region_name, expected_type=type_hints["region_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if provider_name is not None:
            self._values["provider_name"] = provider_name
        if region_name is not None:
            self._values["region_name"] = region_name

    @builtins.property
    def provider_name(
        self,
    ) -> typing.Optional["ServerlessInstanceProviderSettingsProviderName"]:
        '''Human-readable label that identifies the cloud service provider.

        :schema: ServerlessInstanceProviderSettings#ProviderName
        '''
        result = self._values.get("provider_name")
        return typing.cast(typing.Optional["ServerlessInstanceProviderSettingsProviderName"], result)

    @builtins.property
    def region_name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the geographic location of your MongoDB serverless instance.

        The region you choose can affect network latency for clients accessing your databases. For a complete list of region names, see `AWS <https://docs.atlas.mongodb.com/reference/amazon-aws/#std-label-amazon-aws>`_, `GCP <https://docs.atlas.mongodb.com/reference/google-gcp/>`_, and `Azure <https://docs.atlas.mongodb.com/reference/microsoft-azure/>`_.

        :schema: ServerlessInstanceProviderSettings#RegionName
        '''
        result = self._values.get("region_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerlessInstanceProviderSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="awscdk-resources-mongodbatlas.ServerlessInstanceProviderSettingsProviderName"
)
class ServerlessInstanceProviderSettingsProviderName(enum.Enum):
    '''Human-readable label that identifies the cloud service provider.

    :schema: ServerlessInstanceProviderSettingsProviderName
    '''

    SERVERLESS = "SERVERLESS"
    '''SERVERLESS.'''


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.Specs",
    jsii_struct_bases=[],
    name_mapping={
        "disk_iops": "diskIops",
        "ebs_volume_type": "ebsVolumeType",
        "instance_size": "instanceSize",
        "node_count": "nodeCount",
    },
)
class Specs:
    def __init__(
        self,
        *,
        disk_iops: typing.Optional[builtins.str] = None,
        ebs_volume_type: typing.Optional[builtins.str] = None,
        instance_size: typing.Optional[builtins.str] = None,
        node_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param disk_iops: Target throughput desired for storage attached to your AWS-provisioned cluster. Only change this parameter if you:. set "replicationSpecs[n].regionConfigs[m].providerName" : "AWS". set "replicationSpecs[n].regionConfigs[m].electableSpecs.instanceSize" : "M30" or greater not including Mxx_NVME tiers. The maximum input/output operations per second (IOPS) depend on the selected .instanceSize and .diskSizeGB. This parameter defaults to the cluster tier's standard IOPS value. Changing this value impacts cluster cost. MongoDB Cloud enforces minimum ratios of storage capacity to system memory for given cluster tiers. This keeps cluster performance consistent with large datasets. Instance sizes M10 to M40 have a ratio of disk capacity to system memory of 60:1. Instance sizes greater than M40 have a ratio of 120:1.
        :param ebs_volume_type: Type of storage you want to attach to your AWS-provisioned cluster. STANDARD volume types can't exceed the default input/output operations per second (IOPS) rate for the selected volume size. PROVISIONED volume types must fall within the allowable IOPS range for the selected volume size."
        :param instance_size: Hardware specification for the instance sizes in this region. Each instance size has a default storage and memory capacity. The instance size you select applies to all the data-bearing hosts in your instance size. If you deploy a Global Cluster, you must choose a instance size of M30 or greater.
        :param node_count: Number of read-only nodes for MongoDB Cloud deploys to the region. Read-only nodes can never become the primary, but can enable local reads.

        :schema: specs
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a0e995f634f6b4a5db684d55bc035ad49fb0c807c4d056a9bec5cc340be6586)
            check_type(argname="argument disk_iops", value=disk_iops, expected_type=type_hints["disk_iops"])
            check_type(argname="argument ebs_volume_type", value=ebs_volume_type, expected_type=type_hints["ebs_volume_type"])
            check_type(argname="argument instance_size", value=instance_size, expected_type=type_hints["instance_size"])
            check_type(argname="argument node_count", value=node_count, expected_type=type_hints["node_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if disk_iops is not None:
            self._values["disk_iops"] = disk_iops
        if ebs_volume_type is not None:
            self._values["ebs_volume_type"] = ebs_volume_type
        if instance_size is not None:
            self._values["instance_size"] = instance_size
        if node_count is not None:
            self._values["node_count"] = node_count

    @builtins.property
    def disk_iops(self) -> typing.Optional[builtins.str]:
        '''Target throughput desired for storage attached to your AWS-provisioned cluster. Only change this parameter if you:.

        set "replicationSpecs[n].regionConfigs[m].providerName" : "AWS".
        set "replicationSpecs[n].regionConfigs[m].electableSpecs.instanceSize" : "M30" or greater not including Mxx_NVME tiers.
        The maximum input/output operations per second (IOPS) depend on the selected .instanceSize and .diskSizeGB. This parameter defaults to the cluster tier's standard IOPS value. Changing this value impacts cluster cost. MongoDB Cloud enforces minimum ratios of storage capacity to system memory for given cluster tiers. This keeps cluster performance consistent with large datasets.

        Instance sizes M10 to M40 have a ratio of disk capacity to system memory of 60:1.
        Instance sizes greater than M40 have a ratio of 120:1.

        :schema: specs#DiskIOPS
        '''
        result = self._values.get("disk_iops")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_volume_type(self) -> typing.Optional[builtins.str]:
        '''Type of storage you want to attach to your AWS-provisioned cluster.

        STANDARD volume types can't exceed the default input/output operations per second (IOPS) rate for the selected volume size.

        PROVISIONED volume types must fall within the allowable IOPS range for the selected volume size."

        :schema: specs#EbsVolumeType
        '''
        result = self._values.get("ebs_volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_size(self) -> typing.Optional[builtins.str]:
        '''Hardware specification for the instance sizes in this region.

        Each instance size has a default storage and memory capacity. The instance size you select applies to all the data-bearing hosts in your instance size. If you deploy a Global Cluster, you must choose a instance size of M30 or greater.

        :schema: specs#InstanceSize
        '''
        result = self._values.get("instance_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_count(self) -> typing.Optional[jsii.Number]:
        '''Number of read-only nodes for MongoDB Cloud deploys to the region.

        Read-only nodes can never become the primary, but can enable local reads.

        :schema: specs#NodeCount
        '''
        result = self._values.get("node_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Specs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.StoreDetail",
    jsii_struct_bases=[],
    name_mapping={
        "additional_storage_classes": "additionalStorageClasses",
        "bucket": "bucket",
        "delimiter": "delimiter",
        "include_tags": "includeTags",
        "name": "name",
        "prefix": "prefix",
        "provider": "provider",
        "region": "region",
    },
)
class StoreDetail:
    def __init__(
        self,
        *,
        additional_storage_classes: typing.Optional[typing.Sequence[builtins.str]] = None,
        bucket: typing.Optional[builtins.str] = None,
        delimiter: typing.Optional[builtins.str] = None,
        include_tags: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        provider: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Configuration information for each data store and its mapping to MongoDB Cloud databases.

        :param additional_storage_classes: Human-readable label that identifies the Federated Database to update.
        :param bucket: Human-readable label that identifies the Federated Database to update.
        :param delimiter: Human-readable label that identifies the Federated Database to update.
        :param include_tags: Human-readable label that identifies the Federated Database to update.
        :param name: Human-readable label that identifies the data store.
        :param prefix: Human-readable label that identifies the Federated Database to update.
        :param provider: Human-readable label that identifies the Federated Database to update.
        :param region: Human-readable label that identifies the Federated Database to update.

        :schema: StoreDetail
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c786ec57c01cbb004c6105896c011b0442b0121ff8242974eb84b31be51ec6cd)
            check_type(argname="argument additional_storage_classes", value=additional_storage_classes, expected_type=type_hints["additional_storage_classes"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument delimiter", value=delimiter, expected_type=type_hints["delimiter"])
            check_type(argname="argument include_tags", value=include_tags, expected_type=type_hints["include_tags"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_storage_classes is not None:
            self._values["additional_storage_classes"] = additional_storage_classes
        if bucket is not None:
            self._values["bucket"] = bucket
        if delimiter is not None:
            self._values["delimiter"] = delimiter
        if include_tags is not None:
            self._values["include_tags"] = include_tags
        if name is not None:
            self._values["name"] = name
        if prefix is not None:
            self._values["prefix"] = prefix
        if provider is not None:
            self._values["provider"] = provider
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def additional_storage_classes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Human-readable label that identifies the Federated Database to update.

        :schema: StoreDetail#AdditionalStorageClasses
        '''
        result = self._values.get("additional_storage_classes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def bucket(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the Federated Database to update.

        :schema: StoreDetail#Bucket
        '''
        result = self._values.get("bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delimiter(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the Federated Database to update.

        :schema: StoreDetail#Delimiter
        '''
        result = self._values.get("delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def include_tags(self) -> typing.Optional[builtins.bool]:
        '''Human-readable label that identifies the Federated Database to update.

        :schema: StoreDetail#IncludeTags
        '''
        result = self._values.get("include_tags")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the data store.

        :schema: StoreDetail#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the Federated Database to update.

        :schema: StoreDetail#Prefix
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the Federated Database to update.

        :schema: StoreDetail#Provider
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the Federated Database to update.

        :schema: StoreDetail#Region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoreDetail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.SynonymSource",
    jsii_struct_bases=[],
    name_mapping={"collection": "collection"},
)
class SynonymSource:
    def __init__(self, *, collection: typing.Optional[builtins.str] = None) -> None:
        '''
        :param collection: Human-readable label that identifies the MongoDB collection that stores words and their applicable synonyms.

        :schema: SynonymSource
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__caccb6c960fb58719d52b223ea81a5b4f4b7cfb6e41288f8025edce4c0d7c3aa)
            check_type(argname="argument collection", value=collection, expected_type=type_hints["collection"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if collection is not None:
            self._values["collection"] = collection

    @builtins.property
    def collection(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the MongoDB collection that stores words and their applicable synonyms.

        :schema: SynonymSource#Collection
        '''
        result = self._values.get("collection")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SynonymSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ThirdPartyIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={"project_id": "projectId", "profile": "profile"},
)
class ThirdPartyIntegrationProps:
    def __init__(
        self,
        *,
        project_id: builtins.str,
        profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param profile: Atlas API keys.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b529551b78555a8abecb5e698997ab77e6f3c865015e596f955c11e12409591)
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_id": project_id,
        }
        if profile is not None:
            self._values["profile"] = profile

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies your project.'''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Atlas API keys.'''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ThirdPartyIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.Validation",
    jsii_struct_bases=[],
    name_mapping={"status": "status", "validation_type": "validationType"},
)
class Validation:
    def __init__(
        self,
        *,
        status: typing.Optional[builtins.str] = None,
        validation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param status: 
        :param validation_type: 

        :schema: Validation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d90b6dd072abd6b2ff8aea1f6c2d2169b6043cbd8ebfdf520e7efc188ffa6aff)
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument validation_type", value=validation_type, expected_type=type_hints["validation_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if status is not None:
            self._values["status"] = status
        if validation_type is not None:
            self._values["validation_type"] = validation_type

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Validation#Status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def validation_type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Validation#ValidationType
        '''
        result = self._values.get("validation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Validation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.ZoneMapping",
    jsii_struct_bases=[],
    name_mapping={"location": "location", "zone": "zone"},
)
class ZoneMapping:
    def __init__(
        self,
        *,
        location: typing.Optional[builtins.str] = None,
        zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param location: Code that represents a location that maps to a zone in your global cluster. MongoDB Cloud represents this location with a ISO 3166-2 location and subdivision codes when possible.
        :param zone: Human-readable label that identifies the zone in your global cluster. This zone maps to a location code.

        :schema: zoneMapping
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6220d1f1292858228949b538159452b8c6e9c242f0500cfa563a3ef797422db)
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if location is not None:
            self._values["location"] = location
        if zone is not None:
            self._values["zone"] = zone

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Code that represents a location that maps to a zone in your global cluster.

        MongoDB Cloud represents this location with a ISO 3166-2 location and subdivision codes when possible.

        :schema: zoneMapping#Location
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zone(self) -> typing.Optional[builtins.str]:
        '''Human-readable label that identifies the zone in your global cluster.

        This zone maps to a location code.

        :schema: zoneMapping#Zone
        '''
        result = self._values.get("zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ZoneMapping(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.DatadogIntegrationProps",
    jsii_struct_bases=[ThirdPartyIntegrationProps],
    name_mapping={
        "project_id": "projectId",
        "profile": "profile",
        "api_key": "apiKey",
        "region": "region",
    },
)
class DatadogIntegrationProps(ThirdPartyIntegrationProps):
    def __init__(
        self,
        *,
        project_id: builtins.str,
        profile: typing.Optional[builtins.str] = None,
        api_key: builtins.str,
        region: DatadogRegion,
    ) -> None:
        '''
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param profile: Atlas API keys.
        :param api_key: Key that allows MongoDB Cloud to access your Datadog account.
        :param region: Two-letter code that indicates which regional URL MongoDB uses to access the Datadog API.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f0086ecfd7718566112a61f855200362f4316843413bc562863c61bd119d214)
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_id": project_id,
            "api_key": api_key,
            "region": region,
        }
        if profile is not None:
            self._values["profile"] = profile

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies your project.'''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Atlas API keys.'''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_key(self) -> builtins.str:
        '''Key that allows MongoDB Cloud to access your Datadog account.'''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> DatadogRegion:
        '''Two-letter code that indicates which regional URL MongoDB uses to access the Datadog API.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(DatadogRegion, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatadogIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.MicrosoftTeamsIntegrationProps",
    jsii_struct_bases=[ThirdPartyIntegrationProps],
    name_mapping={
        "project_id": "projectId",
        "profile": "profile",
        "microsoft_teams_webhook_url": "microsoftTeamsWebhookUrl",
    },
)
class MicrosoftTeamsIntegrationProps(ThirdPartyIntegrationProps):
    def __init__(
        self,
        *,
        project_id: builtins.str,
        profile: typing.Optional[builtins.str] = None,
        microsoft_teams_webhook_url: builtins.str,
    ) -> None:
        '''
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param profile: Atlas API keys.
        :param microsoft_teams_webhook_url: Endpoint web address of the Microsoft Teams webhook to which MongoDB Cloud sends notifications.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2e1d02ed702d6a87cf81eea5c1c4c38f0803f055ba815185a186c1ceb6ed43e)
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument microsoft_teams_webhook_url", value=microsoft_teams_webhook_url, expected_type=type_hints["microsoft_teams_webhook_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_id": project_id,
            "microsoft_teams_webhook_url": microsoft_teams_webhook_url,
        }
        if profile is not None:
            self._values["profile"] = profile

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies your project.'''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Atlas API keys.'''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def microsoft_teams_webhook_url(self) -> builtins.str:
        '''Endpoint web address of the Microsoft Teams webhook to which MongoDB Cloud sends notifications.'''
        result = self._values.get("microsoft_teams_webhook_url")
        assert result is not None, "Required property 'microsoft_teams_webhook_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MicrosoftTeamsIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="awscdk-resources-mongodbatlas.PagerDutyIntegrationProps",
    jsii_struct_bases=[ThirdPartyIntegrationProps],
    name_mapping={
        "project_id": "projectId",
        "profile": "profile",
        "region": "region",
        "service_key": "serviceKey",
    },
)
class PagerDutyIntegrationProps(ThirdPartyIntegrationProps):
    def __init__(
        self,
        *,
        project_id: builtins.str,
        profile: typing.Optional[builtins.str] = None,
        region: PagerDutyRegion,
        service_key: builtins.str,
    ) -> None:
        '''
        :param project_id: Unique 24-hexadecimal digit string that identifies your project.
        :param profile: Atlas API keys.
        :param region: PagerDuty region that indicates the API Uniform Resource Locator (URL) to use.
        :param service_key: Service key associated with your PagerDuty account.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c69e232e879d6582d1ac91e602aa14f79651fcdc4133ebecbb500a99afaa426e)
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument service_key", value=service_key, expected_type=type_hints["service_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_id": project_id,
            "region": region,
            "service_key": service_key,
        }
        if profile is not None:
            self._values["profile"] = profile

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique 24-hexadecimal digit string that identifies your project.'''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Atlas API keys.'''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> PagerDutyRegion:
        '''PagerDuty region that indicates the API Uniform Resource Locator (URL) to use.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(PagerDutyRegion, result)

    @builtins.property
    def service_key(self) -> builtins.str:
        '''Service key associated with your PagerDuty account.'''
        result = self._values.get("service_key")
        assert result is not None, "Required property 'service_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PagerDutyIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccessListDefinition",
    "Action",
    "AdvancedAutoScaling",
    "AdvancedRegionConfig",
    "AdvancedRegionConfigProviderName",
    "AdvancedReplicationSpec",
    "ApiAtlasDiskBackupCopySettingView",
    "ApiAtlasDiskBackupShardedClusterSnapshotMemberView",
    "ApiAtlasDiskBackupShardedClusterSnapshotMemberViewCloudProvider",
    "ApiAtlasDiskBackupShardedClusterSnapshotView",
    "ApiAtlasDiskBackupShardedClusterSnapshotViewFrequencyType",
    "ApiAtlasDiskBackupShardedClusterSnapshotViewSnapshotType",
    "ApiAtlasDiskBackupShardedClusterSnapshotViewStatus",
    "ApiAtlasDiskBackupShardedClusterSnapshotViewType",
    "ApiAtlasFtsAnalyzersViewManual",
    "ApiAtlasFtsMappingsViewManual",
    "ApiAtlasFtsSynonymMappingDefinitionView",
    "ApiAtlasNdsUserToDnMappingView",
    "ApiDeleteCopiedBackupsView",
    "ApiPolicyItemView",
    "ApiPolicyView",
    "AtlasBasic",
    "AtlasBasicPrivateEndpoint",
    "AtlasBasicPrivateEndpointProps",
    "AtlasBasicProps",
    "AtlasEncryptionAtRest",
    "AtlasEncryptionAtRestExpress",
    "AtlasEncryptionAtRestExpressProps",
    "AtlasEncryptionAtRestProps",
    "AtlasRole",
    "AtlasRoleRoleName",
    "AtlasUser",
    "AuthConfig",
    "AuthConfigOperationType",
    "AuthConfigProviders",
    "AwsKmsConfiguration",
    "CfnAlertConfiguration",
    "CfnAlertConfigurationProps",
    "CfnAuditing",
    "CfnAuditingProps",
    "CfnCloudBackUpRestoreJobs",
    "CfnCloudBackUpRestoreJobsProps",
    "CfnCloudBackUpRestoreJobsPropsDeliveryType",
    "CfnCloudBackupSchedule",
    "CfnCloudBackupScheduleProps",
    "CfnCloudBackupSnapshot",
    "CfnCloudBackupSnapshotExportBucket",
    "CfnCloudBackupSnapshotExportBucketProps",
    "CfnCloudBackupSnapshotProps",
    "CfnCloudBackupSnapshotPropsFrequencyType",
    "CfnCloudBackupSnapshotPropsSnapshotType",
    "CfnCluster",
    "CfnClusterProps",
    "CfnClusterPropsBiConnector",
    "CfnClusterPropsEncryptionAtRestProvider",
    "CfnClusterPropsLabels",
    "CfnCustomDbRole",
    "CfnCustomDbRoleProps",
    "CfnCustomDnsConfigurationClusterAws",
    "CfnCustomDnsConfigurationClusterAwsProps",
    "CfnDataLakes",
    "CfnDataLakesProps",
    "CfnDatabaseUser",
    "CfnDatabaseUserProps",
    "CfnDatabaseUserPropsAwsiamType",
    "CfnDatabaseUserPropsLdapAuthType",
    "CfnDatabaseUserPropsX509Type",
    "CfnEncryptionAtRest",
    "CfnEncryptionAtRestProps",
    "CfnFederatedSettingsOrgRoleMapping",
    "CfnFederatedSettingsOrgRoleMappingProps",
    "CfnGlobalClusterConfig",
    "CfnGlobalClusterConfigProps",
    "CfnLdapConfiguration",
    "CfnLdapConfigurationProps",
    "CfnLdapVerify",
    "CfnLdapVerifyProps",
    "CfnMaintenanceWindow",
    "CfnMaintenanceWindowProps",
    "CfnNetworkContainer",
    "CfnNetworkContainerProps",
    "CfnNetworkPeering",
    "CfnNetworkPeeringProps",
    "CfnOnlineArchive",
    "CfnOnlineArchiveProps",
    "CfnOnlineArchivePropsCollectionType",
    "CfnOrgInvitation",
    "CfnOrgInvitationProps",
    "CfnOrgInvitationPropsRoles",
    "CfnPrivateEndPointRegionalMode",
    "CfnPrivateEndPointRegionalModeProps",
    "CfnPrivateEndpoint",
    "CfnPrivateEndpointAdl",
    "CfnPrivateEndpointAdlProps",
    "CfnPrivateEndpointProps",
    "CfnProject",
    "CfnProjectInvitation",
    "CfnProjectInvitationProps",
    "CfnProjectInvitationPropsRoles",
    "CfnProjectIpAccessList",
    "CfnProjectIpAccessListProps",
    "CfnProjectProps",
    "CfnSearchIndex",
    "CfnSearchIndexProps",
    "CfnServerlessInstance",
    "CfnServerlessInstanceProps",
    "CfnTeams",
    "CfnTeamsProps",
    "CfnTeamsPropsRoleNames",
    "CfnThirdPartyIntegration",
    "CfnThirdPartyIntegrationProps",
    "CfnThirdPartyIntegrationPropsScheme",
    "CfnThirdPartyIntegrationPropsServiceDiscovery",
    "CfnThirdPartyIntegrationPropsType",
    "CfnTrigger",
    "CfnTriggerProps",
    "CfnX509AuthenticationDatabaseUser",
    "CfnX509AuthenticationDatabaseUserProps",
    "ClusterProps",
    "Compute",
    "ConnectionStrings",
    "CriteriaView",
    "CriteriaViewDateFormat",
    "CriteriaViewType",
    "CustomerX509",
    "DataLakeAwsCloudProviderConfigView",
    "DataLakeCloudProviderConfigView",
    "DataLakeDataProcessRegionView",
    "DataLakeDataProcessRegionViewCloudProvider",
    "DataLakeDataProcessRegionViewRegion",
    "DataLakeDatabaseCollectionView",
    "DataLakeDatabaseDataSourceView",
    "DataLakeDatabaseDataSourceViewDefaultFormat",
    "DataLakeDatabaseView",
    "DataLakeStorageView",
    "DataLakeViewView",
    "DatabaseConfig",
    "DatabaseConfigOperationTypes",
    "DatabaseUserProps",
    "DatadogIntegration",
    "DatadogIntegrationProps",
    "DatadogRegion",
    "DiskGb",
    "EncryptionAtRestProps",
    "Endpoint",
    "Event",
    "EventAwseventbridge",
    "EventAwseventbridgeAwsConfig",
    "EventFunction",
    "EventFunctionFuncConfig",
    "Export",
    "InheritedRole",
    "IntegerThresholdView",
    "IntegerThresholdViewOperator",
    "IpAccessListProps",
    "LabelDefinition",
    "Link",
    "ListOptions",
    "ManagedNamespace",
    "Matcher",
    "MatcherFieldName",
    "MatcherOperator",
    "MetricThresholdView",
    "MetricThresholdViewMode",
    "MetricThresholdViewOperator",
    "MicrosoftTeamsIntegration",
    "MicrosoftTeamsIntegrationProps",
    "NotificationView",
    "NotificationViewDatadogRegion",
    "NotificationViewOpsGenieRegion",
    "NotificationViewRoles",
    "NotificationViewSeverity",
    "NotificationViewTypeName",
    "PagerDutyIntegration",
    "PagerDutyIntegrationProps",
    "PagerDutyRegion",
    "PartitionFieldView",
    "PartitionFieldViewFieldType",
    "PrivateEndpoint",
    "PrivateEndpointProps",
    "ProcessArgs",
    "ProjectApiKey",
    "ProjectProps",
    "ProjectSettings",
    "ProjectTeam",
    "Resource",
    "RoleAssignment",
    "RoleDefinition",
    "ScheduleConfig",
    "ScheduleView",
    "ScheduleViewType",
    "ScopeDefinition",
    "ScopeDefinitionType",
    "ServerlessInstanceConnectionStrings",
    "ServerlessInstancePrivateEndpoint",
    "ServerlessInstancePrivateEndpointEndpoint",
    "ServerlessInstancePrivateEndpointType",
    "ServerlessInstanceProviderSettings",
    "ServerlessInstanceProviderSettingsProviderName",
    "Specs",
    "StoreDetail",
    "SynonymSource",
    "ThirdPartyIntegrationProps",
    "Validation",
    "ZoneMapping",
]

publication.publish()

def _typecheckingstub__c95ca92412af9e60fd32fabdf8a64b384ec620641a1767b8699a24ce265e8c77(
    *,
    aws_security_group: typing.Optional[builtins.str] = None,
    cidr_block: typing.Optional[builtins.str] = None,
    comment: typing.Optional[builtins.str] = None,
    delete_after_date: typing.Optional[builtins.str] = None,
    ip_address: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4c2b51f44f5320b4b6204a6c2e4237c395d8be8b851a1aff6fd2fbaccebffde(
    *,
    action: typing.Optional[builtins.str] = None,
    resources: typing.Optional[typing.Sequence[typing.Union[Resource, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac917b855a047532ce73b0f00ca7514f93d4661841803d30fd263b12ed2a4b57(
    *,
    compute: typing.Optional[typing.Union[Compute, typing.Dict[builtins.str, typing.Any]]] = None,
    disk_gb: typing.Optional[typing.Union[DiskGb, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__862cd9358d07b2b78562a3e3584bc148b035b9f38266e5522b3bea0cbaae1473(
    *,
    analytics_auto_scaling: typing.Optional[typing.Union[AdvancedAutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
    analytics_specs: typing.Optional[typing.Union[Specs, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_scaling: typing.Optional[typing.Union[AdvancedAutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
    backing_provider_name: typing.Optional[builtins.str] = None,
    electable_specs: typing.Optional[typing.Union[Specs, typing.Dict[builtins.str, typing.Any]]] = None,
    priority: typing.Optional[jsii.Number] = None,
    provider_name: typing.Optional[AdvancedRegionConfigProviderName] = None,
    read_only_specs: typing.Optional[typing.Union[Specs, typing.Dict[builtins.str, typing.Any]]] = None,
    region_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58913fadf8dd44199500c4dc60f4d148cb0bb418b7eea67df88294e1559ac5db(
    *,
    advanced_region_configs: typing.Optional[typing.Sequence[typing.Union[AdvancedRegionConfig, typing.Dict[builtins.str, typing.Any]]]] = None,
    id: typing.Optional[builtins.str] = None,
    num_shards: typing.Optional[jsii.Number] = None,
    zone_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5fa3e8f2afa69a76f26b01b4b454e19ee37ec11540b5696c986feed55bdd551(
    *,
    cloud_provider: typing.Optional[builtins.str] = None,
    frequencies: typing.Optional[typing.Sequence[builtins.str]] = None,
    region_name: typing.Optional[builtins.str] = None,
    replication_spec_id: typing.Optional[builtins.str] = None,
    should_copy_oplogs: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4e6b3d1e03871f93cf35cef4e9b9a9e64e19a6371d56a868de493caabcdf7f8(
    *,
    cloud_provider: typing.Optional[ApiAtlasDiskBackupShardedClusterSnapshotMemberViewCloudProvider] = None,
    id: typing.Optional[builtins.str] = None,
    replica_set_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__146d6e2792ffe8ca573648d29829309cd1ab0dae9b194541f355d17534634fa1(
    *,
    created_at: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    expires_at: typing.Optional[builtins.str] = None,
    frequency_type: typing.Optional[ApiAtlasDiskBackupShardedClusterSnapshotViewFrequencyType] = None,
    id: typing.Optional[builtins.str] = None,
    master_key_uuid: typing.Optional[builtins.str] = None,
    members: typing.Optional[typing.Sequence[typing.Union[ApiAtlasDiskBackupShardedClusterSnapshotMemberView, typing.Dict[builtins.str, typing.Any]]]] = None,
    mongod_version: typing.Optional[builtins.str] = None,
    policy_items: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_type: typing.Optional[ApiAtlasDiskBackupShardedClusterSnapshotViewSnapshotType] = None,
    status: typing.Optional[ApiAtlasDiskBackupShardedClusterSnapshotViewStatus] = None,
    storage_size_bytes: typing.Optional[builtins.str] = None,
    type: typing.Optional[ApiAtlasDiskBackupShardedClusterSnapshotViewType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d95cf8751425648c9192218f3c835c3361006d1555b7ef3c0ade93a78a633a7(
    *,
    char_filters: typing.Optional[typing.Sequence[typing.Any]] = None,
    name: typing.Optional[builtins.str] = None,
    token_filters: typing.Optional[typing.Sequence[typing.Any]] = None,
    tokenizer: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf0b4b56e5803c25ffcc1d174524561964e5439926621ecbc2210ca575e55357(
    *,
    dynamic: typing.Optional[builtins.bool] = None,
    fields: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab7d3cb96638b70da5f4ee06bbaca4e02962e20e1fc0b57368a6f8a5491c5833(
    *,
    analyzer: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    source: typing.Optional[typing.Union[SynonymSource, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6d3a9fa0d7784b3a1c43d99716c4869d5dc8be079748328cd1c43a4e49538b3(
    *,
    ldap_query: typing.Optional[builtins.str] = None,
    match: typing.Optional[builtins.str] = None,
    substitution: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30bd9d2e1004548ab815b4223767fb9673db3b56f9e7b7d327bf025e34d0f506(
    *,
    cloud_provider: typing.Optional[builtins.str] = None,
    region_name: typing.Optional[builtins.str] = None,
    replication_spec_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2f115084308517a41f040e7fb2335843a23bfc5b583498250061514ac4d3f96(
    *,
    frequency_interval: typing.Optional[jsii.Number] = None,
    frequency_type: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    retention_unit: typing.Optional[builtins.str] = None,
    retention_value: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66300e76f7281d11014f5beeeb5c606f84ee2abc698090f850a29d9967bd5218(
    *,
    id: typing.Optional[builtins.str] = None,
    policy_items: typing.Optional[typing.Sequence[typing.Union[ApiPolicyItemView, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09a55f3bb77dc35f1cf8e82985ed9e9356b19aef3b78a58f27213fea7ac0ae72(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_props: typing.Union[ClusterProps, typing.Dict[builtins.str, typing.Any]],
    project_props: typing.Union[ProjectProps, typing.Dict[builtins.str, typing.Any]],
    db_user_props: typing.Optional[typing.Union[DatabaseUserProps, typing.Dict[builtins.str, typing.Any]]] = None,
    ip_access_list_props: typing.Optional[typing.Union[IpAccessListProps, typing.Dict[builtins.str, typing.Any]]] = None,
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b95159a964749cd6793dc2842badabf780be08d986e82290a4538e7f33fa987(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    atlas_basic_props: typing.Union[AtlasBasicProps, typing.Dict[builtins.str, typing.Any]],
    private_endpoint_props: typing.Union[PrivateEndpointProps, typing.Dict[builtins.str, typing.Any]],
    profile: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0861be50ce20d9bd65c7aab5af1aaefaefa9301d16772a9e668ce3ba885df54f(
    *,
    atlas_basic_props: typing.Union[AtlasBasicProps, typing.Dict[builtins.str, typing.Any]],
    private_endpoint_props: typing.Union[PrivateEndpointProps, typing.Dict[builtins.str, typing.Any]],
    profile: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93da559aa417299c3d6c0b4d6d651c13874200057b5e18bd3f6cb3c0ba8f05a7(
    *,
    cluster_props: typing.Union[ClusterProps, typing.Dict[builtins.str, typing.Any]],
    project_props: typing.Union[ProjectProps, typing.Dict[builtins.str, typing.Any]],
    db_user_props: typing.Optional[typing.Union[DatabaseUserProps, typing.Dict[builtins.str, typing.Any]]] = None,
    ip_access_list_props: typing.Optional[typing.Union[IpAccessListProps, typing.Dict[builtins.str, typing.Any]]] = None,
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eb2b1030acc5acca2fc4d2ecdf71aeb4a3143194e1f8a93dab798e2f0ffd4ef(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    customer_master_key_id: builtins.str,
    project_id: builtins.str,
    role_id: builtins.str,
    enabled: typing.Optional[builtins.bool] = None,
    profile: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8b33dd54ddc5da7412cb321438f6afb0d99afb6e8988b1007798ea762133760(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    encryption_at_rest: typing.Union[EncryptionAtRestProps, typing.Dict[builtins.str, typing.Any]],
    project_id: builtins.str,
    access_list: typing.Optional[typing.Union[IpAccessListProps, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster: typing.Optional[typing.Union[ClusterProps, typing.Dict[builtins.str, typing.Any]]] = None,
    database_user: typing.Optional[typing.Union[DatabaseUserProps, typing.Dict[builtins.str, typing.Any]]] = None,
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0852dfead77edf0f28ec2bd3a9cbb3609afa983a72902f7f9c51444eb18eff2c(
    *,
    encryption_at_rest: typing.Union[EncryptionAtRestProps, typing.Dict[builtins.str, typing.Any]],
    project_id: builtins.str,
    access_list: typing.Optional[typing.Union[IpAccessListProps, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster: typing.Optional[typing.Union[ClusterProps, typing.Dict[builtins.str, typing.Any]]] = None,
    database_user: typing.Optional[typing.Union[DatabaseUserProps, typing.Dict[builtins.str, typing.Any]]] = None,
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2055422c6e521e83bb98bde13173f68b0fcf55f218fc6c7eb6ed9d6b0fe46bbe(
    *,
    customer_master_key_id: builtins.str,
    project_id: builtins.str,
    role_id: builtins.str,
    enabled: typing.Optional[builtins.bool] = None,
    profile: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2e9b38f68e7180f738aab12a9bcebcfdd6b552b0f1f800a61f7073a2a26bf21(
    *,
    org_id: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    role_name: typing.Optional[AtlasRoleRoleName] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1db857eabeffa5d4ead7ea85b91a863188acc280436bd51eb07ccab300640459(
    *,
    country: typing.Optional[builtins.str] = None,
    email_address: typing.Optional[builtins.str] = None,
    first_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    last_name: typing.Optional[builtins.str] = None,
    links: typing.Optional[typing.Sequence[typing.Union[Link, typing.Dict[builtins.str, typing.Any]]]] = None,
    mobile_number: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    roles: typing.Optional[typing.Sequence[typing.Union[AtlasRole, typing.Dict[builtins.str, typing.Any]]]] = None,
    team_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5226df9d8aa32f5d603a743768e2851f951f3da7c1954ac02c0e59a1a83b6261(
    *,
    operation_type: AuthConfigOperationType,
    providers: typing.Sequence[AuthConfigProviders],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7388feda47d948491eb9f6057d8e8d13c0fa2d221eed6e7ec474b0ae15fc00f(
    *,
    customer_master_key_id: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[builtins.bool] = None,
    region: typing.Optional[builtins.str] = None,
    role_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1da040dafccf3c31fc01d7d84650c82a95e60338eae23c0d0e0e264555272322(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    created: typing.Optional[builtins.str] = None,
    event_type_name: typing.Optional[builtins.str] = None,
    matchers: typing.Optional[typing.Sequence[typing.Union[Matcher, typing.Dict[builtins.str, typing.Any]]]] = None,
    metric_threshold: typing.Optional[typing.Union[MetricThresholdView, typing.Dict[builtins.str, typing.Any]]] = None,
    notifications: typing.Optional[typing.Sequence[typing.Union[NotificationView, typing.Dict[builtins.str, typing.Any]]]] = None,
    profile: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    threshold: typing.Optional[typing.Union[IntegerThresholdView, typing.Dict[builtins.str, typing.Any]]] = None,
    type_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__124a8c3213791f916b7d88df4adbcca6ef1de224de7be7cd6a830df6113f4ef8(
    *,
    created: typing.Optional[builtins.str] = None,
    event_type_name: typing.Optional[builtins.str] = None,
    matchers: typing.Optional[typing.Sequence[typing.Union[Matcher, typing.Dict[builtins.str, typing.Any]]]] = None,
    metric_threshold: typing.Optional[typing.Union[MetricThresholdView, typing.Dict[builtins.str, typing.Any]]] = None,
    notifications: typing.Optional[typing.Sequence[typing.Union[NotificationView, typing.Dict[builtins.str, typing.Any]]]] = None,
    profile: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    threshold: typing.Optional[typing.Union[IntegerThresholdView, typing.Dict[builtins.str, typing.Any]]] = None,
    type_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a26aea3c99c1ed5d3bb2bc42924ccb83bd9c0d582ab6564ad459d34982cb0a9b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    group_id: builtins.str,
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3478ad6f6a0f7e5f69e0f8e3efee5546775e0c04b0842546e587aee290cc4f1(
    *,
    group_id: builtins.str,
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d5a576b5b88e386d800cf2be9f8dd13676ca57ee8ff8653f832b0d7cc06b8cf(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_name: builtins.str,
    project_id: builtins.str,
    cancelled: typing.Optional[builtins.bool] = None,
    delivery_type: typing.Optional[CfnCloudBackUpRestoreJobsPropsDeliveryType] = None,
    expired: typing.Optional[builtins.bool] = None,
    instance_name: typing.Optional[builtins.str] = None,
    op_log_inc: typing.Optional[builtins.str] = None,
    op_log_ts: typing.Optional[builtins.str] = None,
    point_in_time_utc_seconds: typing.Optional[jsii.Number] = None,
    profile: typing.Optional[builtins.str] = None,
    snapshot_id: typing.Optional[builtins.str] = None,
    target_cluster_name: typing.Optional[builtins.str] = None,
    target_project_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c452f384c2684cd0393e2f443bac830ff55b9ea890ebb7fb44b8bd797fdda1a9(
    *,
    cluster_name: builtins.str,
    project_id: builtins.str,
    cancelled: typing.Optional[builtins.bool] = None,
    delivery_type: typing.Optional[CfnCloudBackUpRestoreJobsPropsDeliveryType] = None,
    expired: typing.Optional[builtins.bool] = None,
    instance_name: typing.Optional[builtins.str] = None,
    op_log_inc: typing.Optional[builtins.str] = None,
    op_log_ts: typing.Optional[builtins.str] = None,
    point_in_time_utc_seconds: typing.Optional[jsii.Number] = None,
    profile: typing.Optional[builtins.str] = None,
    snapshot_id: typing.Optional[builtins.str] = None,
    target_cluster_name: typing.Optional[builtins.str] = None,
    target_project_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bfdd674c8b0e499ab1f52cd281df10bf04b830fce65245beea7d06c6b570b57(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    cluster_name: builtins.str,
    project_id: builtins.str,
    auto_export_enabled: typing.Optional[builtins.bool] = None,
    copy_settings: typing.Optional[typing.Sequence[typing.Union[ApiAtlasDiskBackupCopySettingView, typing.Dict[builtins.str, typing.Any]]]] = None,
    delete_copied_backups: typing.Optional[typing.Sequence[typing.Union[ApiDeleteCopiedBackupsView, typing.Dict[builtins.str, typing.Any]]]] = None,
    export: typing.Optional[typing.Union[Export, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    links: typing.Optional[typing.Sequence[typing.Union[Link, typing.Dict[builtins.str, typing.Any]]]] = None,
    policies: typing.Optional[typing.Sequence[typing.Union[ApiPolicyView, typing.Dict[builtins.str, typing.Any]]]] = None,
    profile: typing.Optional[builtins.str] = None,
    reference_hour_of_day: typing.Optional[jsii.Number] = None,
    reference_minute_of_hour: typing.Optional[jsii.Number] = None,
    restore_window_days: typing.Optional[jsii.Number] = None,
    update_snapshots: typing.Optional[builtins.bool] = None,
    use_org_and_group_names_in_export_prefix: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2200bd53f19ffb8d78ee28d63e9f901d04707cca2ada01f3a1c4aa6c97d8aef(
    *,
    cluster_name: builtins.str,
    project_id: builtins.str,
    auto_export_enabled: typing.Optional[builtins.bool] = None,
    copy_settings: typing.Optional[typing.Sequence[typing.Union[ApiAtlasDiskBackupCopySettingView, typing.Dict[builtins.str, typing.Any]]]] = None,
    delete_copied_backups: typing.Optional[typing.Sequence[typing.Union[ApiDeleteCopiedBackupsView, typing.Dict[builtins.str, typing.Any]]]] = None,
    export: typing.Optional[typing.Union[Export, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    links: typing.Optional[typing.Sequence[typing.Union[Link, typing.Dict[builtins.str, typing.Any]]]] = None,
    policies: typing.Optional[typing.Sequence[typing.Union[ApiPolicyView, typing.Dict[builtins.str, typing.Any]]]] = None,
    profile: typing.Optional[builtins.str] = None,
    reference_hour_of_day: typing.Optional[jsii.Number] = None,
    reference_minute_of_hour: typing.Optional[jsii.Number] = None,
    restore_window_days: typing.Optional[jsii.Number] = None,
    update_snapshots: typing.Optional[builtins.bool] = None,
    use_org_and_group_names_in_export_prefix: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__529f49fdab044e02ca0bd055ed41fa8d7b5b244ba250907765c0fc282e21cd88(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_name: builtins.str,
    project_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    frequency_type: typing.Optional[CfnCloudBackupSnapshotPropsFrequencyType] = None,
    include_count: typing.Optional[builtins.bool] = None,
    instance_name: typing.Optional[builtins.str] = None,
    items_per_page: typing.Optional[jsii.Number] = None,
    members: typing.Optional[typing.Sequence[typing.Union[ApiAtlasDiskBackupShardedClusterSnapshotMemberView, typing.Dict[builtins.str, typing.Any]]]] = None,
    page_num: typing.Optional[jsii.Number] = None,
    policy_items: typing.Optional[typing.Sequence[builtins.str]] = None,
    profile: typing.Optional[builtins.str] = None,
    results: typing.Optional[typing.Sequence[typing.Union[ApiAtlasDiskBackupShardedClusterSnapshotView, typing.Dict[builtins.str, typing.Any]]]] = None,
    retention_in_days: typing.Optional[jsii.Number] = None,
    snapshot_type: typing.Optional[CfnCloudBackupSnapshotPropsSnapshotType] = None,
    total_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d2cbf89a63594824b85f7bcf3bf165f87cb367057546423748ece0b111c26ff(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bucket_name: builtins.str,
    iam_role_id: builtins.str,
    project_id: builtins.str,
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bbf399890a7be0cef3c6995156840980718a18571938b035823d3ca4cf5afe7(
    *,
    bucket_name: builtins.str,
    iam_role_id: builtins.str,
    project_id: builtins.str,
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a6774a317e39f3d32c18b6b78f8e6e5fb3dc632b6d633d27d87b2e7381a39b9(
    *,
    cluster_name: builtins.str,
    project_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    frequency_type: typing.Optional[CfnCloudBackupSnapshotPropsFrequencyType] = None,
    include_count: typing.Optional[builtins.bool] = None,
    instance_name: typing.Optional[builtins.str] = None,
    items_per_page: typing.Optional[jsii.Number] = None,
    members: typing.Optional[typing.Sequence[typing.Union[ApiAtlasDiskBackupShardedClusterSnapshotMemberView, typing.Dict[builtins.str, typing.Any]]]] = None,
    page_num: typing.Optional[jsii.Number] = None,
    policy_items: typing.Optional[typing.Sequence[builtins.str]] = None,
    profile: typing.Optional[builtins.str] = None,
    results: typing.Optional[typing.Sequence[typing.Union[ApiAtlasDiskBackupShardedClusterSnapshotView, typing.Dict[builtins.str, typing.Any]]]] = None,
    retention_in_days: typing.Optional[jsii.Number] = None,
    snapshot_type: typing.Optional[CfnCloudBackupSnapshotPropsSnapshotType] = None,
    total_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bc5e075eab328219b963df173ff94d0a7cace489d75a5b5cb407bb5cc93bd2c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    project_id: builtins.str,
    advanced_settings: typing.Optional[typing.Union[ProcessArgs, typing.Dict[builtins.str, typing.Any]]] = None,
    backup_enabled: typing.Optional[builtins.bool] = None,
    bi_connector: typing.Optional[typing.Union[CfnClusterPropsBiConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_type: typing.Optional[builtins.str] = None,
    disk_size_gb: typing.Optional[jsii.Number] = None,
    encryption_at_rest_provider: typing.Optional[CfnClusterPropsEncryptionAtRestProvider] = None,
    labels: typing.Optional[typing.Sequence[typing.Union[CfnClusterPropsLabels, typing.Dict[builtins.str, typing.Any]]]] = None,
    mongo_db_major_version: typing.Optional[builtins.str] = None,
    paused: typing.Optional[builtins.bool] = None,
    pit_enabled: typing.Optional[builtins.bool] = None,
    profile: typing.Optional[builtins.str] = None,
    replication_specs: typing.Optional[typing.Sequence[typing.Union[AdvancedReplicationSpec, typing.Dict[builtins.str, typing.Any]]]] = None,
    root_cert_type: typing.Optional[builtins.str] = None,
    termination_protection_enabled: typing.Optional[builtins.bool] = None,
    version_release_system: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1bc8a0a1d2a548e1055aa8d1afa8fe110f9e5280af17a15ff7166a8deb02fb8(
    *,
    name: builtins.str,
    project_id: builtins.str,
    advanced_settings: typing.Optional[typing.Union[ProcessArgs, typing.Dict[builtins.str, typing.Any]]] = None,
    backup_enabled: typing.Optional[builtins.bool] = None,
    bi_connector: typing.Optional[typing.Union[CfnClusterPropsBiConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_type: typing.Optional[builtins.str] = None,
    disk_size_gb: typing.Optional[jsii.Number] = None,
    encryption_at_rest_provider: typing.Optional[CfnClusterPropsEncryptionAtRestProvider] = None,
    labels: typing.Optional[typing.Sequence[typing.Union[CfnClusterPropsLabels, typing.Dict[builtins.str, typing.Any]]]] = None,
    mongo_db_major_version: typing.Optional[builtins.str] = None,
    paused: typing.Optional[builtins.bool] = None,
    pit_enabled: typing.Optional[builtins.bool] = None,
    profile: typing.Optional[builtins.str] = None,
    replication_specs: typing.Optional[typing.Sequence[typing.Union[AdvancedReplicationSpec, typing.Dict[builtins.str, typing.Any]]]] = None,
    root_cert_type: typing.Optional[builtins.str] = None,
    termination_protection_enabled: typing.Optional[builtins.bool] = None,
    version_release_system: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2b38734bb7f9f3cc0507c7b2e3b52a5a5b9c79037624c47f3dac930e5ce4915(
    *,
    enabled: typing.Optional[builtins.bool] = None,
    read_preference: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33e9c067ab8e3a2f0cafd43d6b7169c56c130a69745e771874e75f1649c24441(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a9ff921996dfab88be67df88221f112970c5268971a7c2a5f35106d61086898(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    project_id: builtins.str,
    role_name: builtins.str,
    actions: typing.Optional[typing.Sequence[typing.Union[Action, typing.Dict[builtins.str, typing.Any]]]] = None,
    inherited_roles: typing.Optional[typing.Sequence[typing.Union[InheritedRole, typing.Dict[builtins.str, typing.Any]]]] = None,
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cfe2387200229b4088642580d5165b7db0ad0d54a7c635a501846f530e63ef8(
    *,
    project_id: builtins.str,
    role_name: builtins.str,
    actions: typing.Optional[typing.Sequence[typing.Union[Action, typing.Dict[builtins.str, typing.Any]]]] = None,
    inherited_roles: typing.Optional[typing.Sequence[typing.Union[InheritedRole, typing.Dict[builtins.str, typing.Any]]]] = None,
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0f88706de82c968034f862c67a677a4d3e6a276cc00f97836cc0d94795fa79f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    project_id: builtins.str,
    enabled: typing.Optional[builtins.bool] = None,
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbd42d5139b917f1ba7ff5f24d5756e205ae53489e0d73e76fb1959cb88b5e6a(
    *,
    project_id: builtins.str,
    enabled: typing.Optional[builtins.bool] = None,
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__664ca025502c6690a88bf9d84e9fa20afda504cf270dfbe1bd90611bbd258a85(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cloud_provider_config: typing.Optional[typing.Union[DataLakeCloudProviderConfigView, typing.Dict[builtins.str, typing.Any]]] = None,
    data_process_region: typing.Optional[typing.Union[DataLakeDataProcessRegionView, typing.Dict[builtins.str, typing.Any]]] = None,
    end_date: typing.Optional[jsii.Number] = None,
    profile: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    skip_role_validation: typing.Optional[builtins.bool] = None,
    storage: typing.Optional[typing.Union[DataLakeStorageView, typing.Dict[builtins.str, typing.Any]]] = None,
    tenant_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06a68589750feeb65d350ba54a786ffc318e6300dc2af852a16fbfb9796ed9f4(
    *,
    cloud_provider_config: typing.Optional[typing.Union[DataLakeCloudProviderConfigView, typing.Dict[builtins.str, typing.Any]]] = None,
    data_process_region: typing.Optional[typing.Union[DataLakeDataProcessRegionView, typing.Dict[builtins.str, typing.Any]]] = None,
    end_date: typing.Optional[jsii.Number] = None,
    profile: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    skip_role_validation: typing.Optional[builtins.bool] = None,
    storage: typing.Optional[typing.Union[DataLakeStorageView, typing.Dict[builtins.str, typing.Any]]] = None,
    tenant_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8406f4354e90478b4bbd52a6ceff6a23c4965a2fc56673977d90dbd7ab8a3a40(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    database_name: builtins.str,
    project_id: builtins.str,
    roles: typing.Sequence[typing.Union[RoleDefinition, typing.Dict[builtins.str, typing.Any]]],
    username: builtins.str,
    awsiam_type: typing.Optional[CfnDatabaseUserPropsAwsiamType] = None,
    delete_after_date: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Sequence[typing.Union[LabelDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    ldap_auth_type: typing.Optional[CfnDatabaseUserPropsLdapAuthType] = None,
    password: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    scopes: typing.Optional[typing.Sequence[typing.Union[ScopeDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    x509_type: typing.Optional[CfnDatabaseUserPropsX509Type] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b56b500507bd311917a33a9fbfa2f5edb8bae24b9fbd3dc38b4055df3f7c04c4(
    *,
    database_name: builtins.str,
    project_id: builtins.str,
    roles: typing.Sequence[typing.Union[RoleDefinition, typing.Dict[builtins.str, typing.Any]]],
    username: builtins.str,
    awsiam_type: typing.Optional[CfnDatabaseUserPropsAwsiamType] = None,
    delete_after_date: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Sequence[typing.Union[LabelDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    ldap_auth_type: typing.Optional[CfnDatabaseUserPropsLdapAuthType] = None,
    password: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    scopes: typing.Optional[typing.Sequence[typing.Union[ScopeDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    x509_type: typing.Optional[CfnDatabaseUserPropsX509Type] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c180750d8057b1363f69c973f8fccb55c27fd802c69977654436226f96f5a18(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    aws_kms: typing.Union[AwsKmsConfiguration, typing.Dict[builtins.str, typing.Any]],
    project_id: builtins.str,
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd94222cd7a5c427770775c9b15177a7efcab7ada166391b9cbe1c543d5c9b3c(
    *,
    aws_kms: typing.Union[AwsKmsConfiguration, typing.Dict[builtins.str, typing.Any]],
    project_id: builtins.str,
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f167859158100888bcb0726ac79d0893ccc2bebaebcff902410f2693dc55077(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    external_group_name: builtins.str,
    federation_settings_id: builtins.str,
    org_id: builtins.str,
    role_assignments: typing.Sequence[typing.Union[RoleAssignment, typing.Dict[builtins.str, typing.Any]]],
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c3839f13da84cc0789dea989620ab43857742ae7373d4038e286df38f05a3a1(
    *,
    external_group_name: builtins.str,
    federation_settings_id: builtins.str,
    org_id: builtins.str,
    role_assignments: typing.Sequence[typing.Union[RoleAssignment, typing.Dict[builtins.str, typing.Any]]],
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2437c69bb17314d4c89174a53a50594fb17919e17b6dc40fc3df6c906430422(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_name: builtins.str,
    project_id: builtins.str,
    custom_zone_mappings: typing.Optional[typing.Sequence[typing.Union[ZoneMapping, typing.Dict[builtins.str, typing.Any]]]] = None,
    managed_namespaces: typing.Optional[typing.Sequence[typing.Union[ManagedNamespace, typing.Dict[builtins.str, typing.Any]]]] = None,
    profile: typing.Optional[builtins.str] = None,
    remove_all_zone_mapping: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2abf09a412ab7492653aa5101a0106311ebaa3b5f1356b6df31145b1c366979f(
    *,
    cluster_name: builtins.str,
    project_id: builtins.str,
    custom_zone_mappings: typing.Optional[typing.Sequence[typing.Union[ZoneMapping, typing.Dict[builtins.str, typing.Any]]]] = None,
    managed_namespaces: typing.Optional[typing.Sequence[typing.Union[ManagedNamespace, typing.Dict[builtins.str, typing.Any]]]] = None,
    profile: typing.Optional[builtins.str] = None,
    remove_all_zone_mapping: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64ba1f8429afaf86fe658100b8053a07f434a9162e0c336885568446454a3c23(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bind_password: builtins.str,
    bind_username: builtins.str,
    hostname: builtins.str,
    port: jsii.Number,
    project_id: builtins.str,
    authentication_enabled: typing.Optional[builtins.bool] = None,
    authorization_enabled: typing.Optional[builtins.bool] = None,
    authz_query_template: typing.Optional[builtins.str] = None,
    ca_certificate: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
    user_to_dn_mapping: typing.Optional[typing.Sequence[typing.Union[ApiAtlasNdsUserToDnMappingView, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c3cc1347bf0066c86c262b5e05f16ab053181b08277183625438baf0e95d338(
    *,
    bind_password: builtins.str,
    bind_username: builtins.str,
    hostname: builtins.str,
    port: jsii.Number,
    project_id: builtins.str,
    authentication_enabled: typing.Optional[builtins.bool] = None,
    authorization_enabled: typing.Optional[builtins.bool] = None,
    authz_query_template: typing.Optional[builtins.str] = None,
    ca_certificate: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
    user_to_dn_mapping: typing.Optional[typing.Sequence[typing.Union[ApiAtlasNdsUserToDnMappingView, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de93db0c4570397a56ad2208f6f7c27ba66fa5f7ca40ed2393a5f3c43a35dba4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bind_password: builtins.str,
    bind_username: builtins.str,
    host_name: builtins.str,
    port: jsii.Number,
    project_id: builtins.str,
    authz_query_template: typing.Optional[builtins.str] = None,
    ca_certificate: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    validations: typing.Optional[typing.Sequence[typing.Union[Validation, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bb6ed957d2c446f2c47a1acae65ef2695e9d225c57a70e5b6a16dfd1f65b1e1(
    *,
    bind_password: builtins.str,
    bind_username: builtins.str,
    host_name: builtins.str,
    port: jsii.Number,
    project_id: builtins.str,
    authz_query_template: typing.Optional[builtins.str] = None,
    ca_certificate: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    validations: typing.Optional[typing.Sequence[typing.Union[Validation, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d709ba18cbc2813f625dfc983f1b51f0464eb8649a41db43931af94a23a82a3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    hour_of_day: jsii.Number,
    auto_defer_once_enabled: typing.Optional[builtins.bool] = None,
    day_of_week: typing.Optional[jsii.Number] = None,
    profile: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    start_asap: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23b64b93b716fc5c18498400d8d433073e8609bac008d6faf8110daea0f7c05a(
    *,
    hour_of_day: jsii.Number,
    auto_defer_once_enabled: typing.Optional[builtins.bool] = None,
    day_of_week: typing.Optional[jsii.Number] = None,
    profile: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    start_asap: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c9284447403a32509edf70d5f679ba1a327089973b2567a6f61cee465c831a3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    atlas_cidr_block: builtins.str,
    project_id: builtins.str,
    region_name: builtins.str,
    profile: typing.Optional[builtins.str] = None,
    provisioned: typing.Optional[builtins.bool] = None,
    vpc_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d55f15d0316fc413650d60ddc210fc38142413a4558f6b547d6a0546f9785ce1(
    *,
    atlas_cidr_block: builtins.str,
    project_id: builtins.str,
    region_name: builtins.str,
    profile: typing.Optional[builtins.str] = None,
    provisioned: typing.Optional[builtins.bool] = None,
    vpc_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dc613947bd4db1c6d883903dd838f6dd48daf92a78cc07faa959edc47dd394d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    container_id: builtins.str,
    project_id: builtins.str,
    vpc_id: builtins.str,
    accepter_region_name: typing.Optional[builtins.str] = None,
    aws_account_id: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    route_table_cidr_block: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf187f1934d98a58159cf134a6c59635175a6c762f497b087153852b583c0a51(
    *,
    container_id: builtins.str,
    project_id: builtins.str,
    vpc_id: builtins.str,
    accepter_region_name: typing.Optional[builtins.str] = None,
    aws_account_id: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    route_table_cidr_block: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25747c28460f7bc027e8af0fd1cda9b7810bca745f7c6a7796a795d2a50eda19(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_name: builtins.str,
    criteria: typing.Union[CriteriaView, typing.Dict[builtins.str, typing.Any]],
    collection_type: typing.Optional[CfnOnlineArchivePropsCollectionType] = None,
    coll_name: typing.Optional[builtins.str] = None,
    db_name: typing.Optional[builtins.str] = None,
    include_count: typing.Optional[builtins.bool] = None,
    items_per_page: typing.Optional[jsii.Number] = None,
    page_num: typing.Optional[jsii.Number] = None,
    partition_fields: typing.Optional[typing.Sequence[typing.Union[PartitionFieldView, typing.Dict[builtins.str, typing.Any]]]] = None,
    profile: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    schedule: typing.Optional[typing.Union[ScheduleView, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dc840e142e8ce043b5b416cacb0e1a1607e1d4e5390581f081a08db637b0242(
    *,
    cluster_name: builtins.str,
    criteria: typing.Union[CriteriaView, typing.Dict[builtins.str, typing.Any]],
    collection_type: typing.Optional[CfnOnlineArchivePropsCollectionType] = None,
    coll_name: typing.Optional[builtins.str] = None,
    db_name: typing.Optional[builtins.str] = None,
    include_count: typing.Optional[builtins.bool] = None,
    items_per_page: typing.Optional[jsii.Number] = None,
    page_num: typing.Optional[jsii.Number] = None,
    partition_fields: typing.Optional[typing.Sequence[typing.Union[PartitionFieldView, typing.Dict[builtins.str, typing.Any]]]] = None,
    profile: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    schedule: typing.Optional[typing.Union[ScheduleView, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b8ff8ce5f7a7ea00a66d0e978debe840bc4cbeceff0ce4d149b9417f22787a6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    profile: builtins.str,
    include_count: typing.Optional[builtins.bool] = None,
    invitation_id: typing.Optional[builtins.str] = None,
    items_per_page: typing.Optional[jsii.Number] = None,
    org_id: typing.Optional[builtins.str] = None,
    org_name: typing.Optional[builtins.str] = None,
    page_num: typing.Optional[jsii.Number] = None,
    roles: typing.Optional[typing.Sequence[CfnOrgInvitationPropsRoles]] = None,
    team_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    total_count: typing.Optional[jsii.Number] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4debf5f8d3f86c022ce01796305d032e187d832088fee5bd7ccb6a59205e58c8(
    *,
    profile: builtins.str,
    include_count: typing.Optional[builtins.bool] = None,
    invitation_id: typing.Optional[builtins.str] = None,
    items_per_page: typing.Optional[jsii.Number] = None,
    org_id: typing.Optional[builtins.str] = None,
    org_name: typing.Optional[builtins.str] = None,
    page_num: typing.Optional[jsii.Number] = None,
    roles: typing.Optional[typing.Sequence[CfnOrgInvitationPropsRoles]] = None,
    team_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    total_count: typing.Optional[jsii.Number] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd290a53b40e29a12f462b44c95c57ad20233cd8ec27bdbdc1fc106d01113bbb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    project_id: builtins.str,
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5ff57abc06e2b5595ea609b4ae3ea8224a750d84b0f1dca9ec5bdfa5d2d0a73(
    *,
    project_id: builtins.str,
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0dbda165f7b651d611d7156024f4f600cbf49239fe921d963641818d1bf4c19(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    group_id: builtins.str,
    region: builtins.str,
    endpoint_service_name: typing.Optional[builtins.str] = None,
    error_message: typing.Optional[builtins.str] = None,
    private_endpoints: typing.Optional[typing.Sequence[typing.Union[PrivateEndpoint, typing.Dict[builtins.str, typing.Any]]]] = None,
    profile: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93ffa99fc434f910a3dc07e98db360988b295acaf9b124a9debcdcb19ed5e568(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    project_id: builtins.str,
    provider: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    endpoint_id: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef85df101cf97dd94f21606b0fa2a06158a450835b83d6a4b9a567769e27dfd1(
    *,
    project_id: builtins.str,
    provider: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    endpoint_id: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46573598388bf535906c153a38c5e97b0d217854095d2c6e68527125ece7cde3(
    *,
    group_id: builtins.str,
    region: builtins.str,
    endpoint_service_name: typing.Optional[builtins.str] = None,
    error_message: typing.Optional[builtins.str] = None,
    private_endpoints: typing.Optional[typing.Sequence[typing.Union[PrivateEndpoint, typing.Dict[builtins.str, typing.Any]]]] = None,
    profile: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd86e13237877e63b918eea83edf0a7eb5b7192a9299d3e126ca3b58578e33f0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    org_id: builtins.str,
    profile: typing.Optional[builtins.str] = None,
    project_api_keys: typing.Optional[typing.Sequence[typing.Union[ProjectApiKey, typing.Dict[builtins.str, typing.Any]]]] = None,
    project_settings: typing.Optional[typing.Union[ProjectSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    project_teams: typing.Optional[typing.Sequence[typing.Union[ProjectTeam, typing.Dict[builtins.str, typing.Any]]]] = None,
    with_default_alerts_settings: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90fac7f9abc853c6415068d2b1ab6b61fd76f88b72c44d45a40492dd51a31c37(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    invitation_id: typing.Optional[builtins.str] = None,
    page_num: typing.Optional[jsii.Number] = None,
    profile: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    roles: typing.Optional[typing.Sequence[CfnProjectInvitationPropsRoles]] = None,
    total_count: typing.Optional[jsii.Number] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64950b750c4efa479cd1f86be0676ebda8c896441134de0602b875ece4fa2679(
    *,
    invitation_id: typing.Optional[builtins.str] = None,
    page_num: typing.Optional[jsii.Number] = None,
    profile: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    roles: typing.Optional[typing.Sequence[CfnProjectInvitationPropsRoles]] = None,
    total_count: typing.Optional[jsii.Number] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35c78432304d8ff29b8ff635279a10a18ae86da66b463c4be35eefb2b857aff3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    project_id: builtins.str,
    access_list: typing.Optional[typing.Sequence[typing.Union[AccessListDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    list_options: typing.Optional[typing.Union[ListOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    profile: typing.Optional[builtins.str] = None,
    total_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1967529b2e1355374728ffccdc38342d901bb46d7dbb4210cd964605a1cffd6(
    *,
    project_id: builtins.str,
    access_list: typing.Optional[typing.Sequence[typing.Union[AccessListDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    list_options: typing.Optional[typing.Union[ListOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    profile: typing.Optional[builtins.str] = None,
    total_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21510fd9984fce1826e8fccc145cf4e38e8554a29c5321d2960683f3d1851daf(
    *,
    name: builtins.str,
    org_id: builtins.str,
    profile: typing.Optional[builtins.str] = None,
    project_api_keys: typing.Optional[typing.Sequence[typing.Union[ProjectApiKey, typing.Dict[builtins.str, typing.Any]]]] = None,
    project_settings: typing.Optional[typing.Union[ProjectSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    project_teams: typing.Optional[typing.Sequence[typing.Union[ProjectTeam, typing.Dict[builtins.str, typing.Any]]]] = None,
    with_default_alerts_settings: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b13164dd11ebbec9ed7c892c14e8bbeddef284fe865e7f4b3f8b6cbb00703b99(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_name: builtins.str,
    collection_name: builtins.str,
    database: builtins.str,
    mappings: typing.Union[ApiAtlasFtsMappingsViewManual, typing.Dict[builtins.str, typing.Any]],
    analyzer: typing.Optional[builtins.str] = None,
    analyzers: typing.Optional[typing.Sequence[typing.Union[ApiAtlasFtsAnalyzersViewManual, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    search_analyzer: typing.Optional[builtins.str] = None,
    synonyms: typing.Optional[typing.Sequence[typing.Union[ApiAtlasFtsSynonymMappingDefinitionView, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d4e976f5c6c5f42fe823f301f998aa27f79845058acebf22b666fb42a65238c(
    *,
    cluster_name: builtins.str,
    collection_name: builtins.str,
    database: builtins.str,
    mappings: typing.Union[ApiAtlasFtsMappingsViewManual, typing.Dict[builtins.str, typing.Any]],
    analyzer: typing.Optional[builtins.str] = None,
    analyzers: typing.Optional[typing.Sequence[typing.Union[ApiAtlasFtsAnalyzersViewManual, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    search_analyzer: typing.Optional[builtins.str] = None,
    synonyms: typing.Optional[typing.Sequence[typing.Union[ApiAtlasFtsSynonymMappingDefinitionView, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71c2fac1e4b79aeb2fe8c14ae8952822335988c0afa9fbc18ab1bec25c7cc2b5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    connection_strings: typing.Optional[typing.Union[ServerlessInstanceConnectionStrings, typing.Dict[builtins.str, typing.Any]]] = None,
    continuous_backup_enabled: typing.Optional[builtins.bool] = None,
    include_count: typing.Optional[builtins.bool] = None,
    items_per_page: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    page_num: typing.Optional[jsii.Number] = None,
    profile: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    provider_settings: typing.Optional[typing.Union[ServerlessInstanceProviderSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    termination_protection_enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d484760f72034dea11f0a7d6b1ec64440d35ec4867e3d0503e858340a4744b35(
    *,
    connection_strings: typing.Optional[typing.Union[ServerlessInstanceConnectionStrings, typing.Dict[builtins.str, typing.Any]]] = None,
    continuous_backup_enabled: typing.Optional[builtins.bool] = None,
    include_count: typing.Optional[builtins.bool] = None,
    items_per_page: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    page_num: typing.Optional[jsii.Number] = None,
    profile: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    provider_settings: typing.Optional[typing.Union[ServerlessInstanceProviderSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    termination_protection_enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf5e9c70fe6389958baf6253e0662ec2c9d33390b067c6ad31b0899588d24378(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: typing.Optional[builtins.str] = None,
    org_id: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    role_names: typing.Optional[typing.Sequence[CfnTeamsPropsRoleNames]] = None,
    usernames: typing.Optional[typing.Sequence[builtins.str]] = None,
    users: typing.Optional[typing.Sequence[typing.Union[AtlasUser, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a745e370f70f5b5f1354161322a7e239c35a2b265f58562ffb60e5564303102(
    *,
    name: typing.Optional[builtins.str] = None,
    org_id: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    role_names: typing.Optional[typing.Sequence[CfnTeamsPropsRoleNames]] = None,
    usernames: typing.Optional[typing.Sequence[builtins.str]] = None,
    users: typing.Optional[typing.Sequence[typing.Union[AtlasUser, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5130cb31b4f4c657c02dff85f9317186b660fbbaa5e5e2a99aad6ebc444b618(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_key: typing.Optional[builtins.str] = None,
    api_token: typing.Optional[builtins.str] = None,
    channel_name: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[builtins.bool] = None,
    listen_address: typing.Optional[builtins.str] = None,
    microsoft_teams_webhook_url: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    routing_key: typing.Optional[builtins.str] = None,
    scheme: typing.Optional[CfnThirdPartyIntegrationPropsScheme] = None,
    secret: typing.Optional[builtins.str] = None,
    service_discovery: typing.Optional[CfnThirdPartyIntegrationPropsServiceDiscovery] = None,
    service_key: typing.Optional[builtins.str] = None,
    team_name: typing.Optional[builtins.str] = None,
    tls_pem_path: typing.Optional[builtins.str] = None,
    type: typing.Optional[CfnThirdPartyIntegrationPropsType] = None,
    url: typing.Optional[builtins.str] = None,
    user_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be1439beaf06f53b34343a6c639a60c17b217e6a3a9b6d45d474ea3be41fa30d(
    *,
    api_key: typing.Optional[builtins.str] = None,
    api_token: typing.Optional[builtins.str] = None,
    channel_name: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[builtins.bool] = None,
    listen_address: typing.Optional[builtins.str] = None,
    microsoft_teams_webhook_url: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    routing_key: typing.Optional[builtins.str] = None,
    scheme: typing.Optional[CfnThirdPartyIntegrationPropsScheme] = None,
    secret: typing.Optional[builtins.str] = None,
    service_discovery: typing.Optional[CfnThirdPartyIntegrationPropsServiceDiscovery] = None,
    service_key: typing.Optional[builtins.str] = None,
    team_name: typing.Optional[builtins.str] = None,
    tls_pem_path: typing.Optional[builtins.str] = None,
    type: typing.Optional[CfnThirdPartyIntegrationPropsType] = None,
    url: typing.Optional[builtins.str] = None,
    user_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6bdbf471d26e0ad87a81655e01a9beddf96f71e5232ef55c13171c50b162c02(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    app_id: builtins.str,
    project_id: builtins.str,
    auth_trigger: typing.Optional[typing.Union[AuthConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    database_trigger: typing.Optional[typing.Union[DatabaseConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    disabled: typing.Optional[builtins.bool] = None,
    event_processors: typing.Optional[typing.Union[Event, typing.Dict[builtins.str, typing.Any]]] = None,
    function_id: typing.Optional[builtins.str] = None,
    function_name: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    schedule_trigger: typing.Optional[typing.Union[ScheduleConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7db6e39c2f2c99b7eb0bc2548c65b47123dfba34574ee5f34fe937ef4416aef5(
    *,
    app_id: builtins.str,
    project_id: builtins.str,
    auth_trigger: typing.Optional[typing.Union[AuthConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    database_trigger: typing.Optional[typing.Union[DatabaseConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    disabled: typing.Optional[builtins.bool] = None,
    event_processors: typing.Optional[typing.Union[Event, typing.Dict[builtins.str, typing.Any]]] = None,
    function_id: typing.Optional[builtins.str] = None,
    function_name: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    schedule_trigger: typing.Optional[typing.Union[ScheduleConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13b9b050ae1c7a9ab6d780c0f2c1a0409182aa3712dd04020715b8aef6c02048(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    customer_x509: typing.Optional[typing.Union[CustomerX509, typing.Dict[builtins.str, typing.Any]]] = None,
    months_until_expiration: typing.Optional[jsii.Number] = None,
    profile: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    total_count: typing.Optional[jsii.Number] = None,
    user_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce69c30cea79a8a0148655e04b8eb82131c7a4b60f382199c9085a21b5729936(
    *,
    customer_x509: typing.Optional[typing.Union[CustomerX509, typing.Dict[builtins.str, typing.Any]]] = None,
    months_until_expiration: typing.Optional[jsii.Number] = None,
    profile: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    total_count: typing.Optional[jsii.Number] = None,
    user_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aa8d6bf21c97655b6cbb7136f7ee1cbd527d1d9246da810f82ed4420d0456e9(
    *,
    advanced_settings: typing.Optional[typing.Union[ProcessArgs, typing.Dict[builtins.str, typing.Any]]] = None,
    backup_enabled: typing.Optional[builtins.bool] = None,
    bi_connector: typing.Optional[typing.Union[CfnClusterPropsBiConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_type: typing.Optional[builtins.str] = None,
    connection_strings: typing.Optional[typing.Union[ConnectionStrings, typing.Dict[builtins.str, typing.Any]]] = None,
    disk_size_gb: typing.Optional[jsii.Number] = None,
    encryption_at_rest_provider: typing.Optional[CfnClusterPropsEncryptionAtRestProvider] = None,
    labels: typing.Optional[typing.Sequence[typing.Union[CfnClusterPropsLabels, typing.Dict[builtins.str, typing.Any]]]] = None,
    mongo_db_major_version: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    paused: typing.Optional[builtins.bool] = None,
    pit_enabled: typing.Optional[builtins.bool] = None,
    project_id: typing.Optional[builtins.str] = None,
    replication_specs: typing.Optional[typing.Sequence[typing.Union[AdvancedReplicationSpec, typing.Dict[builtins.str, typing.Any]]]] = None,
    root_cert_type: typing.Optional[builtins.str] = None,
    termination_protection_enabled: typing.Optional[builtins.bool] = None,
    version_release_system: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fc92953d030e14f8e475637fe710ef24fa4306fc84ca82ab7017b88af8b5076(
    *,
    enabled: typing.Optional[builtins.bool] = None,
    max_instance_size: typing.Optional[builtins.str] = None,
    min_instance_size: typing.Optional[builtins.str] = None,
    scale_down_enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__597338f96c3a4d62d6939ce0f092a5160cae79412897f58a15ddfb72d6f47d80(
    *,
    aws_private_link: typing.Optional[builtins.str] = None,
    aws_private_link_srv: typing.Optional[builtins.str] = None,
    private: typing.Optional[builtins.str] = None,
    private_endpoint: typing.Optional[typing.Sequence[typing.Union[PrivateEndpoint, typing.Dict[builtins.str, typing.Any]]]] = None,
    private_srv: typing.Optional[builtins.str] = None,
    standard: typing.Optional[builtins.str] = None,
    standard_srv: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9178a762a9d17a97c4394e06788cc6c7cefffda2394f9af1cc3375a2f0e0cedf(
    *,
    date_field: typing.Optional[builtins.str] = None,
    date_format: typing.Optional[CriteriaViewDateFormat] = None,
    expire_after_days: typing.Optional[jsii.Number] = None,
    query: typing.Optional[builtins.str] = None,
    type: typing.Optional[CriteriaViewType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8955783ba140d2d218b792195af3b8f839d43594be8ad7cb1b77dd1d80fc1fcf(
    *,
    cas: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64dae4bb023041c371e115c80ad9c19c45f3d9fe02e856c6300a224b0db099d9(
    *,
    external_id: typing.Optional[builtins.str] = None,
    iam_assumed_role_arn: typing.Optional[builtins.str] = None,
    iam_user_arn: typing.Optional[builtins.str] = None,
    role_id: typing.Optional[builtins.str] = None,
    test_s3_bucket: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7917368b756c11887541463887ec1b21b43fa1fe5cab7730a08caf1a0da47cd6(
    *,
    aws: typing.Optional[typing.Union[DataLakeAwsCloudProviderConfigView, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__446e9a05d8da528c995e54b7696432dabaf21c2c6d09fa3a6638fdafcbe9f7f3(
    *,
    cloud_provider: typing.Optional[DataLakeDataProcessRegionViewCloudProvider] = None,
    region: typing.Optional[DataLakeDataProcessRegionViewRegion] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b48e2673acdeedad71f44b9523bd52f699c40277e2249f516c67ce3085455630(
    *,
    data_sources: typing.Optional[typing.Sequence[typing.Union[DataLakeDatabaseDataSourceView, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dc74245ff120308aa3a02abf2de5307f8184271fca6b0b9ab5930c7d926163b(
    *,
    allow_insecure: typing.Optional[builtins.bool] = None,
    collection: typing.Optional[builtins.str] = None,
    collection_regex: typing.Optional[builtins.str] = None,
    database: typing.Optional[builtins.str] = None,
    default_format: typing.Optional[DataLakeDatabaseDataSourceViewDefaultFormat] = None,
    path: typing.Optional[builtins.str] = None,
    store_name: typing.Optional[builtins.str] = None,
    urls: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb7c74972eb221456a5310f41795e50b4a9f95119db53ad880587aaa365a5c70(
    *,
    collections: typing.Optional[typing.Sequence[typing.Union[DataLakeDatabaseCollectionView, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_wildcard_collections: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    views: typing.Optional[typing.Sequence[typing.Union[DataLakeViewView, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__491fe317a24ece5d6ac226c05284632fcbce71ac270d33bd6c7e52adeeeabed7(
    *,
    databases: typing.Optional[typing.Sequence[typing.Union[DataLakeDatabaseView, typing.Dict[builtins.str, typing.Any]]]] = None,
    stores: typing.Optional[typing.Sequence[typing.Union[StoreDetail, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b23815afaae89643b0bf0689d6cd80752628bf73c49a1f2bd336360124c40886(
    *,
    name: typing.Optional[builtins.str] = None,
    pipeline: typing.Optional[builtins.str] = None,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c596fa3d50439f8375e9aa957e6ae339cc4ef295e632b62bcd5147d6a908f38d(
    *,
    collection: typing.Optional[builtins.str] = None,
    database: typing.Optional[builtins.str] = None,
    full_document: typing.Optional[builtins.bool] = None,
    full_document_before_change: typing.Optional[builtins.bool] = None,
    match: typing.Optional[builtins.str] = None,
    operation_types: typing.Optional[typing.Sequence[DatabaseConfigOperationTypes]] = None,
    project: typing.Optional[builtins.str] = None,
    service_id: typing.Optional[builtins.str] = None,
    skip_catchup_events: typing.Optional[builtins.bool] = None,
    tolerate_resume_errors: typing.Optional[builtins.bool] = None,
    unordered: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f89b9e37c1287f462039a624c6fa1c72740a2fa064ed0647aea56514a661a69(
    *,
    awsiam_type: typing.Optional[CfnDatabaseUserPropsAwsiamType] = None,
    database_name: typing.Optional[builtins.str] = None,
    delete_after_date: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Sequence[typing.Union[LabelDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    ldap_auth_type: typing.Optional[CfnDatabaseUserPropsLdapAuthType] = None,
    password: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    roles: typing.Optional[typing.Sequence[typing.Union[RoleDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    scopes: typing.Optional[typing.Sequence[typing.Union[ScopeDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    username: typing.Optional[builtins.str] = None,
    x509_type: typing.Optional[CfnDatabaseUserPropsX509Type] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56eba705c7c584194b1cc1f13195601f403c2566fc48adba8efd0fdd059a6dfd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_key: builtins.str,
    region: DatadogRegion,
    project_id: builtins.str,
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10fcd199c44bba3157e152dd42a416da985ab6b1b0cc94062bd34e86ef8e4a85(
    *,
    enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__253978e3e3456c45cbc4a9c6cf2c9245ed80da206221d014db914b2702a7574b(
    *,
    customer_master_key_id: builtins.str,
    role_id: builtins.str,
    enabled_encryption_at_rest: typing.Optional[builtins.bool] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccae3eff9124ff17212ad0fbcb5515d1b4300cc0911df3d2086c1774127cdd03(
    *,
    endpoint_id: typing.Optional[builtins.str] = None,
    provider_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0dc245443948b2ecc2b90f9696d91c16d5b80819be3878518bc91675db9ea50(
    *,
    awseventbridge: typing.Optional[typing.Union[EventAwseventbridge, typing.Dict[builtins.str, typing.Any]]] = None,
    function: typing.Optional[typing.Union[EventFunction, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccb20a14bea734882010cbf52775743642365eeb4a04d7727b7f9bc8eabf5341(
    *,
    aws_config: typing.Optional[typing.Union[EventAwseventbridgeAwsConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__171cb758e4fd8eadf647fb131f3f029d40f7d0aca69e5223c23803a0bc1000a8(
    *,
    account_id: typing.Optional[builtins.str] = None,
    extended_json_enabled: typing.Optional[builtins.bool] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29a68d656e22e4e69d8e52f1162ca3bacb251ab920f753a5799d04e6c2aed37a(
    *,
    func_config: typing.Optional[typing.Union[EventFunctionFuncConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c938d24f56144895cdf1463b758f168301b2c657fd5bc09eda286bde4135f38(
    *,
    function_id: typing.Optional[builtins.str] = None,
    function_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7332b18961cc042f9a0c566841cf2685eece9e1b8ac11fa81944688826e6a42f(
    *,
    export_bucket_id: typing.Optional[builtins.str] = None,
    frequency_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffb58f5e14a6c6202ae6a247485c1a771bdbcf4faf4f5127281018096ec7ea7e(
    *,
    db: typing.Optional[builtins.str] = None,
    role: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce5e7db4624f7765b99e64e51ce61c9491658bd0e6e96f4dfa31f550e4d3e43b(
    *,
    operator: typing.Optional[IntegerThresholdViewOperator] = None,
    threshold: typing.Optional[jsii.Number] = None,
    units: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f7d63d578a57067631a2a1db8a32af1ddfa54c5ea6ddeb8a83d8fccd180b69a(
    *,
    access_list: typing.Sequence[typing.Union[AccessListDefinition, typing.Dict[builtins.str, typing.Any]]],
    list_options: typing.Optional[typing.Union[ListOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    project_id: typing.Optional[builtins.str] = None,
    total_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8c031af21c2cdb4b9e1a18fd37d89f994af7a0789480328d6defe09a75e8ce6(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c52915f0b0cda2d2fc193f5a02edc121c5cddb3ed21a4241f3cbabffec1b4ced(
    *,
    href: typing.Optional[builtins.str] = None,
    rel: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37f570e907501747a6f0a9537110ff2c160b28ece28a9bc456a39b023474ec39(
    *,
    include_count: typing.Optional[builtins.bool] = None,
    items_per_page: typing.Optional[jsii.Number] = None,
    page_num: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54680a11e9c3c9531eb236189cac739387e25736004725511d1445883cc1f274(
    *,
    collection: typing.Optional[builtins.str] = None,
    custom_shard_key: typing.Optional[builtins.str] = None,
    db: typing.Optional[builtins.str] = None,
    is_custom_shard_key_hashed: typing.Optional[builtins.bool] = None,
    is_shard_key_unique: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32b2259b94ea91c87f55ce869b3a735b3844213b5d13c282ad53f024b95395ab(
    *,
    field_name: typing.Optional[MatcherFieldName] = None,
    operator: typing.Optional[MatcherOperator] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c291ccce2257cf6fd490c747b0093b22db3ae35f9b19ed83014f2205fbeee58(
    *,
    metric_name: typing.Optional[builtins.str] = None,
    mode: typing.Optional[MetricThresholdViewMode] = None,
    operator: typing.Optional[MetricThresholdViewOperator] = None,
    threshold: typing.Optional[jsii.Number] = None,
    units: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73e18f91e94120d8c86aeb405540116b113fb0abc1dee76b3bd19a5a1046ecb3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    microsoft_teams_webhook_url: builtins.str,
    project_id: builtins.str,
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18ce630edcb8981a87f2402df2cecd72fb5a7a174629deea172a99f905404141(
    *,
    api_token: typing.Optional[builtins.str] = None,
    channel_name: typing.Optional[builtins.str] = None,
    datadog_api_key: typing.Optional[builtins.str] = None,
    datadog_region: typing.Optional[NotificationViewDatadogRegion] = None,
    delay_min: typing.Optional[jsii.Number] = None,
    email_address: typing.Optional[builtins.str] = None,
    email_enabled: typing.Optional[builtins.bool] = None,
    flowdock_api_token: typing.Optional[builtins.str] = None,
    flow_name: typing.Optional[builtins.str] = None,
    interval_min: typing.Optional[jsii.Number] = None,
    microsoft_teams_webhook_url: typing.Optional[builtins.str] = None,
    mobile_number: typing.Optional[builtins.str] = None,
    notification_token: typing.Optional[builtins.str] = None,
    ops_genie_api_key: typing.Optional[builtins.str] = None,
    ops_genie_region: typing.Optional[NotificationViewOpsGenieRegion] = None,
    org_name: typing.Optional[builtins.str] = None,
    roles: typing.Optional[typing.Sequence[NotificationViewRoles]] = None,
    room_name: typing.Optional[builtins.str] = None,
    service_key: typing.Optional[builtins.str] = None,
    severity: typing.Optional[NotificationViewSeverity] = None,
    sms_enabled: typing.Optional[builtins.bool] = None,
    team_id: typing.Optional[builtins.str] = None,
    team_name: typing.Optional[builtins.str] = None,
    type_name: typing.Optional[NotificationViewTypeName] = None,
    username: typing.Optional[builtins.str] = None,
    victor_ops_api_key: typing.Optional[builtins.str] = None,
    victor_ops_routing_key: typing.Optional[builtins.str] = None,
    webhook_secret: typing.Optional[builtins.str] = None,
    webhook_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0947dfb5400d003085185a98017709c7ac8199d73096c8b71a8790a3a95f7d61(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    region: PagerDutyRegion,
    service_key: builtins.str,
    project_id: builtins.str,
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8e23aeb1d228b2b98874cd221e4205b7c6c6bafcff0c2c2340206323db86463(
    *,
    field_name: typing.Optional[builtins.str] = None,
    field_type: typing.Optional[PartitionFieldViewFieldType] = None,
    order: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe378b6ecf361d53088f4dcb74bbbd22a1efc46e97cfe68ce0de004545a34cdb(
    *,
    atlas_private_endpoint_status: typing.Optional[builtins.str] = None,
    aws_private_endpoint_status: typing.Optional[builtins.str] = None,
    interface_endpoint_id: typing.Optional[builtins.str] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    vpc_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb5c702819b6ee32bef8ed1262e84c3dec760c7a2e7bfeaef3fffcc5819b070c(
    *,
    endpoint_service_name: typing.Optional[builtins.str] = None,
    error_message: typing.Optional[builtins.str] = None,
    group_id: typing.Optional[builtins.str] = None,
    private_endpoints: typing.Optional[typing.Sequence[typing.Union[PrivateEndpoint, typing.Dict[builtins.str, typing.Any]]]] = None,
    region: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27eeb5507fb2bc60736ccb27da8ac7a1b3ab43c84cb503f6d94a89b50115f391(
    *,
    default_read_concern: typing.Optional[builtins.str] = None,
    default_write_concern: typing.Optional[builtins.str] = None,
    fail_index_key_too_long: typing.Optional[builtins.bool] = None,
    javascript_enabled: typing.Optional[builtins.bool] = None,
    minimum_enabled_tls_protocol: typing.Optional[builtins.str] = None,
    no_table_scan: typing.Optional[builtins.bool] = None,
    oplog_min_retention_hours: typing.Optional[jsii.Number] = None,
    oplog_size_mb: typing.Optional[jsii.Number] = None,
    sample_refresh_interval_bi_connector: typing.Optional[jsii.Number] = None,
    sample_size_bi_connector: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91daed197f501b7fd9f92d1d7731074280b321ae722ebf63b85a29b93b007a1c(
    *,
    key: typing.Optional[builtins.str] = None,
    role_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18cb6c98d5bad22aef897af56a5ba523c7eb8616b58bf4c75bb719ac53e1b889(
    *,
    org_id: builtins.str,
    cluster_count: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    project_api_keys: typing.Optional[typing.Sequence[typing.Union[ProjectApiKey, typing.Dict[builtins.str, typing.Any]]]] = None,
    project_owner_id: typing.Optional[builtins.str] = None,
    project_settings: typing.Optional[typing.Union[ProjectSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    project_teams: typing.Optional[typing.Sequence[typing.Union[ProjectTeam, typing.Dict[builtins.str, typing.Any]]]] = None,
    with_default_alerts_settings: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__507a4ab615a966f162caf3cbd9e8cb3a69fdb875a77c88eb53283cdb14bc7784(
    *,
    is_collect_database_specifics_statistics_enabled: typing.Optional[builtins.bool] = None,
    is_data_explorer_enabled: typing.Optional[builtins.bool] = None,
    is_performance_advisor_enabled: typing.Optional[builtins.bool] = None,
    is_realtime_performance_panel_enabled: typing.Optional[builtins.bool] = None,
    is_schema_advisor_enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82fae69953a2a39be1284fe9158aeef8885c67726b3e35cdec3e8819d704fd32(
    *,
    role_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    team_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cda0ca68d66524a23a9186fd3afdf8b3d7b4ce9c02ceb5f2ca293f0ab24b268(
    *,
    cluster: typing.Optional[builtins.bool] = None,
    collection: typing.Optional[builtins.str] = None,
    db: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72371f97531e42912048f6782cab67619ac5520a56a158d50a2a201f543f15a0(
    *,
    org_id: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    role: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__529daedbf89ca5908579cea08ccd15f9eafe0971359fe062d851868734b98576(
    *,
    collection_name: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    role_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__843802625c48ab9b6849df3c2e0baede76ea75e1e0b66ce231db2295f73d74ea(
    *,
    schedule: typing.Optional[builtins.str] = None,
    skipcatchup_events: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cc397c278727b04c15dbb5da033aa1b05323068a00cc34118b971ff6c456d3b(
    *,
    day_of_month: typing.Optional[jsii.Number] = None,
    day_of_week: typing.Optional[jsii.Number] = None,
    end_hour: typing.Optional[jsii.Number] = None,
    end_minute: typing.Optional[jsii.Number] = None,
    start_hour: typing.Optional[jsii.Number] = None,
    start_minute: typing.Optional[jsii.Number] = None,
    type: typing.Optional[ScheduleViewType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33863fef557cc51b9b5fdfc6e05962108c9253ac9a133d92d211b1fc2f87c2d2(
    *,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[ScopeDefinitionType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__233f155335ccb1a613f2dc06a72ed7e43a897b210fe3ae1a7f4dead54585bb74(
    *,
    private_endpoint: typing.Optional[typing.Sequence[typing.Union[ServerlessInstancePrivateEndpoint, typing.Dict[builtins.str, typing.Any]]]] = None,
    standard_srv: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__958247bcbc9a391c48d0f6a979e76086abb9df4cf214cbe24cd943d1a969e320(
    *,
    endpoints: typing.Optional[typing.Sequence[typing.Union[ServerlessInstancePrivateEndpointEndpoint, typing.Dict[builtins.str, typing.Any]]]] = None,
    srv_connection_string: typing.Optional[builtins.str] = None,
    type: typing.Optional[ServerlessInstancePrivateEndpointType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1328265175dc11efbfc92ac3a4a35f4478033611ff57e7fec38e7349829f0b41(
    *,
    endpoint_id: typing.Optional[builtins.str] = None,
    provider_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab7d13f61158c6dc5e7248221fdd372bc869a6caf5c8645c35d51293406b5159(
    *,
    provider_name: typing.Optional[ServerlessInstanceProviderSettingsProviderName] = None,
    region_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a0e995f634f6b4a5db684d55bc035ad49fb0c807c4d056a9bec5cc340be6586(
    *,
    disk_iops: typing.Optional[builtins.str] = None,
    ebs_volume_type: typing.Optional[builtins.str] = None,
    instance_size: typing.Optional[builtins.str] = None,
    node_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c786ec57c01cbb004c6105896c011b0442b0121ff8242974eb84b31be51ec6cd(
    *,
    additional_storage_classes: typing.Optional[typing.Sequence[builtins.str]] = None,
    bucket: typing.Optional[builtins.str] = None,
    delimiter: typing.Optional[builtins.str] = None,
    include_tags: typing.Optional[builtins.bool] = None,
    name: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    provider: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caccb6c960fb58719d52b223ea81a5b4f4b7cfb6e41288f8025edce4c0d7c3aa(
    *,
    collection: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b529551b78555a8abecb5e698997ab77e6f3c865015e596f955c11e12409591(
    *,
    project_id: builtins.str,
    profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d90b6dd072abd6b2ff8aea1f6c2d2169b6043cbd8ebfdf520e7efc188ffa6aff(
    *,
    status: typing.Optional[builtins.str] = None,
    validation_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6220d1f1292858228949b538159452b8c6e9c242f0500cfa563a3ef797422db(
    *,
    location: typing.Optional[builtins.str] = None,
    zone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f0086ecfd7718566112a61f855200362f4316843413bc562863c61bd119d214(
    *,
    project_id: builtins.str,
    profile: typing.Optional[builtins.str] = None,
    api_key: builtins.str,
    region: DatadogRegion,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2e1d02ed702d6a87cf81eea5c1c4c38f0803f055ba815185a186c1ceb6ed43e(
    *,
    project_id: builtins.str,
    profile: typing.Optional[builtins.str] = None,
    microsoft_teams_webhook_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c69e232e879d6582d1ac91e602aa14f79651fcdc4133ebecbb500a99afaa426e(
    *,
    project_id: builtins.str,
    profile: typing.Optional[builtins.str] = None,
    region: PagerDutyRegion,
    service_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
