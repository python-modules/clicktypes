# Clicktypes - Networking

These types are useful for web purposes.

## Email Addresses

Validation/normalization for email addresses.

### EmailParam

Used to validate and convert email address to lower case.

Example usage:

```python
from clicktypes.web import EmailParam

@click.argument(
    'email',
    nargs           = -1,
    required        = True,
    type            = EmailParam(),
)
```

## Domains

Validation/normalization for domain names.

### DomainParam

Used to validate and convert domain names to lower case.

Example usage:

```python
from clicktypes.web import DomainParam

@click.argument(
    'domain',
    nargs           = -1,
    required        = True,
    type            = DomainParam(),
)
```
