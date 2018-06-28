# -*- coding:utf-8 -*-

from model.ErrorRecordModel import ErrorRecordModel

class ErrorRecordUtil:

    def __init__(self):
        self.error = None

    def recordSave(self,ret,errorMsg,jsonMsg):
        e = ErrorRecordModel(ret=ret,error_msg=errorMsg,json_msg=jsonMsg)
        e.save()
