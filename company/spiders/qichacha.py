# -*- coding: utf-8 -*-
import scrapy
import pymongo
from urllib import parse


class QichachaSpider(scrapy.Spider):
    name = 'qichacha'
    allowed_domains = ['qichacha.com']
    start_urls = ['https://www.tianyancha.com/']

    def parse(self, response):
        # host = settings['MONGODB_HOST']
        # port = settings['MONGODB_PORT']
        # dbname = settings['MONGODB_DBNAME']
        # client = pymongo.MongoClient(host=host,port=port)
        # mdb = client[dbname]
        # collection = mdb[settings['MONGODB_COLLECTION']]

        # results = collection.find()
        # for info in results[:10]:
        #     reg_name = info['reg_name']
        #     url = 'https://www.tianyancha.com/search?'
        #     kw = {'key':reg_name}
        #     url += parse.urlencode(kw)
        #     yield scrapy.Request(url, callback=self.parse_page)
        pass
