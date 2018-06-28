# -*- coding:utf-8 -*-

from mongoengine import *
from datetime import datetime
from util import Constants

class StockNotFullModel(Document):
    """
    档期不足记录表
    """

    create_time = DateTimeField(default=datetime.now())   # 记录时间
    user_id = StringField(required=True)                  # 用户id
    ip = StringField(required=True)                       # 用户ip
    sku_id = StringField(required=True)                   # 下单SKU
    city_id = StringField(required=True)                  # 下单城市
    begin_date = StringField(required=True)               # 档期开始日期
    end_date = StringField(required=True)                 # 档期结束日期
    deliver_type = StringField(required=True)             # 物流方式(快递,自提)
    count = IntField(default=1)                           # 数量
    client = StringField(required=True, choices=Constants.CLIENT)  # 客户端

if __name__ == '__main__':
    from DB.DB import DB

    DB.start()
    full = StockNotFullModel()
    full.user_id = "28"
    full.ip = "192.168.0.0"
    full.sku_id = "2904"
    full.city_id = "194"
    full.begin_date = "2018-06-10"
    full.end_date = "2018-06-20"
    full.deliver_type = "1"
    full.count = 1
    full.save()