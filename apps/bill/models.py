#_*_coding:utf-8_*_
from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from utils.get_order_id import get_order_id

# Create your models here.
class Supplier(models.Model):
    id      = models.AutoField(primary_key = True)
    name    = models.CharField(max_length  = 200            , verbose_name = _(u'供应商名称'))
    addr    = models.CharField(max_length  = 200            , verbose_name = _(u'地址'))
    contact = models.CharField(max_length  = 200            , verbose_name = _(u'联系人'))
    phone   = models.CharField(max_length  = 200            , verbose_name = _(u'联系电话'))
    date    = models.DateTimeField(default = datetime.now   , verbose_name = _(u'创建时间'))
    extra   = models.TextField(blank       = True,verbose_name             = _(u'备注'))
    class Meta:
        verbose_name_plural = verbose_name = _(u'供货商列表')
    def __unicode__(self):
        return self.name


class BuyList(models.Model):
    id           = models.AutoField(primary_key              = True)
    supplier     = models.ForeignKey(Supplier , verbose_name = '供货商')
    product_name = models.CharField(max_length               = 200            , verbose_name   = _(u'商品名称'))
    product_size = models.CharField(max_length               = 200            , verbose_name   = _(u'规格'))
    unit         = models.CharField(max_length               = 200            , verbose_name   = _(u'单位'))
    product_num  = models.CharField(max_length               = 200            , verbose_name   = _(u'数量'))
    unit_price   = models.DecimalField(max_digits            = 10             , decimal_places = 2      , default = 0.00    , verbose_name = _(u'单价'))
    total_RMB    = models.DecimalField(max_digits            = 10             , decimal_places = 2      , default = 0.00    , verbose_name = _(u'金额'))
    date         = models.DateTimeField(default              = datetime.now   , verbose_name   = _(u'创建时间'))
    extra        = models.TextField(blank                    = True   , verbose_name           = _(u'备注'))
    class Meta:
        verbose_name_plural = verbose_name = _(u'进货')
    def __unicode__(self):
        return self.product_name

class CustomersList(models.Model):
    id      = models.AutoField(primary_key = True)
    name    = models.CharField(max_length  = 200,verbose_name               = _(u'供应商名称'))
    addr    = models.CharField(max_length  = 200,blank                      = True,verbose_name = _(u'地址'))
    contact = models.CharField(max_length  = 200,blank                      = True,verbose_name = _(u'联系人'))
    phone   = models.CharField(max_length  = 200,blank                      = True,verbose_name = _(u'联系电话'))
    date    = models.DateTimeField(default = datetime.now   ,verbose_name = _(u'创建时间'))
    extra   = models.TextField(blank       = True,verbose_name              = _(u'备注'))
    class Meta:
        verbose_name_plural = verbose_name = _(u'客户列表')
    def __unicode__(self):
        return self.name


class Sales(models.Model):
    id                 = models.AutoField(primary_key                 = True)
    coustomer_name     = models.ForeignKey(CustomersList,verbose_name = _(u'客户名称'))
    sales_order_num    = models.CharField(db_index = True,unique  = True,editable = False,max_length  = 20,default = lambda:get_order_id(),verbose_name = _(u'销售单号'))
    salse_product_name = models.CharField(max_length                  = 200,verbose_name            = _(u'产品名称'))
    sales_product_size = models.CharField(max_length                  = 200,verbose_name            = _(u'规格'))
    sales_unit         = models.CharField(max_length                  = 200,verbose_name            = _(u'单位'))
    sales_num          = models.CharField(max_length                  = 200,verbose_name            = _(u'数量'))
    sales_unit_price   = models.DecimalField(max_digits               = 10,decimal_places           = 2,default          = 0.00,verbose_name = _(u'单价'))
    total_RMB          = models.DecimalField(max_digits               = 10,decimal_places           = 2,default          = 0.00,verbose_name = _(u'金额'))
    is_payment         = models.BooleanField(verbose_name             = _(u'付款状态'),help_text        = _(u'0：未付款，1：已付款'))
    sales_date         = models.DateTimeField(default                 = datetime.now,verbose_name = _(u'销售日期'))
    extra              = models.TextField(blank                       = True,verbose_name           = _(u'备注'))
    class Meta:
        verbose_name_plural = verbose_name = _(u'销售')
    def __unicode__(self):
        return self.coustomer_name.name

