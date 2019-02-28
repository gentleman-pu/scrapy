# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 每个职位名称
    PositionName = scrapy.Field()
    # 每个职位的链接
    PositionLink = scrapy.Field()
    # 每个职位的类别
    PositionType = scrapy.Field()
    # 职位招聘人数
    PositionNum = scrapy.Field()
    # 职位招聘地点
    PositionAddress = scrapy.Field()
    # 职位招聘信息发布时间
    PositionTime = scrapy.Field()
