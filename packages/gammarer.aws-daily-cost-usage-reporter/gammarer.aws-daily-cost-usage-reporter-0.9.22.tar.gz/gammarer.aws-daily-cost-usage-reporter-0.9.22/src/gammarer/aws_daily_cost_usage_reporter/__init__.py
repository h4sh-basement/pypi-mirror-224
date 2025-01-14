'''
# AWS Daily Cost Usage Reports

AWS Cost And Usage report to Slack on daily 09:01.

* Report type

  * Services

    * This is Cost by AWS Services.
  * Accounts

    * This is Cost by Linked Account (when organization master account)

## Resources

This construct creating resource list.

* Lambda function execution role
* Lambda function
* EventBridge Scheduler execution role
* EventBridge Scheduler

## Install

### TypeScript

```shell
npm install @gammarer/aws-daily-cost-usage-repoter
# or
yarn add @gammarer/aws-daily-cost-usage-repoter
```

### Python

```shell
pip install gammarer.aws-daily-cost-usage-repoter
```

## Example

```shell
npm install @gammarer/aws-daily-cost-usage-repoter
```

```python
import { CostGroupType, DailyCostUsageReporter } from '@gammarer/aws-daily-cost-usage-repoter';

new DailyCostUsageReporter(stack, 'DailyCostUsageReporter', {
  slackWebhookUrl: 'https://hooks.slack.com/services/xxxxxxxxxx', // already created slack webhook url
  slackPostChannel: 'example-channel', // already created slack channel
  costGroupType: CostGroupType.SERVICES,
});
```

## License

This project is licensed under the Apache-2.0 License.
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

import constructs as _constructs_77d1e7e8


@jsii.enum(jsii_type="@gammarer/aws-daily-cost-usage-reporter.CostGroupType")
class CostGroupType(enum.Enum):
    ACCOUNTS = "ACCOUNTS"
    SERVICES = "SERVICES"


class DailyCostUsageReporter(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@gammarer/aws-daily-cost-usage-reporter.DailyCostUsageReporter",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cost_group_type: CostGroupType,
        slack_channel: builtins.str,
        slack_token: builtins.str,
        schedule_timezone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cost_group_type: 
        :param slack_channel: 
        :param slack_token: 
        :param schedule_timezone: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4026c1864e10cf2a5cc626ef1775e773301024c66e66748ff2a4812271829d0b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DailyCostUsageReporterProps(
            cost_group_type=cost_group_type,
            slack_channel=slack_channel,
            slack_token=slack_token,
            schedule_timezone=schedule_timezone,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@gammarer/aws-daily-cost-usage-reporter.DailyCostUsageReporterProps",
    jsii_struct_bases=[],
    name_mapping={
        "cost_group_type": "costGroupType",
        "slack_channel": "slackChannel",
        "slack_token": "slackToken",
        "schedule_timezone": "scheduleTimezone",
    },
)
class DailyCostUsageReporterProps:
    def __init__(
        self,
        *,
        cost_group_type: CostGroupType,
        slack_channel: builtins.str,
        slack_token: builtins.str,
        schedule_timezone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cost_group_type: 
        :param slack_channel: 
        :param slack_token: 
        :param schedule_timezone: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a4bbf0413b61a0e37986b805b537669107f07069d965420fae79cf4d8fc275d)
            check_type(argname="argument cost_group_type", value=cost_group_type, expected_type=type_hints["cost_group_type"])
            check_type(argname="argument slack_channel", value=slack_channel, expected_type=type_hints["slack_channel"])
            check_type(argname="argument slack_token", value=slack_token, expected_type=type_hints["slack_token"])
            check_type(argname="argument schedule_timezone", value=schedule_timezone, expected_type=type_hints["schedule_timezone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cost_group_type": cost_group_type,
            "slack_channel": slack_channel,
            "slack_token": slack_token,
        }
        if schedule_timezone is not None:
            self._values["schedule_timezone"] = schedule_timezone

    @builtins.property
    def cost_group_type(self) -> CostGroupType:
        result = self._values.get("cost_group_type")
        assert result is not None, "Required property 'cost_group_type' is missing"
        return typing.cast(CostGroupType, result)

    @builtins.property
    def slack_channel(self) -> builtins.str:
        result = self._values.get("slack_channel")
        assert result is not None, "Required property 'slack_channel' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def slack_token(self) -> builtins.str:
        result = self._values.get("slack_token")
        assert result is not None, "Required property 'slack_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule_timezone(self) -> typing.Optional[builtins.str]:
        result = self._values.get("schedule_timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DailyCostUsageReporterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CostGroupType",
    "DailyCostUsageReporter",
    "DailyCostUsageReporterProps",
]

publication.publish()

def _typecheckingstub__4026c1864e10cf2a5cc626ef1775e773301024c66e66748ff2a4812271829d0b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cost_group_type: CostGroupType,
    slack_channel: builtins.str,
    slack_token: builtins.str,
    schedule_timezone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a4bbf0413b61a0e37986b805b537669107f07069d965420fae79cf4d8fc275d(
    *,
    cost_group_type: CostGroupType,
    slack_channel: builtins.str,
    slack_token: builtins.str,
    schedule_timezone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
