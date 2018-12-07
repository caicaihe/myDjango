# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from .backend import robotExec
from . import change_config
import os
import time
import sys



sys.path.append("../")
from env_setting.env_CRUD import *


# 表单
def run(request):
    return render_to_response('runapitest.html')



def postenv(request):
    ctx = {}
    result = testdb_all(request)
    if request.POST:
        Nametmp = request.POST['nn']
        tmpdata = testdb_get(request, Nametmp)
        IPtmp = tmpdata[0].IP
        change_config.change_config_IP(IPtmp)
        singalend = robotExec.runRobot("devops")
        for i in range(10):
            time.sleep(5)
            if singalend == 0:
                backWord = 'doing'
                ctx['rlt'] = backWord
                return render(request, "devopstest.html", ctx)
            else:
                ctx['rlt'] = 'done'
                return render(request, "devopstest.html", ctx)
    return render(request, "devopstest.html", {'li': result})


def registry(request):
    ctx = {}

    result = testdb_all(request)
    if request.POST:
        Nametmp = request.POST['nn']
        tmpdata = testdb_get(request, Nametmp)
        IPtmp = tmpdata[0].IP
        registrytmp = tmpdata[0].Registry
        change_config.change_config_IP(IPtmp)
        change_config.change_config_registry(registrytmp)
        singalend = robotExec.runRobot("registry")
        for i in range(10):
            time.sleep(5)
            if singalend == 0:
                backWord = 'doing'
                ctx['rlt'] = backWord
                return render(request, "registrytest.html", ctx)
            else:
                ctx['rlt'] = 'done'
                return render(request, "registrytest.html", ctx)
    return render(request, "registrytest.html", {'li': result})