# -*- coding: utf-8 -*-
 

 
from .models import envinfo

def testdb(request, Nametmp):
    response = envinfo.objects.filter(Name=Nametmp)
    print(response)

    return response

def testdball(request):
    response = envinfo.objects.all()
    print(response)

    return response
