# makeconfig

根据需要，编写filebeat配置文件，但是filebeat配置文件每主机下，每个应用日志路径，插入字段都有区别，需要区别对待。利用脚本生成，在传入主机使用。


Usage:    
 #python make_config_file.py info.yml
 
filebeat配置样例：    
```
filebeat.prospectors:
####################A0001###############################
- type: log
  enabled: true
  paths:
    - /myapp/apps/java/A0001/module_logs/dev/dev.log
  fields:
    host: "192.168.2.1"
    app: "A0001"
    module: "dev"
  multiline.pattern: '^[0-9]{4}-[0-9]{2}-[0-9]{2}'
  multiline.negate: true
  multiline.match: after
- type: log
  enabled: true
  paths:
    - /myapp/apps/java/A0001/module_logs/test-core/test-core.log
  fields:
    host: "192.168.2.1"
    app: "A0001"
    module: "test-core"
  multiline.pattern: '^[0-9]{4}-[0-9]{2}-[0-9]{2}'
  multiline.negate: true
  multiline.match: after
- type: log
  enabled: true
  paths:
    - /myapp/apps/java/A0001/module_logs/test-nice/test-nice.log
  fields:
    host: "192.168.2.1"
    app: "A0001"
    module: "test-nice"
  multiline.pattern: '^[0-9]{4}-[0-9]{2}-[0-9]{2}'
  multiline.negate: true
  multiline.match: after
####################B0001###############################
- type: log
  enabled: true
  paths:
    - /myapp/apps/java/B0001/module_logs/dev/dev.log
  fields:
    host: "192.168.2.1"
    app: "B0001"
    module: "dev"
  multiline.pattern: '^[0-9]{4}-[0-9]{2}-[0-9]{2}'
  multiline.negate: true
  multiline.match: after
- type: log
  enabled: true
  paths:
    - /myapp/apps/java/B0001/module_logs/test-core-b0001/test-core-b0001.log
  fields:
    host: "192.168.2.1"
    app: "B0001"
    module: "test-core-b0001"
  multiline.pattern: '^[0-9]{4}-[0-9]{2}-[0-9]{2}'
  multiline.negate: true
  multiline.match: after
- type: log
  enabled: true
  paths:
    - /myapp/apps/java/B0001/module_logs/test-core-b0002/test-core-b0002.log
  fields:
    host: "192.168.2.1"
    app: "B0001"
    module: "test-core-b0002"
  multiline.pattern: '^[0-9]{4}-[0-9]{2}-[0-9]{2}'
  multiline.negate: true
  multiline.match: after
output.kafka:
  hosts: ["192.168.2.1:9092","192.168.2.2:9092"]
  topic: "test"
processors:
- drop_fields:
    fields: ["beat.hostname", "beat.name", "beat.version", "host.name", "log.flags","offset"]
```
