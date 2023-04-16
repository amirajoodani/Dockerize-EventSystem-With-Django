from django.http import JsonResponse
from asyncio import events
from cmath import log
from multiprocessing import Event
from typing_extensions import Required
from urllib import response
from django.shortcuts import render,redirect ,HttpResponseRedirect 
from django.http import HttpResponse
from django.urls import path
from django.db.models.signals import pre_save
from django.dispatch import receiver
from log.forms import EventForm , responsetimeform , pushform , E1MPLSform
from log.models import EventKindofProblem , ResponseTime , Push
from django.contrib import messages
from django.views.generic.edit import UpdateView ,CreateView , DeleteView
from django.http import FileResponse
import io
from django.views.generic import FormView
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file
from django.views.decorators.cache import cache_page
from .filters import eventfilter
from .filters import pushfilter , E1MPLSfilter
from django.db.models import F
import djqscsv
from excel_response import ExcelResponse
import csv 
from django.urls import reverse_lazy
#from .forms import CreateEventForm
from .models import EventMainProblem ,EventDetailProblem ,E1MPLS
import datetime
#CreateList-------------------------------------------------------------------

def event(request):
    context ={}
    events=EventForm()
    print("user",request.user.username, "Logined into Event",datetime.datetime.now())
    #print("OK")
    if request.method == 'POST':
        #image=request.FILES['image']
        #print('printing POST:' , request.POST)
        events=EventForm(request.POST, request.FILES)
        if events.is_valid():
            events.save()
            return redirect('/eventlist/')
        else:
            print("Error")
            print(events.errors)
            #messages.error(request, "Error")
    context={'form': events}
    return render(request,'event.html',context)


def push(request):
    context ={}
    pushs=pushform()
    #print("OK")
    if request.method == 'POST':
        #image=request.FILES['image']
        #print('printing POST:' , request.POST)
        pushs=pushform(request.POST, request.FILES)
        if pushs.is_valid():
            pushs.save()
            return redirect('/pushlist/')
        else:
            print("Error")
            print(pushs.errors)
            #messages.error(request, "Error")
    context={'form': pushs}
    return render(request,'push.html',context)


def E1MPLScreate(request):
    context ={}
    E1MPLSs=E1MPLSform()
    #print("OK")
    if request.method == 'POST':
        #image=request.FILES['image']
        #print('printing POST:' , request.POST)
        E1MPLSs=E1MPLSform(request.POST, request.FILES)
        if E1MPLSs.is_valid():
            E1MPLSs.save()
            return redirect('/E1MPLSlist/')
        else:
            print("Error")
            print(E1MPLSs.errors)
            #messages.error(request, "Error")
    context={'form': E1MPLSs}
    return render(request,'E1MPLS.html',context)
        

#UpdateView-----------------------------------------------------------------------

class EventUpdateView(UpdateView):
    
    fields = '__all__'
    #fields = ['image']
    template_name = 'eventedit.html'
    #form = 'EventForm'
    model = EventKindofProblem
    
    success_url ="/eventlist/"
    #success_url = reverse_lazy('/eventlist/')

class PushUpdateView(UpdateView):
    
    fields = '__all__'
    #fields = ['image']
    template_name = 'pushupdate.html'
    #form = 'pushForm'
    model = Push
    
    success_url ="/pushlist/"
    #success_url = reverse_lazy('/eventlist/')

class E1MPLSUpdateView(UpdateView):
    
    fields = '__all__'
    #fields = ['image']
    template_name = 'E1MPLSupdate.html'
    #form = 'pushForm'
    model = E1MPLS
    
    success_url ="/E1MPLSlist/"
    #success_url = reverse_lazy('/eventlist/')

#EditView------------------------------------------------------------------------

def eventedit(request, id): 
    context ={} 
    
    event = EventKindofProblem.objects.get(id=id) 
    form = EventForm(request.POST , instance=event )
    print("ok")
    #year_of_start=request.POST.get('year_of_start')
    #form.fields['year_of_start'].choices = [(year_of_start,year_of_start)]
    if request.method=='POST':
        form = EventForm(request.POST , instance=event )
        if form.is_valid():   
            form.save() 
            print('printing POST:' , request.POST)  
            print("ok")
            #print("user",request.user.username, "Edit the Event","id",id)
            return HttpResponseRedirect('/eventlist/')
        else:
            print("Error")
            print(form.errors)
            messages.error(request, "Error")
   
    return render(request, 'eventedit.html',{'event':event } ) 


def pushedit(request, id): 
    context ={} 
    
    push = Push.objects.get(id=id) 
    form = pushform(request.POST , instance=push )
    print("ok")
    #year_of_start=request.POST.get('year_of_start')
    #form.fields['year_of_start'].choices = [(year_of_start,year_of_start)]
    if request.method=='POST':
        form = pushform(request.POST , instance=push )
        if form.is_valid():   
            form.save() 
            print('printing POST:' , request.POST)  
            print("ok")
            #print("user",request.user.username, "Edit the Event","id",id)
            return HttpResponseRedirect('/pushlist/')
        else:
            print("Error")
            print(form.errors)
            messages.error(request, "Error")
   
    return render(request, 'pushupdate.html',{'push':push } ) 


def E1MPLSedit(request, id): 
    context ={} 
    
    E1MPLSs =E1MPLS.objects.get(id=id) 
    form = E1MPLSform(request.POST , instance=E1MPLSs )
    print("ok")
    #year_of_start=request.POST.get('year_of_start')
    #form.fields['year_of_start'].choices = [(year_of_start,year_of_start)]
    if request.method=='POST':
        form = E1MPLSform(request.POST , instance=E1MPLS )
        if form.is_valid():   
            form.save() 
            print('printing POST:' , request.POST)  
            print("ok")
            #print("user",request.user.username, "Edit the Event","id",id)
            return HttpResponseRedirect('/E1MPLSlist/')
        else:
            print("Error")
            print(form.errors)
            messages.error(request, "Error")
   
    return render(request, 'E1MPLSupdate.html',{'E1MPLS':E1MPLS } ) 


#update--------------------------------------------------------------------------------------

   

def eventupdate(request, id): 
    event = EventKindofProblem.objects.get(id=id)
    #print(request.username)
    #print("user",request.user.username, "update the Event","id",id)
    return render(request, 'eventedit.html',{'event':event } ) 



def pushupdate(request, id): 
    push = Push.objects.get(id=id)
    #print(request.username)
    #print("user",request.user.username, "update the Event","id",id)
    return render(request, 'pushupdate.html',{'push':push } ) 

def E1MPLSupdate(request, id): 
    E1MPLS = E1MPLS.objects.get(id=id)
    #print(request.username)
    #print("user",request.user.username, "update the Event","id",id)
    return render(request, 'E1MPLsupdate.html',{'E1MPLS':E1MPLS } ) 


#List--------------------------------------------------------------------------------------




def eventlist(request):
    allevent=EventKindofProblem.objects.all().order_by('-id')[:5]
    events = EventKindofProblem.objects.all().order_by('-id')
    print("user",request.user.username, "Logined into Eventlist",datetime.datetime.now())
    #print(request.datetime.datetime.now())
        #id=request.POST['id']
        #print("id",id)
        #print("day_of_start",event.day_of_start)
        #print(request.user.username)
    #export_to_CSV = forms.BooleanField(Required=False)
    myFilter=eventfilter(request.GET,queryset=events)
    events=myFilter.qs
    form=EventForm()
    context ={'events':events ,'myFilter':myFilter }
    return render(request,'eventlist.html',context)




def pushlist(request):
    allpush=Push.objects.all().order_by('-id')[:5]
    pushs = Push.objects.all().order_by('-id')
    #export_to_CSV = forms.BooleanField(Required=False)
    myFilter=pushfilter(request.GET,queryset=pushs)
    pushs=myFilter.qs
    form=pushform()
    context ={'pushs':pushs ,'myFilter':myFilter }
    return render(request,'pushlist.html',context)

def E1MPLSlist(request):
    allE1MPLS = E1MPLS.objects.all().order_by('-id')[:5]
    E1MPLSs = E1MPLS.objects.all().order_by('-id')
    #export_to_CSV = forms.BooleanField(Required=False)
    myFilter=E1MPLSfilter(request.GET,queryset=E1MPLSs)
    E1MPLSs=myFilter.qs
    form=E1MPLSform()
    context ={'E1MPLSs':E1MPLSs ,'myFilter':myFilter }
    return render(request,'E1MPLSlist.html',context)


#-----------------------------------------------------------------------------------

# Generate a PDF File Form events

def eventpdf(request):
    #create ByteStream Buffer
    buf=io.BytesIO()
    #create canvas
    c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
    #create text Object
    textob=c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",8)
    #loop 
    lines=[]
    events = EventKindofProblem.objects.all()
    myFilter=eventfilter(request.GET,queryset=events)
    eventsfilters=myFilter.qs
    #pdf_file = generateTablePDF('events', myFilter)
    #context ={'events':events ,'myFilter':myFilter}
    for event in eventsfilters:
        lines.append(eventsfilters.name)
        lines.append("===========")
        #lines.append(event.day_of_start)
    for line in lines:
        textob.textLine(line)
    #Finish up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse (buf,as_attachment=True,filename='report.PDF')

def get_csv(request):
    events=EventKindofProblem.objects.all()
    myFilter=eventfilter(request.GET, queryset=events).qs
    #result=myFilter.qs
    #return djqscsv.render_to_csv_response(result,append_datestamp=True,field_header_map={'id':'شماره'} )
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="result.csv"'
    writer = csv.writer(response)
    writer.writerow(['day_of_start','mounth_of_start','year_of_start','hour_of_start','minute_of_start','day_of_end','mounth_of_end','year_of_end','hour_of_end','minute_of_end','deltatime','mainproblem','detailproblem','Bank','city','Connection','IncidentID','DownTime','ReportToDepartment','Assign_to_name1','Assign_to_name2','Assign_to_name3','Assign_to_name4','Assigng_to_others',  'image', 'SMS', 'description'])
    #writer.writerow('__all__')
    events = myFilter.values_list('id','day_of_start', 'mounth_of_start', 'year_of_start', 'hour_of_start', 'minute_of_start',
                         'day_of_end', 'mounth_of_end', 'year_of_end', 'hour_of_end', 'minute_of_end',
                         'mainproblem__name', 'detailproblem__name', 'Bank__name', 'city__name',
                         'Connection__Connection', 'IncidentID', 'DownTime', 'ReportToDepartment__Department',
                         'Assign_to_name1__name', 'Assign_to_name2__name', 'Assign_to_name3__name',
                         'Assign_to_name4__name', 'Assigng_to_others__organization', 'SMS', 'description')
    events_list = [event for event in events]
    for event in events_list:
        clened_event = ['--' if not x else x for x in event]
        event_obj = EventKindofProblem.objects.get(id=int(event[0]))
        clened_event.insert(11, event_obj.deltatime)
        if event_obj.image:
            image_url = request.build_absolute_uri(event_obj.image.url)
            clened_event.insert(-2, image_url)
        else:
            clened_event.insert(-2, '--')

        del clened_event[0]
        writer.writerow(clened_event)
    return response 


    
    








    
     
    
	
	
		
		
#Delete----------------------------------------------------------------------------

def eventdestroy(request, id):  
    event = EventKindofProblem.objects.get(id=id)
    context ={} 
    if request.method =="POST":
        # delete object
        event.delete()
        # after deleting redirect to
        # home page
        print("user",request.user.username, "Deleted the Event","id",id)
        #print(request.datetime.datetime.now())
        #id=request.POST['id']
        #print("id",id)
        #print("day_of_start",event.day_of_start)
        #print(request.user.username)
        return HttpResponseRedirect("/eventlist/")
        
 
    return render(request, "eventdelete.html", context) 


def pushdestroy(request, id):  
    push = push.objects.get(id=id)
    context ={} 
    if request.method =="POST":
        # delete object
        push.delete()
        # after deleting redirect to
        # home page
        print("user",request.user.username, "Deleted the Push ","id",id)
        #print(request.datetime.datetime.now())
        #id=request.POST['id']
        #print("id",id)
        #print("day_of_start",event.day_of_start)
        #print(request.user.username)
        return HttpResponseRedirect("/pushlist/")
        
 
    return render(request, "pushdelete.html", context) 

def E1MPLSdestroy(request, id):  
    E1MPLS = E1MPLS.objects.get(id=id)
    context ={} 
    if request.method =="POST":
        # delete object
        E1MPLS.delete()
        # after deleting redirect to
        # home page
        print("user",request.user.username, "Deleted the E1MPLS ","id",id)
        #print(request.datetime.datetime.now())
        #id=request.POST['id']
        #print("id",id)
        #print("day_of_start",event.day_of_start)
        #print(request.user.username)
        return HttpResponseRedirect("/E1MPLSlist/")
        
 
    return render(request, "E1MPLSdelete.html", context) 

#-------------------------------------------------------------------------------------



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



def durations(request):
    durations = EventKindofProblem.objects.annotate(duration = F('minute_of_end') - F('minute_of_start'))
    for duration in durations:
        print(duration)
    return HttpResponse(f'')

def history_of_event(request, pk):
    if request.method == "GET":
       obj = EventKindofProblem.objects.get(pk=pk)
       return render(request, 'eventlist.html', context={'object': obj})



#class PersonCreateView(CreateView):
#    model =EventKindofProblem 
#    form_class = CreateEventForm
#    success_url = reverse_lazy('person_changelist')


def load_problems(request):
    event_main_problems_id = request.GET.get('EventMainProblem')
    event_detail_problems = EventDetailProblem.objects.filter(eventmainproblem__id=event_main_problems_id).order_by('name').values('id', 'name')
    # data = [{'id': problem.pk, 'name': problem.name} for problem in event_detail_problems]
    # print(data)
    return render(request, 'datiled_event_options.html', {'detailedproblems':  event_detail_problems})






