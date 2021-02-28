# Création machines virtuelles

Création des machines virtuelles servant de template
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

Export de la VM dans le fichier debian.box :

```bash
vagrant package --base /home/antonin/virtualbox/debian_vagrant_base --output debian.box 
```