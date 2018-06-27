# -*- coding:utf-8 -*-

from mongoengine import *
from datetime import datetime

class ErrorRecordModel(Document):
    """
    错误记录表
    """
    create_time = DateTimeField(default=datetime.now()) # 记录时间
    ret = IntField(required=True,default=0)             # 报错类型
    error_msg = StringField(required=True)              # 错误内容
    json_msg = StringField(required=True)               # 传输内容