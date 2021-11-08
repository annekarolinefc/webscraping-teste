#importar scrapy
import scrapy

#cria uma classe quotesSpider
class QuotesSpider(scrapy.Spider): #tem como entrada o scrapy.spider
    name = 'QuotesSpider'
    start_ruls=["https://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.xpath("*//div[@class='quote']")
        #para q em quotes
        for q in quotes:
            
            #retornar
            yield{
                #dicionario
                'title': q.xpath(".//span[@class='text']/text()").get(),
                'author': q.xpath(".//small[@class='author']/text()").get(),
                'tags': q.xpath(".//div[@class='tag']/a[@class='tag']/text()").getall()
            }
            
        next_page = response.xpath("*//li[@class='next']/a/@href").get();

        #se a nova pagina nao for nula
        if next_page is not None:
            #acessar nova url
            yield scrapy.Request(response.urljoin(next_page))#https://quotes.toscrape.com/page/2