from csv import field_size_limit
from pyexpat import model
from django import forms  
from log.models import EventKindofProblem ,ResponseTime ,EventMainProblem,EventDetailProblem


class EventForm(forms.ModelForm):
    #export_to_CSV = forms.BooleanField(required=False, label="Export to CSV")
    class Meta:  
        model = EventKindofProblem  
        fields = '__all__' 

class responsetimeform(forms.ModelForm):

    class Meta:
        model = ResponseTime
        fields = '__all__'

#class CreateEventForm(forms.ModelForm):
#   class Meta:

#        model=EventKindofProblem
#        field=('EventMainProblem','EventDetailProblem')
    
#   def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['EventDetailProblem'].queryset = EventDetailProblem.objects.none()
#        if 'EventMainProblem' in self.data:
#            try:
#               EventMainProblem_id=int(self.data.get('EventMainProblem'))
#               self.fields['EventDetailProblem'].queryset = EventMainProblem.objects.filter(EventMainProblem_id=EventMainProblem_id).order_by('name')
#           except (ValueError,TypeError):
#               pass
#        elif self.instance.pk:
#            self.fields['EventDetailProblem'].queryset = self.instance.EventMainProblem.EventDetailProblem_set.order_by('name')
