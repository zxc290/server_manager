#!/usr/bin/env python
# -*- coding=utf-8 -*-
import socket
import threading
import sys
import requests
import win32api
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# 正式使用时修改socket的ip获取


def get_out_ip(url=r'http://www.ip138.com/'):
    r1 = requests.get(url)
    txt = r1.text
    soup = BeautifulSoup(txt, "html.parser").iframe

    r2 = requests.get(soup["src"])
    txt = r2.text
    ip = txt[txt.find("[") + 1: txt.find("]")]

    return ip

def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 防止socket server重启后端口被占用（socket.error: [Errno 98] Address already in use）
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('127.0.0.1', 20000))
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