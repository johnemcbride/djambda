from django.contrib import admin

from django.db import models
from django import forms
from .models import ProductPackage, Term, TermProductPackagePrice, Product, ProductCategory


class ProductPackageAdmin(admin.StackedInline):
    model = ProductPackage
    list_display = ["name"]
    extra = 0
    formfield_overrides = {
        models.FloatField: {'widget': forms.TextInput(attrs={'size': '10'})},
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
    }


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
    extra = 1
    inlines = [ProductAdmin, ProductPackageAdmin]


class TermPriceInline(admin.StackedInline):
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
