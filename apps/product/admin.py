#_*_coding:utf-8_*_

from django.contrib import admin
from models import Supplier,Customer
from models import ProductCategory,ProductSpec,ProductUnit,Product
from models import StoreHouse

class SupplierAdmin(admin.ModelAdmin):
    search_fields = ('name','contact','phone','date')
    list_display = ('name','contact','phone','addr','date','remark')
    ordering = ('-date','name')

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('name','contact','phone','date')
    list_display = ('name','contact','phone','addr','date','remark')
    ordering = ('-date','name')

class ProductCategoryAdmin(admin.ModelAdmin):
    pass
class ProductSpecAdmin(admin.ModelAdmin):
    pass
class ProductUnitAdmin(admin.ModelAdmin):
    pass
class ProductAdmin(admin.ModelAdmin):
    pass
class StoreHouseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Supplier,SupplierAdmin)
admin.site.register(Customer,CustomerAdmin)

admin.site.register(ProductCategory,ProductCategoryAdmin)
admin.site.register(ProductSpec,ProductSpecAdmin)
admin.site.register(ProductUnit,ProductUnitAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(StoreHouse,StoreHouseAdmin)
