from ..items import TutorialItem
import scrapy
from bs4 import BeautifulSoup


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        data_list = soup.find(class_='col-md-8').find_all(class_='quote')
        for data in data_list:
            item = TutorialItem()
            item['text'] = data.find(class_='text').string
            item['author'] = data.find(class_='author').string
            item['tags'] = ', '.join(i.string for i in data.find(class_='tag'))
            yield item
        try:
            next = soup.find(class_='next').a['href']
        except Exception as e:
            next = None
        if next:
            url = response.urljoin(next)
            yield scrapy.Request(url, callback=self.parse)

