import django_filters
from .models import *

class eventfilter(django_filters.FilterSet):
    day_of_start = django_filters.NumberFilter()
    #day_of_start__gt = django_filters.NumberFilter(field_name='day_of_start', lookup_expr='gt')
    #day_of_start__lt = django_filters.NumberFilter(field_name='day_of_start', lookup_expr='lt')


    class Meta:
        model = EventKindofProblem
        fields=['day_of_start']