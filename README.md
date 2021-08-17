# Virtualbox automation

**CE PROJET N'EST PLUS MAINTENU ET EST CONSIDERE COMME OBSOLETE.**

Automatisation de déploiement de machines virtuelles Virtualbox.

## Installation des logiciels nécessaires

### Installation Vagrant

Il existe deux méthodes pour installer Vagrant.

1. Installation avec gestionnaire de paquet
2. Installation depuis [vagrantup.com](https://www.vagrantup.com)

La méthode 2 est recommandée en raison d'un problème de dépendances rencontré
avec Vagrant installé via le gestionnaire de paquet DNF en méthode 1.

##### Méthode 1 - Installation avec gestionnaire de paquet

```bash
dnf install vagrant
```

L'installation du pckage bsdtar peut éventuellement être nécessaire.

##### Méthode 2 - Installation depuis [vagrantup.com](https://www.vagrantup.com)

L'installation de Vagrant se fait en téléchargeant le package sur
[vagrantup.com](https://www.vagrantup.com/download) et le déplacant dans /usr/bin.
Penser à rendre le binaire exécutable.

Dans les deux cas, installer par la suite le plugin vagrant-vbguest permettant
d'installer les additions invités de Virtualbox sur les machines virtuelles.

```bash
vagrant plugin install vagrant-vbguest
```

### Installation Jenkins

La procédure d'installation est décrite [ici](https://www.jenkins.io/doc/book/installing/linux).

Après installation :

```bash
vim /etc/sysconfig/jenkins
# Editer les variables suivantes :
# JENKINS_USER="antonin"
# JENKINS_LISTEN_ADDRESS="127.0.0.1"

chown -R antonin:antonin /var/log/jenkins
chown -R antonin:antonin /var/cache/jenkins
chown -R antonin:antonin /var/lib/jenkins
```

Installation du plugin Active Choices Plug-in nécessaire pour le bon fonctionnement
des jobs.

La restauration de job jenkins se fait en plaçant les sauvegardes des jobs situés dans le
répertoire jenkins dans /var/lib/jenkins. Il faut placer ces jobs dans des répertoires et
nommer les fichiers config.xml :

```bash
mkdir /var/lib/jenkins/jobs/deploy_vm
mkdir /var/lib/jenkins/jobs/install_gui
mkdir /var/lib/jenkins/jobs/install_software

cp jenkins/deploy_vm.xml /var/lib/jenkins/jobs/deploy_vm/config.xml
cp jenkins/install_gui.xml /var/lib/jenkins/jobs/install_gui/config.xml
cp jenkins/install_software.xml /var/lib/jenkins/jobs/install_software/config.xml
```

### Installation Ansible

```bash
dnf install ansible
```

## Versions

Versions des logiciels utilisés :

* Vagrant 2.2.14
* Jenkins 2.281
* Ansible 2.9.17