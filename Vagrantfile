# -*- mode: ruby -*-
# vi: set ft=ruby :

$VM_NAME = "vm_name"
$VM_TYPE = "vm_type" + ".box"
$IP_ADDRESS = "vm_ip_address"
$MEMORY = vm_memory
$CPU = vm_cpu
$SHARED_FOLDER = vm_shared_folder

Vagrant.configure("2") do |config|

  config.vm.define $VM_NAME do | config |

    config.vm.box = $VM_TYPE
    config.vm.hostname = $VM_NAME

    config.vm.network "private_network", ip: $IP_ADDRESS

    if $SHARED_FOLDER
      config.vm.synced_folder "/home/antonin/virtualbox/shared_folder", "/share"
    end

    if $VM_TYPE == "windows.box"
      config.vm.communicator = "winrm"
      config.winrm.username = "antonin"
      config.winrm.password = "mdp"
    else
      config.ssh.username = "root"
      config.ssh.password = "mdp"
      config.ssh.keys_only = false
      config.ssh.insert_key = false
    end
    
    config.vm.provider "virtualbox" do |vb|

      vb.gui = false
      vb.memory = $MEMORY
      vb.cpus = $CPU
      vb.name = $VM_NAME

    end

  end
  
end
