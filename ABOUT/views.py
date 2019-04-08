from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Author1,Artical,Catagory
# Create your views here.

# start blogapp

def about(request):
    post=Artical.objects.all()
    return render(request,'about.html',{'post':post})

def getauthor(request,name):
    return render(request,'profile.html')


def getsingle(request,id):
    post=get_object_or_404(Artical,pk=id)
    first=Artical.objects.first()
    last=Artical.objects.last()
    context={
        'post':post,
        'first':first,
        'last':last
    }
    return render(request,'single.html',context)


def gettopic(request,name):
    return render(request,'catagory.html')

# end blogapp