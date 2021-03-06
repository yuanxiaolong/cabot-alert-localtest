Cabot Localtest Plugin
=====

## 简介

根据 [https://github.com/bonniejools/cabot-alert-skeleton](https://github.com/bonniejools/cabot-alert-skeleton) 来做一个简单测试

效果：在 ```/tmp/``` 目录下 新建一个空文件 代表执行了报警逻辑，用于本地测试。

```
root@MacBook-Pro ~$ ll /tmp/ | grep cabot
-rw-r--r--   1 root    wheel       0 12 10 14:03 cabotTestLocalAlert_20151210_140306
-rw-r--r--   1 root    wheel       0 12 10 14:15 cabotTestLocalAlert_20151210_141543
```

---

## 插件安装

前置：
* 已进入cabot的安装目录，例如 ``` /usr/local/datacenter/cabot ```
* 已停止 cabot 相关进程，有2组进程。
    * 消息队列处理进程 ```ps -ef | grep python | grep celery``` 10个进程
    * UI 进程 ``` ps -ef | grep python | grep manage.py ``` 1个进程（或许你有其他 django 应用在运行，请自己通过端口区分）
  如果你实在记不清，也可以通过启动日志查看，类似这样的日志
  ```
  14:04:00 web.1    | started with pid 36652
  14:04:00 celery.1 | started with pid 36653
  ```


1.编写配置文件,添加 插件名称（注意是下划线，不是工程名，而是里面的 模块名，由setup.py里指定的）, 并修改 ```setup.py``` 内的相关信息

```
vi conf/development.env

# Plugins to be loaded at launch
CABOT_PLUGINS_ENABLED=cabot_alert_hipchat==1.7.0,cabot_alert_twilio==1.6.1,cabot_alert_email==1.3.1,cabot_alert_localtest==0.0.1

```

2.通过 pip 安装自定义插件

```
pip install git+git://github.com/yuanxiaolong/cabot-alert-localtest.git
```

3.初始化数据库

```
sh setup_dev.sh
```

4.无误后，启动 cabot

``` nohup foreman start & ```

---

## 插件编写

不建议直接 clone 或 fork 此工程，因为此工程是测试工程。可以直接 fork 官方的「骨架工程」 [https://github.com/bonniejools/cabot-alert-skeleton](https://github.com/bonniejools/cabot-alert-skeleton)
然后自己新建个仓库，再cp必要文件过去，进行修改调试
