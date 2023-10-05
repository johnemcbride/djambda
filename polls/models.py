import datetime

from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.contrib import admin


class ProductCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product Categories"


class Product(models.Model):

    name = models.CharField(max_length=200)

    product_category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Term(models.Model):

    name = models.CharField(max_length=20, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class ProductPackage(models.Model):
    name = models.CharField(max_length=200)
    product_category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, related_name='product_category')

    products = models.ManyToManyField(
        Product, blank=True)

    def __str__(self):
        return self.name

    def cat(self):
        return self.product_category


class TermProductPackagePrice(models.Model):

    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    product_package = models.ForeignKey(
        ProductPackage, on_delete=models.CASCADE)
    full_price = models.FloatField(default=0)
    under_30s_price = models.FloatField(default=0)
    sibling_price = models.FloatField(default=0)

    def __str__(self):
        return ''

class Member(models.Model):

    class MemberType(models.TextChoices):
        SIBLING = "SIBLING"
        UNDER30 = "UNDER30"
        FULL = "FULL"
    
    class Gender(models.TextChoices):
        MALE = "MALE"
        FEMALE = "FEMALE"
        PREFERNOTSAY = "PREFERNOTSAY"
        OTHER = "OTHER"


    username = models.CharField(max_length=200)
    email = models.EmailField()
    forename = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    siblings = models.BooleanField()
    profile = models.CharField(
        max_length=200,
        choices=MemberType.choices
    )
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=200,
        choices=Gender.choices
    )
    ethnicity = models.CharField(max_length=200)
    payment_holiday = models.BooleanField()



