# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from .backend import robotExec
from . import changeconfig
import os
import time
 
# 表单
def run(request):
    return render_to_response('run-test.html')

 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
        command = 'echo'+' '+request.GET['q']+'>ddd'
        os.system(command)
    else:
        message = '你提交了空表单'
    return HttpResponse(message)


def postenv(request):
    ctx = {}
    if request.POST:
        singalend = robotExec.runRobot()
        IP = request.POST['q']
        changeconfig.changeconfigIP(IP)
        for i in range(10):
            time.sleep(5)
            if singalend == 0:
                backWord = 'doing'
                ctx['rlt'] = backWord
                return render(request, "devopsapienv.html", ctx)
            else:
                ctx['rlt'] = 'done'
                return render(request, "devopsapienv.html", ctx)
    return render(request, "devopsapienv.html", ctx)

