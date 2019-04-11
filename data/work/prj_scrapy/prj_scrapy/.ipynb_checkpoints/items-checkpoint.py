# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PrjScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class EncansItem(scrapy.Item):
    id = scrapy.Field() 
    batch_id = scrapy.Field()
    scraped_time = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    