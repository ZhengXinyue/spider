import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from fake_useragent import UserAgent

"""
拿到弹幕数据网站
"""


if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/80.0.3987.87 Safari/537.36',
               'Referer': 'https://v.youku.com/v_show/id_XMzgzOTgyMzc4MA==.html?spm=a2h0k.11417342.soresults.dplaybutton&s=c6c62a475a5d4a14ab48',
               'Host': 'acs.youku.com',
               'Origin': 'https://v.youku.com'}
    url = ''
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup)