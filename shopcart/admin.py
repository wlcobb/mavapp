from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Style
from .models import Feature
from .models import Brand
from .models import Appliance
from .models import AppliaceFeature
from .models import ApplianceStyle
from .models import Order
from .models import OrderAppliances

class CategoryList(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ['name']

class StyleList(admin.ModelAdmin):
    list_display = ('name','category',)
    ordering = ['category']

class FeatureList(admin.ModelAdmin):
    list_display = ('name','category',)
    ordering = ['category']

class BrandList(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ['name']

class ApplianceList(admin.ModelAdmin):
    list_display = ('name', 'model', 'price', 'category', 'brand')
    ordering = ['name']

class ApplianceFeatureList(admin.ModelAdmin):
    list_display = ('appliance','feature',)
    ordering = ['appliance']

class ApplianceStyleList(admin.ModelAdmin):
    list_display = ('appliance','style',)
    ordering = ['appliance']

class OrderList(admin.ModelAdmin):
    list_display = ('customer',)
    ordering = ['customer']

class OrderAppliancesList(admin.ModelAdmin):
    list_display = ('order','appliance', 'style',)
    ordering = ['order']

admin.site.register(Category, CategoryList)
admin.site.register(Style, StyleList)
admin.site.register(Feature, FeatureList)
admin.site.register(Brand, BrandList)
admin.site.register(Appliance, ApplianceList)
admin.site.register(AppliaceFeature, ApplianceFeatureList)
admin.site.register(ApplianceStyle, ApplianceStyleList)
admin.site.register(Order, OrderList)
admin.site.register(OrderAppliances, OrderAppliancesList)
