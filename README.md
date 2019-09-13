<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-srv_monit.svg)](https://github.com/while-true-do/ansible-role-srv_monit/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-srv_monit.svg)](https://github.com/while-true-do/ansible-role-srv_monit/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-srv_monit.svg)](https://github.com/while-true-do/ansible-role-srv_monit/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-srv_monit.svg)](https://github.com/while-true-do/ansible-role-srv_monit/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-srv_monit.svg)](https://travis-ci.com/while-true-do/ansible-role-srv_monit)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_monit%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_monit)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_monit%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_monit)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_monit%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_monit)

# Ansible Role: srv_monit

An Ansible Role to install and configure monit.

## Motivation

[Monit](https://mmonit.com/monit/) is a simple, yet powerful monitoring
software. It is easy to configure and most servers some kind of monitoring.

## Description

This role installs and configures monit.

- install the packages
- configure mail server
- configure alerts
- configure web access
- configure basic checks
- configure the firewall

You will be able to put your additional checks in '/etc/monit.d/'.

## Requirements

Dependency Roles:

For CentOS and RHEL Systems, the [EPEL](https://fedoraproject.org/wiki/EPEL)
repository must be enabled. You can achieve this by using the
[while_true_do.rpo_epel](https://github.com/while-true-do/ansible-role-rpo_epel)
Ansible Role.

Used Modules:

-   [Ansible Package Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible File Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible Service Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible Template Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible Firewalld Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/srv_monit)
```
ansible-galaxy install while_true_do.srv_monit
```

Install from [Github](https://github.com/while-true-do/ansible-role-srv_monit)
```
git clone https://github.com/while-true-do/ansible-role-srv_monit.git while_true_do.srv_monit
```

Dependencies:

```
ansible-galaxy install -r requirements.yml
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.srv_monit

## Package Management
wtd_srv_monit_package: "monit"
# State can be present|latest|absent
wtd_srv_monit_package_state: "present"

## Configuration Management
wtd_srv_monit_conf: []
# daemon: 30
# start_delay: 30
# log: "syslog"
# pidfile: "/var/run/monit.pid"
# idfile: "/var/monit/monit.id"
# statefile: "/var/monit/monit.state"
# eventqueue:
#   basedir: "/var/monit/events/"
#   slots: "1000"
# mmonit: ""

wtd_srv_monit_conf_alert: []
# recipients:
#   - "mail-address [with reminder on number <cycles>] [{ filter }]"
# mailserver:
#   host: "<hostname>|<ip-address>"
#   port: "25"

wtd_srv_monit_conf_web:
  enabled: true
# port: "2812"
# address: "127.0.0.1"
# signature: "disable"
# ssl: false
# pemfile: "<path to pemfile>"
# pam: true
# allows: ""
#   - "<username>:<password> [read-only]"
#   - "<fqdn>"
#   - "<ip-address>"
#   - "<ip-range>"
#   - "<@unix-group>"

# Enable checks for system resources
wtd_srv_monit_conf_check_system:
  enabled: true
wtd_srv_monit_conf_check_mounts:
  enabled: true
  mounts:
    - name: "rootfs"
      mount: "/"

## Service Management
wtd_srv_monit_service: "monit"
# State can be started|stopped
wtd_srv_monit_service_state: "started"
wtd_srv_monit_service_enabled: true

## Firewalld Management
wtd_srv_monit_fw_mgmt: true
wtd_srv_monit_fw_port: "{{ wtd_srv_monit_conf_web.port | default('2812') }}/tcp"
# State can be enabled|disabled
wtd_srv_monit_fw_state: "enabled"
# Zone can be according to defined zones on your machine.
wtd_srv_monit_fw_zone: "public"
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.rpo_epel
    - role: while_true_do.srv_monit
```

#### Advanced

Configure the webserver to listen on all addresses, add an admin user and
allow the wheel-group (sudoers) to access with read only permission.

```
- hosts: all
  roles:
    - role: while_true_do.rpo_epel
    - role: while_true_do.srv_monit
      wtd_srv_monit_conf_web:
        enabled: true
        address: "0.0.0.0"
        allows:
          - "admin:admin"
          - "@wheel read-only"
```

## Known Issues

1.  RedHat Testing is currently not possible in public, due to limitations
    in subscriptions.
2.  Some services and features cannot be tested properly, due to limitations
    in docker.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com/while-true-do).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-srv_monit/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-srv_monit/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
