from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import requests
from requests.cookies import RequestsCookieJar
import json
import os
from bs4 import BeautifulSoup


def requests_save_cookies():
    session = requests.Session()
    session.get('https://www.baidu.com')
    cookies = requests.utils.dict_from_cookiejar(session.cookies)
    with open('cookies.txt', 'w') as f:
        json.dump(cookies, f)


def requests_load_cookies():
    session = requests.Session()
    jar = RequestsCookieJar()
    with open('cookies.txt', 'r') as f:
        cookies = json.load(f)
        for cookie in cookies:
            jar.set(cookie['name'], cookie['value'])
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/80.0.3987.87 Safari/537.36'}
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
    response = session.get('', headers=headers, cookies=jar)
    print(BeautifulSoup(response.text, 'lxml'))


def selenium_login():
    button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#switchAccountLogin')))
    button.click()

    # switch iframe
    password_login_frame = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginDiv"]/iframe')))
    browser.switch_to.frame(password_login_frame)

    time.sleep(2)

    user_name = wait.until(EC.presence_of_element_located((By.NAME, 'email')))
    password = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
    login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#dologin')))
    remember_me = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#un-login')))
    remember_me.click()
    user_name.clear()
    password.clear()
    user_name.send_keys('zhengxinyue9099')
    time.sleep(2)
    password.send_keys('Zxy123456')
    login_button.click()
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#h1Logo')))
        print('succeed')
        cookies = browser.get_cookies()
        with open('cookies.txt', 'w') as f:
            json.dump(cookies, f)
    except TimeoutException:
        print('fail')
        selenium_login()
    finally:
        browser.close()


def selenium_load_cookies():
    with open('cookies.txt', 'w') as f:
        cookies = json.load(f)
        for cookie in cookies:
            browser.add_cookie(cookie)


if __name__ == '__main__':
    if not os.path.exists('cookies.txt'):
        browser = webdriver.Chrome(executable_path=r'D:\chromewebdriver\chromedriver_win32\chromedriver.exe')
        browser.get('https://mail.163.com/')
        wait = WebDriverWait(browser, 10)
        selenium_login()
    requests_load_cookies()

