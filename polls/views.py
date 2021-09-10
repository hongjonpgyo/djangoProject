import qrcode
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpRequest


def index(request):
    qrc = qrcode.make('2008103')
    return

class ImageForm:
    pass


def post(request):
#    imageForm = ImageForm(request.POST, request.FILES)
    qrc = qrcode.make('2222222')
    qrc.save('./static/2222222.png')
    return render(request, './htmlForImage.html')



# Create your views here.
