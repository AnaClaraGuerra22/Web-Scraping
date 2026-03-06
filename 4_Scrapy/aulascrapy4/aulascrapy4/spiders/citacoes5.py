# AULA 9 - SEGUIR LINKS RECURSIVAMENTE


import scrapy

class QuotesSpider(scrapy.Spider):
    name = "citacoes5" 

    start_urls = ["https://quotes.toscrape.com/page/1/"]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'texto': quote.css('span.text::text').get(),
                'autor': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall()
            }

        partes_url = [p for p in response.url.split("/") if p]
        num_pagina = partes_url[-1] if partes_url[-1].isdigit() else "1"
        
        nome_arquivo = f'citacoes5-pagina-{num_pagina}.html'
        with open(nome_arquivo, 'wb') as f:
            f.write(response.body)

        # 3. Paginação (CORRIGIDO: next_page com underline)
        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            # urljoin transforma "/page/2/" em "https://quotes.toscrape.com/page/2/"
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            self.log("Finalizado: Não há mais páginas.")
