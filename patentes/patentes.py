import scrapy

class Patente(scrapy.Item):
    link = scrapy.Field();
    title = scrapy.Field();
    tags = scrapy.Field();
    #entre outras


class CapturaPatentes(scrapy.Spider):
    name = 'patentes existentes'

    def __init__(self, tag=None):
        patentes_url = 'https://ipportal.wipo.int/'
        if tag:
            patentes_url += '/target/%s' % tag
            self.start_urls = [patentes_url + '?sort=frequent']
