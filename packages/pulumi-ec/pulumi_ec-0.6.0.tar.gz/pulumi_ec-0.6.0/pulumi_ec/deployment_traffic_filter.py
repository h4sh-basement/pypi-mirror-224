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
from ._inputs import *

__all__ = ['DeploymentTrafficFilterArgs', 'DeploymentTrafficFilter']

@pulumi.input_type
class DeploymentTrafficFilterArgs:
    def __init__(__self__, *,
                 region: pulumi.Input[str],
                 type: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 include_by_default: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentTrafficFilterRuleArgs']]]] = None):
        """
        The set of arguments for constructing a DeploymentTrafficFilter resource.
        :param pulumi.Input[str] region: Filter region, the ruleset can only be attached to deployments in the specific region
        :param pulumi.Input[str] type: Type of the ruleset. It can be `ip`, `vpce`, `azure_private_endpoint`, or `gcp_private_service_connect_endpoint`
        :param pulumi.Input[str] description: Ruleset description
        :param pulumi.Input[bool] include_by_default: Indicates that the ruleset should be automatically included in new deployments (Defaults to false)
        :param pulumi.Input[str] name: Name of the ruleset
        :param pulumi.Input[Sequence[pulumi.Input['DeploymentTrafficFilterRuleArgs']]] rules: Set of rules, which the ruleset is made of.
        """
        pulumi.set(__self__, "region", region)
        pulumi.set(__self__, "type", type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if include_by_default is not None:
            pulumi.set(__self__, "include_by_default", include_by_default)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        Filter region, the ruleset can only be attached to deployments in the specific region
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Type of the ruleset. It can be `ip`, `vpce`, `azure_private_endpoint`, or `gcp_private_service_connect_endpoint`
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Ruleset description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="includeByDefault")
    def include_by_default(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates that the ruleset should be automatically included in new deployments (Defaults to false)
        """
        return pulumi.get(self, "include_by_default")

    @include_by_default.setter
    def include_by_default(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_by_default", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the ruleset
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentTrafficFilterRuleArgs']]]]:
        """
        Set of rules, which the ruleset is made of.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentTrafficFilterRuleArgs']]]]):
        pulumi.set(self, "rules", value)


@pulumi.input_type
class _DeploymentTrafficFilterState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 include_by_default: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentTrafficFilterRuleArgs']]]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DeploymentTrafficFilter resources.
        :param pulumi.Input[str] description: Ruleset description
        :param pulumi.Input[bool] include_by_default: Indicates that the ruleset should be automatically included in new deployments (Defaults to false)
        :param pulumi.Input[str] name: Name of the ruleset
        :param pulumi.Input[str] region: Filter region, the ruleset can only be attached to deployments in the specific region
        :param pulumi.Input[Sequence[pulumi.Input['DeploymentTrafficFilterRuleArgs']]] rules: Set of rules, which the ruleset is made of.
        :param pulumi.Input[str] type: Type of the ruleset. It can be `ip`, `vpce`, `azure_private_endpoint`, or `gcp_private_service_connect_endpoint`
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if include_by_default is not None:
            pulumi.set(__self__, "include_by_default", include_by_default)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Ruleset description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="includeByDefault")
    def include_by_default(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates that the ruleset should be automatically included in new deployments (Defaults to false)
        """
        return pulumi.get(self, "include_by_default")

    @include_by_default.setter
    def include_by_default(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_by_default", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the ruleset
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Filter region, the ruleset can only be attached to deployments in the specific region
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentTrafficFilterRuleArgs']]]]:
        """
        Set of rules, which the ruleset is made of.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentTrafficFilterRuleArgs']]]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of the ruleset. It can be `ip`, `vpce`, `azure_private_endpoint`, or `gcp_private_service_connect_endpoint`
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class DeploymentTrafficFilter(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 include_by_default: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeploymentTrafficFilterRuleArgs']]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage
        ### IP based traffic filter

        ```python
        import pulumi
        import pulumi_ec as ec

        latest = ec.get_stack(version_regex="latest",
            region="us-east-1")
        example = ec.DeploymentTrafficFilter("example",
            region="us-east-1",
            type="ip",
            rules=[ec.DeploymentTrafficFilterRuleArgs(
                source="0.0.0.0/0",
            )])
        # Create an Elastic Cloud deployment
        example_minimal = ec.Deployment("exampleMinimal",
            region="us-east-1",
            version=latest.version,
            deployment_template_id="aws-io-optimized-v2",
            traffic_filters=[example.id],
            elasticsearch=ec.DeploymentElasticsearchArgs(
                hot=ec.DeploymentElasticsearchHotArgs(
                    autoscaling=ec.DeploymentElasticsearchHotAutoscalingArgs(),
                ),
            ),
            kibana=ec.DeploymentKibanaArgs())
        ```
        ### Azure Private Link traffic filter

        ```python
        import pulumi
        import pulumi_ec as ec

        region = azure_australiaeast
        latest = ec.get_stack(version_regex="latest",
            region=region)
        azure = ec.DeploymentTrafficFilter("azure",
            region=region,
            type="azure_private_endpoint",
            rules=[ec.DeploymentTrafficFilterRuleArgs(
                azure_endpoint_name="my-azure-pl",
                azure_endpoint_guid="78c64959-fd88-41cc-81ac-1cfcdb1ac32e",
            )])
        # Create an Elastic Cloud deployment
        example_minimal = ec.Deployment("exampleMinimal",
            region=region,
            version=latest.version,
            deployment_template_id="azure-io-optimized-v3",
            traffic_filters=[azure.id],
            elasticsearch=ec.DeploymentElasticsearchArgs(
                hot=ec.DeploymentElasticsearchHotArgs(
                    autoscaling=ec.DeploymentElasticsearchHotAutoscalingArgs(),
                ),
            ),
            kibana=ec.DeploymentKibanaArgs())
        ```

        ###GCP Private Service Connect traffic filter

        ```python
        import pulumi
        import pulumi_ec as ec

        region = asia_east1
        latest = ec.get_stack(version_regex="latest",
            region=region)
        gcp_psc = ec.DeploymentTrafficFilter("gcpPsc",
            region=region,
            type="gcp_private_service_connect_endpoint",
            rules=[ec.DeploymentTrafficFilterRuleArgs(
                source="18446744072646845332",
            )])
        # Create an Elastic Cloud deployment
        example_minimal = ec.Deployment("exampleMinimal",
            region=region,
            version=latest.version,
            deployment_template_id="gcp-storage-optimized",
            traffic_filters=[gcp_psc.id],
            elasticsearch=ec.DeploymentElasticsearchArgs(
                hot=ec.DeploymentElasticsearchHotArgs(
                    autoscaling=ec.DeploymentElasticsearchHotAutoscalingArgs(),
                ),
            ),
            kibana=ec.DeploymentKibanaArgs())
        ```

        ## Import

        Traffic filters can be imported using the `id`, for example

        ```sh
         $ pulumi import ec:index/deploymentTrafficFilter:DeploymentTrafficFilter name 320b7b540dfc967a7a649c18e2fce4ed
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Ruleset description
        :param pulumi.Input[bool] include_by_default: Indicates that the ruleset should be automatically included in new deployments (Defaults to false)
        :param pulumi.Input[str] name: Name of the ruleset
        :param pulumi.Input[str] region: Filter region, the ruleset can only be attached to deployments in the specific region
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeploymentTrafficFilterRuleArgs']]]] rules: Set of rules, which the ruleset is made of.
        :param pulumi.Input[str] type: Type of the ruleset. It can be `ip`, `vpce`, `azure_private_endpoint`, or `gcp_private_service_connect_endpoint`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeploymentTrafficFilterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage
        ### IP based traffic filter

        ```python
        import pulumi
        import pulumi_ec as ec

        latest = ec.get_stack(version_regex="latest",
            region="us-east-1")
        example = ec.DeploymentTrafficFilter("example",
            region="us-east-1",
            type="ip",
            rules=[ec.DeploymentTrafficFilterRuleArgs(
                source="0.0.0.0/0",
            )])
        # Create an Elastic Cloud deployment
        example_minimal = ec.Deployment("exampleMinimal",
            region="us-east-1",
            version=latest.version,
            deployment_template_id="aws-io-optimized-v2",
            traffic_filters=[example.id],
            elasticsearch=ec.DeploymentElasticsearchArgs(
                hot=ec.DeploymentElasticsearchHotArgs(
                    autoscaling=ec.DeploymentElasticsearchHotAutoscalingArgs(),
                ),
            ),
            kibana=ec.DeploymentKibanaArgs())
        ```
        ### Azure Private Link traffic filter

        ```python
        import pulumi
        import pulumi_ec as ec

        region = azure_australiaeast
        latest = ec.get_stack(version_regex="latest",
            region=region)
        azure = ec.DeploymentTrafficFilter("azure",
            region=region,
            type="azure_private_endpoint",
            rules=[ec.DeploymentTrafficFilterRuleArgs(
                azure_endpoint_name="my-azure-pl",
                azure_endpoint_guid="78c64959-fd88-41cc-81ac-1cfcdb1ac32e",
            )])
        # Create an Elastic Cloud deployment
        example_minimal = ec.Deployment("exampleMinimal",
            region=region,
            version=latest.version,
            deployment_template_id="azure-io-optimized-v3",
            traffic_filters=[azure.id],
            elasticsearch=ec.DeploymentElasticsearchArgs(
                hot=ec.DeploymentElasticsearchHotArgs(
                    autoscaling=ec.DeploymentElasticsearchHotAutoscalingArgs(),
                ),
            ),
            kibana=ec.DeploymentKibanaArgs())
        ```

        ###GCP Private Service Connect traffic filter

        ```python
        import pulumi
        import pulumi_ec as ec

        region = asia_east1
        latest = ec.get_stack(version_regex="latest",
            region=region)
        gcp_psc = ec.DeploymentTrafficFilter("gcpPsc",
            region=region,
            type="gcp_private_service_connect_endpoint",
            rules=[ec.DeploymentTrafficFilterRuleArgs(
                source="18446744072646845332",
            )])
        # Create an Elastic Cloud deployment
        example_minimal = ec.Deployment("exampleMinimal",
            region=region,
            version=latest.version,
            deployment_template_id="gcp-storage-optimized",
            traffic_filters=[gcp_psc.id],
            elasticsearch=ec.DeploymentElasticsearchArgs(
                hot=ec.DeploymentElasticsearchHotArgs(
                    autoscaling=ec.DeploymentElasticsearchHotAutoscalingArgs(),
                ),
            ),
            kibana=ec.DeploymentKibanaArgs())
        ```

        ## Import

        Traffic filters can be imported using the `id`, for example

        ```sh
         $ pulumi import ec:index/deploymentTrafficFilter:DeploymentTrafficFilter name 320b7b540dfc967a7a649c18e2fce4ed
        ```

        :param str resource_name: The name of the resource.
        :param DeploymentTrafficFilterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeploymentTrafficFilterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 include_by_default: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeploymentTrafficFilterRuleArgs']]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeploymentTrafficFilterArgs.__new__(DeploymentTrafficFilterArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["include_by_default"] = include_by_default
            __props__.__dict__["name"] = name
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            __props__.__dict__["rules"] = rules
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(DeploymentTrafficFilter, __self__).__init__(
            'ec:index/deploymentTrafficFilter:DeploymentTrafficFilter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            include_by_default: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeploymentTrafficFilterRuleArgs']]]]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'DeploymentTrafficFilter':
        """
        Get an existing DeploymentTrafficFilter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Ruleset description
        :param pulumi.Input[bool] include_by_default: Indicates that the ruleset should be automatically included in new deployments (Defaults to false)
        :param pulumi.Input[str] name: Name of the ruleset
        :param pulumi.Input[str] region: Filter region, the ruleset can only be attached to deployments in the specific region
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeploymentTrafficFilterRuleArgs']]]] rules: Set of rules, which the ruleset is made of.
        :param pulumi.Input[str] type: Type of the ruleset. It can be `ip`, `vpce`, `azure_private_endpoint`, or `gcp_private_service_connect_endpoint`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DeploymentTrafficFilterState.__new__(_DeploymentTrafficFilterState)

        __props__.__dict__["description"] = description
        __props__.__dict__["include_by_default"] = include_by_default
        __props__.__dict__["name"] = name
        __props__.__dict__["region"] = region
        __props__.__dict__["rules"] = rules
        __props__.__dict__["type"] = type
        return DeploymentTrafficFilter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Ruleset description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="includeByDefault")
    def include_by_default(self) -> pulumi.Output[bool]:
        """
        Indicates that the ruleset should be automatically included in new deployments (Defaults to false)
        """
        return pulumi.get(self, "include_by_default")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the ruleset
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        Filter region, the ruleset can only be attached to deployments in the specific region
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional[Sequence['outputs.DeploymentTrafficFilterRule']]]:
        """
        Set of rules, which the ruleset is made of.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the ruleset. It can be `ip`, `vpce`, `azure_private_endpoint`, or `gcp_private_service_connect_endpoint`
        """
        return pulumi.get(self, "type")

