import scrapy



#aulascrapy/ (raiz)
#├── scrapy.cfg
#└── aulascrapy/
#    ├── spiders/
#    │   ├── __init__.py
#    │   └── citacoes.py  <-- ELE PRECISA ESTAR AQUI!
#    ├── items.py
#    └── settings.py



class SpiderCitacoes(scrapy.Spider):
    name = 'citacoes'

    def start_requests(self):
        urls = [ "https://quotes.toscrape.com/page/1/", "https://quotes.toscrape.com/page/2/" ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            # yield: retorno que nao sai do loop, envia a resposta


    # resultado: ['https:', '','quotes.toscrape.com', 'page', '1', '']
    def parse(self, response):
        pagina = response.url.split("/")[-2] # vai pegar o numero da pagina page/'1'
        nome_arquivo = f'citacoes-{pagina}.html'

        with open(nome_arquivo, 'wb') as f:
            f.write(response.body)

        self.log(f'Arquivo salvo {nome_arquivo}')


        
