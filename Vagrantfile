# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/xenial64"
  
    config.vm.box_check_update = false
  
    config.vm.synced_folder ".", "/vagrant"
    config.vm.network "forwarded_port", guest: 9200, host: 29200
    config.vm.network "forwarded_port", guest: 5601, host: 25601
    config.vm.network "forwarded_port", guest: 8080, host: 28080
    config.vm.provider :virtualbox do |p|
      p.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      p.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
      p.customize ["modifyvm", :id, "--natnet1", "192.168.253/24"]
      p.customize ["guestproperty", "set", :id, "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 10000 ]
      p.memory = "5120"
      p.cpus = 2
    end
  
  
    config.vm.provision "shell", inline: <<-SHELL
      if [ -z "$(which docker)" ]; then
        apt-get update
        apt-get install apt-transport-https ca-certificates curl software-properties-common -y
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
        echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
        apt-get update
        apt-get install docker-ce -y
        usermod -aG docker vagrant
      fi
      if [ -z "$(which docker-compose)" ]; then
        curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/bin/docker-compose
        chmod +x /usr/bin/docker-compose
      fi
      if [ -z "$(which ctop)" ]; then
        curl -L "https://github.com/bcicen/ctop/releases/download/v0.7.2/ctop-0.7.2-linux-amd64" -o /usr/bin/ctop
        chmod +x /usr/bin/ctop
      fi
    SHELL

    config.vm.provision "shell", inline: <<-SHELL
      grep -o vm.max_map_count /etc/sysctl.conf || echo vm.max_map_count=262144 >> /etc/sysctl.conf && sysctl -p /etc/sysctl.conf
      cd /vagrant
      sudo -u vagrant docker-compose up -d
    SHELL
  
  end