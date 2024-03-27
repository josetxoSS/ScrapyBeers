# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BeersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name_beer = scrapy.Field()
    name_brewery = scrapy.Field()
    beer_style = scrapy.Field()
    alcohol_content = scrapy.Field()
    fermentation = scrapy.Field()
    ingredients = scrapy.Field()
    color_transparency = scrapy.Field()
    serving_temperature = scrapy.Field()
    serving_glass = scrapy.Field()
    character_tastes_aromas = scrapy.Field()
    culinary = scrapy.Field()
    keeping_storage = scrapy.Field()
    #availability = scrapy.Field() #Image dont extract

    pass
