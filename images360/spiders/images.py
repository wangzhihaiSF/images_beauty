# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from urllib.parse import urlencode
import json


class ImagesSpider(Spider):
    name = 'images'
    allowed_domains = ['images.so.com']

    def start_requests(self):
        data = {"ch": "beauty", "listtype": "new", "temp": 1}
        base_url = "https://image.so.com/zjl?"
        for page in range(1, self.settings.get("MAX_PAGE") + 1):
            data["sn"] = page * 30
            params = urlencode(data) # 利用 urlencode() 方法将字典转化为 url 的 get 参数
            url = base_url + params # 构造完整的 url
            yield Request(url, self.parse)


    def parse(self, response):
        print(type(response))
        result = json.loads(response.text)
        for image in result.get("list"):
            item = ImageItem()
            item["id"] = image.get("imageid")
            item["url"] = image.get("qhimg_url")
            item["title"] = image.get("group_title")
            item["thumb"] = image.get("qhimg_thumb_utl")
            yield item



