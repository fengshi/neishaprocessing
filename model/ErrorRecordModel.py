# -*- coding:utf-8 -*-

from mongoengine import *
from datetime import datetime

class ErrorRecordModel(Document):
    """
    错误记录表
    """
    create_time = DateTimeField(default=datetime.now())
    ret = IntField(required=True,default=0)
    error_msg = StringField(required=True)
    json_msg = StringField(required=True)