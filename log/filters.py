import django_filters
from .models import *

class eventfilter(django_filters.FilterSet):
    
    mounth_of_start_gt = django_filters.NumberFilter(field_name='mounth_of_start', lookup_expr='gt')
    mounth_of_start_lt = django_filters.NumberFilter(field_name='mounth_of_start', lookup_expr='lt')
    #day_of_start = django_filters.CharFilter()
    day_of_start_gt = django_filters.NumberFilter(field_name='day_of_start', lookup_expr='gt')
    day_of_start_lt = django_filters.NumberFilter(field_name='day_of_start', lookup_expr='lt')
    #day_of_end = django_filters.NumberFilter()
    #mounth_of_start = django_filters.CharFilter()
    
    
    #city = django_filters.CharFilter(field_name='city',lookup_expr='exact')


    class Meta:
        model = EventKindofProblem
        fields=['day_of_start','mounth_of_start','hour_of_start','day_of_end','mounth_of_end','hour_of_end','city','Connection','mainproblem','detailproblem']