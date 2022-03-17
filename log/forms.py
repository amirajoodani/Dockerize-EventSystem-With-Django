from django import forms  
from log.models import EventKindofProblem

class EventForm(forms.ModelForm):  
    class Meta:  
        model = EventKindofProblem  
        fields = "__all__"  

