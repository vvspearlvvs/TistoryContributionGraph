import os
import re
from requests import get
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

kakao_id =""
kakao_pw =""
client_id=""
client_secret=""
redirect_url ="http://tistory.com"
chromedriver_path = "C:/Users/gg664/IdeaProjects/TistoryJandi-graph/tistory-contribution-graph-master/crawling/chromedriver.exe"

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
    url ="https://www.tistory.com/auth/login?redirect_uri=%s" % (redirect_url)
    driver.get(url) #로그인방법 선택페이지 접근
    driver.find_element_by_xpath('//*[@id="cMain"]/div/div/div/a[1]/span[2]').click() #카카오로 로그인선택
    driver.find_element_by_name('email').send_keys(kakao_id) #id입력
    driver.find_element_by_name('password').send_keys(kakao_pw) #pw입력
    driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button[1]').click() #로그인 선택

    print("로그인완료!")
    return driver

# authentication code 정보를 가져옵니다.
def get_authentication_code(driver, client_id, redirect_url):
    req_url = 'https://www.tistory.com/oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code&state=langoo' % (client_id, redirect_url)
    driver.get(req_url) #접근허가 페이지 접근
    print(req_url)
    driver.implicitly_wait(5)

    #print(driver.page_source)
    #element = driver.find_element_by_xpath("//button[@onclick=\"controlOAuthPopup('ok')\"]")
    #print(element)
    #driver.execute_script("javascript:controlOAuthPopup('ok')")
    print("허가 선택완료!")
    redirect_url = driver.current_url
    temp = re.split('code=', redirect_url) #리다이렉션 페이지에서 code= 뒷부분 가져옴
    code = re.split('&state=', temp[1])[0]
    return code


# http://www.tistory.com/guide/api/index
# access token 정보를 가져옵니다.
def get_access_token(code, client_id, client_secret, redirect_url):
    url = 'https://www.tistory.com/oauth/access_token?'
    payload = {'client_id': client_id,
               'client_secret': client_secret,
               'redirect_uri': redirect_url,
               'code': code,
               'grant_type': 'authorization_code'}
    res = get(url, params=payload)
    token = res.text.split('=')[1]
    return token


def main():
    driver = tistory_login()
    code = get_authentication_code(driver, client_id, redirect_url)
    token = get_access_token(code, client_id, client_secret, redirect_url)
    print(token)


if __name__ == '__main__':
    main()
