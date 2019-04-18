from django.shortcuts import render,HttpResponse,get_object_or_404
from django.shortcuts import redirect
from .models import Artical
from .forms import CreateForms
# Create your views here.

# start blogapp

def contact(request):

    if request.method == 'POST':
        form = CreateForms(request.POST)
        form.save()
        return redirect()

    else:
        form = CreateForms()

    context={'post':Artical.objects.all(),
             'form':CreateForms()}
    return render(request,'contact.html',context)




# start blogapp