import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_mandatory_vars(host):
    i = host.iptables

    assert '-A INPUT -p tcp -m tcp --dport 1337 -j DROP' in i.rules(
        'filter', 'INPUT')


def test_persist(host):
    v4 = host.file('/etc/iptables/rules.v4')
    v6 = host.file('/etc/iptables/rules.v6')

    assert v4.contains('-A INPUT -p tcp -m tcp --dport 1337 -j DROP')
    assert v6.contains('-A INPUT -p tcp -m tcp --dport 1337 -j DROP')
