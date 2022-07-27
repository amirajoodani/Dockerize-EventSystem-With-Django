
import xlwt
from django.http import HttpResponse
from django.core.exceptions import FieldDoesNotExist
from django.utils.encoding import force_text
from django.conf.urls import url
from django.contrib import admin
import six

'''
To add export button to an admin page
 - inherit 'ExcelExportAdmin'
 - add fields to be exported, export_excel_fields = '',''...
 - mention path to 'change_list_template'
Usage of the below code is explained here - https://truptishetty.medium.com/how-to-export-filtered-data-in-django-58129833239e
'''
class ExcelExportAdmin(admin.ModelAdmin):
 
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        uri = request.build_absolute_uri().split("?")
        params = ""
        if len(uri) > 1:
            params = "?"+uri[1]
        extra_context['export_link'] = request.get_full_path().split("?")[0]+'export/'+params
        return super().changelist_view(request, extra_context=extra_context)
  
    def get_urls(self):
        urls = super().get_urls()
        export_url = [
               url(r'^export/$', self.export)]     
        return export_url + urls  
    
    def export(self, request):       
        export_excel = ExcelExport(self)
        return export_excel.export(request)
    
class ExcelExport():
    def __init__(self,admin_instance):
        self.admin_instance = admin_instance
    
    def export(self,request):  
        file_name = str(self.admin_instance.model._meta.verbose_name_plural)
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="'+file_name+'.xls"'
        cl = self.admin_instance.get_changelist_instance(request)
        queryset = cl.get_queryset( request)
        #queryset = self.admin_instance.get_queryset(request)
        #field_names = self.get_fields(queryset)
        columns = [self.get_header_name(queryset.model, field_name) for field_name in list(self.admin_instance.export_excel_fields)]
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet(file_name)
        
        # Sheet header, first row
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
    
        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        for obj in queryset:
            row_num += 1
            col_num = 1
            for col_num in range(len(self.admin_instance.export_excel_fields)):
                field_value = self.get_field_value(obj,  self.admin_instance.export_excel_fields[col_num])
                ws.write(row_num, col_num, str(field_value), font_style)
    
        wb.save(response)
        return response
    
    def get_header_name(self, model, field_name):
        """ Override if a custom value or behaviour is required for specific fields. """
        if '__' not in field_name:
            try:
                field = model._meta.get_field(field_name)
            except FieldDoesNotExist as e:
                return field_name.replace('_', ' ').title()
    
            return force_text(field.verbose_name).title()
        else:
            related_field_names = field_name.split('__')
            field = model._meta.get_field(related_field_names[0])
            assert field.is_relation
            return force_text(related_field_names[0]).title()
        
    def get_field_value(self, obj, field_name):
        """ Override if a custom value or behaviour is required for specific fields. """
        if '__' not in field_name:
            if hasattr(obj, 'all') and hasattr(obj, 'iterator'):
                return ','.join([getattr(ro, field_name) for ro in obj.all()])
    
            try:
                field = obj._meta.get_field(field_name)
            except FieldDoesNotExist as e:
                if not hasattr(obj, field_name):
                    # if it is a custom property defined in admin page
                    invert_op = getattr(self.admin_instance, field_name, None)
                    if callable(invert_op):
                        return eval("self.admin_instance."+field_name+"(obj)")           
                    raise e
                # field_name is a property.
                return getattr(obj, field_name)
    
            value = field.value_from_object(obj)
            if field.many_to_many:
                return ','.join([six.text_type(ro) for ro in value])
            elif field.choices:
                if value is None or six.text_type(value).strip() == '':
                    return ''
                return dict(field.choices)[value]
            return field.value_from_object(obj)
        else:
            related_field_names = field_name.split('__')
            related_obj = getattr(obj, related_field_names[0])
            related_field_name = '__'.join(related_field_names[1:])
            if related_obj:
                return self.get_field_value( related_obj, related_field_name)
            else:
                return ''
        