![](logoimg.png)
# Zapay Challenge

## Pré-requisitos para execução do projeto
* python3
* pip
* virtualenv

## Como executar o projeto?
O primeiro passo é criar um ambiente virtual que utilize python3 atráves do seguinte comando  
``` $ virtualenv -p python3 venv ```  
Após esse passo bem-sucedido é necessário acessar o ambiente virtual criado  
``` $ source venv/bin/activate ```  
Agora finalmente para executar o projeto basta executar o script  
``` $ sh ./run.sh ```  
O projeto estará disponível para acesso pelo browser ou ferramenta de requisições no seguinte endereço  
``` http://localhost:8800/products```  


## Como testar o projeto?
As urls disponíveis para uso são _/products_ e _/product/id_, onde o id corresponde ao número único atribuído a cada item da página.

## Bibliotecas externas utilizadas
* Requests
* bs4 - BeautifulSoup
  
## Quais os padrões adotados para o desenvolvimento?
Decidi desacoplar o código o máximo que pude, assim, criando arquivos e funções indepentes para executar as diferentes necessidades para funcionamento da aplicação. A lógica para execução do _Web Scraping_ se encontra no arquivo [/product_scraper/scraper_helper.py](https://github.com/lucasdutraf/django-web-scraping/blob/devel/product_scraper/scraper_helper.py), já a comunicação com o banco de dados está em [/product_scraper/db_helper.py](https://github.com/lucasdutraf/django-web-scraping/blob/devel/product_scraper/db_helper.py). Deste modo, as views tem total independência, sendo responsáveis somente por se comunicar com o banco de dados para retornar em formato _JSON_ os dados.

## Banco de dados utilizado
* SQLite3

## Site utilizado para _Web Scraping_
Disponível em: https://nerdstore.com.br/categoria/especiais/game-of-thrones/
