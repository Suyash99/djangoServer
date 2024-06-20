from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
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
    