from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('testing.html')
    return HttpResponse(template.render())

def firsthtml(request):
    template = loader.get_template('firstHtml.html')
    return HttpResponse(template.render())

def membersList(request):
    template = loader.get_template('memberList.html')
    context = {
        'memberList': Member.objects.all().values()
    }
    return HttpResponse(template.render(context=context,request=request))

def specificmember(request, id):
    template = loader.get_template('memberDetail.html')
    
    context = {
        'member': Member.objects.filter(id=id).values().first()
    }
    return HttpResponse(template.render(context=context,request=request))
    