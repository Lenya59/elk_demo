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
   qualities of the system in a very convenient mode. And as a consequence, prevent different fuckups that may arise :D



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



Let's [continue](https://www.elastic.co/guide/en/beats/filebeat/7.1/filebeat-installation.html) ))

* To download and install Filebeat, use the commands that work with your system.

```bash
vagrant@ubuntu-xenial:/$ sudo curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.1.1-amd64.deb
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 13.1M  100 13.1M    0     0  7359k      0  0:00:01  0:00:01 --:--:-- 7358k
vagrant@ubuntu-xenial:/$ sudo dpkg -i filebeat-7.1.1-amd64.deb
Selecting previously unselected package filebeat.
(Reading database ... 58487 files and directories currently installed.)
Preparing to unpack filebeat-7.1.1-amd64.deb ...
Unpacking filebeat (7.1.1) ...
Setting up filebeat (7.1.1) ...
Processing triggers for ureadahead (0.100.0-19.1) ...
Processing triggers for systemd (229-4ubuntu21.21) ...
```

* Next step is configuring ```filebeat.yml```:

```shell
vagrant@ubuntu-xenial:/$ cd /etc/filebeat && ll
total 308
drwxr-xr-x  3 root root   4096 Jun 10 12:05 ./
drwxr-xr-x 95 root root   4096 Jun 10 12:05 ../
-rw-r--r--  1 root root 219681 May 23 13:21 fields.yml
-rw-r--r--  1 root root  71973 May 23 13:21 filebeat.reference.yml
-rw-------  1 root root   7745 May 23 13:21 filebeat.yml
drwxr-xr-x  2 root root   4096 Jun 10 12:05 modules.d/
```

```bash
sudo cat filebeat.yml
###################### Filebeat Configuration Example #########################

# This file is an example configuration file highlighting only the most common
# options. The filebeat.reference.yml file from the same directory contains all the
# supported options with more comments. You can use it as a reference.
#
# You can find the full configuration reference here:
# https://www.elastic.co/guide/en/beats/filebeat/index.html

# For more available modules and options, please see the filebeat.reference.yml sample
# configuration file.

#=========================== Filebeat inputs =============================

filebeat.inputs:

# Each - is an input. Most options can be set at the input level, so
# you can use different inputs for various configurations.
# Below are the input specific configurations.

- type: log

  # Change to true to enable this input configuration.
  enabled: false

  # Paths that should be crawled and fetched. Glob based paths.
  paths:
    - /var/log/*.log
    #- c:\programdata\elasticsearch\logs\*

  # Exclude lines. A list of regular expressions to match. It drops the lines that are
  # matching any regular expression from the list.
  #exclude_lines: ['^DBG']

  # Include lines. A list of regular expressions to match. It exports the lines that are
  # matching any regular expression from the list.
  #include_lines: ['^ERR', '^WARN']

  # Exclude files. A list of regular expressions to match. Filebeat drops the files that
  # are matching any regular expression from the list. By default, no files are dropped.
  #exclude_files: ['.gz$']

  # Optional additional fields. These fields can be freely picked
  # to add additional information to the crawled log files for filtering
  #fields:
  #  level: debug
  #  review: 1

  ### Multiline options

  # Multiline can be used for log messages spanning multiple lines. This is common
  # for Java Stack Traces or C-Line Continuation

  # The regexp Pattern that has to be matched. The example pattern matches all lines starting with [
  #multiline.pattern: ^\[

  # Defines if the pattern set under pattern should be negated or not. Default is false.
  #multiline.negate: false

  # Match can be set to "after" or "before". It is used to define if lines should be append to a pattern
  # that was (not) matched before or after or as long as a pattern is not matched based on negate.
  # Note: After is the equivalent to previous and before is the equivalent to to next in Logstash
  #multiline.match: after


#============================= Filebeat modules ===============================

filebeat.config.modules:
  # Glob pattern for configuration loading
  path: ${path.config}/modules.d/*.yml

  # Set to true to enable config reloading
  reload.enabled: false

  # Period on which files under path should be checked for changes
  #reload.period: 10s

#==================== Elasticsearch template setting ==========================

setup.template.settings:
  index.number_of_shards: 1
  #index.codec: best_compression
  #_source.enabled: false

#================================ General =====================================

# The name of the shipper that publishes the network data. It can be used to group
# all the transactions sent by a single shipper in the web interface.
#name:

# The tags of the shipper are included in their own field with each
# transaction published.
#tags: ["service-X", "web-tier"]

# Optional fields that you can specify to add additional information to the
# output.
#fields:
#  env: staging


#============================== Dashboards =====================================
# These settings control loading the sample dashboards to the Kibana index. Loading
# the dashboards is disabled by default and can be enabled either by setting the
# options here or by using the `setup` command.
#setup.dashboards.enabled: false

# The URL from where to download the dashboards archive. By default this URL
# has a value which is computed based on the Beat name and version. For released
# versions, this URL points to the dashboard archive on the artifacts.elastic.co
# website.
#setup.dashboards.url:

#============================== Kibana =====================================

# Starting with Beats version 6.0.0, the dashboards are loaded via the Kibana API.
# This requires a Kibana endpoint configuration.
setup.kibana:

  # Kibana Host
  # Scheme and port can be left out and will be set to the default (http and 5601)
  # In case you specify and additional path, the scheme is required: http://localhost:5601/path
  # IPv6 addresses should always be defined as: https://[2001:db8::1]:5601
  #host: "localhost:5601"

  # Kibana Space ID
  # ID of the Kibana Space into which the dashboards should be loaded. By default,
  # the Default Space will be used.
  #space.id:

#============================= Elastic Cloud ==================================

# These settings simplify using filebeat with the Elastic Cloud (https://cloud.elastic.co/).

# The cloud.id setting overwrites the `output.elasticsearch.hosts` and
# `setup.kibana.host` options.
# You can find the `cloud.id` in the Elastic Cloud web UI.
#cloud.id:

# The cloud.auth setting overwrites the `output.elasticsearch.username` and
# `output.elasticsearch.password` settings. The format is `<user>:<pass>`.
#cloud.auth:

#================================ Outputs =====================================

# Configure what output to use when sending the data collected by the beat.

#-------------------------- Elasticsearch output ------------------------------
output.elasticsearch:
  # Array of hosts to connect to.
  hosts: ["localhost:9200"]

  # Optional protocol and basic auth credentials.
  #protocol: "https"
  #username: "elastic"
  #password: "changeme"

#----------------------------- Logstash output --------------------------------
output.logstash:
  hosts: ["127.0.0.1:5044"]
#output.logstash:
  # The Logstash hosts
  #hosts: ["localhost:5044"]

  # Optional SSL. By default is off.
  # List of root certificates for HTTPS server verifications
  #ssl.certificate_authorities: ["/etc/pki/root/ca.pem"]

  # Certificate for SSL client authentication
  #ssl.certificate: "/etc/pki/client/cert.pem"

  # Client Certificate Key
  #ssl.key: "/etc/pki/client/cert.key"

#================================ Processors =====================================

# Configure processors to enhance or manipulate events generated by the beat.

processors:
  - add_host_metadata: ~
  - add_cloud_metadata: ~

#================================ Logging =====================================

# Sets log level. The default log level is info.
# Available log levels are: error, warning, info, debug
#logging.level: debug

# At debug level, you can selectively enable logging only for some components.
# To enable all selectors use ["*"]. Examples of other selectors are "beat",
# "publish", "service".
#logging.selectors: ["*"]

#============================== Xpack Monitoring ===============================
# filebeat can export internal metrics to a central Elasticsearch monitoring
# cluster.  This requires xpack monitoring to be enabled in Elasticsearch.  The
# reporting is disabled by default.

# Set to true to enable the monitoring reporter.
#xpack.monitoring.enabled: false

# Uncomment to send the metrics to Elasticsearch. Most settings from the
# Elasticsearch output are accepted here as well. Any setting that is not set is
# automatically inherited from the Elasticsearch output configuration, so if you
# have the Elasticsearch output configured, you can simply uncomment the
# following line.
#xpack.monitoring.elasticsearch:

#================================= Migration ==================================

# This allows to enable 6.7 migration aliases
#migration.6_to_7.enabled: true
```

If you want to use Logstash to perform additional processing on the data collected by Filebeat, you need to configure Filebeat to use Logstash.

To do this, you edit the Filebeat configuration file to disable the Elasticsearch output by commenting it out and enable the Logstash output by uncommenting the logstash section:
```shell
#----------------------------- Logstash output --------------------------------
output.logstash:
  hosts: ["127.0.0.1:5044"]
  ```
* Load the index [template](https://www.elastic.co/guide/en/beats/filebeat/7.1/filebeat-template.html) in Elasticsearch

The recommended index template file for Filebeat is installed by the Filebeat packages. If you accept the default configuration in the filebeat.yml config file, Filebeat loads the template automatically after successfully connecting to Elasticsearch. If the template already exists, it’s not overwritten unless you configure Filebeat to do so.

* Also you can load your template manually:

```shell
vagrant@ubuntu-xenial:/etc/filebeat$ sudo filebeat setup --template -E output.logstash.enabled=false -E 'output.elasticsearch.hosts=["localhost:9200"]'
Index setup complete.
```

Force Kibana to look at newest documentsedit
If you’ve already used Filebeat to index data into Elasticsearch, the index may contain old documents. After you load the index template, you can delete the old documents from filebeat-* to force Kibana to look at the newest documents.

Use this command:
```shell
curl -XDELETE 'http://localhost:9200/filebeat-*'
```

Set up the Kibana dashboards:

```shell
filebeat setup --dashboards
```

* Set up dashboards for Logstash output:

```shell
filebeat setup -e \
  -E output.logstash.enabled=false \
  -E output.elasticsearch.hosts=['localhost:9200'] \
  -E output.elasticsearch.username=filebeat_internal \
  -E output.elasticsearch.password=YOUR_PASSWORD \
  -E setup.kibana.host=localhost:5601
  ```



* Start Filebeat:
Start Filebeat by issuing the appropriate command for your platform. If you are accessing a secured Elasticsearch cluster, make sure you’ve configured credentials

```shell
vagrant@ubuntu-xenial:/etc/filebeat$ sudo service filebeat start
vagrant@ubuntu-xenial:/etc/filebeat$ sudo service filebeat status
● filebeat.service - Filebeat sends log files to Logstash or directly to Elasticsearch.
   Loaded: loaded (/lib/systemd/system/filebeat.service; disabled; vendor preset: enabled)
   Active: active (running) since Mon 2019-06-10 12:51:31 UTC; 20s ago
     Docs: https://www.elastic.co/products/beats/filebeat
 Main PID: 25497 (filebeat)
    Tasks: 9
   Memory: 6.0M
      CPU: 19ms
   CGroup: /system.slice/filebeat.service
           └─25497 /usr/share/filebeat/bin/filebeat -e -c /etc/filebeat/filebeat.yml -path.home /usr/share/filebeat -path.config /etc/filebeat -path.data /var/lib/filebeat -path.logs /var/log/filebeat

Jun 10 12:51:31 ubuntu-xenial filebeat[25497]: 2019-06-10T12:51:31.426Z        INFO        [monitoring]        log/log.go:117        Starting metrics logging every 30s
Jun 10 12:51:31 ubuntu-xenial filebeat[25497]: 2019-06-10T12:51:31.426Z        INFO        registrar/migrate.go:112        Initialize registry meta file
Jun 10 12:51:31 ubuntu-xenial filebeat[25497]: 2019-06-10T12:51:31.427Z        INFO        registrar/registrar.go:108        No registry file found under: /var/lib/filebeat/registry/filebeat/data.json. Creating a new registry file.
Jun 10 12:51:31 ubuntu-xenial filebeat[25497]: 2019-06-10T12:51:31.428Z        INFO        registrar/registrar.go:145        Loading registrar data from /var/lib/filebeat/registry/filebeat/data.json
Jun 10 12:51:31 ubuntu-xenial filebeat[25497]: 2019-06-10T12:51:31.428Z        INFO        registrar/registrar.go:152        States Loaded from registrar: 0
Jun 10 12:51:31 ubuntu-xenial filebeat[25497]: 2019-06-10T12:51:31.428Z        INFO        crawler/crawler.go:72        Loading Inputs: 1
Jun 10 12:51:31 ubuntu-xenial filebeat[25497]: 2019-06-10T12:51:31.428Z        INFO        crawler/crawler.go:106        Loading and starting Inputs completed. Enabled inputs: 0
Jun 10 12:51:31 ubuntu-xenial filebeat[25497]: 2019-06-10T12:51:31.428Z        INFO        cfgfile/reload.go:150        Config reloader started
Jun 10 12:51:31 ubuntu-xenial filebeat[25497]: 2019-06-10T12:51:31.429Z        INFO        cfgfile/reload.go:205        Loading of config files completed.
Jun 10 12:51:34 ubuntu-xenial filebeat[25497]: 2019-06-10T12:51:34.417Z        INFO        add_cloud_metadata/add_cloud_metadata.go:346        add_cloud_metadata: hosting provider type not detected.
```

* View the sample Kibana dashboards:
Go to the Dashboard page and select the dashboard that you want to open.

![filebeat-dash](https://user-images.githubusercontent.com/30426958/59196682-fd72ea00-8b97-11e9-8265-d5d05a0c3f29.png)
These dashboards are designed to work out-of-the box when you use Filebeat modules. However, you can also use them as examples and customize them to meet your needs even if you aren’t using Filebeat modules
