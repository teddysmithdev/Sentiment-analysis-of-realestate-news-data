# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BlogItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    snippet = scrapy.Field()
    sentiment = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()
    pass
    

class AvgItem(scrapy.Item):
    sentiment_avg = scrapy.Field()
    date = scrapy.Field()
    pass
