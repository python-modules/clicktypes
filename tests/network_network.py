import click
import clicktypes.network
from ipaddress import IPv4Address, IPv6Address, IPv4Network, IPv6Network
from typing import Tuple, List, Union


@click.command()
@click.argument(
    "networks",
    nargs=-1,
    required=True,
    type=clicktypes.network.IPNetworkParam(),
)
def ip_network_param(networks=Tuple):
    ## Put networks into a unique list
    networks: List[Union[IPv4Network, IPv6Network]] = list(dict.fromkeys(networks))

    ## Print each network result
    for network in networks:
        click.echo(f"{network}")
