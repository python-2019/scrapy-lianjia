# -*- coding: utf-8 -*-
import copy

import scrapy
from lianjia.items import LianjiaItem


class lianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['cd.fang.lianjia.com']
    host = "https://cd.fang.lianjia.com"
    start_urls = [host + "/loupan/"]
    page_url = "/loupan/pg"
    # 开始页码
    page_start = 1
    # 爬取前100页
    page_last = 100

    def parse(self, response):
        div_list = response.xpath("//div[@class='resblock-desc-wrapper']")
        for div in div_list:
            item = LianjiaItem()
            item['name'] = div.xpath("./div/a/text()").extract_first()
            item['href'] = self.host + div.xpath("./div/a/@href").extract_first()
            item['addr'] = div.xpath("./div[2]/span[1]/text()").extract_first() + "|" + div.xpath(
                "./div[2]/span[2]/text()").extract_first() + "|" + div.xpath("./div[2]/a/text()").extract_first()
            item['base_info'] = div.xpath("./div[1]/span/text()").extract()
            item['apartment'] = div.xpath("./a/span/text()").extract()
            item['area'] = div.xpath("./div[3]/span/text()").extract()
            item['unit_price'] = div.xpath("./div[6]/div[1]/span[1]/text()").extract_first()
            item['total_price'] = div.xpath("/div[6]/div[2]/text()").extract()
            item['advantage'] = div.xpath("./div[5]/span/text()").extract()
            yield scrapy.Request(
                item['href'],
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}
            )
        #     翻页处理
        # 测试返回的网页
        # with open('a.html', 'w', encoding='utf-8') as f:
        #     body = response.body.decode('utf-8')
        #     f.write(body)
        #     当前页 xpath helper 能获取到 但是程序里面获取不到 返回的response 里面不存在 页码 待分析
        # page = response.xpath("//span[@class='active']/text()").extract_first()
        # 最大页码
        # max_page = response.xpath("//span[contains(text(),'...')]/following-sibling::a[1]/text()").extract_first()
        # 下一页
        next_page = self.page_start + 1
        self.page_start = next_page
        next_page_url = self.host + self.page_url + str((next_page + 1))
        print(next_page_url)
        yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_detail(self, response):
        item = response.meta['item']
        item['start_time'] = response.xpath("//p[@class='when manager']/span[2]/text()").extract_first()
        yield item
