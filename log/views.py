from asyncio import events
from cmath import log
from multiprocessing import Event
from django.shortcuts import render,redirect ,HttpResponseRedirect 
from .models import EventKindofProblem
from django.http import HttpResponse
from django.urls import path
from django.db.models.signals import pre_save
from django.dispatch import receiver
from log.forms import EventForm , responsetimeform
from log.models import EventKindofProblem , ResponseTime
from django.contrib import messages
from django.views.generic.edit import UpdateView



# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file
from django.views.decorators.cache import cache_page
from .filters import eventfilter



def event(request):
    context ={}
    events=EventForm()
    #print("OK")
    if request.method=='POST':
        #image=request.FILES['image']
        #print('printing POST:' , request.POST)
        events=EventForm(request.POST,request.FILES)
        if events.is_valid():
            
            events.save()
            return redirect('/eventlist/')
    context={'form':events}
    return render(request,'event.html',context)
        


class EventUpdateView(UpdateView):
    
    fields = '__all__'
    template_name = 'eventedit.html'
    #form = 'EventForm'
    model = EventKindofProblem
    success_url ="/eventlist "







def eventedit(request, id): 
    context ={} 
    
    event = EventKindofProblem.objects.get(id=id) 
    form = EventForm(request.POST , instance=event )
    year_of_start=request.POST.get('year_of_start')
    form.fields['year_of_start'].choices = [(year_of_start,year_of_start)]
    if request.method=='POST':
        form = EventForm(request.POST , instance=event )
        if form.is_valid():   
            form.save() 
            print('printing POST:' , request.POST)  
            print("ok")
            return HttpResponseRedirect('/eventlist/')
        else:
            print("Error")
            print(form.errors)
            messages.error(request, "Error")
   
    return render(request, 'eventedit.html',{'event':event } ) 

   

def eventupdate(request, id): 
    event = EventKindofProblem.objects.get(id=id)
    return render(request, 'eventedit.html',{'event':event } ) 



def eventlist(request):
    events = EventKindofProblem.objects.all()
    myFilter=eventfilter(request.GET,queryset=events)
    events=myFilter.qs
    form=EventForm()
    context ={'events':events ,'myFilter':myFilter}
    return render(request,'eventlist.html',context)







#def eventupdate(request, pk):
#    event=EventKindofProblem.objects.get(id=pk)
    
     
    
	
	
		
		
		
			
			
	
	






def eventdestroy(request, id):  
    event = EventKindofProblem.objects.get(id=id)
    context ={} 
    if request.method =="POST":
        # delete object
        event.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/eventlist/")
 
    return render(request, "eventdelete.html", context) 
    

def home(request):
    return render(request,"registration/home.html")


def responsetimelist(request):
    if request.method=="POST" and 'submit' in request.POST:
        fm=responsetimeform(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request ,'Form saved Successfully')
    if request.method=="POST" and 'delete' in request.POST:
        id=request.POST['id']
        ResponseTime.objects.get(pk=id).delete()
        messages.success(request ,'Form delete Successfully')
    fm=responsetimeform()
    responsetimelist=ResponseTime.objects.all()
    return render (request,'responsetimelist.html', context={'fm':fm,'responsetimelist':responsetimelist})

def responsetimeedit(request,id):
    instance=ResponseTime.objects.get(pk=id)
    fm=responsetimeform(request.POST,instance=instance)
    if fm.is_valid():
        fm.save()
        messages.success(request ,'Form delete Successfully')
        return redirect('/responsetimelist')
    fm=responsetimeform(instance=instance)
    return render (request ,'responsetimeedit.html',context={'fm':fm})

            



def search(request):
    event_list = EventKindofProblem.objects.all()
    event_filter = eventfilter(request.GET, queryset=event_list)
    return render(request, '/search/event_list.html', {'filter': event_filter})
 