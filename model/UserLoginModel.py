# -*- coding: utf-8 -*-

from mongoengine import *
from util import Constants
from datetime import datetime

class UserLoginModel(Document):
    """
    用户登录记录
    """
    login_time = DateTimeField(default=datetime.now())
    user_id = StringField(required=True)
    ip = StringField(required=True)
    client = StringField(required=True,choices=Constants.CLIENT)
