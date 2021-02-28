# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "debian.box"
  config.vm.define "debian"
  config.vm.hostname = "test"

  config.vm.network "private_network", ip: "192.168.33.10"

  config.vm.synced_folder "/home/antonin/virtualbox/shared_folder", "/share"

  config.ssh.username = "root"
  config.ssh.password = "mdp"
  #config.ssh.port = 22
  config.ssh.keys_only = false
  config.ssh.insert_key = false

  config.vm.provider "virtualbox" do |vb|

    # Display the VirtualBox GUI when booting the machine
    vb.gui = false
    vb.memory = "4000"
    vb.cpus = 4

  end
  
end
