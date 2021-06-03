# -*- coding: utf-8 -*-
import scrapy

from ..items import TestxItem
from .. import settings

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        x = TestxItem()
        print("===Existing settings: {}".format(self.settings.attributes.keys()))
        print "="*30
        for k, v in self.settings.attributes.items():
            print 'key:{},val:{}'.format(k, v)
        print "xxxx=>", self.settings.attributes.get('CSV_DELIMITER', ',')
