# -*- coding: utf-8 -*-
import scrapy
from xiaohuaPro.items import XiaohuaproItem
class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    #allowed_domains = ['www.521609.com/daxuemeinv']
    start_urls = ['http://www.521609.com/daxuemeinv/']
    url = 'http://www.521609.com/daxuemeinv/list8%d.html'
    page_num = 1
    def parse(self, response):
        li_list = response.xpath('//*[@id="content"]/div[2]/div[2]/ul/li')
        for li in li_list:
            item = XiaohuaproItem()
            item['img_url'] = li.xpath('./a/img/@src').extract_first()
            #拼接图片下载的url
            item['img_url'] = 'http://www.521609.com'+item['img_url']
            item['img_name'] = li.xpath('./a/img/@alt').extract_first()

            yield item
        if self.page_num <= 23:
            self.page_num += 1
            url = format(self.url%self.page_num)
            yield scrapy.Request(url=url,callback=self.parse)
