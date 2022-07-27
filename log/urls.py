from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.conf.urls import url
from django_downloadview import ObjectDownloadView
from .models import EventKindofProblem
from .views import EventUpdateView
download = ObjectDownloadView.as_view(model=EventKindofProblem, file_field='file')
from .admin import *

admin.site.site_header = "SADADPSP Log Admin"
admin.site.site_title = "SADADPSP Log Admin Portal"
admin.site.index_title = "SADADPSP Log Administartions "


urlpatterns = [
 path('eventlist/', views.eventlist, name='eventlist'),
 path('', TemplateView.as_view(template_name='home.html'), name='home'),
 path('event/', views.event, name='event'),
 path('eventlist/<int:id>',views.eventlist),
 path('/eventlist/%<int:id>',views.eventlist),  
 #path('eventedit/<int:id>', views.eventedit),
 path('eventedit/<int:pk>/', EventUpdateView.as_view(),name='event-update'),
 path('eventedit/', views.eventedit),  
 path('eventupdate/<int:id>', views.eventupdate),  
 path('eventdelete/<int:id>', views.eventdestroy),
 path('responsetimelist/', views.responsetimelist , name = "responsetimelist"),
 path('responsetimeedit/<int:id>', views.responsetimeedit , name="responsetimeedit"),
 path(r'^search/$', views.search , name="search"),
 path('eventlist/eventpdf', views.eventpdf , name='eventpdf'), 
 path('eventlist/get_csv', views.get_csv , name='get_csv'),


]
#urlpatterns = [
#    url(r'^search/$', views.search, name='search'),
#]