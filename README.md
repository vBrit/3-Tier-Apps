# 3-Tier-Apps
![Overview Image](https://github.com/vBrit/3-Tier-Apps/blob/main/images/3-Tier.png)
## Overview

This playbook will create a new 3 Tier Apps based on the 3-Tier Apps used in the HOL from VMWare. I created this to spin up quick 3-Tier apps to run 
inside SDDC created using https://github.com/rutgerblom/SDDC.Lab/tree/dev-v3

## Requirements

Ansible Controller - I used ubuntu 18

Update `playbooks/deploy_ova_vms.yml` to point to the location of the Photon OS OVA on your Ansible controller (current default is Photon v5).

NSX Segments named SEG-App, SEG-Web, SEG-DB (or change them via `Common.PortGroups` in `all.yml`).

Edit the inventory/production/group_vars/all.yml and update 

Copy the template first:

```
cp inventories/production/group_vars/all.yml.template inventories/production/group_vars/all.yml
```

Do not commit `inventories/production/group_vars/all.yml` (local secrets/config only).

* SiteCode - I used 21 and with my IPv4 the IP's used will be 10.225.21.11, 12, 13 for Web Servers, 10.225.22.10 App Server and 10.225.23.10 for DB Server.
* Passwords
* DNS - Not that its used but it may later
* IPv4 - 10.225.
* vCenter FQDN
* Username
* DataCenter
* Cluster
* DataStore

### Inventory variables

PortGroups are now centralized in `inventories/production/group_vars/all.yml`:

```yaml
Common:
  PortGroups:
    app: "SEG-App"
    db: "SEG-DB"
    web: "SEG-Web"
```

Group vars (`app.yml`, `db.yml`, `web.yml`) consume these values.

### Connection model (No SSH for role configuration)

Role playbooks now run with `connection: local` and configure guests through VMware Guest Operations modules:

* `community.vmware.vmware_vm_shell`
* `community.vmware.vmware_guest_file_operation`

Because of this, `open-vm-tools` must be installed and running in guest VMs. The bootstrap playbook (`playbooks/configure_vms.yml`) now installs `open-vm-tools` and enables `vmtoolsd` before role execution.

### DB changes (Planetary dataset)

The DB role no longer uses the original sample `Rank/Name/Universe/Revenue` data.

Current SQLite table (`planets`) in `playbooks/roles/db/files/clients.db` now contains:

* `Planet`
* `DistanceFromSunAU` (used for sorting)
* `DistanceFromSunMiles`
* `Moons`
* `DiameterMiles`
* `MoonDetails`
* `StarDetails` (nearest stars to the Sun, shown under Sun)

Runtime behavior:

* Data is served by `playbooks/roles/db/files/data.py`.
* App UI is rendered from `playbooks/roles/app/templates/app.j2`.
* Planet rows are color-themed by planet.
* Moon rows inherit their parent planet color.
* Sun includes child rows for nearest stars (light-year values).

To apply DB/content changes to deployed VMs without full redeploy:

```bash
ansible-playbook -i inventories/production/inventory.yml playbooks/install_config_db.yml
ansible-playbook -i inventories/production/inventory.yml playbooks/install_config_app.yml
```

### Playbooks

Render inventory aliases from `Common.hostnames` before deploy/undeploy:

```bash
ansible-playbook -i localhost, playbooks/render_inventory.yml
```

Or use wrappers that automatically render first:

```bash
./deploy.sh
./undeploy.sh
```

ansible-playbook -i inventories/production/inventory.yml deploy.yml

## Pre-requisite Steps

The following will need to be installed in order to maintain the collection and use the Playbooks:

* Update Ubuntu
* Git
* Python3 = latest
* Ansible = latest
* Go
* Packer
* Ansible Collections = latest
  * VMmware

### Update Ubuntu
```
sudo apt-get update && sudo apt-get upgrade
```

### Install Core Components

#### Git
```
sudo apt-get install git
```

#### Python3
```
sudo apt-get install python3-pip
```

#### Ansible
```
sudo pip3 install ansible
```

#### Python dependencies (recommended)
```
pip3 install -r requirements.txt
```

### Install Ansible Collections

#### vSphere
```
sudo ansible-galaxy collection install community.vmware
```

Or install collections from file:
```
ansible-galaxy collection install -r collections/requirements.yml
```

### Install Additional Components

#### SSHPass
```
sudo apt-get install sshpass
```

## Thanks to

https://github.com/kwrobert 

& https://github.com/doug-baer/hol-3-tier-app as you fixed some of the issues.

## Author
Karl Newick who has never used Ansible before :)