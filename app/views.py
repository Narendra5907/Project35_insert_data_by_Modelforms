from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def insert_Topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Toipic name inserted successfully')

    return render(request,'insert_Topic.html',d)


def insert_Webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}
    if request.method=='POST':
        WFD=WebpageForm(request.POST)
        if WFD.is_valid():
            WFD.save()
            return HttpResponse('Toipic name inserted successfully')

    return render(request,'insert_Webpage.html',d)


def insert_AccessRecord(request):
    AFO=AccessRecordForm()
    d={'AFO':AFO}
    if request.method=='POST':
        AFD=AccessRecordForm(request.POST)
        if AFD.is_valid():
            AFD.save()
            return HttpResponse('AccessRecord name inserted successfully')

    return render(request,'insert_AccessRecord.html',d)