# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import urllib.request
import os
class XiaohuaproPipeline(object):
    def __init__(self):
        self.fp = None
    def open_spider(self,spider):
        print('开始爬虫')
        self.fp = open('./data.json','w',encoding='utf-8')
    def process_item(self, item, spider):
        img_dic = {
            'img_url':item['img_url'],
            'img_name':item['img_name']
        }
        #json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
        json_string = json.dumps(img_dic,ensure_ascii=False)
        self.fp.write(json_string)

        #下载图片操作
        if not os.path.exists('xiaohua'):
            os.mkdir('xiaohua')
        filePath='xiaohua/'+item['img_name']+'.png'
        urllib.request.urlretrieve(url=item['img_url'],filename=filePath)
        print(filePath+ ':下载成功')

        return item
    def close_spider(self,spider):
        self.fp.close()
        print('爬虫结束')



  #  urlretrieve(url, filename=None, reporthook=None, data=None)   有四个参数
  #前两个是下载的地址和保存的路径
 #'参数 reporthook 是一个回调函数，当连接上服务器、以及相应的数据块传输完毕时会触发该回调，我们可以利用这个回调函数来显示当前的下载进度。' \
 # '参数 data 指 post 到服务器的数据，该方法返回一个包含两个元素的(filename, headers)元组，filename 表示保存到本地的路径，header 表示服务器的响应头。'








