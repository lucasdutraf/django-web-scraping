from .scraper_helper import *
from .models import Item

def add_product(id, name, price, image_link):
    Item.objects.create(id=id, name=name, price=price, image_link=image_link)

def populate_product_db():
    names = get_all_product_name()
    prices = get_all_products_price()
    image_links = get_all_image_links()
    for elements in range(len(names)):
        id = elements + 1
        name = names[elements]
        price = prices[elements]
        image_link = image_links[elements]
        add_product(id, name, price, image_link)