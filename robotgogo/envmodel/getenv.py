# -*- coding: utf-8 -*-
 

 
from .models import envinfo

def testdb(request, Nametmp):
    response = envinfo.objects.filter(Name=Nametmp)

    return response

def testdball(request):
    response = envinfo.objects.all()

    return response
