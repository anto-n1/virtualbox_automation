# Gestion des machines virtuelles

Création et gestion des machines virtuelles servant de template
au format box.

L'objectif est de partir d'une machine quasiment vide la plus petite
possible.

## Debian

Commandes effectuées sur Debian avant l'export :

```bash
apt update
apt install sudo # obligatoire sinon problèmes d'élévation de privilège avec Vagrant
apt clean

vi /etc/ssh/sshd_config # PermitRootLogin yes
dd if=/dev/zero of=/EMPTY bs=1M
rm -rf /EMPTY
cat /dev/null > ~/.bash_history && history -c && sudo poweroff
```

## RedHat

Commandes effectuées sur RedHat avant l'export :

```bash
subscription-manager register --auto-attach
dnf update
dnf clean all

dd if=/dev/zero of=/EMPTY bs=1M
rm -rf /EMPTY
cat /dev/null > ~/.bash_history && history -c && sudo poweroff
```

## Windows

Commandes effectuées en powershell avant l'export :

Se mettre dans un réseau privé puis en tant qu'administrateur :

```powershell
Enable-PSRemoting -force
```

Supprimer tous les programmes inutiles (jeux, onedrive...)

## Package Vagrant

Export d'une VM dans un fichier box :

```bash
cd /home/antonin/virtualbox/ # Se rendre dans le dossier virtualbox pour éviter les erreurs
vagrant package --base debian_vagrant_base --output debian.box # debian_vagrant_base est le nom du dossier de la VM 
vagrant box add debian.box --name=debian.box
```

Dans l'exemple ci-dessus, on utilisera donc le nom "debian.box" pour déployer
la VM avec Vagrant : ```config.vm.box = "debian.box"```.

Déployer une VM en ligne de commande :

```bash
vagrant up --provider=virtualbox
```

Suppression d'une VM enregistrée avec Vagrant :

```bash
vagrant box list
vagrant box remove <id>
```

Il est aussi possible de se rendre dans /home/$USER/.vagrant/boxes afin de manipuler
les boxes.