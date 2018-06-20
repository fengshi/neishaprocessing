# -*- coding:utf-8 -*-

from DB.DB import DB
from model.UserLoginModel import UserLoginModel


def saveUserLoginModel(user_id,ip,client):
    DB.start()
    e = UserLoginModel(user_id=user_id,ip=ip,client=client)
    e.save()


if __name__=="__main__":
    saveUserLoginModel("28","192.168.1.1","ALI_ALIPAY")