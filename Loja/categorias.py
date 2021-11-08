import scrapy

class SkeletonSpider(scrapy.Spider):
    name = 'spider-mummy'
    start_urls = ['http://www.someonlinewebstore.com']

    def parse(self, response):
        for c in [...]:
            url_category = ...
            yield scrapy.Request(url_category, self.parse_category_page)

    def parse_category_page(self, response):
        for p in [...]:
            url_product = ...
            yield scrapy.Request(url_product, self.parse_product)

    def parse_product(self, response):
        ...