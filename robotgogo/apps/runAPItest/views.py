# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from .backend import robotExec
from . import changeconfig
import os
import time
import sys



sys.path.append("..")
from envSetting.env_CRUD import *


# 表单
def run(request):
    return render_to_response('runapitest.html')



def postenv(request):
    ctx = {}
    result = testdball(request)
    print("good")
    if request.POST:
        singalend = robotExec.runRobot("devops")
        Nametmp = request.POST['nn']
        tmpdata = testdb_get(request, Nametmp)
        IPtmp = tmpdata[0].IP
        changeconfig.changeconfigIP(IPtmp)
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

    result = testdball(request)

    if request.POST:
        singalend = robotExec.runRobot("registry")
        Nametmp = request.POST['nn']
        tmpdata = testdb(request, Nametmp)
        IPtmp = tmpdata[0].IP
        changeconfig.changeconfigIP(IPtmp)
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