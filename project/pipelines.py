# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from project.settings import *
import pymysql


class ProjectPipeline(object):
    def process_item(self, item, spider):
        print("=================")
        print(item["PositionName"])
        print(item["PositionLink"])
        print(item["PositionType"])
        print(item["PositionNum"])
        print(item["PositionAddress"])
        print(item["PositionTime"])
        print("=================")
	
        return item

# 数据库管道类
class MysqlPipeline(object):
    def __init__(self):
        # 建立数据库连接对象
        self.db = pymysql.connect(
                        host = MYSQL_HOST,
                        user = MYSQL_USER,
                        password = MYSQL_PWD,
                        database = MYSQL_DB,
                        charset = "utf8"
                )
        # 创建游标对象
        self.cursor = self.db.cursor()

    def process_item(self,item,spider):
        # 数据插入数据库
        position = 'insert into jobs values(%s,%s,%s,%s,%s,%s)'
        L = [item['PositionName'].strip(),
             item['PositionLink'].strip(),
             item['PositionType'].strip(),
             # 将人数由字符串改成数字类型
             int(item['PositionNum'].strip()),
             item['PositionAddress'].strip(),
             item['PositionTime'].strip(),
            ]
	print(L)
        self.cursor.execute(position,L)
        # 提交到数据库执行
        self.db.commit()
        return item
    
    # process_item处理完成后会执行此方法
    # 此方法是关闭游标，断开数据库链接
    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()
        print("MySQL数据库断开连接")
