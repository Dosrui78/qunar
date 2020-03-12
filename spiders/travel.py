# -*- coding: utf-8 -*-
import scrapy,re
from scrapy import Request, Spider
from qunar.items import QunarItem
from scrapy.selector import Selector
class TravelSpider(scrapy.Spider):
    name = 'travel'
    allowed_domains = ['piao.qunar.com']
    start_urls = 'http://piao.qunar.com/ticket/list.htm?keyword=%E4%B8%AD%E5%9B%BD&region=&from=mpl_search_suggest&page='

    def start_requests(self):
        for i in range(1,100):
            url = self.start_urls + str(i+1)
            yield Request(url=url, callback=self.parse, )

    def parse(self, response):
        sel = Selector(response)
        item = QunarItem()
        items = sel.xpath('//div[contains(@class,"sight_item_detail")]')
        for i in items:
            item['name'] = ''.join(i.xpath('.//div[@class="sight_item_about"]/h3//text()').extract()).strip()
            item['level'] = ''.join(i.xpath('.//div[@class="sight_item_info"]//span[@class="level"]//text()').extract()).replace('景区','')
            item['hot'] = ''.join(i.xpath('.//div[@class="sight_item_info"]/div[@class="clrfix"]//div[@class="sight_item_hot"]//em/span/text()').extract()).replace('热度','')
            item['address'] = ''.join(i.xpath('.//div[@class="sight_item_info"]/p[contains(@class,"address")]/span//text()').extract()).replace("地址：","")    
            item['comment'] = ''.join(i.xpath('.//div[@class="sight_item_info"]//div[contains(@class,"intro")]//text()').extract())
            item['price'] = ''.join(i.xpath('.//div[@class="sight_item_pop"]').re('<span .*?>.*?<em>(.*?)</em>.*?</span>'))     
            item['saleCount'] = ''.join(i.xpath('.//div[@class="sight_item_pop"]').re('<td.*?>.*?<span class="hot_num">(.*?)</span></td>'))                             
            yield item
        


        
