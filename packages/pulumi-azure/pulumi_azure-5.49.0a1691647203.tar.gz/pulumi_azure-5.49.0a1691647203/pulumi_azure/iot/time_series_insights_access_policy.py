# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TimeSeriesInsightsAccessPolicyArgs', 'TimeSeriesInsightsAccessPolicy']

@pulumi.input_type
class TimeSeriesInsightsAccessPolicyArgs:
    def __init__(__self__, *,
                 principal_object_id: pulumi.Input[str],
                 roles: pulumi.Input[Sequence[pulumi.Input[str]]],
                 time_series_insights_environment_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TimeSeriesInsightsAccessPolicy resource.
        :param pulumi.Input[str] principal_object_id: The id of the principal in Azure Active Directory. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: A list of roles to apply to the Access Policy. Valid values include `Contributor` and `Reader`.
        :param pulumi.Input[str] time_series_insights_environment_id: The resource ID of the Azure IoT Time Series Insights Environment in which to create the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created.
        :param pulumi.Input[str] description: The description of the Azure IoT Time Series Insights Access Policy.
        :param pulumi.Input[str] name: Specifies the name of the Azure IoT Time Series Insights Access Policy. Changing this forces a new resource to be created. Must be globally unique.
        """
        pulumi.set(__self__, "principal_object_id", principal_object_id)
        pulumi.set(__self__, "roles", roles)
        pulumi.set(__self__, "time_series_insights_environment_id", time_series_insights_environment_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="principalObjectId")
    def principal_object_id(self) -> pulumi.Input[str]:
        """
        The id of the principal in Azure Active Directory. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "principal_object_id")

    @principal_object_id.setter
    def principal_object_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "principal_object_id", value)

    @property
    @pulumi.getter
    def roles(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of roles to apply to the Access Policy. Valid values include `Contributor` and `Reader`.
        """
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "roles", value)

    @property
    @pulumi.getter(name="timeSeriesInsightsEnvironmentId")
    def time_series_insights_environment_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the Azure IoT Time Series Insights Environment in which to create the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "time_series_insights_environment_id")

    @time_series_insights_environment_id.setter
    def time_series_insights_environment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "time_series_insights_environment_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Azure IoT Time Series Insights Access Policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Azure IoT Time Series Insights Access Policy. Changing this forces a new resource to be created. Must be globally unique.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _TimeSeriesInsightsAccessPolicyState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 principal_object_id: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 time_series_insights_environment_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TimeSeriesInsightsAccessPolicy resources.
        :param pulumi.Input[str] description: The description of the Azure IoT Time Series Insights Access Policy.
        :param pulumi.Input[str] name: Specifies the name of the Azure IoT Time Series Insights Access Policy. Changing this forces a new resource to be created. Must be globally unique.
        :param pulumi.Input[str] principal_object_id: The id of the principal in Azure Active Directory. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: A list of roles to apply to the Access Policy. Valid values include `Contributor` and `Reader`.
        :param pulumi.Input[str] time_series_insights_environment_id: The resource ID of the Azure IoT Time Series Insights Environment in which to create the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if principal_object_id is not None:
            pulumi.set(__self__, "principal_object_id", principal_object_id)
        if roles is not None:
            pulumi.set(__self__, "roles", roles)
        if time_series_insights_environment_id is not None:
            pulumi.set(__self__, "time_series_insights_environment_id", time_series_insights_environment_id)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Azure IoT Time Series Insights Access Policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Azure IoT Time Series Insights Access Policy. Changing this forces a new resource to be created. Must be globally unique.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="principalObjectId")
    def principal_object_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the principal in Azure Active Directory. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "principal_object_id")

    @principal_object_id.setter
    def principal_object_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_object_id", value)

    @property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of roles to apply to the Access Policy. Valid values include `Contributor` and `Reader`.
        """
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "roles", value)

    @property
    @pulumi.getter(name="timeSeriesInsightsEnvironmentId")
    def time_series_insights_environment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the Azure IoT Time Series Insights Environment in which to create the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "time_series_insights_environment_id")

    @time_series_insights_environment_id.setter
    def time_series_insights_environment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_series_insights_environment_id", value)


class TimeSeriesInsightsAccessPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 principal_object_id: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 time_series_insights_environment_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an Azure IoT Time Series Insights Access Policy.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_time_series_insights_standard_environment = azure.iot.TimeSeriesInsightsStandardEnvironment("exampleTimeSeriesInsightsStandardEnvironment",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="S1_1",
            data_retention_time="P30D")
        example_time_series_insights_access_policy = azure.iot.TimeSeriesInsightsAccessPolicy("exampleTimeSeriesInsightsAccessPolicy",
            time_series_insights_environment_id=example_time_series_insights_standard_environment.name,
            principal_object_id="aGUID",
            roles=["Reader"])
        ```

        ## Import

        Azure IoT Time Series Insights Access Policy can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:iot/timeSeriesInsightsAccessPolicy:TimeSeriesInsightsAccessPolicy example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/example/providers/Microsoft.TimeSeriesInsights/environments/environment1/accessPolicies/example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the Azure IoT Time Series Insights Access Policy.
        :param pulumi.Input[str] name: Specifies the name of the Azure IoT Time Series Insights Access Policy. Changing this forces a new resource to be created. Must be globally unique.
        :param pulumi.Input[str] principal_object_id: The id of the principal in Azure Active Directory. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: A list of roles to apply to the Access Policy. Valid values include `Contributor` and `Reader`.
        :param pulumi.Input[str] time_series_insights_environment_id: The resource ID of the Azure IoT Time Series Insights Environment in which to create the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TimeSeriesInsightsAccessPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an Azure IoT Time Series Insights Access Policy.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_time_series_insights_standard_environment = azure.iot.TimeSeriesInsightsStandardEnvironment("exampleTimeSeriesInsightsStandardEnvironment",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="S1_1",
            data_retention_time="P30D")
        example_time_series_insights_access_policy = azure.iot.TimeSeriesInsightsAccessPolicy("exampleTimeSeriesInsightsAccessPolicy",
            time_series_insights_environment_id=example_time_series_insights_standard_environment.name,
            principal_object_id="aGUID",
            roles=["Reader"])
        ```

        ## Import

        Azure IoT Time Series Insights Access Policy can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:iot/timeSeriesInsightsAccessPolicy:TimeSeriesInsightsAccessPolicy example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/example/providers/Microsoft.TimeSeriesInsights/environments/environment1/accessPolicies/example
        ```

        :param str resource_name: The name of the resource.
        :param TimeSeriesInsightsAccessPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TimeSeriesInsightsAccessPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 principal_object_id: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 time_series_insights_environment_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TimeSeriesInsightsAccessPolicyArgs.__new__(TimeSeriesInsightsAccessPolicyArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if principal_object_id is None and not opts.urn:
                raise TypeError("Missing required property 'principal_object_id'")
            __props__.__dict__["principal_object_id"] = principal_object_id
            if roles is None and not opts.urn:
                raise TypeError("Missing required property 'roles'")
            __props__.__dict__["roles"] = roles
            if time_series_insights_environment_id is None and not opts.urn:
                raise TypeError("Missing required property 'time_series_insights_environment_id'")
            __props__.__dict__["time_series_insights_environment_id"] = time_series_insights_environment_id
        super(TimeSeriesInsightsAccessPolicy, __self__).__init__(
            'azure:iot/timeSeriesInsightsAccessPolicy:TimeSeriesInsightsAccessPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            principal_object_id: Optional[pulumi.Input[str]] = None,
            roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            time_series_insights_environment_id: Optional[pulumi.Input[str]] = None) -> 'TimeSeriesInsightsAccessPolicy':
        """
        Get an existing TimeSeriesInsightsAccessPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the Azure IoT Time Series Insights Access Policy.
        :param pulumi.Input[str] name: Specifies the name of the Azure IoT Time Series Insights Access Policy. Changing this forces a new resource to be created. Must be globally unique.
        :param pulumi.Input[str] principal_object_id: The id of the principal in Azure Active Directory. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: A list of roles to apply to the Access Policy. Valid values include `Contributor` and `Reader`.
        :param pulumi.Input[str] time_series_insights_environment_id: The resource ID of the Azure IoT Time Series Insights Environment in which to create the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TimeSeriesInsightsAccessPolicyState.__new__(_TimeSeriesInsightsAccessPolicyState)

        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["principal_object_id"] = principal_object_id
        __props__.__dict__["roles"] = roles
        __props__.__dict__["time_series_insights_environment_id"] = time_series_insights_environment_id
        return TimeSeriesInsightsAccessPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the Azure IoT Time Series Insights Access Policy.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Azure IoT Time Series Insights Access Policy. Changing this forces a new resource to be created. Must be globally unique.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="principalObjectId")
    def principal_object_id(self) -> pulumi.Output[str]:
        """
        The id of the principal in Azure Active Directory. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "principal_object_id")

    @property
    @pulumi.getter
    def roles(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of roles to apply to the Access Policy. Valid values include `Contributor` and `Reader`.
        """
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter(name="timeSeriesInsightsEnvironmentId")
    def time_series_insights_environment_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the Azure IoT Time Series Insights Environment in which to create the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "time_series_insights_environment_id")

