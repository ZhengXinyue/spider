from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from PIL import Image
import time
from random import uniform
from io import BytesIO

"""
点触式验证码识别： 按顺序拿到字符的坐标
"""


def main():
    user_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#session_email_or_mobile_number')))
    password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#session_password')))
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#sign-in-form-submit-btn')))

    user_name.clear()
    password.clear()
    user_name.send_keys('15651015503')
    time.sleep(uniform(1, 2))
    password.send_keys('Zxy123456')
    time.sleep(uniform(1, 2))
    login_button.click()

    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_item_img')))
    location = element.location
    size = element.size
    top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size['width']
    screenshot = browser.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))
    jianshu_code = screenshot.crop((left, top, right, bottom))



    # # 获取验证码url
    # wait.until(EC.presence_of_element_located((
    #     By.CSS_SELECTOR, 'body > div:nth-child(9) > div.geetest_panel_box.geetest_no_logo.geetest_panelshowclick'
    #                      ' > div.geetest_panel_next > div > div > div.geetest_head > div.geetest_tips > '
    #                      'div.geetest_tip_img')))
    #
    # soup = BeautifulSoup(browser.page_source, 'lxml')
    # image_url = soup.select('body > div:nth-child(9) > div.geetest_panel_box.geetest_no_logo.geetest_panelshowclick '
    #                         '> div.geetest_panel_next > div > div > div.geetest_head > div.geetest_tips > '
    #                         'div.geetest_tip_img')[0]['style'].split('"')[1]
    # # 获取验证码
    # image_content = requests.get(image_url, headers=headers).content
    # image = Image.open(BytesIO(image_content))



if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/80.0.3987.87 Safari/537.36'}
    browser = webdriver.Chrome(executable_path=r'D:\chromewebdriver\chromedriver_win32\chromedriver.exe')
    browser.get('https://www.jianshu.com/sign_in')
    browser.maximize_window()
    wait = WebDriverWait(browser, 10)
    main()
