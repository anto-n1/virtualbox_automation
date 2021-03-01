# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "debian.box"
  config.vm.define "debian"
  config.vm.hostname = "debian"

  config.vm.network "private_network", ip: "192.168.56.100", name: "vboxnet0"

  config.vm.synced_folder "/home/antonin/virtualbox/shared_folder", "/share"

  config.ssh.username = "root"
  config.ssh.password = "mdp"
  config.ssh.keys_only = false
  config.ssh.insert_key = false

  config.vm.provider "virtualbox" do |vb|

    vb.gui = false
    vb.memory = "4000"
    vb.cpus = 4
    vb.customize ["modifyvm", :id, "--nicpromisc1", "allow-all"]

  end
  
end
