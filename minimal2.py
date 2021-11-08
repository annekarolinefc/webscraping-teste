#CODIGO MAIS ENXUTO

import scrapy

class MinimalSpider(scrapy.Spider):
    """A menor Scrapy-Aranha do mundo!"""
    name='minimal'

    #retorna um iterable contento as primeiras requisições feitas para o spider. Geração de requisições HTTP(objeto do tipo Request)
    #esse exemplo retorna uma lista de requisições simples para o site do Google e do Yahoo
    start_urls = [
        'http://www.google.com',
        'http://yahoo.com',
        ]

    #registrar função callback para objetos do tipo Request
    def parse(self, response):
        self.log('Acessando URL: %s' %response.url)

