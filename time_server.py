#!/usr/bin/env python
# -*- coding=utf-8 -*-
import socket
import threading
import sys
import win32api
import win32timezone
from datetime import datetime, timedelta


def socket_service():
    # 获取本机电脑名
    myname = socket.getfqdn(socket.gethostname())
    # 获取本机ip
    ip = socket.gethostbyname(myname)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 防止socket server重启后端口被占用（socket.error: [Errno 98] Address already in use）
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ip, 20000))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print('Waiting connection...')
    while 1:
        conn, addr = s.accept()
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()


def deal_data(conn, addr):
    print('已与 {0} 建立连接'.format(addr))
    data = conn.recv(1024)
    print('客户端 {0} 发送的数据是 {1}'.format(addr, data))
    if data == b'get_time':
        # 获取服务器本地时间
        localtime = win32api.GetLocalTime()  # tuple
        ctime = '{}-{}-{} {}:{}:{}'.format(localtime[0], localtime[1], localtime[3], localtime[4], localtime[5],
                                               localtime[6]).encode('utf8')  # tuple --> str --> bytes
    else:
        # 修改服务器本地时间
        wtime = datetime.strptime(data.decode('utf8'), '%Y-%m-%d %H:%M:%S') + timedelta(hours=8)
        win32api.SetLocalTime(wtime)
        ctime = data
    conn.send(ctime)
    conn.close()


if __name__ == '__main__':
    socket_service()