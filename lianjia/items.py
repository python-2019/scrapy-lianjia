# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    """
        链家网 成都新楼盘 信息
    """
    # 楼盘名称
    name = scrapy.Field()
    # 详情地址
    href = scrapy.Field()
    # 位置
    addr = scrapy.Field()
    # 基础信息(住宅 在售等信息)
    base_info = scrapy.Field()
    # 户型
    apartment = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 单价 元
    unit_price = scrapy.Field()
    # 总价
    total_price = scrapy.Field()
    # 优势 品牌房企 公交直达等
    advantage = scrapy.Field()
    # 开售时间
    start_time = scrapy.Field()