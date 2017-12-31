#! /usr/bin/env python
# coding: utf-8
from __future__ import print_function
# 
import os, sys, time, random
import dlib
from queue import Queue

from wxpy import *
from configs import *

# TODO: 根据日期时间与内容动态加载模块和配置
from .plugin import Addhat, Faceswapper, Makeup
addhat = Addhat()
swapper = Faceswapper()
makeup = Makeup()

faces = dlib.get_frontal_face_detector()

# 初始化机器人，扫码登陆
bot = Bot(True, True)

# global_use = partial(pytest.fixture, scope='session', autouse=True)



# 自动接受新的好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    new_friend.send(welcome_msg)
    try:
        msg.reply(RANDOM_MSG[random.randint(0,NUM_MSG)] + ADS_MSG)
        avtar_path = os.path.join(AVTAR_DIR, new_friend.uin() + '.jpg')
        avatar = new_friend.get_avatar(avtar_path)
        LOGGER.debug(avtar_path)
        LOGGER.debug(avatar)
        xmas_img = addhat.add_hat_file(avtar_path)
        LOGGER.debug(xmas_img)        
        new_friend.send_image(xmas_img)
    except Exception as e:
        LOGGER.exception(e)
        new_friend.send(ERROR_MSG)
        # raise e
    

# 自动回复图片
@bot.register(msg_types=PICTURE)
def auto_reply_picture(msg):
    # 向好友发送消息
    try:
        msg.reply(RANDOM_MSG[random.randint(0,NUM_MSG)] + ADS_MSG)
        avtar_path = os.path.join(AVTAR_DIR, str(msg.id) + '.jpg')
        avatar = msg.get_file(avtar_path)
        LOGGER.debug(avtar_path)
        LOGGER.debug(avatar)
        xmas_img = addhat.add_hat_file(avtar_path)
        LOGGER.debug(xmas_img)
        msg.reply_image(xmas_img)
    except Exception as e:
        LOGGER.exception(e)
        msg.reply(ERROR_MSG)
        # raise e

# 自动回复语音
@bot.register(msg_types=RECORDING)
def auto_reply_picture(msg):
    # 向好友发送消息
    try:
        msg.reply(RANDOM_MSG[random.randint(0,NUM_MSG)] + ADS_MSG)
        audio_path = os.path.join(AUDIO_DIR, str(msg.id))
        audio = msg.get_file(audio_path)
        LOGGER.debug(audio_path)
        LOGGER.debug(audio)
        msg.reply(building_msg)
    except Exception as e:
        LOGGER.exception(e)
        msg.reply(ERROR_MSG)
        # raise e
        
# 关键字处理
@bot.register(msg_types=TEXT)
def auto_reply_keywords(msg):
    if msg.text.find(u'圣诞') > -1 or msg.text.find(u'xms') > -1 or msg.text.find(u'christmas') > -1:
        try:
            msg.reply(RANDOM_MSG[random.randint(0,NUM_MSG)] + ADS_MSG)
            avtar_path = os.path.join(AVTAR_DIR, str(msg.id) + '.jpg')
            avatar = msg.chat.get_avatar(avtar_path)
            LOGGER.debug(avtar_path)
            LOGGER.debug(avatar)
            xmas_img = addhat.add_hat_file(avtar_path)
            LOGGER.debug(xmas_img)
            msg.reply_image(xmas_img)
        except Exception as e:
            LOGGER.exception(e)
            msg.reply(ERROR_MSG)
            # raise e
    
    elif msg.raw.get('FromUserName') == admin_request_name:
        # adminer = ensure_one(bot.friends(update=True).search(admin_request_name))
        if u'备份' in msg.text:
            msg.sender.send_file('test.log')
        elif msg.text.find(u'群发') >= 0 :
            friendList = bot.friends(update=True)[1:]
            for friend in friendList:
                bot.send(msg.text.replace(u'群发', (friend['DisplayName']
                    or friend['NickName']), friend['UserName']))
                time.sleep(.5)
        else:
            return "请检查命令是否输入正确"
    
    elif msg.is_at :
        my_group = ensure_one(bot.groups(update=True).search(group_name))
        group_admin = my_group.members.search(admin_request_name)[0]
        if '踢出' in msg.text:
            LOGGER.debug(msg.member)
            LOGGER.debug(group_admin)
            if msg.member == group_admin :
                for member_name in msg.text.split('@')[2:]:
                    LOGGER.info(member_name)
                    re_name = my_group.members.search(member_name)[0].remove()
                    LOGGER.info(re_name)
                    msg.sender.send("已经移出:"+member_name)
            else:
                return "你不是管理员不能进行踢人操作"

    else:
        chatbot = Tuling(api_key='42bbff0b64664a1a8014466d7c374352')
        # chatbot = XiaoI('PQunMu3c66bM', 'FrQl1oi1YzpDSULeAIit')
        chatbot.do_reply(msg)

# 进入 Python 命令行、让程序保持运行
embed(local=None, banner=u'进入命令行', shell='python')

# 或者仅仅堵塞线程，后台执行
# bot.join()
# 
# daemon_init('/dev/null','./daemon.log','./daemon.err')
