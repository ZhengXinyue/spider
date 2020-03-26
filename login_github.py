import requests
from bs4 import BeautifulSoup
import pandas as pd


"""
finished
"""


def get_token():
    response = session.get(login_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    token = soup.select('#login > form > input[type=hidden]:nth-child(1)')[0]['value']
    return token


def login(token):
    post_data = {'commit': 'Sign in',
                 'authenticity_token': token,
                 'utf8': '✓',
                 'login': user_name,
                 'password': password}
    response = session.post('https://github.com/session', data=post_data, headers=headers)
    if response.status_code == 200:
        print('login succeeded')
        return BeautifulSoup(response.text, 'lxml')
    else:
        print('login failed')


def parse_page(r):
    repo_list = r.find('ul', class_='list-style-none').find_all('li')
    for repo in repo_list:
        name = repo.a['href']
        data.append(name)


def main():
    token = get_token()
    r = login(token)
    if r:
        parse_page(r)


if __name__ == '__main__':
    session = requests.Session()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/80.0.3987.87 Safari/537.36',
               'Referer': 'https://github.com',
               'Host': 'github.com'}
    login_url = 'https://github.com/login'
    user_name = '909956683@qq.com'
    password = 'Zxy031510430'
    data = []
    main()
    df = pd.DataFrame(data, columns=['repo_name'])
    df.to_excel('data/repo-data.xlsx', encoding='UTF-8')