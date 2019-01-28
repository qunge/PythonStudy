import itchat

"""
# 简单入门示例，有了itchat，如果你想要给文件传输助手发一条信息，只需要这样：
itchat.auto_login()
itchat.send('Hello,fileHelper', toUserName='filehelper')
"""


# 如果你想要回复发给自己的文本消息，只需要这样：回复同样的内容
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text


itchat.auto_login()
itchat.run()
