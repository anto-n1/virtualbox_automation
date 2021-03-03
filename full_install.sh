#!/bin/bash

# Installation de tous les éléments nécessaires au fonctionnement
# de virtualbox_automation

INSTALL_DIR = ""

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit 1
fi

echo "Ce script installera Jenkins, Vagrant, Ansible."
echo "Ce script est adapaté pour Fedora33 et ne fonctionnera pas pour d'autres distributions." # Ajouter fonction vérification

echo "Git clone project dans ${INSTALL_DIR}..."
cd ${INSTALL_DIR}
git clone http://git.antonin.io/projets_personnels/virtualbox_automation.git

echo "Installation de Vagrant et Ansible..."
dnf udpate
dnf install ansible vagrant bsdtar

echo "Installation de plugins Vagrant..."
vagrant plugin install vagrant-vbguest

echo "Installation de Jenkins..."
sudo wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo
sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key
sudo dnf udpate
sudo dnf install jenkins java-devel

echo "Copie des jobs dans Jenkins..."

echo "Démarrage de Jenkins"
sudo systemctl start Jenkins

