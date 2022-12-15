from dingtalkchatbot.chatbot import DingtalkChatbot
from django.conf import settings


def send(message, at_mobiles=[]):
	# 2022.9.22 新建的机器人需要启用加签中的其中一个功能才可以使用
	djbot = DingtalkChatbot(settings.DINGTALK_WEB_HOOK, secret=settings.DINGTALK_SECRET)

	if len(at_mobiles) > 0:
		djbot.send_text(msg=("面试通知:\n{}".format(message)), at_mobiles=at_mobiles)
	else:
		djbot.send_text(msg=("面试通知:\n{}".format(message)), is_at_all=True)
