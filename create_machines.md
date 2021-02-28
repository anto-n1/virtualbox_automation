# Création Debian

sudo apt install sudo
sudo gpasswd -a antonin sudo
sudo vim /etc/ssh/sshd_config
edit root password

sudo apt-get clean

sudo dd if=/dev/zero of=/EMPTY bs=1M
sudo rm -f /EMPTY

cat /dev/null > ~/.bash_history && history -c && sudo poweroff

vagrant package --base /home/antonin/virtualbox/debian_vagrant_base --output debian.box 
