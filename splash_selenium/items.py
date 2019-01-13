# -*- coding: utf-8 -*-
import scrapy
class QuoteItem(scrapy.Item):
    content = scrapy.Field()
    author = scrapy.Field()