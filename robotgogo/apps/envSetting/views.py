# -*- coding: utf-8 -*-

import os
import sys

sys.path.append("..")
from django.http import HttpResponse
from django.shortcuts import render

# from models import envinfo
from .models import envinfo
from .getenv import testdb

import sys

sys.path.append("..")
from .getenv import testdball, testdb


# 表单


def env_setting(request):
    ctx = {}
    result = testdball(request)
    if request.POST:
        Nametmp = request.POST['n']
        IPtmp = request.POST['q']
        Registrytmp = request.POST['r']
        test1 = envinfo(Name=Nametmp, IP=IPtmp, Registry=Registrytmp)
        test1.save()
        result = testdb(request, Nametmp)
        ctx['rln'] = result[0].Name
        ctx['rlt'] = result[0].IP
        ctx['rlk'] = result[0].Registry
    return render(request, "env_setting.html", {'li': result})
