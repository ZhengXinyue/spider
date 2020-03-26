import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import pandas as pd
import time
from random import uniform


"""
finished
"""


def get_page(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return BeautifulSoup(response.text, 'lxml')
        else:
            return None
    except RequestException:
        return None


def parse_page(html):
    movie_list = html.find(class_='board-wrapper').find_all('dd')
    info = []
    for movie in movie_list:
        name = movie.find(class_='name').a['title']
        link = 'https://maoyan.com' + movie.find(class_='name').a['href']
        star = movie.find(class_='star').string.strip()[3:]
        release_time = movie.find(class_='releasetime').string[5:].strip()
        info.append([name, link, star, release_time])
    return info


def main(offset):
    url = 'https://maoyan.com/board/4?offset=%d' % offset
    html = get_page(url)
    if not html:
        print('page %d fails' % (offset / 10))
        return
    info = parse_page(html)
    print('page %d succeeds' % (offset / 10))
    data.extend(info)


if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/80.0.3987.87 Safari/537.36'}
    data = []
    for i in range(10):
        main(i * 10)
        time.sleep(uniform(1, 2))
    df = pd.DataFrame(data, columns=['name', 'link', 'star', 'release_time'])
    df.to_excel('data/maoyan-top100-data.xlsx', encoding='UTF-8')


