import socket
import sys
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Server
# Create your views here.


def index(request):
    server_list = Server.objects.all()
    return render(request, 'my_server/index.html', {'server_list': server_list})


@csrf_exempt
@require_POST
def get_server_time(request):
    id = request.POST.get('id')
    server = Server.objects.get(id=id)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server.ip_address, 20000))
    except socket.error as e:
        print(e)
        sys.exit(1)
    s.send('get_time'.encode('utf8'))
    ctime = s.recv(1024).decode('utf8')
    print('服务器当前时间是: {}, 关闭连接...'.format(ctime))
    s.close()
    return HttpResponse(ctime)

@csrf_exempt
@require_POST
def set_server_time(request):
    id = request.POST.get('id')
    time = request.POST.get('time')
    server = Server.objects.get(id=id)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server.ip_address, 20000))
    except socket.error as e:
        print(e)
        sys.exit(1)
    s.send(time.encode('utf8'))
    ctime = s.recv(1024).decode('utf8')
    print('服务器当前时间是: {}, 关闭连接...'.format(ctime))
    s.close()
    return HttpResponse(ctime)


