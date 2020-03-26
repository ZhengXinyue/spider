import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from fake_useragent import UserAgent


"""
finished
"""


def get_page(url):
    response = requests.get(url, headers=headers)
    response = BeautifulSoup(response.text, 'lxml')
    process(response)


def process(r):
    article_list = r.find('div', id='post_list').find_all('div', class_='post_item')
    for article in article_list:
        title = article.find(class_='titlelnk').string
        link = article.find(class_='titlelnk')['href']
        info = list(article.find(class_='post_item_foot').stripped_strings)
        author = info[0]
        date = info[1]
        comment = info[2]
        view = info[3]
        data.append([title, link, author, date, comment, view])


if __name__ == '__main__':
    base_url = 'https://www.cnblogs.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/80.0.3987.87 Safari/537.36'}
    random_headers = {'User-Agent': UserAgent().random}
    data = []
    for page_num in range(1, 3):
        if page_num == 1:
            url = base_url
        else:
            url = base_url + 'sitehome/p/%d' % page_num
        get_page(url)
        print('%d finished' % page_num)
        time.sleep(2)
    df = pd.DataFrame(data, columns=['title', 'link', 'author', 'date', 'comment', 'view'])
    df.to_excel('data/bokeyuan-data.xlsx', encoding='UTF-8')