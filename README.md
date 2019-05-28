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


## Problemas encontrados
Nas últimas horas antes da entrega me deparei com um erro de migrations, quando era utilizada a abordagem de banco de dados que não consegui reverter de maneira alguma. Após algumas pesquisas, percebi que podia ser um erro devido a versão do sqlite3 e que não haviam muitas respostas para o tal erro.  
Assim, tomei a decisão de implementar a view somente fazendo o que era pedido, o Web Scraping e retornando o conteúdo da página, sem demais perfumarias. O código ficou bem curto e não muito bem estruturado, mas foi o que eu pude recorrer nos últimos instantes.  
Para funcionamento da versão com models implentadas, basta trocar o nome da model e e o mesmo em todas as referências e rodar o script novamente. Esta versão se encontra [aqui](https://github.com/lucasdutraf/django-web-scraping/tree/devel). No README.md desta branch contém uma rota a mais, que realiza a pesquisa de produto por id.  

## Como testar o projeto?
A url disponível para uso é _/products_.

## Bibliotecas externas utilizadas
* Requests
* bs4 - BeautifulSoup
  
## Quais os padrões adotados para o desenvolvimento?
Decidi desacoplar o código o máximo que pude, assim, criando arquivos e funções indepentes para executar as diferentes necessidades para funcionamento da aplicação. A lógica para execução do _Web Scraping_ se encontra no arquivo [/product_scraper/scraper_helper.py](https://github.com/lucasdutraf/django-web-scraping/blob/devel/product_scraper/scraper_helper.py), já a comunicação com o banco de dados está em [/product_scraper/db_helper.py](https://github.com/lucasdutraf/django-web-scraping/blob/devel/product_scraper/db_helper.py). Deste modo, as views tem total independência, sendo responsáveis somente por se comunicar com o banco de dados para retornar em formato _JSON_ os dados.  
Além disso, utilizei as branches do git, subindo para a master apenas código estável e funcional e mantendo o desenvolvimento constante na branch devel.  

## Banco de dados utilizado
* SQLite3

## Site utilizado para _Web Scraping_
Disponível em: https://nerdstore.com.br/categoria/especiais/game-of-thrones/
