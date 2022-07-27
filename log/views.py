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
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file
from django.views.decorators.cache import cache_page
from .filters import eventfilter
from django.db.models import F
import djqscsv
from excel_response import ExcelResponse



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
            print("user",request.user.username, "Create the Event", request.POST)
            return redirect('/eventlist/')
        else:
            print("Error")
            print(events.errors)
            #messages.error(request, "Error")
    context={'form':events}
    return render(request,'event.html',context)
        


class EventUpdateView(UpdateView):
    
    fields = '__all__'
    template_name = 'eventedit.html'
    #form = 'EventForm'
    model = EventKindofProblem
    
    success_url ="/eventlist/"







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

   

def eventupdate(request, id): 
    event = EventKindofProblem.objects.get(id=id)
    #print(request.username)
    #print("user",request.user.username, "update the Event","id",id)
    return render(request, 'eventedit.html',{'event':event } ) 



def eventlist(request):
    allevent=EventKindofProblem.objects.all().order_by('-id')[:5]
    events = EventKindofProblem.objects.all()
    
    myFilter=eventfilter(request.GET,queryset=events)
    events=myFilter.qs
    form=EventForm()
    context ={'events':events ,'myFilter':myFilter}
    return render(request,'eventlist.html',context)


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
    qs=EventKindofProblem.objects.all()
    myFilter=eventfilter(request.GET,queryset=qs)
    return djqscsv.render_to_csv_response(myFilter.qs,append_datestamp=True,field_header_map={'id':'شماره'} )
    
    








    
     
    
	
	
		
		


def eventdestroy(request, id):  
    event = EventKindofProblem.objects.get(id=id)
    context ={} 
    if request.method =="POST":
        # delete object
        event.delete()
        # after deleting redirect to
        # home page
        print("user",request.user.username, "Deleted the Event","id",id,request.POST)
        #print(request.datetime.datetime.now())
        #id=request.POST['id']
        #print("id",id)
        #print("day_of_start",event.day_of_start)
        #print(request.user.username)
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



def durations(request):
    durations = EventKindofProblem.objects.annotate(duration = F('minute_of_end') - F('minute_of_start'))
    return render(request, 'eventlist.html', {'durations':durations})

def history_of_event(request, pk):
    if request.method == "GET":
       obj = EventKindofProblem.objects.get(pk=pk)
       return render(request, 'eventlist.html', context={'object': obj})