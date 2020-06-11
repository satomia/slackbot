import chromedriver_binary #nopa
from selenium import webdriver

#WebDriverのオプションを設定する
options = webdriver.ChromeOptions()
# options.add_argument('--headless')

print('connectiong to remote brwser...')
driver = webdriver.Chrome(options=options)

driver.get('http://qiita.com')
print(driver.current_url)

#ブラウザを終了する
driver.quit()