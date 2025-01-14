# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetRulesetResult',
    'AwaitableGetRulesetResult',
    'get_ruleset',
    'get_ruleset_output',
]

@pulumi.output_type
class GetRulesetResult:
    """
    A collection of values returned by getRuleset.
    """
    def __init__(__self__, id=None, name=None, routing_keys=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if routing_keys and not isinstance(routing_keys, list):
            raise TypeError("Expected argument 'routing_keys' to be a list")
        pulumi.set(__self__, "routing_keys", routing_keys)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the found ruleset.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="routingKeys")
    def routing_keys(self) -> Sequence[str]:
        """
        Routing keys routed to this ruleset.
        """
        return pulumi.get(self, "routing_keys")


class AwaitableGetRulesetResult(GetRulesetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRulesetResult(
            id=self.id,
            name=self.name,
            routing_keys=self.routing_keys)


def get_ruleset(name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRulesetResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_pagerduty as pagerduty

    example = pagerduty.get_ruleset(name="My Ruleset")
    foo = pagerduty.RulesetRule("foo",
        ruleset=example.id,
        position=0,
        disabled=False,
        conditions=pagerduty.RulesetRuleConditionsArgs(
            operator="and",
            subconditions=[
                pagerduty.RulesetRuleConditionsSubconditionArgs(
                    operator="contains",
                    parameters=[pagerduty.RulesetRuleConditionsSubconditionParameterArgs(
                        value="disk space",
                        path="payload.summary",
                    )],
                ),
                pagerduty.RulesetRuleConditionsSubconditionArgs(
                    operator="contains",
                    parameters=[pagerduty.RulesetRuleConditionsSubconditionParameterArgs(
                        value="db",
                        path="payload.source",
                    )],
                ),
            ],
        ),
        actions=pagerduty.RulesetRuleActionsArgs(
            routes=[pagerduty.RulesetRuleActionsRouteArgs(
                value="P5DTL0K",
            )],
        ))
    ```
    ### Default Global Ruleset

    ```python
    import pulumi
    import pulumi_pagerduty as pagerduty

    default_global = pagerduty.get_ruleset(name="Default Global")
    ```


    :param str name: The name of the ruleset to find in the PagerDuty API.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('pagerduty:index/getRuleset:getRuleset', __args__, opts=opts, typ=GetRulesetResult).value

    return AwaitableGetRulesetResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        routing_keys=pulumi.get(__ret__, 'routing_keys'))


@_utilities.lift_output_func(get_ruleset)
def get_ruleset_output(name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRulesetResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_pagerduty as pagerduty

    example = pagerduty.get_ruleset(name="My Ruleset")
    foo = pagerduty.RulesetRule("foo",
        ruleset=example.id,
        position=0,
        disabled=False,
        conditions=pagerduty.RulesetRuleConditionsArgs(
            operator="and",
            subconditions=[
                pagerduty.RulesetRuleConditionsSubconditionArgs(
                    operator="contains",
                    parameters=[pagerduty.RulesetRuleConditionsSubconditionParameterArgs(
                        value="disk space",
                        path="payload.summary",
                    )],
                ),
                pagerduty.RulesetRuleConditionsSubconditionArgs(
                    operator="contains",
                    parameters=[pagerduty.RulesetRuleConditionsSubconditionParameterArgs(
                        value="db",
                        path="payload.source",
                    )],
                ),
            ],
        ),
        actions=pagerduty.RulesetRuleActionsArgs(
            routes=[pagerduty.RulesetRuleActionsRouteArgs(
                value="P5DTL0K",
            )],
        ))
    ```
    ### Default Global Ruleset

    ```python
    import pulumi
    import pulumi_pagerduty as pagerduty

    default_global = pagerduty.get_ruleset(name="Default Global")
    ```


    :param str name: The name of the ruleset to find in the PagerDuty API.
    """
    ...
