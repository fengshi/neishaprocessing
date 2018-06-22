# -*- coding:utf-8 -*-

from model.UserLoginModel import UserLoginModel
import traceback
import json
from util import Constants

class UserLoginService:

    def __init__(self,jsonMsg):
        self.msg = jsonMsg.decode('utf-8')

    def excute(self):
        if self.msg:
            myJson = json.load(self.msg)

            user_id = myJson.get("user_id","-1")
            ip = myJson.get("ip","0.0.0.0")
            client = myJson.get("client",Constants.UNKOWN)

            try:
                e = UserLoginModel(user_id=user_id,ip=ip,client=client)
                e.save()
                return {"ret":0}
            except Exception as e:
                print(e)
                return {"ret":500,"msg":traceback.format_exc()}
        return {"ret":500,"msg":"the msg error"}
