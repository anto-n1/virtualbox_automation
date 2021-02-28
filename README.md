# virtualbox_automation

Automation of virtual machine deployment and configuration.

```bash
dnf install vagrant bsdtar
```

vagrant package --base Debian
vagrant box add debian.box --name=debian
vagrant box list
vagrant box rm

vagrant up --provider=virtualbox

base : activer root et authent root ssh

installation de vagrant en téléchargeant le package sur le site et le déplacant dans /usr/bin
car problème d'installation de ./vagrant plugin install vagrant-vbguest sinon

vagrant 2.2.14

jenkins : https://www.jenkins.io/doc/book/installing/linux/

Following process is for CentOS

    Open up the this script (using VIM or other editor):

vim /etc/sysconfig/jenkins

$JENKINS_USER="root"

sudo chown -R antonin:antonin /var/log/jenkins
sudo chown -R antonin:antonin /var/cache/jenkins
sudo chown -R antonin:antonin /var/lib/jenkins