from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Artical
# Create your views here.



def videos_gallery(request):
    post=Artical.objects.all()
    return render(request,'videos_gallery.html',{'post':post})
