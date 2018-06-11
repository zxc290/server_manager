import requests
from bs4 import BeautifulSoup


# 获取外网IP
def get_out_ip(url=r'http://www.ip138.com/'):
    r1 = requests.get(url)
    txt = r1.text
    soup = BeautifulSoup(txt, "html.parser").iframe

    r2 = requests.get(soup["src"])
    txt = r2.text
    ip = txt[txt.find("[") + 1: txt.find("]")]

    return ip



if __name__ == '__main__':
    get_out_ip()
