from slackbot.bot import respond_to, default_reply, listen_to
import random
from datetime import datetime
import locale

# locale.setlocale(locale.LC_CTYPE, "Japanese_Japan.932")

@respond_to('今何時')
def now(message):
    # strftime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    # message.reply(strftime)
    message.reply('何時だろう？')

@respond_to('こんにちは')
def mention_func(message):
    message.reply('こんにちは！')

@respond_to('おはよう')
@respond_to('おは')
@respond_to('おはー')
@respond_to('おはようございます')
def mention_func(message):
    message.reply('おはよ～')

@respond_to('進捗どう')
def mention_func(message):
    message.reply('問題ありません')

@respond_to('ねむい')
def mention_func(message):
    message.reply('起きてー！')

@respond_to('これなんだっけ')
def mention_func(message):
    message.reply('確認します')

# #オウム返し
# @respond_to('(.*)')
# def mention_func(message, something):
#     message.reply(something)


@listen_to('(.*)')
def hello(message, something):

# @respond_to('こうぺんちゃん')
# def mention_func(message):
    # if message == "こんにちは":
    #         message.reply('こんにちは！')
    # else:
    i = random.randint(0, 6)
    if i == 0:
        message.reply("立てぇぇ 立つんだぁぁ ジョォォォォ")
    elif i ==1:
        message.reply("燃えたよ… 真っ白… 燃え尽きた… 真っ白な灰に…")
    elif i ==2:
        message.reply("真犯人はこの中にいる！")
    elif i ==3:
        message.reply("飛べねぇ豚はただの豚だ。")
    elif i ==4:
        message.reply("ジッチャンの名にかけて！")
    elif i ==5:
        message.reply("40秒で支度しな")


# #@なしで書き込むと反応する
# @listen_to('私は(.*)です')
# @listen_to('わたしは(.*)です')
# def hello(message, something):
#     message.reply('こんにちは!{0}さん。'.format(something))

@respond_to('今日の天気')
def weather(message):
    import urllib
    import json

    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
    # '130010'とすると東京の情報を取得してくれる
    # ここを変えれば任意の地域の天気情報を取得できる
    city_id = '140010'
    html = urllib.request.urlopen(url + city_id)
    jsonfile = json.loads(html.read().decode('utf-8'))
    title = jsonfile['title'] 
    telop = jsonfile['forecasts'][0]['telop']
    #telopが晴れだったら晴れのスラックのアイコンとか場合分け
    telop_icon = ''
    if telop.find('雪') > -1:    
        telop_icon = ':showman:'
    elif telop.find('雷') > -1:
        telop_icon = ':thinder_cloud_and_rain:'
    elif telop.find('晴') > -1:
        if telop.find('曇') > -1:
            telop_icon = ':partly_sunny:'
        elif telop.find('雨') > -1:
            telop_icon = ':partly_sunny_rain:'
        else:
            telop_icon = ':sunny:'
    elif telop.find('雨') > -1:
        telop_icon = ':umbrella:'
    elif telop.find('曇') > -1:
        telop_icon = ':cloud:'
    else:
        telop_icon = ':fire:'
    text = title + '\n' + '今日の天気　' + telop + telop_icon
    message.send(text) 

