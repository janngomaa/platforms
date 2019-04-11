# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime
import configparser
import json
import hashlib

from scrapy.exceptions import DropItem


class EncansItem(object):
    #helper = SourceFileLoader("ShudHelper", "/home/jovyan/work/shud/helper/helper.py").load_module()
    #config = helper.ShudHelper.getConfig()
    config = configparser.ConfigParser()
    config.read('encans.ini')
        
    startTime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S.%f")
    batch_id = "encans_" + startTime
    fileName = config.get('dir', 'datadir') + batch_id + '.jl'
    
    def open_spider(self, spider):
        self.file = open(self.fileName, 'w')

    def close_spider(self, spider):
        self.file.close()
        #Insert into param table
        
        
    def process_item(self, item, spider):
        if item['url'] is None:
            raise DropItem("Missing title in %s" % item)
            return
        else:
            item['scraped_time'] = self.startTime
            item['batch_id'] = self.batch_id
            item['id'] = hashlib.md5(bytes(str(item['url']),"ascii")).hexdigest()
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
            return item
    
class PrjScrapyPipeline(object):
    def process_item(self, item, spider):
        return item
