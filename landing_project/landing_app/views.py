from django.shortcuts import render
from .models import Customer



def home(request):

    if request.method=="POST":
        model=Customer()
        model.name=request.POST.get('name',None)
        model.email=request.POST.get('email',None)
        model.number=request.POST.get('number',None)

        model.save()


    return render (request,'index.html')

# Create your views here.
