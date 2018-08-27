firewall_rule
=========
  [![Build Status](https://travis-ci.org/coaxial/ansible-role-firewall-rule.svg?branch=master)](https://travis-ci.org/coaxial/ansible-role-firewall-rule)

Add firewall rules and persist them. This role is pretty much a wrapper around
the [iptables module](https://docs.ansible.com/ansible/2.5/modules/iptables_module.html) with a handler that will persist the rules after adding them using `iptables-persist`.

Role Variables
--------------

Name | Default | Possible values | Description
---|---|---|---
`fwr__rules` | `[]` | An array of rules; rules take the same keys as the [iptables module](https://docs.ansible.com/ansible/2.5/modules/iptables_module.html) | The rules to add/amend/remove from iptables.


Example Playbook
----------------

```yaml
- hosts: all
  vars:
    fwr__rules:
      - chain: INPUT
        destination_port: 1337
        protocol: tcp
        jump: DROP
        comment: example rule
  roles:
    - firewall-rule
```

License
-------

MIT

Author Information
------------------

Coaxial ([64b.it](https://64b.it))
