import pytest
from click.testing import CliRunner
from .network_network import ip_network_param
from typing import List

def test_ip_network_param_single_ipv4_valid():
  """Test accepting a single valid IPv4 address (which will be normalized into a prefix)
  """
  runner = CliRunner()
  result = runner.invoke(ip_network_param, ['192.0.2.0'])
  assert not result.exception
  assert result.exit_code == 0
  assert result.output.strip() == '192.0.2.0/32'

def test_ip_network_param_single_ipv4_invalid():
  """Test rejecting a single invalid IPv4 address
  """
  runner = CliRunner()
  result = runner.invoke(ip_network_param, ['192.0.2.256'])
  assert result.exception
  assert result.exit_code == 2

def test_ip_network_param_single_ipv6_valid():
  """Test accepting a single valid IPv6 address (which will be normalized into a prefix)
  """
  runner = CliRunner()
  result = runner.invoke(ip_network_param, ['2001:DB8:0000::0000'])
  assert not result.exception
  assert result.exit_code == 0
  assert result.output.strip() == '2001:db8::/128'

def test_ip_network_param_single_ipv6_invalid():
  """Test rejeting a single invalid IPv6 address
  """
  runner = CliRunner()
  result = runner.invoke(ip_network_param, ['2001:DB8:gah::/32'])
  assert result.exception
  assert result.exit_code == 2

def test_ip_network_param_multiple_valid():
    """Test accepting multiple valid networks for both IPv4 and IPv6 with a variety of prefix lengths
    """
    ## List of networks to test
    networks: List[str] = ['192.0.2.0', '192.0.2.0/24', '192.0.2.2/28', '2001:DB8::/32', '2001:DB8:0000::/48', '2001:DB8:0101::/33']

    ## Invoke runner
    runner = CliRunner()
    result = runner.invoke(ip_network_param, networks)

    ## Test for exception and exit code
    assert not result.exception
    assert result.exit_code == 0

    ## Split output into list
    output: List[str] = result.output.splitlines()

    ## Make sure the number of results input matches output
    assert len(output) == len(networks)

    ## Test the results match what is expected
    assert '192.0.2.0/32' in output
    assert '192.0.2.0/24' in output
    assert '192.0.2.0/28' in output
    assert '2001:db8::/32' in output
    assert '2001:db8::/48' in output
    assert '2001:db8::/33' in output

def test_ip_network_param_multiple_invalid():
    """Test rejecting a list of networks which contains a single invalid entry
    """
    ## List of networks to test
    networks: List[str] = ['192.0.2.0', '192.0.2.0/24', '192.0.2.2/28', '2001:DB8:gah:/32']

    ## Invoke runner
    runner = CliRunner()
    result = runner.invoke(ip_network_param, networks)

    ## Test for exception and exit code
    assert result.exception
    assert result.exit_code == 2