# -*- coding:utf-8 -*-

import socket
from tornado.ioloop import IOLoop
from functools import partial
from service import ServiceFactory

class SocketServer:
    def __init__(self,host,port,maxConn = 5):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.socket.setblocking(0)
        self.socket.bind((self.host,self.port))
        self.socket.listen(maxConn)

        self.service = ServiceFactory.ServiceFactory()

        server_fd = self.socket.fileno()

        self.fd_map = {}

        self.fd_map[server_fd] = self.socket

        self.ioloop = IOLoop.instance()

        self.ioloop.add_handler(server_fd,self._handle_server,IOLoop.READ)

    def _handle_server(self,fd,event):
        s = self.fd_map[fd]

        if event & IOLoop.READ:
            client_conn,client_addr = s.accept()
            print("connect socket %s " % client_addr[0])
            client_conn.setblocking(0)

            client_fd = client_conn.fileno()
            self.fd_map[client_fd] = client_conn

            handle = partial(self._handle_client,client_addr)
            self.ioloop.add_handler(client_fd,handle,IOLoop.READ)

    def _handle_client(self,client_addr,client_fd,event):
        client_socket = self.fd_map[client_fd]

        if event & IOLoop.READ:
            client_data = client_socket.recv(1024)
            if client_data:
                print("receive %s from %s " % (client_data.decode('utf-8'),client_addr))

                self.service.excute(client_data)

            else:
                self.ioloop.remove_handler(client_fd)
                client_socket.close()

    def start(self):
        print("server start.......")
        self.ioloop.start()

if __name__ == "__main__":
    server = SocketServer("127.0.0.1",50000)
    server.start()