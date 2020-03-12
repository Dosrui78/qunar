# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QunarItem(scrapy.Item):
    # define the fields for your item here like:
    collection = 'qunar'
    name = scrapy.Field()
    price = scrapy.Field()
    level = scrapy.Field()
    address = scrapy.Field()
    saleCount = scrapy.Field()
    hot = scrapy.Field()
    comment = scrapy.Field()
