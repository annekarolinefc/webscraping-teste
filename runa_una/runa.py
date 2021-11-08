#importar scrapy
import scrapy

class InstituicoesAnima(scrapy.Item):
    nomeInstituicao = scrapy.Field()
    link = scrapy.Field()

#cria uma classe quotesSpider
class RunaSpider(scrapy.Spider): #tem como entrada o scrapy.spider
    name = 'RunaSpider'
    start_url=["https://repositorio.animaeducacao.com.br/"]

    def parse(self, response):
        """Recebe o site da RUNA , encontra os links das instituicoes e gera requisições para a pagina de cada instituição"""
        instituicoes = response.xpath("*//div/span[@class='text'/a]/text()").getall()

        for instituicao in instituicoes:
            #dicionario
            {
                'title': instituicao.xpath("*//div/span[@class='text'/a]/text()").get(),
               
            }

        links_intituicoes = response.xpath(".//div/h4/a/@href")
        links_intituicoes = response.xpath(".//div/h4/a/@href").extract()
        for link in links_intituicoes:
            url_instituicao = response.xpath(".//div/h4/a/@href").extract().get()
            yield scrapy.Request(url_instituicao, self.extrai_intituicao)


    def extrai_intituicao(self, response):
        """Receb a resposta da página de instituicoes e extrai uma instituicao"""
        animaInstituicao = InstituicoesAnima()

        animaInstituicao['nomeInstituicao'] = response.xpath("*//div/span[@class='text'/a]/text()").getall()
        animaInstituicao['link'] = response.xpath(".//div/h4/a/@href")

        yield animaInstituicao



        #response.xpath("*//div/span[@class='text']").getall()
         #response.xpath("*//div/span[@class='text'/a]").getall()
         #INTITUIÇÕES
         #response.xpath("*//div/span[@class='text'/a]/text()").getall()