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

__all__ = ['LogSearchArgs', 'LogSearch']

@pulumi.input_type
class LogSearchArgs:
    def __init__(__self__, *,
                 parent_id: pulumi.Input[str],
                 query_string: pulumi.Input[str],
                 time_range: pulumi.Input['LogSearchTimeRangeArgs'],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parsing_mode: Optional[pulumi.Input[str]] = None,
                 query_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['LogSearchQueryParameterArgs']]]] = None,
                 run_by_receipt_time: Optional[pulumi.Input[bool]] = None,
                 schedule: Optional[pulumi.Input['LogSearchScheduleArgs']] = None):
        """
        The set of arguments for constructing a LogSearch resource.
        :param pulumi.Input[str] parent_id: The identifier of the folder to create the log search in.
        :param pulumi.Input[str] query_string: Log query to perform.
        :param pulumi.Input['LogSearchTimeRangeArgs'] time_range: Time range of the log search. See time range schema
        :param pulumi.Input[str] description: Description of the search.
        :param pulumi.Input[str] name: Name of the search.
        :param pulumi.Input[str] parsing_mode: Define the parsing mode to scan the JSON format log messages. Possible values are:
               `AutoParse` and  `Manual`. Default value is `Manual`.
               
               In `AutoParse` mode, the system automatically figures out fields to parse based on the search query. While in
               the `Manual` mode, no fields are parsed out automatically. For more information see
               [Dynamic Parsing](https://help.sumologic.com/?cid=0011).
        :param pulumi.Input[bool] run_by_receipt_time: This has the value `true` if the search is to be run by receipt time and
               `false` if it is to be run by message time. Default value is `false`.
        :param pulumi.Input['LogSearchScheduleArgs'] schedule: Schedule of the log search. See schedule schema
        """
        pulumi.set(__self__, "parent_id", parent_id)
        pulumi.set(__self__, "query_string", query_string)
        pulumi.set(__self__, "time_range", time_range)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parsing_mode is not None:
            pulumi.set(__self__, "parsing_mode", parsing_mode)
        if query_parameters is not None:
            pulumi.set(__self__, "query_parameters", query_parameters)
        if run_by_receipt_time is not None:
            pulumi.set(__self__, "run_by_receipt_time", run_by_receipt_time)
        if schedule is not None:
            pulumi.set(__self__, "schedule", schedule)

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> pulumi.Input[str]:
        """
        The identifier of the folder to create the log search in.
        """
        return pulumi.get(self, "parent_id")

    @parent_id.setter
    def parent_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "parent_id", value)

    @property
    @pulumi.getter(name="queryString")
    def query_string(self) -> pulumi.Input[str]:
        """
        Log query to perform.
        """
        return pulumi.get(self, "query_string")

    @query_string.setter
    def query_string(self, value: pulumi.Input[str]):
        pulumi.set(self, "query_string", value)

    @property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> pulumi.Input['LogSearchTimeRangeArgs']:
        """
        Time range of the log search. See time range schema
        """
        return pulumi.get(self, "time_range")

    @time_range.setter
    def time_range(self, value: pulumi.Input['LogSearchTimeRangeArgs']):
        pulumi.set(self, "time_range", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the search.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the search.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="parsingMode")
    def parsing_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Define the parsing mode to scan the JSON format log messages. Possible values are:
        `AutoParse` and  `Manual`. Default value is `Manual`.

        In `AutoParse` mode, the system automatically figures out fields to parse based on the search query. While in
        the `Manual` mode, no fields are parsed out automatically. For more information see
        [Dynamic Parsing](https://help.sumologic.com/?cid=0011).
        """
        return pulumi.get(self, "parsing_mode")

    @parsing_mode.setter
    def parsing_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parsing_mode", value)

    @property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LogSearchQueryParameterArgs']]]]:
        return pulumi.get(self, "query_parameters")

    @query_parameters.setter
    def query_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LogSearchQueryParameterArgs']]]]):
        pulumi.set(self, "query_parameters", value)

    @property
    @pulumi.getter(name="runByReceiptTime")
    def run_by_receipt_time(self) -> Optional[pulumi.Input[bool]]:
        """
        This has the value `true` if the search is to be run by receipt time and
        `false` if it is to be run by message time. Default value is `false`.
        """
        return pulumi.get(self, "run_by_receipt_time")

    @run_by_receipt_time.setter
    def run_by_receipt_time(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "run_by_receipt_time", value)

    @property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input['LogSearchScheduleArgs']]:
        """
        Schedule of the log search. See schedule schema
        """
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input['LogSearchScheduleArgs']]):
        pulumi.set(self, "schedule", value)


@pulumi.input_type
class _LogSearchState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 parsing_mode: Optional[pulumi.Input[str]] = None,
                 query_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['LogSearchQueryParameterArgs']]]] = None,
                 query_string: Optional[pulumi.Input[str]] = None,
                 run_by_receipt_time: Optional[pulumi.Input[bool]] = None,
                 schedule: Optional[pulumi.Input['LogSearchScheduleArgs']] = None,
                 time_range: Optional[pulumi.Input['LogSearchTimeRangeArgs']] = None):
        """
        Input properties used for looking up and filtering LogSearch resources.
        :param pulumi.Input[str] description: Description of the search.
        :param pulumi.Input[str] name: Name of the search.
        :param pulumi.Input[str] parent_id: The identifier of the folder to create the log search in.
        :param pulumi.Input[str] parsing_mode: Define the parsing mode to scan the JSON format log messages. Possible values are:
               `AutoParse` and  `Manual`. Default value is `Manual`.
               
               In `AutoParse` mode, the system automatically figures out fields to parse based on the search query. While in
               the `Manual` mode, no fields are parsed out automatically. For more information see
               [Dynamic Parsing](https://help.sumologic.com/?cid=0011).
        :param pulumi.Input[str] query_string: Log query to perform.
        :param pulumi.Input[bool] run_by_receipt_time: This has the value `true` if the search is to be run by receipt time and
               `false` if it is to be run by message time. Default value is `false`.
        :param pulumi.Input['LogSearchScheduleArgs'] schedule: Schedule of the log search. See schedule schema
        :param pulumi.Input['LogSearchTimeRangeArgs'] time_range: Time range of the log search. See time range schema
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parent_id is not None:
            pulumi.set(__self__, "parent_id", parent_id)
        if parsing_mode is not None:
            pulumi.set(__self__, "parsing_mode", parsing_mode)
        if query_parameters is not None:
            pulumi.set(__self__, "query_parameters", query_parameters)
        if query_string is not None:
            pulumi.set(__self__, "query_string", query_string)
        if run_by_receipt_time is not None:
            pulumi.set(__self__, "run_by_receipt_time", run_by_receipt_time)
        if schedule is not None:
            pulumi.set(__self__, "schedule", schedule)
        if time_range is not None:
            pulumi.set(__self__, "time_range", time_range)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the search.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the search.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the folder to create the log search in.
        """
        return pulumi.get(self, "parent_id")

    @parent_id.setter
    def parent_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_id", value)

    @property
    @pulumi.getter(name="parsingMode")
    def parsing_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Define the parsing mode to scan the JSON format log messages. Possible values are:
        `AutoParse` and  `Manual`. Default value is `Manual`.

        In `AutoParse` mode, the system automatically figures out fields to parse based on the search query. While in
        the `Manual` mode, no fields are parsed out automatically. For more information see
        [Dynamic Parsing](https://help.sumologic.com/?cid=0011).
        """
        return pulumi.get(self, "parsing_mode")

    @parsing_mode.setter
    def parsing_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parsing_mode", value)

    @property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LogSearchQueryParameterArgs']]]]:
        return pulumi.get(self, "query_parameters")

    @query_parameters.setter
    def query_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LogSearchQueryParameterArgs']]]]):
        pulumi.set(self, "query_parameters", value)

    @property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[pulumi.Input[str]]:
        """
        Log query to perform.
        """
        return pulumi.get(self, "query_string")

    @query_string.setter
    def query_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "query_string", value)

    @property
    @pulumi.getter(name="runByReceiptTime")
    def run_by_receipt_time(self) -> Optional[pulumi.Input[bool]]:
        """
        This has the value `true` if the search is to be run by receipt time and
        `false` if it is to be run by message time. Default value is `false`.
        """
        return pulumi.get(self, "run_by_receipt_time")

    @run_by_receipt_time.setter
    def run_by_receipt_time(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "run_by_receipt_time", value)

    @property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input['LogSearchScheduleArgs']]:
        """
        Schedule of the log search. See schedule schema
        """
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input['LogSearchScheduleArgs']]):
        pulumi.set(self, "schedule", value)

    @property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> Optional[pulumi.Input['LogSearchTimeRangeArgs']]:
        """
        Time range of the log search. See time range schema
        """
        return pulumi.get(self, "time_range")

    @time_range.setter
    def time_range(self, value: Optional[pulumi.Input['LogSearchTimeRangeArgs']]):
        pulumi.set(self, "time_range", value)


class LogSearch(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 parsing_mode: Optional[pulumi.Input[str]] = None,
                 query_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LogSearchQueryParameterArgs']]]]] = None,
                 query_string: Optional[pulumi.Input[str]] = None,
                 run_by_receipt_time: Optional[pulumi.Input[bool]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['LogSearchScheduleArgs']]] = None,
                 time_range: Optional[pulumi.Input[pulumi.InputType['LogSearchTimeRangeArgs']]] = None,
                 __props__=None):
        """
        Provides a Sumologic Log Search.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        personal_folder = sumologic.get_personal_folder()
        example_log_search = sumologic.LogSearch("exampleLogSearch",
            description="Demo search description",
            parent_id=personal_folder.id,
            query_string="_sourceCategory=api error | count by _sourceHost",
            parsing_mode="AutoParse",
            run_by_receipt_time=True,
            time_range=sumologic.LogSearchTimeRangeArgs(
                begin_bounded_time_range=sumologic.LogSearchTimeRangeBeginBoundedTimeRangeArgs(
                    from_=sumologic.LogSearchTimeRangeBeginBoundedTimeRangeFromArgs(
                        relative_time_range=sumologic.LogSearchTimeRangeBeginBoundedTimeRangeFromRelativeTimeRangeArgs(
                            relative_time="-30m",
                        ),
                    ),
                ),
            ),
            schedule=sumologic.LogSearchScheduleArgs(
                cron_expression="0 0 * * * ? *",
                mute_error_emails=False,
                notification=sumologic.LogSearchScheduleNotificationArgs(
                    email_search_notification=sumologic.LogSearchScheduleNotificationEmailSearchNotificationArgs(
                        include_csv_attachment=False,
                        include_histogram=False,
                        include_query=True,
                        include_result_set=True,
                        subject_template="Search Alert: {{TriggerCondition}} found for {{SearchName}}",
                        to_lists=["will@acme.com"],
                    ),
                ),
                parseable_time_range=sumologic.LogSearchScheduleParseableTimeRangeArgs(
                    begin_bounded_time_range=sumologic.LogSearchScheduleParseableTimeRangeBeginBoundedTimeRangeArgs(
                        from_=sumologic.LogSearchScheduleParseableTimeRangeBeginBoundedTimeRangeFromArgs(
                            relative_time_range=sumologic.LogSearchScheduleParseableTimeRangeBeginBoundedTimeRangeFromRelativeTimeRangeArgs(
                                relative_time="-15m",
                            ),
                        ),
                    ),
                ),
                schedule_type="1Week",
                threshold=sumologic.LogSearchScheduleThresholdArgs(
                    count=10,
                    operator="gt",
                    threshold_type="group",
                ),
                time_zone="America/Los_Angeles",
            ))
        ```
        ## Attributes reference

        In addition to all arguments above, the following attributes are exported:

        - `id` - The ID of the log search.

        ## Import

        A log search can be imported using it's identifier, e.g.hcl

        ```sh
         $ pulumi import sumologic:index/logSearch:LogSearch example_search 0000000007FFD79D
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the search.
        :param pulumi.Input[str] name: Name of the search.
        :param pulumi.Input[str] parent_id: The identifier of the folder to create the log search in.
        :param pulumi.Input[str] parsing_mode: Define the parsing mode to scan the JSON format log messages. Possible values are:
               `AutoParse` and  `Manual`. Default value is `Manual`.
               
               In `AutoParse` mode, the system automatically figures out fields to parse based on the search query. While in
               the `Manual` mode, no fields are parsed out automatically. For more information see
               [Dynamic Parsing](https://help.sumologic.com/?cid=0011).
        :param pulumi.Input[str] query_string: Log query to perform.
        :param pulumi.Input[bool] run_by_receipt_time: This has the value `true` if the search is to be run by receipt time and
               `false` if it is to be run by message time. Default value is `false`.
        :param pulumi.Input[pulumi.InputType['LogSearchScheduleArgs']] schedule: Schedule of the log search. See schedule schema
        :param pulumi.Input[pulumi.InputType['LogSearchTimeRangeArgs']] time_range: Time range of the log search. See time range schema
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LogSearchArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Sumologic Log Search.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        personal_folder = sumologic.get_personal_folder()
        example_log_search = sumologic.LogSearch("exampleLogSearch",
            description="Demo search description",
            parent_id=personal_folder.id,
            query_string="_sourceCategory=api error | count by _sourceHost",
            parsing_mode="AutoParse",
            run_by_receipt_time=True,
            time_range=sumologic.LogSearchTimeRangeArgs(
                begin_bounded_time_range=sumologic.LogSearchTimeRangeBeginBoundedTimeRangeArgs(
                    from_=sumologic.LogSearchTimeRangeBeginBoundedTimeRangeFromArgs(
                        relative_time_range=sumologic.LogSearchTimeRangeBeginBoundedTimeRangeFromRelativeTimeRangeArgs(
                            relative_time="-30m",
                        ),
                    ),
                ),
            ),
            schedule=sumologic.LogSearchScheduleArgs(
                cron_expression="0 0 * * * ? *",
                mute_error_emails=False,
                notification=sumologic.LogSearchScheduleNotificationArgs(
                    email_search_notification=sumologic.LogSearchScheduleNotificationEmailSearchNotificationArgs(
                        include_csv_attachment=False,
                        include_histogram=False,
                        include_query=True,
                        include_result_set=True,
                        subject_template="Search Alert: {{TriggerCondition}} found for {{SearchName}}",
                        to_lists=["will@acme.com"],
                    ),
                ),
                parseable_time_range=sumologic.LogSearchScheduleParseableTimeRangeArgs(
                    begin_bounded_time_range=sumologic.LogSearchScheduleParseableTimeRangeBeginBoundedTimeRangeArgs(
                        from_=sumologic.LogSearchScheduleParseableTimeRangeBeginBoundedTimeRangeFromArgs(
                            relative_time_range=sumologic.LogSearchScheduleParseableTimeRangeBeginBoundedTimeRangeFromRelativeTimeRangeArgs(
                                relative_time="-15m",
                            ),
                        ),
                    ),
                ),
                schedule_type="1Week",
                threshold=sumologic.LogSearchScheduleThresholdArgs(
                    count=10,
                    operator="gt",
                    threshold_type="group",
                ),
                time_zone="America/Los_Angeles",
            ))
        ```
        ## Attributes reference

        In addition to all arguments above, the following attributes are exported:

        - `id` - The ID of the log search.

        ## Import

        A log search can be imported using it's identifier, e.g.hcl

        ```sh
         $ pulumi import sumologic:index/logSearch:LogSearch example_search 0000000007FFD79D
        ```

        :param str resource_name: The name of the resource.
        :param LogSearchArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LogSearchArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 parsing_mode: Optional[pulumi.Input[str]] = None,
                 query_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LogSearchQueryParameterArgs']]]]] = None,
                 query_string: Optional[pulumi.Input[str]] = None,
                 run_by_receipt_time: Optional[pulumi.Input[bool]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['LogSearchScheduleArgs']]] = None,
                 time_range: Optional[pulumi.Input[pulumi.InputType['LogSearchTimeRangeArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LogSearchArgs.__new__(LogSearchArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if parent_id is None and not opts.urn:
                raise TypeError("Missing required property 'parent_id'")
            __props__.__dict__["parent_id"] = parent_id
            __props__.__dict__["parsing_mode"] = parsing_mode
            __props__.__dict__["query_parameters"] = query_parameters
            if query_string is None and not opts.urn:
                raise TypeError("Missing required property 'query_string'")
            __props__.__dict__["query_string"] = query_string
            __props__.__dict__["run_by_receipt_time"] = run_by_receipt_time
            __props__.__dict__["schedule"] = schedule
            if time_range is None and not opts.urn:
                raise TypeError("Missing required property 'time_range'")
            __props__.__dict__["time_range"] = time_range
        super(LogSearch, __self__).__init__(
            'sumologic:index/logSearch:LogSearch',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parent_id: Optional[pulumi.Input[str]] = None,
            parsing_mode: Optional[pulumi.Input[str]] = None,
            query_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LogSearchQueryParameterArgs']]]]] = None,
            query_string: Optional[pulumi.Input[str]] = None,
            run_by_receipt_time: Optional[pulumi.Input[bool]] = None,
            schedule: Optional[pulumi.Input[pulumi.InputType['LogSearchScheduleArgs']]] = None,
            time_range: Optional[pulumi.Input[pulumi.InputType['LogSearchTimeRangeArgs']]] = None) -> 'LogSearch':
        """
        Get an existing LogSearch resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the search.
        :param pulumi.Input[str] name: Name of the search.
        :param pulumi.Input[str] parent_id: The identifier of the folder to create the log search in.
        :param pulumi.Input[str] parsing_mode: Define the parsing mode to scan the JSON format log messages. Possible values are:
               `AutoParse` and  `Manual`. Default value is `Manual`.
               
               In `AutoParse` mode, the system automatically figures out fields to parse based on the search query. While in
               the `Manual` mode, no fields are parsed out automatically. For more information see
               [Dynamic Parsing](https://help.sumologic.com/?cid=0011).
        :param pulumi.Input[str] query_string: Log query to perform.
        :param pulumi.Input[bool] run_by_receipt_time: This has the value `true` if the search is to be run by receipt time and
               `false` if it is to be run by message time. Default value is `false`.
        :param pulumi.Input[pulumi.InputType['LogSearchScheduleArgs']] schedule: Schedule of the log search. See schedule schema
        :param pulumi.Input[pulumi.InputType['LogSearchTimeRangeArgs']] time_range: Time range of the log search. See time range schema
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LogSearchState.__new__(_LogSearchState)

        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["parent_id"] = parent_id
        __props__.__dict__["parsing_mode"] = parsing_mode
        __props__.__dict__["query_parameters"] = query_parameters
        __props__.__dict__["query_string"] = query_string
        __props__.__dict__["run_by_receipt_time"] = run_by_receipt_time
        __props__.__dict__["schedule"] = schedule
        __props__.__dict__["time_range"] = time_range
        return LogSearch(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the search.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the search.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> pulumi.Output[str]:
        """
        The identifier of the folder to create the log search in.
        """
        return pulumi.get(self, "parent_id")

    @property
    @pulumi.getter(name="parsingMode")
    def parsing_mode(self) -> pulumi.Output[Optional[str]]:
        """
        Define the parsing mode to scan the JSON format log messages. Possible values are:
        `AutoParse` and  `Manual`. Default value is `Manual`.

        In `AutoParse` mode, the system automatically figures out fields to parse based on the search query. While in
        the `Manual` mode, no fields are parsed out automatically. For more information see
        [Dynamic Parsing](https://help.sumologic.com/?cid=0011).
        """
        return pulumi.get(self, "parsing_mode")

    @property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> pulumi.Output[Optional[Sequence['outputs.LogSearchQueryParameter']]]:
        return pulumi.get(self, "query_parameters")

    @property
    @pulumi.getter(name="queryString")
    def query_string(self) -> pulumi.Output[str]:
        """
        Log query to perform.
        """
        return pulumi.get(self, "query_string")

    @property
    @pulumi.getter(name="runByReceiptTime")
    def run_by_receipt_time(self) -> pulumi.Output[Optional[bool]]:
        """
        This has the value `true` if the search is to be run by receipt time and
        `false` if it is to be run by message time. Default value is `false`.
        """
        return pulumi.get(self, "run_by_receipt_time")

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional['outputs.LogSearchSchedule']]:
        """
        Schedule of the log search. See schedule schema
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> pulumi.Output['outputs.LogSearchTimeRange']:
        """
        Time range of the log search. See time range schema
        """
        return pulumi.get(self, "time_range")

