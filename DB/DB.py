# -*- coding:utf-8 -*-

from mongoengine import connect

db = "neidb"
host = "47.104.29.27"
port = 27017
user = "admin"
pwd = "admin"

class DB:
    @staticmethod
    def start():
        try:
            connect(db,username=user,password=pwd,host=host,port=port)
            print(u"数据库已连接>>>>>>>>")
        except Exception as e:
            print(u"数据库连接错误>>>>>>>>>")
            print(e)

if __name__ == '__main__':
    DB.start()