from django.contrib import admin
from .models import EventKindofProblem , EventMainProblem , EventDetailProblem , IrancellNumber,year,day,mounth,hour,minute,assign_to ,APNIrancell,ResponseTime, Bank , city ,Connection,NoAnswerCall, Report_To , Other_Organization ,expert ,Push_Organization ,E1MPLS,Push,Access
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin
from simple_history.admin import SimpleHistoryAdmin
from django.utils.html import format_html
#from utils.excel_export import ExcelExportAdmin

#admin.site.register(EventKindofProblem,SimpleHistoryAdmin)

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

#class EventKindofProblemAdmin(admin.ModelAdmin):
  #list_filter = ('day_of_start','day_of_end')
  #list_display = ('day_of_start','mounth_of_start','year_of_start','day_of_end','mounth_of_end','year_of_end','mainproblem','detailproblem','Bank','image','city','Connection','IncidentID','DownTime','ReportToDepartment','Assigng_to_others')
  #search_fields = ['day_of_start','mounth_of_start','year_of_start','day_of_end','mounth_of_end','year_of_end','SMS','mainproblem','detailproblem','Bank','image','city','Connection','IncidentID','DownTime','ReportToDepartment','Assign_to_name1','Assign_to_name2','Assign_to_name3','Assign_to_name4','Assigng_to_others']
#admin.site.register(EventKindofProblem,EventKindofProblemAdmin)

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

class IrancellNumberAdmin(admin.ModelAdmin):
  list_filter = ('number','number')
  list_display = ( 'number','number')
  search_fields = ['number']
admin.site.register(IrancellNumber,IrancellNumberAdmin)

class yearAdmin(admin.ModelAdmin):
  list_filter = ('year','year')
  list_display = ( 'year','year')
  search_fields = ['year']
admin.site.register(year,yearAdmin)

class dayAdmin(admin.ModelAdmin):
  list_filter = ('day','day')
  list_display = ( 'day','day')
  search_fields = ['day']
admin.site.register(day,dayAdmin)

class mounthAdmin(admin.ModelAdmin):
  list_filter = ('mounth','mounth')
  list_display = ( 'mounth','mounth')
  search_fields = ['mounth']
admin.site.register(mounth,mounthAdmin)

class hourAdmin(admin.ModelAdmin):
  list_filter = ('hour','hour')
  list_display = ( 'hour','hour')
  search_fields = ['hour']
admin.site.register(hour,hourAdmin)

#class minuteAdmin(admin.ModelAdmin):
#  list_filter = ('minute','minute')
#  list_display = ( 'minute','minute')
#  search_fields = ['minute']
#admin.site.register(minute,minuteAdmin)

#admin.site.register(EventKindofProblem,SimpleHistoryAdmin)

class EventKindofProblemHistoryAdmin(SimpleHistoryAdmin):
  history_list_display = ["changed_fields","list_changes"]
    
  def changed_fields(self, obj):
        if obj.prev_record:
            delta = obj.diff_against(obj.prev_record)
            return delta.changed_fields
        return None

  def list_changes(self, obj):
        fields = ""
        if obj.prev_record:
            delta = obj.diff_against(obj.prev_record)

            for change in delta.changes:
                fields += str("<strong>{}</strong> changed from <span style='background-color:#ffb5ad'>{}</span> to <span style='background-color:#b3f7ab'>{}</span> . <br/>".format(change.field, change.old, change.new))
            return format_html(fields)
        return None


admin.site.register(EventKindofProblem,EventKindofProblemHistoryAdmin)

















