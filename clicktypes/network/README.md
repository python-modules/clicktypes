# Clicktypes - Networking

These types are useful for IP networking purposes.

- [Clicktypes - Networking](#clicktypes---networking)
  - [Network Addresses](#network-addresses)
    - [IPNetworkParam](#ipnetworkparam)
    - [IPv4NetworkParam](#ipv4networkparam)
    - [IPv6NetworkParam](#ipv6networkparam)
    - [IPNetworkStringParam](#ipnetworkstringparam)
    - [IPv4NetworkStringParam](#ipv4networkstringparam)
    - [IPv6NetworkStringParam](#ipv6networkstringparam)
  - [IP Addresses](#ip-addresses)
    - [IPAddressParam](#ipaddressparam)
    - [IPv4AddressParam](#ipv4addressparam)
    - [IPv6AddressParam](#ipv6addressparam)
    - [IPStringParam](#ipstringparam)
    - [IPv4StringParam](#ipv4stringparam)
    - [IPv6StringParam](#ipv6stringparam)

## Network Addresses

IPv4/IPv6 network parameter types. The following types are available:

### IPNetworkParam

Validate and normalize provided value into an IPv4Network or IPv6Network object.

Example usage:

```python
from clicktypes.network import IPNetworkParam

@click.argument(
    'network',
    nargs           = -1,
    required        = True,
    type            = IPNetworkParam(),
)
```

### IPv4NetworkParam

Validate and normalize provided value into an IPv4Network object.

Example usage:

```python
from clicktypes.network import IPv4NetworkParam

@click.argument(
    'network',
    nargs           = -1,
    required        = True,
    type            = IPv4NetworkParam(),
)
```

### IPv6NetworkParam

Validate and normalize provided value into an IPv6Network object.

Example usage:

```python
from clicktypes.network import IPv6NetworkParam

@click.argument(
    'network',
    nargs           = -1,
    required        = True,
    type            = IPv6NetworkParam(),
)
```

### IPNetworkStringParam

Validate and normalize provided value into an IPv4 or IPv6 network and return as string.

Example usage:

```python
from clicktypes.network import IPNetworkStringParam

@click.argument(
    'network',
    nargs           = -1,
    required        = True,
    type            = IPNetworIPNetworkStringParamkParam(),
)
```

### IPv4NetworkStringParam

Validate and normalize provided value into an IPv4 network and return as string.

Example usage:

```python
from clicktypes.network import IPv4NetworkStringParam

@click.argument(
    'network',
    nargs           = -1,
    required        = True,
    type            = IPv4NetworkStringParam(),
)
```

### IPv6NetworkStringParam

Validate and normalize provided value into an IPv6 network and return as string.

Example usage:

```python
from clicktypes.network import IPv6NetworkStringParam

@click.argument(
    'network',
    nargs           = -1,
    required        = True,
    type            = IPv6NetworkStringParam(),
)
```

## IP Addresses

IPv4/IPv6 IP address parameter types. The following types are available:

### IPAddressParam

Validate and normalize provided value into an IPv4Address or IPv6Address object.

Example usage:

```python
from clicktypes.network import IPAddressParam

@click.argument(
    'ip',
    nargs           = -1,
    required        = True,
    type            = IPAddressParam(),
)
```

### IPv4AddressParam

Validate and normalize provided value into an IPv4Address object.

Example usage:

```python
from clicktypes.network import IPv4AddressParam

@click.argument(
    'ip',
    nargs           = -1,
    required        = True,
    type            = IPv4AddressParam(),
)
```

### IPv6AddressParam

Validate and normalize provided value into an IPv6Address object.

Example usage:

```python
from clicktypes.network import IPv6AddressParam

@click.argument(
    'ip',
    nargs           = -1,
    required        = True,
    type            = IPv6AddressParam(),
)
```

### IPStringParam

Validate and normalize provided value as an IP address but return the normalized result as a string.

Example usage:

```python
from clicktypes.network import IPStringParam

@click.argument(
    'ip',
    nargs           = -1,
    required        = True,
    type            = IPStringParam(),
)
```

### IPv4StringParam

Validate and normalize provided value as an IPv4 address but return the normalized result as a string.

Example usage:

```python
from clicktypes.network import IPv4StringParam

@click.argument(
    'ip',
    nargs           = -1,
    required        = True,
    type            = IPv4StringParam(),
)
```

### IPv6StringParam

Validate and normalize provided value as an IPv6 address but return the normalized result as a string.

Example usage:

```python
from clicktypes.network import IPv6StringParam

@click.argument(
    'ip',
    nargs           = -1,
    required        = True,
    type            = IPv6StringParam(),
)
```
