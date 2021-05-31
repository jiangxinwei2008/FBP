# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PeilvItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    cc = scrapy.Field()  # changci
    odd = scrapy.Field()  # oddset
    li = scrapy.Field()  # libo
    b5 = scrapy.Field()  # bet365
    jbb = scrapy.Field()  # jinbaobo
    wl = scrapy.Field()  # weilian
    ms = scrapy.Field()  # mingsheng
    ao = scrapy.Field()  # aomen
    hg = scrapy.Field()  # huangguan
    res = scrapy.Field()  # result
    bstype = scrapy.Field()  # bisaitype
    inte = scrapy.Field()  # interwetten
    w = scrapy.Field()  # weide
    ysb = scrapy.Field()  # yishengbo
    b10 = scrapy.Field()  # 10bet
    pin = scrapy.Field()  # Pinnacle
    sna = scrapy.Field()  # SNAI
