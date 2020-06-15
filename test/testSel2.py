import chromedriver_binary #nopa
from selenium import webdriver
from selenium.webdriver.common.by import By

#WebDriverのオプションを設定する
options = webdriver.ChromeOptions()
# options.add_argument('--headless')

# x. ブラウザの新規ウィンドウを開く
print('connectiong to remote brwser...')
driver = webdriver.Chrome(options=options)

# 1. Qiita の Chanmoro のプロフィールページにアクセスする
driver.get('https://qiita.com/Chanmoro')
print(driver.current_url)

# 2. 「最近の記事」に表示されている記事一覧の 2 ページ目に移動する
driver.find_element(By.XPATH, '//a[@rel="next"]').click()
print(driver.current_url)
# > https://qiita.com/Chanmoro?page=2

# 3. 2 ページ目の一番最初に表示されている記事のタイトルを URL を取得する
# print(driver.find_elements(By.CLASS_NAME ,'AllArticleList__ItemBodyTitle-mhtjc8-6'))
article_links = driver.find_elements(By.CLASS_NAME ,'AllArticleList__ItemBodyTitle-mhtjc8-6')
# print(article_links[0])
# print(article_links[0].text)
# print(article_links[0].get_attribute('href'))

# ページが完全に読み込まれるまでの時間を加味して最大5秒間待ち、スクリーンショットを保存して、画像をpost。
print("スクリーンショット")
driver.set_page_load_timeout(5)
driver.save_screenshot('screenshot.png')
# post_file('./screenShot.png')




#ブラウザを終了する
driver.quit()