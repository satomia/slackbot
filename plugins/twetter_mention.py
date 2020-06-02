from slackbot.bot import Bot, respond_to, listen_to
import re
from datetime import datetime
import locale

locale.setlocale(locale.LC_CTYPE, "Japanese_Japan.932")

# 「@bot名 今何時?」とメッセージすると時間を教えてくれる
# @respond_to('今何時')
# def now(message):
#     strftime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
#     message.reply(strftime)

@respond_to('こんばんは')
def mention_func(message):
    message.reply('こんばんは！')