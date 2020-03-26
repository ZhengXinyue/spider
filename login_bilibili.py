from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

"""
滑动验证码问题
"""

base_url = 'https://passport.bilibili.com/login'
browser = webdriver.Chrome(executable_path=r'D:\chromewebdriver\chromedriver_win32\chromedriver.exe')
browser.set_window_size(1600, 900)
wait = WebDriverWait(browser, 10)
browser.get(base_url)

user_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#login-username')))
passpword = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#login-passwd')))
user_name.send_keys('15651015503')
passpword.send_keys('Zxy123456')

submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#geetest-wrap > div > div.btn-box > '
                                                                        'a.btn.btn-login')))
submit_button.click()


# browser.close()