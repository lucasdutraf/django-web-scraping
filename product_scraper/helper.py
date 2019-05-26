import requests
from bs4 import BeautifulSoup

def get_page_content():
    page = requests.get("https://nerdstore.com.br/categoria/especiais/game-of-thrones/")
    page_content = BeautifulSoup(page.content, "html.parser")
    return page_content

def get_all_product_name():
    page_content = get_page_content()
    products_name = []
    products_name_elements = page_content.find_all(class_="woocommerce-loop-product__title")
    for names in products_name_elements:
        products_name.append(names.get_text())
    return products_name

def get_all_image_links():
    page_content = get_page_content()
    image_links = []
    image_tag_elements = page_content.find_all(class_="attachment-woocommerce_thumbnail size-woocommerce_thumbnail")
    for link in image_tag_elements:
        image_links.append(link.get("src"))
    return image_links