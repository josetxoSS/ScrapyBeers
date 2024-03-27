import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.exceptions import CloseSpider
from scrapy.linkextractors import LinkExtractor
from beers.items import BeersItem
from selenium.webdriver.common.keys import Keys

class BeersSpider(CrawlSpider):
    name = 'beers'
    item_count = 0
    # List of allowed domains to scrape
    allowed_domains = ['www.beertourism.com']
    # Starting URL for the spider
    start_urls = ['https://www.beertourism.com/blogs/belgian-beer']
    # Rules to follow for crawling
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='post-img-wrapp']/a"), callback="parse_item", follow=False),
    )

    def parse_item(self, response):
        #print(response)
        if self.item_count > 2:
            raise CloseSpider('item_exceeded')
        ml_item = BeersItem()
        ml_item["name_beer"] = response.xpath("//h3[@class='entry-title']/text()").get()
        ml_item["name_brewery"] = response.xpath("//div[@class='brewery_details']/b/a/text()").get()
        ml_item["beer_style"] = response.xpath("//h3[contains(text(), 'Beer Style')]/following-sibling::p/text()").get()
        ml_item["alcohol_content"] = response.xpath(
            "//h3[contains(text(), 'Alcohol')]/following-sibling::p/text()").get()
        ml_item["fermentation"] = response.xpath(
            "//h3[contains(text(), 'Fermentation')]/following-sibling::p/text()").get()
        ml_item["ingredients"] = response.xpath(
            "//h3[contains(text(), 'Ingredients')]/following-sibling::p/text()").get()
        ml_item["color_transparency"] = response.xpath(
            "//h3[contains(text(), 'Colour & Transparency')]/following-sibling::p/text()").get()
        ml_item["serving_temperature"] = response.xpath(
            "//h3[contains(text(), 'Serving Temperature')]/following-sibling::p/text()").get()
        ml_item["serving_glass"] = response.xpath(
            "//h3[contains(text(), 'Serving Glass')]/following-sibling::p/text()").get()
        ml_item["character_tastes_aromas"] = response.xpath(
            "//h3[contains(text(), 'Character, Tastes & Aromas')]/following-sibling::p/text()").get()
        ml_item["culinary"] = response.xpath("//h3[contains(text(), 'Culinary')]/following-sibling::p/text()").get()
        ml_item["keeping_storage"] = response.xpath("//h3[contains(text(), 'Keeping and Storage')]/following-sibling::p/text()").get()
        #ml_item["availability"] = response.xpath("//h3[contains(text(), 'Availability')]/following-sibling::p/text()").get()
        #scrapy crawl beers -o output.json
        #scrapy shell https://www.beertourism.com/blogs/belgian-beer/achel-8-blond
        return ml_item
  