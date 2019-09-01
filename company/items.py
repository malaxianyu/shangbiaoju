# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    reg_name = scrapy.Field()    # 公司名
    reg_number = scrapy.Field()    # 注册号
    # company_name = scrapy.Field()
    # company_name = scrapy.Field()
    # company_name = scrapy.Field()
