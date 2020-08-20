# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HackernewsItem(scrapy.Item):
    # define the fields for your item here like:
    headline = scrapy.Field()
    date = scrapy.Field()
    author = scrapy.Field()
    link = scrapy.Field()

