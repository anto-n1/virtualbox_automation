# Virtualbox automation

Automatisation de déploiement de machines virtuelles Virtualbox.

## Installation

### Vagrant

Il existe deux méthodes :

1. Installation avec gestionnaire de paquet

```bash
dnf install vagrant bsdtar
```

2. Installation depuis [vagrantup.com](https://www.vagrantup.com)

Cette méthode est recommandée en raison d'un problème de dépendances rencontré
avec Vagrant installé via le gestionnaire de paquet DNF.

L'installation de Vagrant se fait en téléchargeant le package sur
[vagrantup.com](https://www.vagrantup.com/download) et le déplacant dans /usr/bin.
Penser à rendre le binaire exécutable.

Dans les deux cas, installer par la suite le plugin vagrant-vbguest permettant
d'installer les additions invités de Virtualbox sur les machines virtuelles.

```bash
vagrant plugin install vagrant-vbguest
```

vagrant up --provider=virtualbox

### Jenkins

jenkins : https://www.jenkins.io/doc/book/installing/linux/

```bash
vim /etc/sysconfig/jenkins -> editer la variable $JENKINS_USER="antonin"
````

```bash
chown -R antonin:antonin /var/log/jenkins
chown -R antonin:antonin /var/cache/jenkins
chown -R antonin:antonin /var/lib/jenkins
```

### Ansible

```bash
dnf install ansible
```

## Versions

Versions des logiciels utilisés :

* Vagrant 2.2.14
* Jenkins 2.281
* Ansible 2.9.17