import pandas as pd
import time
from random import uniform
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from io import BytesIO
from PIL import Image


"""
源码变化问题
图片问题
"""


def get_page(page_num):
    print('working at page %d' % page_num)






def parse_page(html):
    pass


def get_cookie():
    browser.get(base_url)
    login_page = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_SiteNavLogin > div.site-nav-menu-hd > '
                                                                    'div.site-nav-sign > a.h')))
    # get to the new page
    login_page.click()

    weibo_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_OtherLogin > a.weibo-login')))
    weibo_login.click()
    # pl_login_logged > div > div:nth-child(2) > div > input
    user_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pl_login_logged > div > div:nth-child(2) > div > input')))
    password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pl_login_logged > div > div:nth-child(3) > div > input')))
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#pl_login_logged > div > div:nth-child(7) > div:nth-child(1) > a > span')))
    user_name.clear()
    password.clear()
    user_name.send_keys('15651015503')
    password.send_keys('Zxy123456')

    # Get the identify code image
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pl_login_logged > div > div:nth-child(4) > div > a.code > img'))).screenshot_as_png
    target_image = Image.open(BytesIO(element))

    # login_button.click()
    cookie = browser.get_cookies()
    return cookie


def main():
    cookie = get_cookie()

    # for page_num in range(1, max_page + 1):
    #     html = get_page(page_num)
    # info = parse_page(html)
    # data.extend(info)


if __name__ == '__main__':
    data = []
    key_word = 'ipad'
    base_url = 'https://www.taobao.com/'
    max_page = 5

    options = webdriver.ChromeOptions()
    # 不加载图片
    # options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    # 开发者模式
    # options.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(executable_path=r'D:\chromewebdriver\chromedriver_win32\chromedriver.exe', options=options)
    wait = WebDriverWait(browser, 10)

    main()

    # df = pd.DataFrame(data, columns=[])
    # df.to_excel('taobao-data.xlsx', encoding='UTF-8')
