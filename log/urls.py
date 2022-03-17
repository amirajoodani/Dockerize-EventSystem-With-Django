from django.urls import path
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
 path('eventlist/', views.eventlist, name='eventlist'),
 path('', TemplateView.as_view(template_name='home.html'), name='home'),
 path('event/', views.event, name='event'),
 #path('eventlist/<int:id>',views.eventlist),  
 path('eventedit/<int:id>', views.eventedit),  
 path('eventupdate/<int:id>', views.eventupdate),  
 path('eventdelete/<int:id>', views.eventdestroy),  


]