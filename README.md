# 3-Tier-Apps
3 Tier app used for testing and demo based on the HOL from VMWare.
# 3-Tier-Apps


ansible-playbook -i inventories/production/inventory.yml deploy.yml

# Lab AutoDeployment Collection !!!!NEEDTOFINISH!!!!

## Overview

This playbook will create a new 3 Tier Apps based on the 3-Tier Apps used in the HOL from VMWare

## Requirements



### Playbooks

#### Root Directory

All playbooks are located in the following root directory, and this directory should be cloned for each unique environment:

 * aos/base
 * aos_cx/base
 * aos_wlan/base
 * central/base

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
  * Fortios
* Packer
  * Go
  * Windows Update Provisioner
* Additional Components
  * Jmespath
  * SSHPass
  * PyVmOmi

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

#### Fortios
```
sudo ansible-galaxy collection install fortinet.fortios
```

### Install Additional Components

#### SSHPass
```
sudo apt-get install sshpass
```

#### Jmespath
```
sudo pip3 install jmespath
```

#### Install PyVmOmi
```
sudo pip3 install pyvmomi
```

### Install Packer Components

#### Go
```
#Download Go and Extract#
wget -c https://golang.org/dl/go1.16.2.linux-amd64.tar.gz -O - | sudo tar -xz -C /usr/local

#Edit Profile File#
sudo nano /etc/profile

#Append the following to Profile File & Save#
export PATH=$PATH:/usr/local/go/bin

#Save Filepath & Load Env Variable Into Shell#
source /etc/profile
```

#### Packer
```
sudo curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update && sudo apt-get install packer
```


### Configure Git Repository

#### Configure Working Directory
```
mkdir ~/lab_auto
cd ~/lab_auto
git init
```


#### Add or Clone the Repository

##### Clone
```
git clone https://github.com/worldcom-exchange/lab_auto --recursive
```

###### Add
```
cd ~/lab_auto
git remote add origin https://github.com/worldcom-exchange/lab_auto
git pull --set-upstream origin master
git branch --set-upstream-to=origin/master master
```

## Ongoing Git Repository Management

### (Optional) Cache GitHub Credentials
```
cd ~/lab_auto
git config credential.helper store
```

### Track New Files
```
cd ~/lab_auto
git add <file path>/<file name>
```

### Commit Local Changes to be Pushed
```
cd ~/lab_auto
git commit -a
```

### Push Commited Changes to Github Repo
```
cd ~/lab_auto
git push
```

## Author
Nick Iliopoulos