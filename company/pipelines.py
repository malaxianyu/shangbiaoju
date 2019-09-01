# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings


class CompanyPipeline(object):

    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']

        client = pymongo.MongoClient(host=host,port=port)

        mdb = client[dbname]
        self.collection = mdb[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        data = dict(item)
        self.collection.update_one({'reg_name':data['reg_name']},{'$set':{'reg_number':data['reg_number']}},True,True)
        # self.collection.insert(data)
        return item
