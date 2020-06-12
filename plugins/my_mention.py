from slackbot.bot import respond_to, default_reply, listen_to
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import tweepy
import os
import chromedriver_binary #nopa
import requests
import re
# from ..slackbot_settings import *

url_slackapi = 'https://slack.com/api/files.upload'

# 指定されたURLのフルスクリーンを取得して返却
# @sugoi-bot ss https://news.yahoo.co.jp/
@respond_to('ss(.*)')
def screenshot(message, url):
    #WebDriverのオプションを設定する
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    # x. ブラウザの新規ウィンドウを開く
    print('connectiong to remote brwser...')
    driver = webdriver.Chrome(options=options)

    # 1. Qiita の Chanmoro のプロフィールページにアクセスする
    # driver.get('https://qiita.com/Chanmoro')
    # すたば
    # print(url)
    # driver.get('https://www.starbucks.co.jp/coffee/?nid=mm_01_pc')

    # print(re.sub(r'<|>', '', url))
    driver.get(re.sub(r'<|>', '', url))
    
    print(driver.current_url)

    # 2. 「最近の記事」に表示されている記事一覧の 2 ページ目に移動する
    # driver.find_element(By.XPATH, '//a[@rel="next"]').click()
    # print(driver.current_url)
    # message.send(driver.current_url)
    # > https://qiita.com/Chanmoro?page=2

    # ページが完全に読み込まれるまでの時間を加味して最大5秒間待ち、スクリーンショットを保存して、画像をpost。
    message.send("スクリーンショットを撮ります。")
    print("スクリーンショット")
    driver.set_page_load_timeout(5)

    # フルスクリーンのキャプチャ取得
    page_width = driver.execute_script('return document.body.scrollWidth')
    print(page_width)
    page_height = driver.execute_script('return document.body.scrollHeight')
    print(page_height)
    driver.set_window_size(page_width, page_height)

    driver.save_screenshot('screenshot.png')
    post_file('./screenshot.png')

    #ブラウザを終了する
    driver.quit()


def post_file(file_path):
    files = {'file': open(file_path, 'rb')}
    slackapi_params = {
        'token': os.environ['SLACK_API_TOKEN'],
        'channels': 'test'
    }
    requests.post(url_slackapi, data=slackapi_params, files=files)






@respond_to('searchTweet(.*)')
def search_tweet(message, word):
    #twitterのアクセス情報
    auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
    auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth)
    post_text = ''
    message.send('「'+ word + '」でtweet検索するね…')
    search_results = api.search(q=word, lang='ja', result_type='recent', count=100)

    #検索結果を辞書[検索結果, いいね数]に詰めていく
    result_dictionary = {}

    cnt = 0
    for result in search_results:
        # message.send('検索できてるっぽいっす。')
        cnt += 1
        user = result.user
        name = user.screen_name
        id = result.id
        tweet_link = 'https://twitter.com/' + name + '/status/' +str(id)
        fav = result.favorite_count
        result_text = '\n' + user.name + '@(' + user.screen_name + ')\n' + result.text + '\n(' + str(result.favorite_count) + 'いいね)' + tweet_link + '\n'
        result_dictionary.setdefault(result_text, result.favorite_count)

    print(cnt)

    if len(result_dictionary) == 0:
        message.send('ツイートが見つかりませんでした。')
        return
    
    #いいね数が多い(valueの降順)ものからユーザ情報とつぶやき文章を取得
    loop_count = 0
    for k, v in sorted(result_dictionary.items(), key = lambda x: -x[1]):
        print("---start---")
        loop_count += 1
        post_text = post_text + '---------------------------------------' + k
        
        #5個分のツイートが取れたらループ中断
        if loop_count >= 5:
            break

    message.send(post_text)








@respond_to('今何時')
def now(message):
    strftime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    message.reply(strftime)
    # message.reply('何時だろう？')

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

