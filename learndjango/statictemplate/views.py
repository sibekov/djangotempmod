from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    mydict={'keybreaker':"We are now rendering from the template!!!!!"}
    return render(request,"statictemplate/index.html",context=mydict)

def help(request):
    mydict={'helpfinder':"supplying help from the template!!!!!"}
    return render(request,"statictemplate/help.html",context=mydict)