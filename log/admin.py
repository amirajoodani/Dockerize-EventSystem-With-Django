from django.contrib import admin
from .models import EventKindofProblem , EventMainProblem , EventDetailProblem , assign_to ,APNIrancell,ResponseTime, Bank , city ,Connection,NoAnswerCall, Report_To , Other_Organization ,expert ,Push_Organization ,E1MPLS,Push,Access
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin

class EventMainProblemAdmin(admin.ModelAdmin):
  list_filter = ('name','name')
  list_display = ('name', 'name')
  search_fields = ['name']
admin.site.register(EventMainProblem,EventMainProblemAdmin)

class EventDetailProblemAdmin(admin.ModelAdmin):
  list_filter = ('name','name')
  list_display = ('name', 'name')
  search_fields = ['name']
admin.site.register(EventDetailProblem,EventDetailProblemAdmin)

class EventKindofProblemAdmin(admin.ModelAdmin):
  list_filter = ('start_date','end_date')
  list_display = ('id', 'name', 'status','description')
  search_fields = ['name','status']
admin.site.register(EventKindofProblem,EventKindofProblemAdmin)

class assign_toAdmin(admin.ModelAdmin):
  list_filter = ('name','name')
  list_display = ( 'name','name')
  search_fields = ['name']
admin.site.register(assign_to,assign_toAdmin)

class BankAdmin(admin.ModelAdmin):
  list_filter = ('name','name')
  list_display = ('name','name')
  search_fields = ['name']
admin.site.register(Bank,BankAdmin)

class expertAdmin(admin.ModelAdmin):
  list_filter = ('name','name')
  list_display = ('name','name')
  search_fields = ['name']
admin.site.register(expert,expertAdmin)

class cityAdmin(admin.ModelAdmin):
  list_filter = ('name', 'name')
  list_display = ('name', 'name')
  search_fields = ['name']
admin.site.register(city,cityAdmin)

class ConnectionAdmin(admin.ModelAdmin):
  list_filter = ('Connection', 'Connection')
  list_display = ('Connection', 'Connection')
  search_fields = ['Connection']
admin.site.register(Connection,ConnectionAdmin)

class Report_ToAdmin(admin.ModelAdmin):
  list_filter = ('Department','Department')
  list_display = ('Department','Department')
  search_fields = ['Department']
admin.site.register(Report_To,Report_ToAdmin)

class Other_OrganizationAdmin(admin.ModelAdmin):
  list_filter = ('organization','organization')
  list_display = ('organization','organization')
  search_fields = ['organization']
admin.site.register(Other_Organization,Other_OrganizationAdmin)

class Push_OrganizationAdmin(admin.ModelAdmin):
  list_filter = ('organization','organization')
  list_display = ('organization','organization')
  search_fields = ['organization']
admin.site.register(Push_Organization,Push_OrganizationAdmin)

class E1MPLSAdmin(admin.ModelAdmin):
  list_filter = ('start_date','end_date')
  list_display = ('start_date','end_date')
  search_fields = ['start_date']
admin.site.register(E1MPLS,E1MPLSAdmin)

class PushAdmin(admin.ModelAdmin):
  list_filter = ('start_date','end_date')
  list_display = ('start_date','end_date')
  search_fields = ['start_date']
admin.site.register(Push,PushAdmin)

class AccessAdmin(admin.ModelAdmin):
  list_filter = ('start_date','end_date')
  list_display = ('start_date','end_date')
  search_fields = ['start_date']
admin.site.register(Access,AccessAdmin)

class NoAnswerCallAdmin(admin.ModelAdmin):
  list_filter = ('call_date','call_date')
  list_display = ('call_date','call_date')
  search_fields = ['call_date']
admin.site.register(NoAnswerCall,NoAnswerCallAdmin)

class ResponseTimeAdmin(admin.ModelAdmin):
  list_filter = ('start_date','start_date')
  list_display = ('start_date','start_date')
  search_fields = ['start_date']
admin.site.register(ResponseTime,ResponseTimeAdmin)

class APNIrancellAdmin(admin.ModelAdmin):
  list_filter = ('date','date')
  list_display = ('date','date')
  search_fields = ['date']
admin.site.register(APNIrancell,APNIrancellAdmin)















