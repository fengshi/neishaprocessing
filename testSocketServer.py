# -*- coding:utf-8 -*-

import socket
import json

from datetime import datetime

#mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#mysocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#mysocket.connect(("127.0.0.1",50000))

#q = input('Enter:')
#mysocket.send(q.encode('utf-8'))
#mysocket.close()


#s = '{"ret":"5499"}'
#a = json.loads(s)
#print(a)

#command = {"userLogin":"UserLoginService"}
#print('userLogin' in command)


print(datetime.now().strftime('%Y-%m-%d'))