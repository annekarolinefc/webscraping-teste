import scrapy

#subclasse de scrapy.Item: adiciona os campos desejados
class Produto(scrapy.Item):
    descricao = scrapy.Field()
    preco = scrapy.Field()
    marca = scrapy.Field()
    categoria = scrapy.Field()