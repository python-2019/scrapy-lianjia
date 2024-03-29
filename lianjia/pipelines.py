# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import datetime

from scrapy.conf import settings


class LianjiaPipeline(object):

    def open_spider(self, spider):
        file_path = settings.get("FILE_PATH")
        self.file = open(file_path, 'w', newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.file)
        headers = ['楼盘名称', '位置', '单价', '总价', '基础信息', '户型', '面积', '优势', '开售时间', '详情地址']
        self.csv_writer.writerow(headers)

    def process_item(self, item, spider):
        if self.time_filter(item['start_time']) and self.base_info_filter(item['base_info']):
            row = [item['name'], item['addr'], item['unit_price'], item['total_price'], item['base_info'],
                   item['apartment'], item['area'],
                   item['advantage'], item['start_time'], item['href']]
            self.csv_writer.writerow(row)
            print(row)
            return item

    def close_spider(self, spider):
            self.file.flush()

    def time_filter(self,date_str):
        """
        过滤开盘时间2019年之前的
        :param date_str: 时间格式字符串 .分割
        :return: bool
        """
        time_limit = '2018.12.31'
        time_limit_timestamp = datetime.datetime.strptime(time_limit, '%Y.%m.%d').timestamp()
        try:
            date = datetime.datetime.strptime(date_str, '%Y.%m.%d')
            timestamp = date.timestamp()
            if timestamp - time_limit_timestamp > 0:
                return True
            else:
                print("当前时间小于: "+time_limit)
                return False
        except Exception:
            date = datetime.datetime.strptime(date_str, '%Y.%m')
            timestamp = date.timestamp()
            if timestamp - time_limit_timestamp > 0:
                return True
            else:
                print("当前时间小于: "+time_limit)
                return False

    def base_info_filter(self,base_info):
        if "住宅" in base_info:
            return True
        else:
            print("当前房屋信息非住宅")
            return  False
