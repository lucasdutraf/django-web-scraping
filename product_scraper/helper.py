import requests
from bs4 import BeautifulSoup

def get_page_content():
    page = requests.get("https://nerdstore.com.br/categoria/especiais/game-of-thrones/")
    page_content = BeautifulSoup(page.content, "html.parser")
    return page_content