# ELK demo
This repository allows you to quickly spin up ELK stack and deploy dummy application which produces various logs

## Prerequisite
* at least 8 GB RAM available (VM will use 5 GB)
* [vagrant](https://www.vagrantup.com/) installed
* [virtualbox](https://www.virtualbox.org/) installed

## How to use

1. run ELK stack with ```vagrant up```
2. login to stack with ```vagrant ssh```
3. change working directory to ```/vagrant```
4. check ELK stack state by executing ```docker-compose ps``` or ```ctop```. All three containers should be up and running
5. execute ```cd templates``` and
    * put global index settings with ```./put.sh global.json```
    * put template for *deployments* index by executing ```./put.sh deployments.json```
6. change working directory to ```/vagrant```
7. deploy first version of our application with ```./deploy.sh 1.0 first release``` or run ```./deploy.sh``` to see all the options
8. enjoy

## Links
* [presentation](https://docs.google.com/presentation/d/1p9F1juSbAZwdOPq3iBQV60VYsfXKB5-3UdElAcqFLOE/edit?usp=sharing)