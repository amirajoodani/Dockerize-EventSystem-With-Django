from asyncio import events
from cmath import log
from django.shortcuts import render,redirect ,HttpResponseRedirect 
from .models import EventKindofProblem
from django.http import HttpResponse
from django.urls import path
from django.db.models.signals import pre_save
from django.dispatch import receiver
from log.forms import EventForm
from log.models import EventKindofProblem
from django.contrib import messages


def event(request):
    context ={}
    if request.method == "POST" :  
        form = EventForm(request.POST or None )  
        if form.is_valid():  
            form.save(commit=True)
            messages.success(request,"Form save succeccfully") 
            context['form']= form 
            return HttpResponseRedirect("/eventlist"+id) 
             
    else:  
        form = EventForm()  
    return render(request,'event.html',{'form':form}) 
  
def eventedit(request, id):  
    event = EventKindofProblem.objects.get(id=id)  
    return render(request,'eventedit.html', {'event':event}) 

def eventlist(request):
    events = EventKindofProblem.objects.all()
    form=EventForm()
    context ={}
    return render(request,'eventlist.html',context={ 'form':form , 'events':events })

def eventupdate(request, id):  
    event = EventKindofProblem.objects.get(pk=id) 
    if request.method=="POST":
        form = EventForm(request.POST or None, instance=event )  
        if form.is_valid(): 
            form = EventForm(request.POST or None, instance=event )   
            form.save()  
            messages.success(request,"Form update succeccfully") 
            return HttpResponseRedirect("/eventlist"+id)
            
    forms=EventForm(event=event)
    return render(request, 'eventedit.html', context={'forms':forms } ) 

def eventdestroy(request, id):  
    event = EventKindofProblem.objects.get(id=id)
    context ={} 
    if request.method =="POST":
        # delete object
        event.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "eventdelete.html", context) 
    

def home(request):
    return render(request,"registration/home.html")




 