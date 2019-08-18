import itchat, time
from itchat.content import *


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING],isGroupChat=True)
def text_reply(msg):
    pass


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    pass


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    pass


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    print(msg.text)
    print('消息来自于:',msg.fromUserName)


itchat.auto_login(enableCmdQR=2, hotReload=True)

itchat.run(True)
