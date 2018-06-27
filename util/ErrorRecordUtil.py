# -*- coding:utf-8 -*-

from DB import DB
from model import ErrorRecordModel

class ErrorRecordUtil:

    def __init__(self):
        self.error = None
        try:
            DB.start()
        except Exception as e:
            print(e)
            self.error = "DB error"

    def recordSave(self,ret,errorMsg,jsonMsg):
        e = ErrorRecordModel(ret=ret,error_msg=errorMsg,json_msg=jsonMsg)
        e.save()
