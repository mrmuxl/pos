#_*_coding:utf-8_*_

from django.contrib import admin
from models import Supplier,Customer,Product_Supplier

class SupplierAdmin(admin.ModelAdmin):
    search_fields = ('name','contact','phone','date')
    list_display = ('name','contact','phone','addr','date','remark')
    ordering = ('-date','name')

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('name','contact','phone','date')
    list_display = ('name','contact','phone','addr','date','remark')
    ordering = ('-date','name')

admin.site.register(Supplier,SupplierAdmin)
admin.site.register(Customer,CustomerAdmin)
