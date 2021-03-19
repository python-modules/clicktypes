# Clicktypes - Networking

These types are useful for IP networking purposes.

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