from django.contrib import admin

from django.db import models
from django import forms
from .models import Band,    BandPackage


class BandPackageAdmin(admin.ModelAdmin):
    model = BandPackage
    list_display = ["name"]
    extra = 0
    formfield_overrides = {
        models.FloatField: {'widget': forms.TextInput(attrs={'size': '10'})},
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
    }


class BandAdmin(admin.ModelAdmin):
    model = Band
    extra = 0
    fieldsets = [
        (None, {"fields": ["name"]}),
    ]
    list_display = ["name"]

    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
    }


admin.site.register(Band, BandAdmin)
admin.site.register(BandPackage, BandPackageAdmin)