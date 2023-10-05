import inspect
from pprint import pprint
import json
from django.contrib import admin

from django.db import models
from django import forms
from .models import ProductPackage, Term, TermProductPackagePrice, Product, ProductCategory, Member


import logging
import logging.config
import sys

from django.contrib import admin
admin.site.site_header = 'East London Community Band Admin'
admin.site.index_title = 'ELCB Admin '    # default: "Site administration". 
admin.site.site_title = 'ELCB ADMIN' # default: "Django site admin"


LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}

logging.config.dictConfig(LOGGING)

class ProductPackageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductPackageForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            self.fields['products'].queryset = Product.objects.filter(
                product_category_id=self.instance.product_category.id)
        
        # logging.info('does it dfie here? - line 40')
       

    
        
class ProductPackageAdmin(admin.StackedInline):

    logging.info('does it dfie here? - line 44')
    model = ProductPackage
    fields = ['products']

    logging.info('does it dfie here?')
    list_display = ["name"]
    extra = 0
    formfield_overrides = {
        models.FloatField: {'widget': forms.TextInput(attrs={'size': '10'})},
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
    }
    form = ProductPackageForm
    # def get_form(self, request, obj, **kwargs):
    #     logging.info('am i even called?')
    #     form = super(ProductPackageAdmin,self).get_form(request, obj, **kwargs)
    #     form.base_fields['products'].queryset=Product.objects.filter(
    #         product_category_id=self.instance.product_category.id)
    #     return form

class ProductAdmin(admin.StackedInline):
    model = Product
    extra = 0
    fieldsets = [
        (None, {"fields": ["name"]}),
    ]
    list_display = ["name"]

    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
    }


class ProductCategoryAdmin(admin.ModelAdmin):
    model = ProductCategory
    extra = 0
    inlines = [ProductAdmin, ProductPackageAdmin]


class TermPriceInline(admin.TabularInline):
    model = TermProductPackagePrice
    extra = 0


class TermAdmin(admin.ModelAdmin):
    model = Term
    extra = 1
    inlines = [TermPriceInline]
    fields = ["name", ("start_date", "end_date")]
    save_as = True


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Term, TermAdmin)
admin.site.register(Member)