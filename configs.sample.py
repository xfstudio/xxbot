import os
from random import randint

APP_NAME = '%s-%d' % ('xxbot', randint(0, 100))
LOG_FORMAT = '%(asctime)-15s %(filename)s:%(funcName)s:[%(levelname)s] %(message)s'
JSON_FORMAT = '%(message)s'

DEBUG = True
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DIR = os.path.join(ROOT_DIR, 'test')
LIBS_DIR = os.path.join(ROOT_DIR, 'libs')
PLUGIN_DIR = os.path.join(ROOT_DIR, 'plugin')
MODELS_DIR = os.path.join(ROOT_DIR, 'models')
DATASET_DIR = os.path.join(ROOT_DIR, 'dataset')
TEST_DATA_DIR = os.path.join(TEST_DIR, 'data')
LOG_DIR = os.path.join(ROOT_DIR, 'log')
INPUT_DIR = os.path.join(ROOT_DIR, 'input')
OUTPUT_DIR = os.path.join(ROOT_DIR, 'output')

ATTACHMENTS_DIR = os.path.join(ROOT_DIR, 'attachments')
IMAGE_DIR = os.path.join(ATTACHMENTS_DIR, 'image')
AVTAR_DIR = os.path.join(ATTACHMENTS_DIR, 'avtar')
XMAS_DIR = os.path.join(ATTACHMENTS_DIR, 'xms')
AUDIO_DIR = os.path.join(ATTACHMENTS_DIR, 'audio')
VEDIO_DIR= os.path.join(ATTACHMENTS_DIR, 'vedio')
# gen_attachment_path = partial(os.path.join, ATTACHMENTS_DIR)

WELCOME_MSG = u'欢迎新朋友，发送“圣诞”、“xms”、“christmas”或者靓照自动送帽子.全能机器人陪聊'
RANDOM_MSG = [u'正在打开PS...', u'正在导入你的照片...', u'正在抠图...', u'正在尬聊...', u'正在制作🎩...', u'正在寻找🎄...']
NUM_MSG = len(random_msg)
ADS_MSG = u'【支付宝】年终红包再加10亿！现在领取还有机会获得惊喜红包哦！长按复制此消息，打开最新版支付宝就能领取！FbZNhS64WT'
ERROR_MSG = u'请上传正面照才能戴的哟：）'
BUILDING_MSG = u'功能正在撸码中:(，加油👨'

ADMINSTRATOR_NAME = u'肖长省'    #定义管理员微信名（必须是机器人的好友）  ps：raw_content字段需要自己手动更改微信名，微信号
ADMINSTRATOR_WECHAT = u'xfolstudio'   #定义管理员微信号（必须是机器人的好友）
ADMIN_GROUP_NAME = u'trade-test'    #定义要查找群的名字（必须添加到通讯录）


def touch(fname: str, times=None, create_dirs: bool = False):
    if create_dirs:
        base_dir = os.path.dirname(fname)
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
    with open(fname, 'a'):
        os.utime(fname, times)


def touch_dir(base_dir: str) -> None:
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)


def _get_logger(name: str):
    import logging.handlers
    touch(LOG_PATH, create_dirs=True)
    touch_dir(MODELS_DIR)
    l = logging.getLogger(name)
    l.setLevel(logging.DEBUG)
    fh = logging.FileHandler(LOG_PATH)
    fh.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    fh.setFormatter(logging.Formatter(LOG_FORMAT))
    ch.setFormatter(logging.Formatter(LOG_FORMAT))
    l.addHandler(fh)
    l.addHandler(ch)
    return l


def get_json_logger(name: str):
    import logging.handlers
    touch(RESULT_PATH, create_dirs=True)
    l = logging.getLogger(__name__ + name)
    l.setLevel(logging.INFO)
    # add rotator to the logger. it's lazy in the sense that it wont rotate unless there are new logs
    fh = logging.FileHandler(RESULT_PATH)
    fh.setLevel(logging.INFO)
    fh.setFormatter(logging.Formatter(JSON_FORMAT))
    l.addHandler(fh)
    return l


LOGGER = _get_logger(__name__)
JSON_LOGGER = get_json_logger('json' + __name__)
