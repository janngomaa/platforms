# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from prj_scrapy.items import EncansItem


class EncansCrawlerSpider(CrawlSpider):
    name = 'encans_crawler'
    allowed_domains = ['vortexauction.com']
    start_urls = ['https://vr2.vortexauction.com/encanouellette/fr/encans/']
    
    rules = (
        Rule(
            LinkExtractor(
                allow=(['\/fr\/encans\/.*cspq.*']),
                deny=(['\/news\/']),
                canonicalize=False,
                unique=True,
            ),
            callback='parse_item', 
            follow=True
        ),
    )

    def parse_item(self, response):
        deal = EncansItem()
        deal['url'] = response.url
        deal['title'] = response.xpath('//title/text()').extract_first()   
        
        
        yield deal
