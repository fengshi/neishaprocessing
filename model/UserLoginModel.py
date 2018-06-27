# -*- coding: utf-8 -*-

from mongoengine import *
from util import Constants
from datetime import datetime

class UserLoginModel(Document):
    """
    用户登录记录
    """
    login_time = DateTimeField(default=datetime.now()) # 登录时间
    user_id = StringField(required=True) # 用户id
    ip = StringField(required=True)      # 用户访问ip
    client = StringField(required=True,choices=Constants.CLIENT) # 客户端
