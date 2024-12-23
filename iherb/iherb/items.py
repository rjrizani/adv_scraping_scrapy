# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from datetime import datetime

class IherbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title : str = scrapy.Field()
    price : float = scrapy.Field()
    product_description : str| list = scrapy.Field()
    product_overview: str = scrapy.Field()
    manufacturer: str = scrapy.Field()
    manufacturer_website: str = scrapy.Field()
    rating: float = scrapy.Field()
    total_rating: int = scrapy.Field()
    in_stock: bool = scrapy.Field()
    url : str = scrapy.Field()
    img_url: str = scrapy.Field()
    data_scraped: datetime = scrapy.Field()
