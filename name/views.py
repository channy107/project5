from django.http import HttpResponse
from django.shortcuts import render
from .models import Name


def insert(request):
    file = open('name/yob1880.txt', 'rt')
    for line in file.readlines():
        line = line.replace('\n','')
        line = line.split(',')[0]
        n = Name(name=line)
        n.save()

    file.close()
    return HttpResponse('insert')
