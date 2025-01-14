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

__all__ = [
    'GetZoneResult',
    'AwaitableGetZoneResult',
    'get_zone',
    'get_zone_output',
]

@pulumi.output_type
class GetZoneResult:
    """
    A collection of values returned by getZone.
    """
    def __init__(__self__, additional_ports=None, additional_primaries=None, dns_servers=None, dnssec=None, expiry=None, hostmaster=None, id=None, link=None, networks=None, nx_ttl=None, primary=None, primary_port=None, refresh=None, retry=None, secondaries=None, ttl=None, zone=None):
        if additional_ports and not isinstance(additional_ports, list):
            raise TypeError("Expected argument 'additional_ports' to be a list")
        pulumi.set(__self__, "additional_ports", additional_ports)
        if additional_primaries and not isinstance(additional_primaries, list):
            raise TypeError("Expected argument 'additional_primaries' to be a list")
        pulumi.set(__self__, "additional_primaries", additional_primaries)
        if dns_servers and not isinstance(dns_servers, str):
            raise TypeError("Expected argument 'dns_servers' to be a str")
        pulumi.set(__self__, "dns_servers", dns_servers)
        if dnssec and not isinstance(dnssec, bool):
            raise TypeError("Expected argument 'dnssec' to be a bool")
        pulumi.set(__self__, "dnssec", dnssec)
        if expiry and not isinstance(expiry, int):
            raise TypeError("Expected argument 'expiry' to be a int")
        pulumi.set(__self__, "expiry", expiry)
        if hostmaster and not isinstance(hostmaster, str):
            raise TypeError("Expected argument 'hostmaster' to be a str")
        pulumi.set(__self__, "hostmaster", hostmaster)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if link and not isinstance(link, str):
            raise TypeError("Expected argument 'link' to be a str")
        pulumi.set(__self__, "link", link)
        if networks and not isinstance(networks, list):
            raise TypeError("Expected argument 'networks' to be a list")
        pulumi.set(__self__, "networks", networks)
        if nx_ttl and not isinstance(nx_ttl, int):
            raise TypeError("Expected argument 'nx_ttl' to be a int")
        pulumi.set(__self__, "nx_ttl", nx_ttl)
        if primary and not isinstance(primary, str):
            raise TypeError("Expected argument 'primary' to be a str")
        pulumi.set(__self__, "primary", primary)
        if primary_port and not isinstance(primary_port, int):
            raise TypeError("Expected argument 'primary_port' to be a int")
        pulumi.set(__self__, "primary_port", primary_port)
        if refresh and not isinstance(refresh, int):
            raise TypeError("Expected argument 'refresh' to be a int")
        pulumi.set(__self__, "refresh", refresh)
        if retry and not isinstance(retry, int):
            raise TypeError("Expected argument 'retry' to be a int")
        pulumi.set(__self__, "retry", retry)
        if secondaries and not isinstance(secondaries, list):
            raise TypeError("Expected argument 'secondaries' to be a list")
        pulumi.set(__self__, "secondaries", secondaries)
        if ttl and not isinstance(ttl, int):
            raise TypeError("Expected argument 'ttl' to be a int")
        pulumi.set(__self__, "ttl", ttl)
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="additionalPorts")
    def additional_ports(self) -> Optional[Sequence[int]]:
        return pulumi.get(self, "additional_ports")

    @property
    @pulumi.getter(name="additionalPrimaries")
    def additional_primaries(self) -> Optional[Sequence[str]]:
        """
        List of additional IPv4 addresses for the primary
        zone.
        """
        return pulumi.get(self, "additional_primaries")

    @property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> str:
        """
        Authoritative Name Servers.
        """
        return pulumi.get(self, "dns_servers")

    @property
    @pulumi.getter
    def dnssec(self) -> bool:
        """
        Whether or not DNSSEC is enabled for the zone.
        """
        return pulumi.get(self, "dnssec")

    @property
    @pulumi.getter
    def expiry(self) -> int:
        """
        The SOA Expiry.
        """
        return pulumi.get(self, "expiry")

    @property
    @pulumi.getter
    def hostmaster(self) -> str:
        """
        The SOA Hostmaster.
        """
        return pulumi.get(self, "hostmaster")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def link(self) -> str:
        """
        The linked target zone.
        """
        return pulumi.get(self, "link")

    @property
    @pulumi.getter
    def networks(self) -> Sequence[int]:
        """
        List of network IDs (`int`) for which the zone should be made
        available. Default is network 0, the primary NSONE Global Network.
        """
        return pulumi.get(self, "networks")

    @property
    @pulumi.getter(name="nxTtl")
    def nx_ttl(self) -> int:
        """
        The SOA NX TTL.
        """
        return pulumi.get(self, "nx_ttl")

    @property
    @pulumi.getter
    def primary(self) -> str:
        """
        The primary zones' IPv4 address.
        """
        return pulumi.get(self, "primary")

    @property
    @pulumi.getter(name="primaryPort")
    def primary_port(self) -> Optional[int]:
        return pulumi.get(self, "primary_port")

    @property
    @pulumi.getter
    def refresh(self) -> int:
        """
        The SOA Refresh.
        """
        return pulumi.get(self, "refresh")

    @property
    @pulumi.getter
    def retry(self) -> int:
        """
        The SOA Retry.
        """
        return pulumi.get(self, "retry")

    @property
    @pulumi.getter
    def secondaries(self) -> Sequence['outputs.GetZoneSecondaryResult']:
        """
        List of secondary servers. Secondaries is
        documented below.
        """
        return pulumi.get(self, "secondaries")

    @property
    @pulumi.getter
    def ttl(self) -> int:
        """
        The SOA TTL.
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter
    def zone(self) -> str:
        return pulumi.get(self, "zone")


class AwaitableGetZoneResult(GetZoneResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetZoneResult(
            additional_ports=self.additional_ports,
            additional_primaries=self.additional_primaries,
            dns_servers=self.dns_servers,
            dnssec=self.dnssec,
            expiry=self.expiry,
            hostmaster=self.hostmaster,
            id=self.id,
            link=self.link,
            networks=self.networks,
            nx_ttl=self.nx_ttl,
            primary=self.primary,
            primary_port=self.primary_port,
            refresh=self.refresh,
            retry=self.retry,
            secondaries=self.secondaries,
            ttl=self.ttl,
            zone=self.zone)


def get_zone(additional_ports: Optional[Sequence[int]] = None,
             additional_primaries: Optional[Sequence[str]] = None,
             primary_port: Optional[int] = None,
             zone: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetZoneResult:
    """
    Provides details about a NS1 Zone. Use this if you would simply like to read
    information from NS1 into your configurations. For read/write operations, you
    should use a resource.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ns1 as ns1

    example = ns1.get_zone(zone="terraform.example.io")
    ```


    :param Sequence[str] additional_primaries: List of additional IPv4 addresses for the primary
           zone.
    :param str zone: The domain name of the zone.
    """
    __args__ = dict()
    __args__['additionalPorts'] = additional_ports
    __args__['additionalPrimaries'] = additional_primaries
    __args__['primaryPort'] = primary_port
    __args__['zone'] = zone
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ns1:index/getZone:getZone', __args__, opts=opts, typ=GetZoneResult).value

    return AwaitableGetZoneResult(
        additional_ports=pulumi.get(__ret__, 'additional_ports'),
        additional_primaries=pulumi.get(__ret__, 'additional_primaries'),
        dns_servers=pulumi.get(__ret__, 'dns_servers'),
        dnssec=pulumi.get(__ret__, 'dnssec'),
        expiry=pulumi.get(__ret__, 'expiry'),
        hostmaster=pulumi.get(__ret__, 'hostmaster'),
        id=pulumi.get(__ret__, 'id'),
        link=pulumi.get(__ret__, 'link'),
        networks=pulumi.get(__ret__, 'networks'),
        nx_ttl=pulumi.get(__ret__, 'nx_ttl'),
        primary=pulumi.get(__ret__, 'primary'),
        primary_port=pulumi.get(__ret__, 'primary_port'),
        refresh=pulumi.get(__ret__, 'refresh'),
        retry=pulumi.get(__ret__, 'retry'),
        secondaries=pulumi.get(__ret__, 'secondaries'),
        ttl=pulumi.get(__ret__, 'ttl'),
        zone=pulumi.get(__ret__, 'zone'))


@_utilities.lift_output_func(get_zone)
def get_zone_output(additional_ports: Optional[pulumi.Input[Optional[Sequence[int]]]] = None,
                    additional_primaries: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                    primary_port: Optional[pulumi.Input[Optional[int]]] = None,
                    zone: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetZoneResult]:
    """
    Provides details about a NS1 Zone. Use this if you would simply like to read
    information from NS1 into your configurations. For read/write operations, you
    should use a resource.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ns1 as ns1

    example = ns1.get_zone(zone="terraform.example.io")
    ```


    :param Sequence[str] additional_primaries: List of additional IPv4 addresses for the primary
           zone.
    :param str zone: The domain name of the zone.
    """
    ...
