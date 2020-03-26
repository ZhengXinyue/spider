import scrapy
from bs4 import BeautifulSoup



class Qiushibaike(scrapy.Spider):
    name = 'qiushibaike'

    def __init__(self):
        super().__init__()
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu '
                                      'Chromium/73.0.3683.86 Chrome/73.0.3683.86 Safari/537.36'}

    def start_requests(self):
        urls = ['https://www.qiushibaike.com/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        with open('qiushibaike.html', 'wb') as f:
            f.write(response.body)

