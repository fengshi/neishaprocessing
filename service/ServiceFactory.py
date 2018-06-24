# -*- coding:utf-8 -*-

from DB.DB import DB
import json
from util import Constants
import importlib


def _checkMsg(jsonMsg):
    try:
        myJson = json.loads(jsonMsg.decode('utf-8'))
        if myJson["command"] and myJson["command"] in Constants.command:
            return myJson["command"]
        else:
            return False
    except Exception as ex:
        print(ex)
        return False


class ServiceFactory:

    def __init__(self):
        self.error = None
        try:
            DB.start()
        except Exception as e:
            print(e)
            self.error = "DB error"

    def excute(self,jsonMsg):
        if self.error:
            return {"ret":500,"msg":self.error}

        command_name = _checkMsg(jsonMsg)

        if command_name:
            try:
                class_name = Constants.command[command_name]
                print(class_name)
                if class_name:
                    my_moudle = importlib.import_module("service." + class_name)
                    p = getattr(my_moudle,class_name)
                    command = p(jsonMsg)
                    result = command.excute()

                    return result
                else:
                    return {"ret":500,"msg":"Not service class"}
            except Exception as e:
                print(e)
                return {"ret":500,"msg:":"class moudle error"}
        return {"ret":500,"msg":"command name error"}
