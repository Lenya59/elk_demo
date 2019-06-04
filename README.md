# ELK

Hello, here you can find task overview! Main task define in README.md file.

Here goes!
## Prerequites

The first thing you need to make sure that all prerequisites are complied with this:

1. at least 8 GB RAM available (VM will use 5 GB)
2. [vagrant](https://www.vagrantup.com/) installed
3. [virtualbox](https://www.virtualbox.org/) installed

## Deploy process
Let's consider, that our first thee steps are completely done, just use ```ctop```:
![image](https://user-images.githubusercontent.com/30426958/58879432-55b07480-86de-11e9-8b8f-58eca2190a73.png)

In a picture screened  above you can see, that three containers up and running.

Let's go to the next step >> ```cd templates```  >> put global index settings with ```./put.sh global.json```

***Be careful  on this step, your scripts should be writing for Unix environment, if it is not you can catch next error:***

```shell
vagrant@ubuntu-xenial:/vagrant/templates$ ./put.sh global.json
-bash: ./put.sh: /bin/bash^M: bad interpreter: No such file or directory
```
For converting I am used simple command ```sed -i -e 's/\r$//' scriptname.sh```

OK, going on:

```Bash
vagrant@ubuntu-xenial:/vagrant/templates$ ./put.sh global.json
{"acknowledged":true}
vagrant@ubuntu-xenial:/vagrant/templates$ ./put.sh deployments.json
{"acknowledged":true}
```
If the previous steps are successfully completed, we can proceed with the deployment of our application:

```Bash
vagrant@ubuntu-xenial:/vagrant$ ./deploy.sh 1.0 first release
Sending build context to Docker daemon  11.72MB
Step 1/9 : FROM python:3.5
3.5: Pulling from library/python
c5e155d5a1d1: Pull complete
221d80d00ae9: Pull complete
4250b3117dca: Pull complete
3b7ca19181b2: Pull complete
425d7b2a5bcc: Pull complete
d7a526a3eca5: Pull complete
03339fb09dd6: Pull complete
594669b0b000: Pull complete
7a79e4a07ea7: Pull complete
Digest: sha256:7f890da10a88c961de1355f82eaf70e1730c1bfa5c06aefcbf58323ea319fcad
Status: Downloaded newer image for python:3.5
 ---> 74a0040526f9
Step 2/9 : WORKDIR /usr/src/petshop
 ---> Running in 4c0db09f54de
Removing intermediate container 4c0db09f54de
 ---> 429464fbdc0c
Step 3/9 : ENV PYTHONPATH=/usr/src/petshop
 ---> Running in c0a8dd86b969
Removing intermediate container c0a8dd86b969
 ---> 4100a8293c64
Step 4/9 : ENV APP_VER=1.0
 ---> Running in b953883b9032
Removing intermediate container b953883b9032
 ---> 175543f4b8a1
Step 5/9 : COPY . .
 ---> 29850fa6fd3e
Step 6/9 : RUN dpkg -i filebeat-oss-6.8.0-amd64.deb &&     rm -rf filebeat-oss-6.8.0-amd64.deb
 ---> Running in a8a0f21bd819
Selecting previously unselected package filebeat.
(Reading database ... 30555 files and directories currently installed.)
Preparing to unpack filebeat-oss-6.8.0-amd64.deb ...
Unpacking filebeat (6.8.0) ...
Setting up filebeat (6.8.0) ...
Removing intermediate container a8a0f21bd819
 ---> fa89ef51e854
Step 7/9 : COPY --chown=root:root filebeat.yml /etc/filebeat/filebeat.yml
 ---> c86a9298c909
Step 8/9 : RUN chmod 644 /etc/filebeat/filebeat.yml
 ---> Running in 26deeb8f8ab2
Removing intermediate container 26deeb8f8ab2
 ---> 893b8655ab61
Step 9/9 : CMD sed -i "s|APP_VER|$APP_VER|" /etc/filebeat/filebeat.yml && service filebeat start && python ./petshop/main.py
 ---> Running in adc698eac526
Removing intermediate container adc698eac526
 ---> 19f5b07c3637
Successfully built 19f5b07c3637
Successfully tagged petshop:latest
"docker rmi" requires at least 1 argument.
See 'docker rmi --help'.

Usage:  docker rmi [OPTIONS] IMAGE [IMAGE...]

Remove one or more images
Creating vagrant_petshop_7_1 ...
Creating vagrant_petshop_10_1 ...
Creating vagrant_petshop_7_1       ... done
Creating vagrant_petshop_10_1      ... done
Creating vagrant_petshop_6_1       ... done
Creating vagrant_petshop_4_1       ... done
Creating vagrant_petshop_2_1       ... done
Recreating vagrant_elasticsearch_1 ... done
Creating vagrant_petshop_8_1       ... done
Creating vagrant_petshop_1_1       ... done
Creating vagrant_petshop_3_1       ... done
Creating vagrant_petshop_5_1       ... done
Creating vagrant_petshop_9_1       ... done
curl: (56) Recv failure: Connection reset by peer
```


Ohhh, It will be pretty if we feed our virtual machine with a much more RAM. In that case, it will definitely be pleased and will not behave indecently :)

Our dummy application is running we can see it by typing ```ctop```:

![ctop-deploy-1](https://user-images.githubusercontent.com/30426958/58878936-29e0bf00-86dd-11e9-9e3d-e3a0c2528c3d.png)

When it done, let's investigate such [wonderful tool](https://www.elastic.co/products/kibana "KIBANA") for visualize data, manage and monitor Elasticsearch cluster:

![Kibana](https://user-images.githubusercontent.com/30426958/58880823-7deda280-86e1-11e9-9c15-65b80215909b.png)


Kibana uses index patterns to retrieve data from Elasticsearch indices for things like visualizations, so lets create one for our needs:

![image](https://user-images.githubusercontent.com/30426958/58881124-2e5ba680-86e2-11e9-8941-35815f9fbb5e.png)


Next step is to creating visualization:

![image](https://user-images.githubusercontent.com/30426958/58881386-cb1e4400-86e2-11e9-9ca5-57512d19e43b.png)
