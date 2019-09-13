import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_monit_package(host):
    pkg = host.package('monit')

    assert pkg.is_installed


def test_monit_service(host):
    srv = host.service('monit')

    assert srv.is_running
    assert srv.is_enabled
