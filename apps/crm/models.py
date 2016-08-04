#_*_coding:utf-8_*_
from django.db import models
from django.utils.translation import ugettext_lazy as _
from apps.product.models import Product
from datetime import datetime

# Create your models here.
class Supplier(models.Model):
    id      = models.AutoField(primary_key = True)
    name    = models.CharField(max_length  = 200            , verbose_name = _(u'供应商名称'))
    addr    = models.CharField(max_length  = 200            , verbose_name = _(u'地址'))
    contact = models.CharField(max_length  = 200            , verbose_name = _(u'联系人'))
    phone   = models.CharField(max_length  = 200            , verbose_name = _(u'联系电话'))
    date    = models.DateTimeField(default = datetime.now   , verbose_name = _(u'创建时间'))
    remark   = models.TextField(blank       = True,verbose_name             = _(u'备注'))
    class Meta:
        verbose_name_plural = verbose_name = _(u'供货商列表')
    def __unicode__(self):
        return self.name


class Customer(models.Model):
    id      = models.AutoField(primary_key = True)
    name    = models.CharField(max_length  = 200            , verbose_name = _(u'客户名称'))
    addr    = models.CharField(max_length  = 200            , verbose_name = _(u'地址'))
    contact = models.CharField(max_length  = 200            , verbose_name = _(u'联系人'))
    phone   = models.CharField(max_length  = 200            , verbose_name = _(u'联系电话'))
    date    = models.DateTimeField(default = datetime.now   , verbose_name = _(u'创建时间'))
    remark   = models.TextField(blank       = True,verbose_name             = _(u'备注'))
    class Meta:
        verbose_name_plural = verbose_name = _(u'客户列表')
    def __unicode__(self):
        return self.name
