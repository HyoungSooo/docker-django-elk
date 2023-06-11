# Docker Django with elk stack

![diagram](https://github.com/HyoungSooo/docker-django-elk/assets/86239441/a2862447-032d-4a77-b0b3-2f455b6baa3a)

### Usage
```shell
docker-compose -f docker-compose.yml -f extensions/filebeat/filebeat-compose.yml up
```

### Docker Container


**The docker container structure is based on the docker-elk repository.**

### filebeat.yml

#### log collection path
```shell
name: filebeat

filebeat.inputs:
- type : log
  enabled: true
  paths:
    - /usr/share/web/logs/*.log

output.logstash:
  hosts: ["logstash:5044"]

setup.kibana:
  hosts: ["kibana:5601"]

```
Default path is **/usr/share/web/logs/**. This is the same as the django app log collection path.
If you want to modify the path, modify the **extension/filebeat/filebeat-compose.yml** file and the volume of the web container in the **root directory docker-compose.yml**.

```shell
extension/filebeat/filebeat-compose.yml

volumes:
  ...
  - logs_volume:/usr/share/web/logs # here

docker-compose.yml
volumes:
  ...
  - ./process/logs:/usr/share/web/logs # here
  ...
  - logs_volume:/usr/share/web/logs # here

```

### logstash

```shell
...

filter {
  mutate {
    split => {"message" => "|"}
    add_field => {
      "ip" => "%{[message][5]}"
    }
    add_field => {
      "function_name" => "%{[message][2]}"
    }
    add_field => {
      "timestamp" => "%{[message][0]}"
    }
    add_field => {
      "level" => "%{[message][1]}"
    }
    remove_field => "host"
    remove_field => "@version"
    remove_field => "@timestamp"
    remove_field => "message"
    remove_field => "ecs"
    remove_field => "tags"
    remove_field => "input"
    remove_field => "log"
    remove_field => "agent"


    add_field => {
      "message" => "%{[message][4]}"
    }
    
  }
  date {
    match => ["timestamp", "YYYY-MM-dd HH:mm:ss.SSS"]
    target => "timestamp"
    timezone => "UTC"
  }
}
...
```
Log data collected by filebeat is processed by logstash. 

```python
LOGGING = {
    ...
    'formatters': {
        'standard': {
            'format': '%(asctime)s.%(msecs)03d|%(levelname)s|%(funcName)s|%(name)s|%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    }
    ...
```
If you need to add log information or collect logs in a different way, modify the log format in settings and the filter section in pipeline/logstach.conf file.

### elasticsearch

```shell
PUT _index_template/<index_name>
{
  "index_patterns" : ["<index_pattern>"],
  "priority" : 1,
  "mappings" : {
    "properties" : {
      "<add your field here>"
    }
  }
}
```
Before collecting logs, you need to create an index template in elasticsearch.

```shell
In default log template
PUT _index_template/<index_name>
{
  "index_patterns" : ["<index_pattern>"],
  "priority" : 1,
  "mappings" : {
    "properties" : {
      "ip" : {"type" : "ip"},
      "function_name" : {
          "type":"text",
          "fields" : {
            "keyword" : {"type" : "keyword"}
          }
        },
      level : {"type" : "keyword"},
      "timestamp" : "date"
    }
  }
}
```

### django api

The API for collecting logs has been created simply for testing purposes.
You should overwrite urls.py, veiws.py for log collection
