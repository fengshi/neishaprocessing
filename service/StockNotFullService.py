# -*- coding:utf-8 -*-

import json
from model import StockNotFullModel
import traceback
from datetime import datetime

class StockNotFullService:

    def __init__(self,jsonMsg):
        self.msg = jsonMsg.decode('utf-8')

    def excute(self):
        if self.msg:
            myJson = json.loads(self.msg)

            user_id = myJson.get("user_id","-1")
            ip = myJson.get("ip","0.0.0.0")
            sku_id = myJson.get("sku_id","-1")
            city_id = myJson.get("city_id","-1")
            begin_date = myJson.get("begin_date",datetime.now().strftime('%Y-%m-%d'))
            end_date = myJson.get("end_date", datetime.now().strftime('%Y-%m-%d'))
            deliver_type = myJson.get("deliver_type","1")
            count = myJson.get("count",1)

            try:
                e = StockNotFullModel(user_id=user_id,ip=ip,sku_id=sku_id,city_id=city_id,
                                      begin_date=begin_date,end_date=end_date,deliver_type=deliver_type,count=count)
                e.save()
                return {"ret":0}
            except Exception as e:
                print(e)
                return {"ret":500,"msg":traceback.format_exc()}
        return {"ret":500,"msg":"the msg error"}
