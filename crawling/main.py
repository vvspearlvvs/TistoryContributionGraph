import os
import re
from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# tistory에 로그인을 합니다.
def tistory_login():
    #tistory_id = os.environ.get('TISTORY_ID')
    #tistory_pw = os.environ.get('TISTORY_PW')
    #chromedriver_path = os.environ.get('CHROMEDRIVER_PATH')
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # chrome 띄워서 보려면 주석처리
    driver = webdriver.Chrome(chromedriver_path, options=chrome_options)
    driver.implicitly_wait(3)
    '''
    driver.get('https://www.tistory.com/auth/login?redirectUrl=http%3A%2F%2Fwww.tistory.com%2F')
    driver.find_element_by_name('loginId').send_keys(tistory_id)
    driver.find_element_by_name('password').send_keys(tistory_pw)
    driver.find_element_by_xpath('//*[@id="authForm"]/fieldset/button').click()
    '''

    driver.get("https://www.tistory.com/auth/login")
    driver.find_element_by_xpath('//*[@id="cMain"]/div/div/div/a[1]/span[2]').click()
    driver.find_element_by_name('email').send_keys(kakao_id)
    driver.find_element_by_name('password').send_keys(kakao_pw)
    driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button[1]').click()

    print("로그인완료!")
    return driver


def main():
    #client_id = os.environ.get('TISTORY_CLIENT_ID')
    #client_secret = os.environ.get('TISTORY_CLIENT_SECRET')
    #redirect_url = os.environ.get('TISTORY_REDIRECT')
    driver = tistory_login()



if __name__ == '__main__':
    main()
