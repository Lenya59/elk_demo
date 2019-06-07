# ELK

Hello, here you can find task overview! Main task define in README_TASK.md file.

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

In the column [Visualization](https://www.elastic.co/guide/en/kibana/5.5/visualize.html), we can choose the appropriate type of information display, such as: Area, Gauge, Heat Map, VEGA (most powerful and most complicated advanced tool). I stopped on this type as Line


![visualize](https://user-images.githubusercontent.com/30426958/59091210-88917d00-8917-11e9-82eb-7ff00034914f.png)

As you can see in the figure below, there are many options for customizing the visualization control. In my case, along the Y axis, an aggregation of the number of elements is given (Count)

On the X-axis, a Date Histogram was chosen, which means time aggregation. A sub-bucket was also added, which Aggregated across the ```host.name.keyword``` field.



![controling](https://user-images.githubusercontent.com/30426958/59091735-a57a8000-8918-11e9-99ee-49b65fca0626.png)


* When we have fully explored the first version of the application, you can proceed to deploy the second version:

```Bash
vagrant@ubuntu-xenial:/vagrant$ ./deploy.sh 2.0 - app with AI
Sending build context to Docker daemon  11.72MB
Step 1/9 : FROM python:3.5
 ---> 74a0040526f9
Step 2/9 : WORKDIR /usr/src/petshop
 ---> Using cache
 ---> 8a0fb4cbd728
Step 3/9 : ENV PYTHONPATH=/usr/src/petshop
 ---> Using cache
 ---> 424c44a174bc
Step 4/9 : ENV APP_VER=1.0
 ---> Using cache
 ---> c0b8798c47ea
Step 5/9 : COPY . .
 ---> Using cache
 ---> ddc5787c756d
Step 6/9 : RUN dpkg -i filebeat-oss-6.8.0-amd64.deb &&     rm -rf filebeat-oss-6.8.0-amd64.deb
 ---> Using cache
 ---> d43ce19f4eee
Step 7/9 : COPY --chown=root:root filebeat.yml /etc/filebeat/filebeat.yml
 ---> Using cache
 ---> 6f1d532ec007
Step 8/9 : RUN chmod 644 /etc/filebeat/filebeat.yml
 ---> Using cache
 ---> fb0f09b7aaed
Step 9/9 : CMD sed -i "s|APP_VER|$APP_VER|" /etc/filebeat/filebeat.yml && service filebeat start && python ./petshop/main.py
 ---> Using cache
 ---> bf119f3134ae
Successfully built bf119f3134ae
Successfully tagged petshop:latest
"docker rmi" requires at least 1 argument.
See 'docker rmi --help'.

Usage:  docker rmi [OPTIONS] IMAGE [IMAGE...]

Remove one or more images
Recreating vagrant_petshop_7_1 ...
vagrant_logstash_1 is up-to-date
Recreating vagrant_petshop_4_1 ...
Recreating vagrant_petshop_7_1  ... done
Recreating vagrant_petshop_4_1  ... done
Recreating vagrant_petshop_1_1  ... done
Recreating vagrant_petshop_8_1  ... done
Recreating vagrant_petshop_5_1  ... done
Recreating vagrant_petshop_6_1  ... done
Recreating vagrant_petshop_10_1 ... done
Recreating vagrant_petshop_9_1  ... done
Recreating vagrant_petshop_2_1  ... done
Recreating vagrant_petshop_3_1  ... done
{"_index":"deployments","_type":"_doc","_id":"FsgsMWsBZhWh5zugbn3y","_version":1,"result":"created","_shards":{"total":1,"successful":1,"failed":0},"_seq_no":0,"_primary_term":1}
```

Let's look at the next useful KIBANA option, it will be a [Dashboard](https://www.elastic.co/guide/en/kibana/5.5/dashboard.html). There you can combine data views from any Kibana app into one dashboard and see everything in one place.


![Dashboard](https://user-images.githubusercontent.com/30426958/59099319-74f01180-892b-11e9-901c-19f6635a05c7.png)

On the newly created dashboard, I added some useful visualizations that can be monitored in near real-time mode (the minimum update time is a millisecond). This allows you to analyze various qualities of the system in a very convenient mode. And as a consequence, prevent different fuckups that may arise :D



Come on! Let's deploy next version of our application

```Bash
vagrant@ubuntu-xenial:/vagrant$ ./deploy.sh 3.0 - 500 error bug
Sending build context to Docker daemon  11.72MB
Step 1/9 : FROM python:3.5
 ---> 74a0040526f9
Step 2/9 : WORKDIR /usr/src/petshop
 ---> Using cache
 ---> 8a0fb4cbd728
Step 3/9 : ENV PYTHONPATH=/usr/src/petshop
 ---> Using cache
 ---> 424c44a174bc
Step 4/9 : ENV APP_VER=1.0
 ---> Using cache
 ---> c0b8798c47ea
Step 5/9 : COPY . .
 ---> Using cache
 ---> ddc5787c756d
Step 6/9 : RUN dpkg -i filebeat-oss-6.8.0-amd64.deb &&     rm -rf filebeat-oss-6.8.0-amd64.deb
 ---> Using cache
 ---> d43ce19f4eee
Step 7/9 : COPY --chown=root:root filebeat.yml /etc/filebeat/filebeat.yml
 ---> Using cache
 ---> 6f1d532ec007
Step 8/9 : RUN chmod 644 /etc/filebeat/filebeat.yml
 ---> Using cache
 ---> fb0f09b7aaed
Step 9/9 : CMD sed -i "s|APP_VER|$APP_VER|" /etc/filebeat/filebeat.yml && service filebeat start && python ./petshop/main.py
 ---> Using cache
 ---> bf119f3134ae
Successfully built bf119f3134ae
Successfully tagged petshop:latest
"docker rmi" requires at least 1 argument.
See 'docker rmi --help'.

Usage:  docker rmi [OPTIONS] IMAGE [IMAGE...]

Remove one or more images
Recreating vagrant_petshop_1_1 ...
Recreating vagrant_petshop_2_1 ...
Recreating vagrant_petshop_6_1 ...
Recreating vagrant_petshop_1_1  ... done
Recreating vagrant_petshop_2_1  ... done
Recreating vagrant_petshop_6_1  ... done
Recreating vagrant_petshop_10_1 ... done
Recreating vagrant_petshop_7_1  ... done
Recreating vagrant_petshop_3_1  ... done
Recreating vagrant_petshop_4_1  ... done
Recreating vagrant_petshop_8_1  ... done
Recreating vagrant_petshop_5_1  ... done
Recreating vagrant_petshop_9_1  ... done
{"_index":"deployments","_type":"_doc","_id":"lOM5MmsBZhWh5zugOqX-","_version":1,"result":"created","_shards":{"total":1,"successful":1,"failed":0},"_seq_no":1,"_primary_term":1}
```

Let's go to our dashboard and investigate what happened after our deployment:

![3.0-deploy-dashboard](https://user-images.githubusercontent.com/30426958/59109352-9231d980-8945-11e9-8c6f-f886e78e82cd.png)

...

...

...

Finally, we have another version of the application. Let's deploy it and see what happened:

```Bash
./deploy.sh anything else - stable app
```
![last-version](https://user-images.githubusercontent.com/30426958/59111874-957b9400-894a-11e9-82b2-6ac707a0f58e.png)

As you can see, KIBANA is very powerful tool for visualize data :D

Next step is investigate [FILEBEAT](https://www.elastic.co/products/beats/filebeat) and [METRICBEAT](https://www.elastic.co/products/beats/metricbeat)
