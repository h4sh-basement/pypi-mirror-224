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
    'GetSasResult',
    'AwaitableGetSasResult',
    'get_sas',
    'get_sas_output',
]

@pulumi.output_type
class GetSasResult:
    """
    A collection of values returned by getSas.
    """
    def __init__(__self__, connection_string=None, expiry=None, id=None, sas=None):
        if connection_string and not isinstance(connection_string, str):
            raise TypeError("Expected argument 'connection_string' to be a str")
        pulumi.set(__self__, "connection_string", connection_string)
        if expiry and not isinstance(expiry, str):
            raise TypeError("Expected argument 'expiry' to be a str")
        pulumi.set(__self__, "expiry", expiry)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if sas and not isinstance(sas, str):
            raise TypeError("Expected argument 'sas' to be a str")
        pulumi.set(__self__, "sas", sas)

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> str:
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter
    def expiry(self) -> str:
        return pulumi.get(self, "expiry")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def sas(self) -> str:
        """
        The computed Event Hub Shared Access Signature (SAS).
        """
        return pulumi.get(self, "sas")


class AwaitableGetSasResult(GetSasResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSasResult(
            connection_string=self.connection_string,
            expiry=self.expiry,
            id=self.id,
            sas=self.sas)


def get_sas(connection_string: Optional[str] = None,
            expiry: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSasResult:
    """
    Use this data source to obtain a Shared Access Signature (SAS Token) for an existing Event Hub.


    :param str connection_string: The connection string for the Event Hub to which this SAS applies.
    :param str expiry: The expiration time and date of this SAS. Must be a valid ISO-8601 format time/date string.
    """
    __args__ = dict()
    __args__['connectionString'] = connection_string
    __args__['expiry'] = expiry
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:eventhub/getSas:getSas', __args__, opts=opts, typ=GetSasResult).value

    return AwaitableGetSasResult(
        connection_string=pulumi.get(__ret__, 'connection_string'),
        expiry=pulumi.get(__ret__, 'expiry'),
        id=pulumi.get(__ret__, 'id'),
        sas=pulumi.get(__ret__, 'sas'))


@_utilities.lift_output_func(get_sas)
def get_sas_output(connection_string: Optional[pulumi.Input[str]] = None,
                   expiry: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSasResult]:
    """
    Use this data source to obtain a Shared Access Signature (SAS Token) for an existing Event Hub.


    :param str connection_string: The connection string for the Event Hub to which this SAS applies.
    :param str expiry: The expiration time and date of this SAS. Must be a valid ISO-8601 format time/date string.
    """
    ...
