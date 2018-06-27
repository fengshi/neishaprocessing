# -*- coding:utf-8 -*-

from mongoengine import *
from datetime import datetime

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