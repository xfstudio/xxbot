# xxbot

[![Build Status](https://travis-ci.org/xfstudio/xxbot.svg?branch=master)](https://travis-ci.org/xfstudio/xxbot)
[![Join the chat at https://gitter.im/xxbot/Lobby](https://badges.gitter.im/xxbot/Lobby.svg)](https://gitter.im/xxbot/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Go Report Card](https://goreportcard.com/badge/github.com/xfstudio/xxbot)](https://goreportcard.com/report/github.com/xfstudio/xxbot)
[![codebeat badge](https://codebeat.co/badges/4f78bcb2-bf75-477d-a8f4-b09fde3dae80)](https://codebeat.co/projects/github-com-xfstudio-xxbot-master)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)]()

微信web版API的python实现，通过gevent实现异步处理和模块的动态加载，接入人工智能和机器学习，极速实现个性化可扩展的智能机器人

* 支持多用户(多开)
* 支持掉线后免扫码重登
* 功能以插件的形式提供，可以根据用户（比如付费情况）选择加载或者不加载某插件
* 插件编写简单, 可定制性强, 无需关心API和消息分发，二次开发极为方便
* 对于加载的插件, 使用机器人的终端用户可以通过微信聊天界面动态开启/关闭.
* 目前已提供头像(性别／年龄)识别, gif搜索, 笑话大全, "阅后即焚", 消息跨群转发, 中英互译，图灵，小i，清粉，群管理，圣诞帽，化妆，换脸等多个有趣插件
* 可以发送图片/文字/gif/视频/表情等多种消息

TODO：
* 处理群、公众号、语音、视频消息
* 多轮对话NLP语义处理
* 使用配置中心管理各模块设置，无重启更新
* 增加性能日志监控，根据负载伸缩服务器配置
* 接入Kubernetes，本地模块容器微服务化
* 扩展python，go，c++，php，nodejs，java等开发工具链，接入CI/CD


## 获取源码
git clone https:/github.com/xfstudio/xxbot


## 编译并运行
#### linux/mac
```
pip install -r requirements.txt
python xxbot.py
```


## 功能清单
##### 基于xxbot创建自定义的机器人
```
非特殊关键字文字默认接入图灵机器人
```
###### addhat 戴帽子 faceswapper 换脸 makeup 化妆 eighteen
```
发送一张图片，使用dlib人脸检测，符合配置文件条件（时间段-人像数=处理模块的格式）即进行处理
```
###### 
## 插件列表
###### switcher
一个管理插件的插件
```
#关闭某个插件, 在微信聊天窗口输入
disable faceplusplus
#开启某个插件, 在微信聊天窗口输入
enable faceplusplus
#查看所有插件信息, 在微信聊天窗口输入
dump
```
###### faceplusplus
对收到的图片做面部识别，返回性别和年龄
###### gifer
以收到的文字消息为关键字做gif搜索，返回gif图, 注意返回的gif可能尺度较大，比如文字消息中包含“污”等关键词。
###### replier
对收到的文字/图片消息，做自动应答，回复固定文字消息
###### laosj
随机获取一张美女图片, 在聊天窗口输入
```
美女
```
###### joker
获取一则笑话, 在聊天窗口输入
```
笑话
```
###### revoker
消息撤回插件, 3s后自动撤回手机端所发的文本消息. 机器人发出的消息需要自己在对应插件里写撤回逻辑.

###### system
处理消息撤回/红包等系统提示

###### forwarder
消息跨群转发, 在插件里修改群名的全拼即可.

###### youdao
中英互译插件, 基于有道翻译API

###### verify
自动接受好友请求, 可以按条件过滤

###### share
资源(纸牌屋)自动分发示例

###### config
配置管理插件
设置配置, 在聊天窗口输入
```
set config key value
```
查看配置，在聊天窗口输入
```
get config key
```

## 测试微信
<img src="https://avatars1.githubusercontent.com/u/2246799?s=400&u=3f0598bd8b29283e7367262345bca6811e39c5c2&v=4" width="480" height="480"/>
