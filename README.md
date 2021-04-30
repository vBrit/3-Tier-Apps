# 3-Tier-Apps
![Overview Image](https://github.com/vBrit/3-Tier-Apps/blob/main/images/3-Tier.png)
## Overview

This playbook will create a new 3 Tier Apps based on the 3-Tier Apps used in the HOL from VMWare. I created this to spin up quick 3-Tier apps to run 
inside SDDC created using https://github.com/rutgerblom/SDDC.Lab/tree/dev-v3

## Requirements

Ansible Controller - I used ubuntu 18

Update deploy_ova_vms.yml to point to the location of the Photon OS on your Ansilble Controller. (Tried and tested with Photon 3, Photon 4 not working atm) 

NSX Segments named SEG-App, SEG-Web, SEG-DB.

Edit the inventory/production/group_vars/all.yml and update 

* SiteCode - I used 21 and with my IPv4 the IP's used will be 10.225.21.11, 12, 13 for Web Servers, 10.225.22.10 App Server and 10.225.23.10 for DB Server.
* Passwords
* DNS - Not that its used but it may later
* IPv4 - 10.225.
* vCenter FQDN
* Username
* DataCenter
* Cluster
* DataStore

### Playbooks

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

### Install Ansible Collections

#### vSphere
```
sudo ansible-galaxy collection install community.vmware
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