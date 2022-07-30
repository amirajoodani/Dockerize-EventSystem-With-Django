from pyexpat import model
from django import forms  
from log.models import EventKindofProblem ,ResponseTime



class EventForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False, label="Export to CSV")
    class Meta:  
        model = EventKindofProblem  
        fields = '__all__' 

class responsetimeform(forms.ModelForm):

    class Meta:
        model = ResponseTime
        fields = '__all__'
