# -*- coding: utf-8 -*-
import scrapy
import json
from company.items import CompanyItem


class ShangbiaoSpider(scrapy.Spider):
    name = 'shangbiao'
    allowed_domains = ['wsgg.sbj.cnipa.gov.cn']
    url = 'http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/annSearchDG.html'

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '277',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'tmas_cookie=51947.7703.15402.0000; JSESSIONID=0000TlkK5OqFBU_3hXEYvKOzHjV:1bm104t91; UM_distinctid=16ce6a704661be-0ec0d3992d5c67-c343162-e1000-16ce6a70467359',
        
        'Host': 'wsgg.sbj.cnipa.gov.cn:9080',
        'Origin': 'http://wsgg.sbj.cnipa.gov.cn:9080',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    formdata = {
        'rows': '10000',
        'totalYOrN': 'false',
        'annType': '',
        'tmType': '',
        'coowner': '',
        'recUserName': '',
        'allowUserName': '',
        'byAllowUserName': '',
        'appId': '',
        'appIdZhiquan': '',
        'bfchangedAgengedName': '',
        'changeLastName': '',
        'transferUserName': '',
        'acceptUserName': '',
        'regName': '',
        'tmName': '',
        'intCls': '',
        'fileType': '',
        'appDateBegin': '',
        'appDateEnd': '',
        'agentName': ''
    }    

    def start_requests(self):
        for i in range(1661, 0, -1):
            self.formdata['page'] = '1'
            self.formdata['annNum'] = str(i)
            self.headers['Referer'] = f'http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum={i}'
            yield scrapy.FormRequest(
                url = self.url,
                headers = self.headers,
                formdata = self.formdata,
                meta = {'annNum':str(i)},
                callback = self.parse_first_page
            )

    def parse_first_page(self, response):
        data = json.loads(response.text)
        total = data['total']
        rows = data['rows']

        item = CompanyItem()
        for row in rows:
            item['reg_name'] = row['reg_name']
            item['reg_number'] = row['reg_num']
            yield item

        if int(total) > 10000:
            self.formdata['annNum'] = response.meta['annNum']
            self.headers['Referer'] = f'http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum={response.meta["annNum"]}'

            for j in range(10001, int(total), 10000):
                self.formdata['page'] = str((j//10000)+1)
                yield scrapy.FormRequest(
                    url = self.url,
                    headers = self.headers,
                    formdata = self.formdata,
                    callback = self.parse_next
                )

    def parse_next(self, response):
        data = json.loads(response.text)
        rows = data['rows']
        item = CompanyItem()
        for row in rows:
            item['reg_name'] = row['reg_name']
            item['reg_number'] = row['reg_num']
            if item['reg_name']:
                yield item