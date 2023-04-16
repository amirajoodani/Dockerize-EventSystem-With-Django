from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.conf.urls import url
from django_downloadview import ObjectDownloadView
from .models import EventKindofProblem
from .views import EventUpdateView , PushUpdateView ,E1MPLSUpdateView
download = ObjectDownloadView.as_view(model=EventKindofProblem, file_field='file')
from .admin import *

admin.site.site_header = "SADADPSP Log Admin"
admin.site.site_title = "SADADPSP Log Admin Portal"
admin.site.index_title = "SADADPSP Log Administartions "


urlpatterns = [
 path('eventlist/', views.eventlist, name='eventlist'),
 path('pushlist/', views.pushlist, name='pushlist'),
 path('', TemplateView.as_view(template_name='home.html'), name='home'),
 path('event/', views.event, name='event'),
 path('push/', views.push, name='push'),
 path('eventlist/<int:id>',views.eventlist),
 path('/eventlist/%<int:id>',views.eventlist),  
 path('pushlist/<int:id>',views.pushlist),
 path('/pushlist/%<int:id>',views.pushlist),  
 #path('eventedit/<int:id>', views.eventedit),
 path('eventedit/<int:pk>/', EventUpdateView.as_view(),name='event-update'),
 path('eventedit/', views.eventedit), 
 path('pushupdate/<int:pk>/', PushUpdateView.as_view(),name='push-update'),
 path('pushupdate/', views.pushedit),   
 path('eventupdate/<int:id>', views.eventupdate),
 path('pushupdate/<int:id>', views.pushupdate),  
 path('eventdelete/<int:id>', views.eventdestroy),
 path('pushdelete/<int:id>', views.pushdestroy),
 path('responsetimelist/', views.responsetimelist , name = "responsetimelist"),
 path('responsetimeedit/<int:id>', views.responsetimeedit , name="responsetimeedit"),
 path(r'^search/$', views.search , name="search"),
 path('eventlist/eventpdf', views.eventpdf , name='eventpdf'), 
 path('eventlist/get_csv', views.get_csv , name='get_csv'),
 path('pushlist/get_csv', views.get_csv , name='get_csv'),
 path('eventlist/load_problems', views.load_problems, name='load_problems'),
 #........................................ E1MPLS.............................................#
 path('E1MPLS/', views.E1MPLS, name='E1MPLS'),
 path('E1MPLSlist/', views.E1MPLSlist, name='E1MPLSlist'),
 path('E1MPLSlist/<int:id>',views.E1MPLS),
 path('/E1MPLSlist/%<int:id>',views.E1MPLS),  
 path('E1MPLSupdate/<int:pk>/', E1MPLSUpdateView.as_view(),name='E1MPLSupdate'),
 path('E1MPLSupdate/', views.E1MPLSedit),
 path('E1MPLSupdate/<int:id>', views.E1MPLSupdate),
 path('E1MPLSdelete/<int:id>', views.E1MPLSdestroy),
 path('E1MPLSlist/get_csv', views.get_csv , name='get_csv'),
 #.............................................................................................#




]
#urlpatterns = [
#    url(r'^search/$', views.search, name='search'),
#]