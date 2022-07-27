from pyexpat import model
from django import forms  
from log.models import EventKindofProblem ,ResponseTime

export_to_csv=forms.BooleanField()

class EventForm(forms.ModelForm):  
    class Meta:  
        model = EventKindofProblem  
        fields = '__all__' 

class responsetimeform(forms.ModelForm):

    class Meta:
        model = ResponseTime
        fields = '__all__'
