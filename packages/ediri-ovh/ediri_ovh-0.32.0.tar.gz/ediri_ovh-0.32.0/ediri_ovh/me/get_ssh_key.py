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
    'GetSshKeyResult',
    'AwaitableGetSshKeyResult',
    'get_ssh_key',
    'get_ssh_key_output',
]

@pulumi.output_type
class GetSshKeyResult:
    """
    A collection of values returned by getSshKey.
    """
    def __init__(__self__, default=None, id=None, key=None, key_name=None):
        if default and not isinstance(default, bool):
            raise TypeError("Expected argument 'default' to be a bool")
        pulumi.set(__self__, "default", default)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key and not isinstance(key, str):
            raise TypeError("Expected argument 'key' to be a str")
        pulumi.set(__self__, "key", key)
        if key_name and not isinstance(key_name, str):
            raise TypeError("Expected argument 'key_name' to be a str")
        pulumi.set(__self__, "key_name", key_name)

    @property
    @pulumi.getter
    def default(self) -> bool:
        """
        True when this public SSH key is used for rescue mode and reinstallations.
        """
        return pulumi.get(self, "default")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The content of the public key.
        E.g.: "ssh-ed25519 AAAAC3..."
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> str:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "key_name")


class AwaitableGetSshKeyResult(GetSshKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSshKeyResult(
            default=self.default,
            id=self.id,
            key=self.key,
            key_name=self.key_name)


def get_ssh_key(key_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSshKeyResult:
    """
    Use this data source to retrieve information about an SSH key.

    ## Example Usage


    :param str key_name: The name of the SSH key.
    """
    __args__ = dict()
    __args__['keyName'] = key_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ovh:Me/getSshKey:getSshKey', __args__, opts=opts, typ=GetSshKeyResult).value

    return AwaitableGetSshKeyResult(
        default=pulumi.get(__ret__, 'default'),
        id=pulumi.get(__ret__, 'id'),
        key=pulumi.get(__ret__, 'key'),
        key_name=pulumi.get(__ret__, 'key_name'))


@_utilities.lift_output_func(get_ssh_key)
def get_ssh_key_output(key_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSshKeyResult]:
    """
    Use this data source to retrieve information about an SSH key.

    ## Example Usage


    :param str key_name: The name of the SSH key.
    """
    ...
