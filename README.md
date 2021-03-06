# Virtualbox automation

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
vim /etc/sysconfig/jenkins -> editer la variable $JENKINS_USER="antonin"

chown -R antonin:antonin /var/log/jenkins
chown -R antonin:antonin /var/cache/jenkins
chown -R antonin:antonin /var/lib/jenkins
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

## TODO

* Refaire une box debian avec 25Go plutot que 15 -> affichage sur Jenkins
* Autologin xfce
* Désactiver le screensaver (blank screen) sur xfce et gnome
* Déploiement machine Windows -> DSC
* Script d'installation de virtualbox_automation
* Utiliser LVM lors de l'installation pour choisir taille du disque plus tard
* Régler problème SSH nouvelle machine
* Autoriser Jenkins uniquement en localhost
* Ajout job destroy VM