import requests
from bs4 import BeautifulSoup
import time


"""
finished
"""


def download_one_page(url):
    response = requests.get(url)
    content = BeautifulSoup(response.text, 'lxml')
    book_list = content.find('ul', class_='bang_list clearfix bang_list_mode').find_all('li')
    book_info = []
    for book in book_list:
        name = book.find('div', class_='name').a['title']
        star = book.find('div', class_='star').find('span', class_='tuijian').string
        star_number = book.find('div', class_='star').a.string
        price = book.find('div', class_='price').find('span', class_='price_n').string
        book_info.append([name, star, star_number, price])
    return book_info


def write_to_file(item):
    with open('data/book.txt', 'a', encoding='UTF-8') as f:
        for i in item:
            f.write(str(i) + '\n')


if __name__ == '__main__':
    for i in range(1, 26):
        info = download_one_page('http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-%d' % i)
        print(str(i) + 'finished')
        time.sleep(60)
        write_to_file(info)


