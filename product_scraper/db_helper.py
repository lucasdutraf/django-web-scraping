from .scraper_helper import *

def populate_product_db():
    names = get_all_product_name()
    prices = get_all_products_price()
    image_links = get_all_image_links()
    response = []
    for elements in range(len(names)):
        id = elements + 1
        name = names[elements]
        price = prices[elements]
        image_link = image_links[elements]
        product = {
            "id": id,
            "price": str(price),
            "image_link": str(image_link)
        }
        response.append(product)
    return response