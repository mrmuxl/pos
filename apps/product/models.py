#_*_coding:utf-8_*_
from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

# Create your models here.
class Supplier(models.Model):
    """供应商信息"""
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
    """客户信息"""
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

class ProductCategory(models.Model):
    """商品分类"""
    name  = models.CharField(max_length  = 200, verbose_name  = _(u'商品分类名称'))
    class Meta:
        verbose_name_plural = verbose_name = _(u'商品分类')
    def __unicode__(self):
        return self.name

class ProductSpec(models.Model):
    """商品包装规格"""
    name    = models.CharField(max_length  = 200, verbose_name  = _(u'规格名称'))
    remark  = models.TextField(blank       = True,verbose_name  = _(u'备注'))
    class Meta:
        verbose_name_plural = verbose_name = _(u'商品规格')
    def __unicode__(self):
        return self.name

class ProductUnit(models.Model):
    """商品计量单位"""
    name    = models.CharField(max_length  = 200, verbose_name  = _(u'计量单位名称'))
    remark  = models.TextField(blank       = True,verbose_name  = _(u'备注'))
    class Meta:
        verbose_name_plural = verbose_name = _(u'商品计量单位')
    def __unicode__(self):
        return self.name

class Product(models.Model):
    """商品的基本信息"""
    name      = models.CharField(max_length= 200 , verbose_name  = _(u'商品名称'))
    category  = models.ForeignKey(ProductCategory,verbose_name   = _(u'商品分类'))
    spec      = models.ForeignKey(ProductSpec,verbose_name       = _(u'规格'))
    unit      = models.ForeignKey(ProductUnit,verbose_name       = _(u'单位'))
#    store_house      = models.ForeignKey(StoreHouse,verbose_name       = _(u'存储仓库'))
    remark    = models.TextField(blank                           = True,verbose_name  = _(u'备注'))
    class Meta:
        verbose_name_plural = verbose_name = _(u'商品基本信息')
    def __unicode__(self):
        return self.name

class StoreHouse(models.Model):
    """仓库信息，（需要添加仓库负责人）"""
    name  = models.CharField(max_length= 200 , verbose_name  = _(u'仓库名称'))
    addr  = models.CharField(max_length                      = 200            , verbose_name  = _(u'仓库地址'))
    phone   = models.CharField(max_length  = 200            , verbose_name = _(u'联系电话'))
    date  = models.DateTimeField(default                     = datetime.now   , verbose_name  = _(u'创建时间'))
    remark    = models.TextField(blank                           = True,verbose_name  = _(u'备注'))
    class Meta:
        verbose_name_plural = verbose_name = _(u'仓库')
    def __unicode__(self):
        return self.name

#
#商品 入库 的时候要跟那个仓库关联，一种商品对应一个仓库
#商品 和 供应商的关系是 多对多 也是在入库的时候决定
#
