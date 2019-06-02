# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

from scrapy.conf import settings


class LianjiaPipeline(object):

    def open_spider(self, spider):
        file_path = settings.get("FILE_PATH")
        self.file = open(file_path, 'w', newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.file)
        headers = ['楼盘名称', '位置', '基础信息', '户型', '面积', '单价', '总价', '优势', '开售时间', '详情地址']
        self.csv_writer.writerow(headers)

    def process_item(self, item, spider):
        row = [item['name'], item['addr'], item['base_info'], item['apartment'], item['area'], item['unit_price'],
               item['total_price'], item['advantage'], item['start_time'], item['href']]
        self.csv_writer.writerow(row)
        print("====="+str(row)+"====")
        return item
