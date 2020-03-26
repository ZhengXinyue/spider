from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd


"""
finished
"""


def search():
    try:
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#nav_searchform > input')))
        submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav_searchform"]/div')))
        input.send_keys('蔡徐坤 篮球')
        submit.click()
        print('get to the new page')
        # 出现新窗口，switch过去
        all_h = browser.window_handles
        browser.switch_to.window(all_h[1])

        get_source()
        total_pages = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#all-list > div.flow-loader > '
                                                                                  'div.page-wrap > div > ul > '
                                                                                  'li.page-item.last > button')))
        return int(total_pages.text)
    except TimeoutException:
        return search()


def get_source():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#all-list > div.flow-loader > div.filter-wrap')))
    soup = BeautifulSoup(browser.page_source, 'lxml')
    process(soup)


def next_page(page_num):
    try:
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#all-list > div.flow-loader > '
                                                                              'div.page-wrap > div > ul > '
                                                                              'li.page-item.next > button')))
        next_button.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#all-list > div.flow-loader > div.page-wrap > '
                                                                      'div > ul > li.page-item.active > button'), str(page_num)))
        get_source()
    except TimeoutException:
        browser.refresh()
        return next_page(page_num)


def process(soup):
    video_list = soup.find(class_='video-list clearfix').find_all(class_='video-item matrix')
    for video in video_list:
        title = video.find('a')['title']
        link = video.find('a')['href']
        watch_num = video.find(class_='so-icon watch-num').text
        biubiu = video.find(class_='so-icon hide').text
        date = video.find(class_='so-icon time').text
        info.append([title, link, watch_num, biubiu, date])


def main():
    try:
        pages_num = search()
        for i in range(2, 2):
            next_page(i)
            print('page %d finished.' % i)
    finally:
        browser.close()


if __name__ == '__main__':
    info = []
    browser = webdriver.Chrome(executable_path=r'D:\chromewebdriver\chromedriver_win32\chromedriver.exe')
    browser.set_window_size(1600, 900)
    browser.get('http://www.bilibili.com')
    wait = WebDriverWait(browser, 10)
    main()
    # data = pd.DataFrame(info, columns=['title', 'link', 'watch_num', 'biubiu', 'date'])
    # data.to_excel('data/ikun.xlsx')




