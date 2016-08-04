#_*_coding:utf-8_*_

from django.contrib import admin
from models import Supplier,BuyList
from models import CustomersList,Sales

class SupplierAdmin(admin.ModelAdmin):
    search_fields = ('name','contact','phone','date')
    list_display = ('name','contact','phone','addr','date','extra')
    ordering = ('-date','name')
class BuyListAdmin(admin.ModelAdmin):
    search_fields = ('product_name','date')
    list_display = ('product_name','supplier','product_size','unit','product_num','unit_price','total_RMB','date','extra')
    ordering = ('-date','product_name')


class CustomersListAdmin(admin.ModelAdmin):
    search_fields = ('name','contact','phone','date')
    list_display = ('name','addr','contact','phone','date','extra')
    ordering = ('-date','name')

class SalesAdmin(admin.ModelAdmin):
    list_filter = ('is_payment',)
    search_fields = ('coustomer_name__name','salse_product_name','sales_date')
    list_display = ('coustomer_name','salse_product_name','sales_product_size','sales_unit','sales_num','sales_unit_price','total_RMB','is_payment','sales_date','extra')
    ordering = ('-sales_date','coustomer_name')


admin.site.register(Supplier,SupplierAdmin)
admin.site.register(BuyList,BuyListAdmin)

admin.site.register(CustomersList,CustomersListAdmin)
admin.site.register(Sales,SalesAdmin)
