# Gestion des machines virtuelles

Création et gestion des machines virtuelles servant de template
au format box.

## Debian

Sur la VM template :

```bash
apt update
apt install sudo
gpasswd -a antonin sudo
vi /etc/ssh/sshd_config -> PermitRootLogin yes

apt clean
dd if=/dev/zero of=/EMPTY bs=1M
rm -rf /EMPTY
cat /dev/null > ~/.bash_history && history -c && sudo poweroff
```

## Package Vagrant

Export d'une VM dans un fichier box :

```bash
vagrant package --base /home/antonin/virtualbox/debian_vagrant_base --output debian.box 
vagrant box add debian.box --name=debian
```

Suppression d'une VM enregistrée avec Vagrant :

```bash
vagrant box list
vagrant box remove <id>
```