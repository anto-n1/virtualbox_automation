#!/usr/bin/python

# Script lancé par Jenkins

# python generate_vagrantfile.py vm_name vm_type ip_address memory cpu shared_folder
# python generate_vagrantfile.py my_vm debian 192.168.10.10 4000 4 true

import sys
import shutil

def main():

    if len(sys.argv) == 2:

        ip_address = sys.argv[1]

        # Ansible hosts file
        filename = "ansible/hosts"
        new_filename = "ansible/hosts_to_use"
        shutil.copy(filename, new_filename)

        with open(new_filename, "r") as file :
            filedata = file.read()

        filedata = filedata.replace("vm_ip_address", ip_address)

        with open(new_filename, "w") as file:
            file.write(filedata)

    elif len(sys.argv) == 7:

        # Vagrantfile
        filename = "Vagrantfile"
        new_filename = "Vagrantfile_to_use"
        shutil.copy(filename, new_filename)
        
        vm_name = sys.argv[1]
        vm_type = sys.argv[2]
        ip_address = sys.argv[3]
        memory = sys.argv[4]
        cpu = sys.argv[5]
        shared_folder = sys.argv[6]

        with open(new_filename, "r") as file :
            filedata = file.read()

        filedata = filedata.replace("vm_name", vm_name) \
            .replace("vm_type", vm_type) \
            .replace("vm_ip_address", ip_address) \
            .replace("vm_memory", memory) \
            .replace("vm_cpu", cpu) \
            .replace("vm_shared_folder", shared_folder)

        with open(new_filename, "w") as file:
            file.write(filedata)

        # Ansible hosts file
        filename = "ansible/hosts"
        new_filename = "ansible/hosts_to_use"
        shutil.copy(filename, new_filename)

        with open(new_filename, "r") as file :
            filedata = file.read()

        filedata = filedata.replace("vm_ip_address", ip_address)

        with open(new_filename, "w") as file:
            file.write(filedata)

if __name__ == "__main__":
    main()