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
    'GetAccountResult',
    'AwaitableGetAccountResult',
    'get_account',
]

@pulumi.output_type
class GetAccountResult:
    """
    A collection of values returned by getAccount.
    """
    def __init__(__self__, address1=None, address2=None, balance=None, city=None, company=None, country=None, email=None, first_name=None, id=None, last_name=None, phone=None, state=None, zip=None):
        if address1 and not isinstance(address1, str):
            raise TypeError("Expected argument 'address1' to be a str")
        pulumi.set(__self__, "address1", address1)
        if address2 and not isinstance(address2, str):
            raise TypeError("Expected argument 'address2' to be a str")
        pulumi.set(__self__, "address2", address2)
        if balance and not isinstance(balance, float):
            raise TypeError("Expected argument 'balance' to be a float")
        pulumi.set(__self__, "balance", balance)
        if city and not isinstance(city, str):
            raise TypeError("Expected argument 'city' to be a str")
        pulumi.set(__self__, "city", city)
        if company and not isinstance(company, str):
            raise TypeError("Expected argument 'company' to be a str")
        pulumi.set(__self__, "company", company)
        if country and not isinstance(country, str):
            raise TypeError("Expected argument 'country' to be a str")
        pulumi.set(__self__, "country", country)
        if email and not isinstance(email, str):
            raise TypeError("Expected argument 'email' to be a str")
        pulumi.set(__self__, "email", email)
        if first_name and not isinstance(first_name, str):
            raise TypeError("Expected argument 'first_name' to be a str")
        pulumi.set(__self__, "first_name", first_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_name and not isinstance(last_name, str):
            raise TypeError("Expected argument 'last_name' to be a str")
        pulumi.set(__self__, "last_name", last_name)
        if phone and not isinstance(phone, str):
            raise TypeError("Expected argument 'phone' to be a str")
        pulumi.set(__self__, "phone", phone)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if zip and not isinstance(zip, str):
            raise TypeError("Expected argument 'zip' to be a str")
        pulumi.set(__self__, "zip", zip)

    @property
    @pulumi.getter
    def address1(self) -> str:
        """
        First line of this Account's billing address.
        """
        return pulumi.get(self, "address1")

    @property
    @pulumi.getter
    def address2(self) -> str:
        """
        Second line of this Account's billing address.
        """
        return pulumi.get(self, "address2")

    @property
    @pulumi.getter
    def balance(self) -> float:
        """
        This Account's balance, in US dollars.
        """
        return pulumi.get(self, "balance")

    @property
    @pulumi.getter
    def city(self) -> str:
        """
        The city for this Account's billing address.
        """
        return pulumi.get(self, "city")

    @property
    @pulumi.getter
    def company(self) -> str:
        """
        The company name associated with this Account.
        """
        return pulumi.get(self, "company")

    @property
    @pulumi.getter
    def country(self) -> str:
        """
        The two-letter country code of this Account's billing address.
        """
        return pulumi.get(self, "country")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        The email address for this Account, for account management communications, and may be used for other communications as configured.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> str:
        """
        The first name of the person associated with this Account.
        """
        return pulumi.get(self, "first_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> str:
        """
        The last name of the person associated with this Account.
        """
        return pulumi.get(self, "last_name")

    @property
    @pulumi.getter
    def phone(self) -> str:
        """
        The phone number associated with this Account.
        """
        return pulumi.get(self, "phone")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        If billing address is in the United States, this is the State portion of the Account's billing address. If the address is outside the US, this is the Province associated with the Account's billing address.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def zip(self) -> str:
        """
        The zip code of this Account's billing address.
        """
        return pulumi.get(self, "zip")


class AwaitableGetAccountResult(GetAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountResult(
            address1=self.address1,
            address2=self.address2,
            balance=self.balance,
            city=self.city,
            company=self.company,
            country=self.country,
            email=self.email,
            first_name=self.first_name,
            id=self.id,
            last_name=self.last_name,
            phone=self.phone,
            state=self.state,
            zip=self.zip)


def get_account(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountResult:
    """
    Provides information about a Linode account.

    This data source should not be used in conjuction with the `LINODE_DEBUG` option.  See the [debugging notes](https://www.terraform.io/providers/linode/linode/latest/docs#debugging) for more details.

    ## Example Usage

    The following example shows how one might use this data source to access account details.

    ```python
    import pulumi
    import pulumi_linode as linode

    account = linode.get_account()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('linode:index/getAccount:getAccount', __args__, opts=opts, typ=GetAccountResult).value

    return AwaitableGetAccountResult(
        address1=pulumi.get(__ret__, 'address1'),
        address2=pulumi.get(__ret__, 'address2'),
        balance=pulumi.get(__ret__, 'balance'),
        city=pulumi.get(__ret__, 'city'),
        company=pulumi.get(__ret__, 'company'),
        country=pulumi.get(__ret__, 'country'),
        email=pulumi.get(__ret__, 'email'),
        first_name=pulumi.get(__ret__, 'first_name'),
        id=pulumi.get(__ret__, 'id'),
        last_name=pulumi.get(__ret__, 'last_name'),
        phone=pulumi.get(__ret__, 'phone'),
        state=pulumi.get(__ret__, 'state'),
        zip=pulumi.get(__ret__, 'zip'))
