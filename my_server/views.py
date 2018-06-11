import socket
import sys
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Server
from .forms import AddServerForm, EditServerForm
# Create your views here.

def index(request):
    form = AddServerForm()
    server_list = Server.objects.all()
    return render(request, 'my_server/index.html', {'server_list': server_list, 'form': form})

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

def set_server_time(request):
    pass

@require_POST
def add_server(request):
    form = AddServerForm(request.POST)
    if form.is_valid():
        server = form.save()
        return render(request, 'my_server/add_server.html', {'server': server})

@csrf_exempt
@require_POST
def delete_server(request):
    id = request.POST.get('id')
    Server.objects.get(id=id).delete()
    return HttpResponse('')


@csrf_exempt
def edit_server(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        server = Server.objects.get(id=id)
        form = EditServerForm(instance=server)
        return render(request, 'my_server/edit_server_form.html', {'form': form})
    if request.method == 'POST':
        id = request.POST.get('id')
        server = Server.objects.get(id=id)
        form = EditServerForm(request.POST, instance=server)
        if form.is_valid():
            form.save()
        return render(request, 'my_server/after_edit.html', {'server': server})


    re