# -*- coding:utf-8 -*-

from mongoengine import connect

db = "test"
host = "localhost"
port = 27017

class DB:
    @staticmethod
    def start():
        try:
            connect(db,host=host,port=port)
            print(u"数据库已连接>>>>>>>>")
        except Exception as e:
            print(u"数据库连接错误>>>>>>>>>")
            print(e)

if __name__ == '__main__':
    DB.start()