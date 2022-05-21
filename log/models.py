from audioop import reverse
from distutils.command.upload import upload
from multiprocessing import connection
from pickle import TRUE
from pyexpat import model
from random import choices
from django.db import models
from django_jalali.db import models as jmodels
from django.db.models import F
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime
from django.contrib.auth.models import User

    
class EventMainProblem(models.Model):
    name =  models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.name
    
class EventDetailProblem(models.Model):
    eventmainproblem = models.ForeignKey(EventMainProblem,on_delete=models.SET_NULL,null=True)
    name =  models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.name
    
class assign_to(models.Model):
    name=models.CharField(max_length=25,unique=True,null=True,blank=True)
    def __str__(self):
        return self.name
    
class expert(models.Model):
    name=models.CharField(max_length=25,unique=True,null=True,blank=True)
    def __str__(self):
        return self.name

class Bank(models.Model):
    name = models.CharField(max_length=20,null=True,blank=True)
    def __str__(self):
        return self.name

class city(models.Model):
    name  = models.CharField(max_length=20,null=True,blank=True)
    def __str__(self):
        return self.name

class Connection(models.Model):
    Connection  = models.CharField(max_length=10,null=True,blank=True)
    def __str__(self):
        return self.Connection
    
class Report_To(models.Model):
    Department  = models.CharField(max_length=10,null=True,blank=True)
    def __str__(self):
        return self.Department

class Other_Organization(models.Model):
    organization=models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.organization

class Push_Organization(models.Model):
    organization=models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.organization

class IrancellNumber(models.Model):
    number=models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.number

class year(models.Model):
    year=models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return self.year

class mounth(models.Model):
    mounth=models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.mounth

class day(models.Model):
    day=models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.day

class hour(models.Model):
    hour=models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.hour

class minute(models.Model):
    minute=models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.minute
    
class EventKindofProblem(models.Model):
    name =  models.CharField(max_length=255)
    #owner = models.ForeignKey('auth.User',on_delete=models.RESTRICT)
    #start_date = jmodels.jDateTimeField(null=True,blank=True)
    #end_date = jmodels.jDateTimeField(null=True,blank=True)
    day_of_start = models.ForeignKey(day,on_delete=models.SET_NULL,null=True,related_name='auth.user+')
    mounth_of_start = models.ForeignKey(minute,on_delete=models.SET_NULL,null=True,related_name='auth.user+')
    year_of_start = models.ForeignKey(year,on_delete=models.SET_NULL,null=True,related_name='auth.user+')
    hour_of_start = models.ForeignKey(hour,on_delete=models.SET_NULL,null=True,related_name='auth.user+')
    minute_of_start =  models.ForeignKey(minute,on_delete=models.SET_NULL,null=True,related_name='auth.user+')
    day_of_end = models.ForeignKey(day,on_delete=models.SET_NULL,null=True,blank=True,related_name='auth.user+')
    mounth_of_end= models.ForeignKey(mounth,on_delete=models.SET_NULL,null=True,blank=True,related_name='auth.user+')
    year_of_end = models.ForeignKey(year,on_delete=models.SET_NULL,null=True,blank=True,related_name='auth.user+')
    hour_of_end = models.ForeignKey(hour,on_delete=models.SET_NULL,null=True,blank=True,related_name='auth.user+')
    minute_of_end =  models.ForeignKey(minute,on_delete=models.SET_NULL,null=True,blank=True,related_name='auth.user+')
    objects = jmodels.jManager()
    status_choice = (('open','OPEN'),('in progress','IN PROGRESS'),('close','CLOSE'),('None','None'))
    status = models.CharField(choices=status_choice,max_length=25,null=True,blank=True)
    mainproblem = models.ForeignKey(EventMainProblem,on_delete=models.SET_NULL,null=True)
    detailproblem = models.ForeignKey(EventDetailProblem,on_delete=models.SET_NULL,null=True)
    Bank= models.ForeignKey(Bank,on_delete=models.SET_NULL,null=True,blank=True)
    image = models.ImageField(upload_to='media',null=True , blank=True)
    city= models.ForeignKey(city,on_delete=models.SET_NULL,null=True,blank=True,related_name='city+')
    Connection=models.ForeignKey(Connection,on_delete=models.SET_NULL,null=True,blank=True,related_name='Connection+')
    IncidentID=models.IntegerField(blank=True,null=True)
    DownTime_choice = (('no','NO'),('yes','YES'))
    DownTime  = models.CharField(choices=DownTime_choice,max_length=4,null=True,blank=True)
    ReportToDepartment= models.ForeignKey(Report_To,on_delete=models.SET_NULL,null=True,blank=True,related_name='auth.user+')
    Assign_to_name1=models.ForeignKey(assign_to,on_delete=models.SET_NULL,null=True,blank=True,related_name='auth.user+')
    Assign_to_name2=models.ForeignKey(assign_to,on_delete=models.SET_NULL,null=True,blank=True,related_name='auth.user+')
    Assign_to_name3=models.ForeignKey(assign_to,on_delete=models.SET_NULL,null=True,blank=True,related_name='auth.user+')
    Assign_to_name4=models.ForeignKey(assign_to,on_delete=models.SET_NULL,null=True,blank=True,related_name='auth.user+')
    Assigng_to_others=models.ForeignKey(Other_Organization,on_delete=models.SET_NULL,null=True,blank=True , related_name='auth.user+')
    SMS_choice = (('sms','SMS'),('nosms','NOSMS'))
    SMS  = models.CharField(choices=SMS_choice,max_length=10,null=True,blank=True)
    description = models.TextField(max_length=255)
    reson = models.TextField(max_length=255)
    Status_Of_People = (('present','PRESENT'),('registrator','REGISTRATOR'),('completor','COMPLETOR'),('remote','REMOTE'),('None','None'))
    Expert1 = models.ForeignKey(expert,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='expert+')
    Status_Of_Expert1 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert2 = models.ForeignKey(expert,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='expert+')
    Status_Of_Expert2 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert3 = models.ForeignKey(expert,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='expert+')
    Status_Of_Expert3 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert4 = models.ForeignKey(expert,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='expert+')
    Status_Of_Expert4 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert5 = models.ForeignKey(expert,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='expert+')
    Status_Of_Expert5 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert6 = models.ForeignKey(expert,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='expert+')
    Status_Of_Expert6 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert7 = models.ForeignKey(expert,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='expert+')
    Status_Of_Expert7 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert8 = models.ForeignKey(expert,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='expert+')
    Status_Of_Expert8 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert9 = models.ForeignKey(expert,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='expert+')
    Status_Of_Expert9 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert10 = models.ForeignKey(expert,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='expert+')
    Status_Of_Expert10 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert11 = models.ForeignKey(expert,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='expert+')
    Status_Of_Expert11 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert12 = models.ForeignKey(expert,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='expert+')
    Status_Of_Expert12 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    problem_status_choice = (('internal','INTERNAL'),('external','EXTERNAL'),('None','None'))
    Status_Of_problem  = models.CharField(choices=problem_status_choice,max_length=10,null=True,blank=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return ('eventlist')
    class Meta:  
        db_table = "event"  

class E1MPLS(models.Model):
    start_date = jmodels.jDateTimeField()
    end_date = jmodels.jDateTimeField(null=True,blank=True) 
    status_choice = (('open','OPEN'),('in progress','IN PROGRESS'),('close','CLOSE'))
    status = models.CharField(choices=status_choice,max_length=25,null=True,blank=True)
    Connection=models.ForeignKey(Connection,on_delete=models.SET_NULL,null=True,blank=True,related_name='Connection+')
    city= models.ForeignKey(city,on_delete=models.SET_NULL,null=True,blank=True,related_name='city+')
    IncidentID=models.IntegerField(blank=True,null=True)
    description = models.TextField(max_length=255)
    Status_Of_People = (('present','PRESENT'),('registrator','REGISTRATOR'),('completor','COMPLETOR'),('remote','REMOTE'))
    Expert1 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert1 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert2 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert2 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert3 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert3 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert4 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert4 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert5 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert5 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert6 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert6 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert7 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert7 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert8 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert8 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert9 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert9 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert10 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert10 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert11 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert11 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert12 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert12 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    problem_status_choice = (('internal','INTERNAL'),('external','EXTERNAL'))
    Status_Of_problem  = models.CharField(choices=problem_status_choice,max_length=10,null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:  
        db_table = "E1MPLS"  

class Push(models.Model):
    start_date = jmodels.jDateTimeField()
    end_date = jmodels.jDateTimeField(null=True,blank=True)
    status_choice = (('open','OPEN'),('in progress','IN PROGRESS'),('close','CLOSE'))
    status = models.CharField(choices=status_choice,max_length=25,null=True,blank=True)
    organization=models.ForeignKey(Push_Organization,on_delete=models.SET_NULL,null=True,related_name='auth.user+')
    description = models.TextField(max_length=255)
    Status_Of_People = (('present','PRESENT'),('registrator','REGISTRATOR'),('completor','COMPLETOR'),('remote','REMOTE'))
    Expert1 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert1 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert2 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert2 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert3 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert3 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert4 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert4 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert5 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert5 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert6 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert6 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert7 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert7 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert8 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert8 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert9 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert9 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert10 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert10 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert11 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert11 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert12 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert12 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    problem_status_choice = (('internal','INTERNAL'),('external','EXTERNAL'))
    Status_Of_problem  = models.CharField(choices=problem_status_choice,max_length=10,null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:  
        db_table = "Push"  

class Access(models.Model):
    boss=models.ForeignKey(assign_to,on_delete=models.SET_NULL,null=True,blank=True,related_name='auth.user+')
    start_date = jmodels.jDateTimeField()
    end_date = jmodels.jDateTimeField(null=True,blank=True)
    expertise=models.ForeignKey(assign_to,on_delete=models.SET_NULL,null=True,blank=True,related_name='auth.user+')
    reson = models.TextField(max_length=255)
    Status_Of_People = (('present','PRESENT'),('registrator','REGISTRATOR'),('completor','COMPLETOR'),('remote','REMOTE'))
    Expert1 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert1 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert2 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert2 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert3 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert3 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert4 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert4 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert5 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert5 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert6 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert6 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert7 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert7 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert8 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert8 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert9 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert9 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert10 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert10 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert11 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert11 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    Expert12 = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    Staus_Of_Expert12 = models.CharField(choices=Status_Of_People,max_length=25,null=True,blank=True)
    problem_status_choice = (('internal','INTERNAL'),('external','EXTERNAL'))
    Status_Of_problem  = models.CharField(choices=problem_status_choice,max_length=10,null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:  
        db_table = "Access"  

class NoAnswerCall(models.Model):
    call_date = jmodels.jDateTimeField()
    expertise=models.ForeignKey(assign_to,on_delete=models.SET_NULL,null=True,blank=True,related_name='auth.user+')
    caller = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    numberofcall=models.IntegerField(blank=True,null=True)
    description = models.TextField(max_length=255)
    def __str__(self):
        return self.name
    class Meta:  
        db_table = "NoAnswerCall"  

class ResponseTime(models.Model):
    name =  models.CharField(max_length=255)
    start_date = jmodels.jDateTimeField()
    SwitchResponseTime=models.FloatField(blank=True,null=True)
    VPGResponseTime=models.FloatField(blank=True,null=True)
    IvaResponseTime=models.FloatField(blank=True,null=True)
    USSDResponseTime=models.FloatField(blank=True,null=True)
    registrator = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    def __str__(self):
        return self.name
    class Meta:  
        db_table = "ResponseTime"  

class APNIrancell(models.Model):
    date = jmodels.jDateTimeField()
    number1= models.ForeignKey(IrancellNumber,on_delete=models.SET_NULL,null=True,blank=True,related_name='Irancellnumber+')
    number3= models.ForeignKey(IrancellNumber,on_delete=models.SET_NULL,null=True,blank=True,related_name='Irancellnumber+')
    number4= models.ForeignKey(IrancellNumber,on_delete=models.SET_NULL,null=True,blank=True,related_name='Irancellnumber+')
    number5= models.ForeignKey(IrancellNumber,on_delete=models.SET_NULL,null=True,blank=True,related_name='Irancellnumber+')
    number6= models.ForeignKey(IrancellNumber,on_delete=models.SET_NULL,null=True,blank=True,related_name='Irancellnumber+')
    registrator = models.ForeignKey(expert,on_delete=models.SET_NULL,null=True,blank=True,related_name='expert+')
    description = models.TextField(max_length=255)
    def __str__(self):
        return self.date
    class Meta:  
        db_table = "APNIrancell"  





    














    





    











