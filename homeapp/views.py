from http.client import HTTPResponse

from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    var={"shubh":"helloworld",
         "one":"twor",
         "two":"three"
         }
    return render(request,'index.html',var)
def about(request):
    return HttpResponse("This is your homepage 3 ")
def contact(request):
    return HttpResponse("This is your homepage 4 ")
def projects(request):
    return HttpResponse("This is your homepage 5 ")
def service(request):
    return HttpResponse("This is your homepage 6 ")

