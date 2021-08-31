# Changelog

Python `clicktypes` changelog.

## [0.0.7] - 2021-08-31

- Fix changelog dates
- Add support for Click 8.0 (resolves issue "AttributeError: 'NoneType' object has no attribute 'upper'")

## [0.0.6] - 2021-03-23

- Fix markdown links

## [0.0.5] - 2021-03-23

- Add IPStringParam, IPv4StringParam and IPv6StringParam
- Add IPNetworkStringParam, IPv4NetworkStringParam and IPv6NetworkStringParam
- Add basic tests
- Remove strict validation for network parameters
- Reformat files with `black`

## [0.0.4] - 2021-03-20

- Add UrlParam
- Add missing dependancy on 'validators'

## [0.0.3] - 2021-03-20

- Add DomainParam
- Add EmailParam

## [0.0.2] - 2021-03-20

- [Add IP address params](clicktypes/network/README.md):
  - IPAddressParam: IPv4 or IPv6 IP addresses
  - IPv4AddressParam: IPv4 IP addresses
  - IPv6AddressParam: IPv6 IP addresses
- Update main README

## [0.0.1] - 2020-03-19

- Initial release
- [Add IP networking params](clicktypes/network/README.md):
  - IPNetworkParam: IPv4 or IPv6 network addresses
  - IPv4NetworkParam: IPv4 network addresses
  - IPv6NetworkParam: IPv6 network addresses
