# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FindlawItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    name = scrapy.Field()
    firm = scrapy.Field()
    streetAddress = scrapy.Field()
    addressLocality = scrapy.Field()
    addressRegion = scrapy.Field()
    postalCode = scrapy.Field()
    officeInfo = scrapy.Field()

    pass
