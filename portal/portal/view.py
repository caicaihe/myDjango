# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from env_setting.env_CRUD import *
from env_setting.models import envinfo

def main(request):
    environments = testdb_all(request)
    return render(request, 'base.html', {'environments': environments})

def addEnvironment(request):
  if request.method == 'POST':
    record = envinfo(Name=request.POST['name'], IP=request.POST['ip'], Registry=request.POST['registry'])
    record.save()
    return HttpResponse("ok")

  return HttpResponse("invalid method: " + request.method)

def deleteEnvironment(request, environment):
  if request.method == 'DELETE':
    print(environment)
    testdb_delete(request, environment)
    return HttpResponse("ok")

  return HttpResponse("invalid method: " + request.method)