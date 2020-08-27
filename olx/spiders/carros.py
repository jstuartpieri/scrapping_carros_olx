# -*- coding: utf-8 -*-
import scrapy


class CarrosSpider(scrapy.Spider):
    name = 'carros'
    allowed_domains = ['sp.olx.com.br']
    start_urls = ['https://sp.olx.com.br/sao-paulo-e-regiao/autos-e-pecas/carros-vans-e-utilitarios?pe=18000']

    def parse(self, response):
        links = response.xpath("//div[@class='sc-1fcmfeb-0 WQhDk']/ul/li/a")
        next_page = response.xpath("//a[@data-lurker-detail='next_page']/@href").get()

        for link in links:
            product_link = link.xpath(".//@href").get()
            yield scrapy.Request (url = product_link, callback = self.parse_cars,  meta = {'link': product_link})
        

        if next_page:
            yield scrapy.Request(url = next_page, callback = self.parse)

    
    def parse_cars (self, response):
        obs = response.xpath("//div[@class='sc-jTzLTM sc-hmzhuo sc-4x7g5o-1 hvIDBk']")
        link = response.request.meta['link']
        all_obs = []

        for i in range(len(obs)):
            all_obs.append(obs[i].xpath(".//text()").get())

        yield {
            'nome': response.xpath("//h1[@class='sc-ifAKCX sc-1q2spfr-0 fxvTMe']/text()").get(),
            'preço': response.xpath("//h2[@class='sc-ifAKCX sc-1leoitd-0 buyYie']/text()").get(),
            'OBS': all_obs,
            'Texto': response.xpath("//span[@class='sc-ifAKCX sc-1sj3nln-1 eqxsIR']/text()").get(),
            'Modelo': response.xpath("//div[@class='sc-jTzLTM sc-hmzhuo sc-1g2w54p-1 JeNxq']/div[@class='sc-bwzfXH h3us20-0 cBfPri']/div[position() = 2]/div/div[@ml=3]/a/text()").get(),
            'Marca': response.xpath("//div[@class='sc-jTzLTM sc-hmzhuo sc-1g2w54p-1 JeNxq']/div[@class='sc-bwzfXH h3us20-0 cBfPri']/div[position() = 3]/div/div[@ml=3]/a/text()").get(),
            'Tipo de veículo': response.xpath("//div[@class='sc-jTzLTM sc-hmzhuo sc-1g2w54p-1 JeNxq']/div[@class='sc-bwzfXH h3us20-0 cBfPri']/div[position() = 4]/div/div[@ml=3]/span[@class='sc-ifAKCX eeuILE']/text()").get(),
            'Ano': response.xpath("//div[@class='sc-jTzLTM sc-hmzhuo sc-1g2w54p-1 JeNxq']/div[@class='sc-bwzfXH h3us20-0 cBfPri']/div[position() = 5]/div/div[@ml=3]/a/text()").get(),
            'KM': response.xpath("//div[@class='sc-jTzLTM sc-hmzhuo sc-1g2w54p-1 JeNxq']/div[@class='sc-bwzfXH h3us20-0 cBfPri']/div[position() = 6]/div/div[@ml=3]/span[@class='sc-ifAKCX eeuILE']/text()").get(),
            'Motor': response.xpath("//div[@class='sc-jTzLTM sc-hmzhuo sc-1g2w54p-1 JeNxq']/div[@class='sc-bwzfXH h3us20-0 cBfPri']/div[position() = 7]/div/div[@ml=3]/span[@class='sc-ifAKCX eeuILE']/text()").get(),
            'Combustivel': response.xpath("//div[@class='sc-jTzLTM sc-hmzhuo sc-1g2w54p-1 JeNxq']/div[@class='sc-bwzfXH h3us20-0 cBfPri']/div[position() = 8]/div/div[@ml=3]/a/text()").get(), 
            'Câmbio': response.xpath("//div[@class='sc-jTzLTM sc-hmzhuo sc-1g2w54p-1 JeNxq']/div[@class='sc-bwzfXH h3us20-0 cBfPri']/div[position() = 9]/div/div[@ml=3]/span[@class='sc-ifAKCX eeuILE']/text()").get(), 
            'Direção': response.xpath("//div[@class='sc-jTzLTM sc-hmzhuo sc-1g2w54p-1 JeNxq']/div[@class='sc-bwzfXH h3us20-0 cBfPri']/div[position() = 10]/div/div[@ml=3]/span[@class='sc-ifAKCX eeuILE']/text()").get(),
            'Cor': response.xpath("//div[@class='sc-jTzLTM sc-hmzhuo sc-1g2w54p-1 JeNxq']/div[@class='sc-bwzfXH h3us20-0 cBfPri']/div[position() = 11]/div/div[@ml=3]/span[@class='sc-ifAKCX eeuILE']/text()").get(),
            'Portas': response.xpath("//div[@class='sc-jTzLTM sc-hmzhuo sc-1g2w54p-1 JeNxq']/div[@class='sc-bwzfXH h3us20-0 cBfPri']/div[position() = 12]/div/div[@ml=3]/span[@class='sc-ifAKCX eeuILE']/text()").get(),
            'Final da Placa': response.xpath("//div[@class='sc-jTzLTM sc-hmzhuo sc-1g2w54p-1 JeNxq']/div[@class='sc-bwzfXH h3us20-0 cBfPri']/div[position() = 13]/div/div[@ml=3]/span[@class='sc-ifAKCX eeuILE']/text()").get(),
            'link': link
        }
