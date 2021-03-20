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
