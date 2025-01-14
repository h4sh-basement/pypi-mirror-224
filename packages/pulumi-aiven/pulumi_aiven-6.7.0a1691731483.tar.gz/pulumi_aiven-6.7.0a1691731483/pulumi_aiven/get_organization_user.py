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
    'GetOrganizationUserResult',
    'AwaitableGetOrganizationUserResult',
    'get_organization_user',
    'get_organization_user_output',
]

@pulumi.output_type
class GetOrganizationUserResult:
    """
    A collection of values returned by getOrganizationUser.
    """
    def __init__(__self__, accepted=None, create_time=None, id=None, invited_by=None, organization_id=None, user_email=None):
        if accepted and not isinstance(accepted, bool):
            raise TypeError("Expected argument 'accepted' to be a bool")
        pulumi.set(__self__, "accepted", accepted)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if invited_by and not isinstance(invited_by, str):
            raise TypeError("Expected argument 'invited_by' to be a str")
        pulumi.set(__self__, "invited_by", invited_by)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)
        if user_email and not isinstance(user_email, str):
            raise TypeError("Expected argument 'user_email' to be a str")
        pulumi.set(__self__, "user_email", user_email)

    @property
    @pulumi.getter
    def accepted(self) -> bool:
        """
        This is a boolean flag that determines whether an invitation was accepted or not by the user. `false` value means that the invitation was sent to the user but not yet accepted. `true` means that the user accepted the invitation and now a member of an organization.
        """
        return pulumi.get(self, "accepted")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Time of creation
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="invitedBy")
    def invited_by(self) -> str:
        """
        The email address of the user who sent an invitation to the user.
        """
        return pulumi.get(self, "invited_by")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        """
        The unique organization ID. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="userEmail")
    def user_email(self) -> str:
        """
        This is a user email address that first will be invited, and after accepting an invitation, they become a member of the organization. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "user_email")


class AwaitableGetOrganizationUserResult(GetOrganizationUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOrganizationUserResult(
            accepted=self.accepted,
            create_time=self.create_time,
            id=self.id,
            invited_by=self.invited_by,
            organization_id=self.organization_id,
            user_email=self.user_email)


def get_organization_user(organization_id: Optional[str] = None,
                          user_email: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOrganizationUserResult:
    """
    The Organization User data source provides information about the existing Aiven Organization User.


    :param str organization_id: The unique organization ID. This property cannot be changed, doing so forces recreation of the resource.
    :param str user_email: This is a user email address that first will be invited, and after accepting an invitation, they become a member of the organization. This property cannot be changed, doing so forces recreation of the resource.
    """
    __args__ = dict()
    __args__['organizationId'] = organization_id
    __args__['userEmail'] = user_email
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aiven:index/getOrganizationUser:getOrganizationUser', __args__, opts=opts, typ=GetOrganizationUserResult).value

    return AwaitableGetOrganizationUserResult(
        accepted=pulumi.get(__ret__, 'accepted'),
        create_time=pulumi.get(__ret__, 'create_time'),
        id=pulumi.get(__ret__, 'id'),
        invited_by=pulumi.get(__ret__, 'invited_by'),
        organization_id=pulumi.get(__ret__, 'organization_id'),
        user_email=pulumi.get(__ret__, 'user_email'))


@_utilities.lift_output_func(get_organization_user)
def get_organization_user_output(organization_id: Optional[pulumi.Input[str]] = None,
                                 user_email: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOrganizationUserResult]:
    """
    The Organization User data source provides information about the existing Aiven Organization User.


    :param str organization_id: The unique organization ID. This property cannot be changed, doing so forces recreation of the resource.
    :param str user_email: This is a user email address that first will be invited, and after accepting an invitation, they become a member of the organization. This property cannot be changed, doing so forces recreation of the resource.
    """
    ...
