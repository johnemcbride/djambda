# Generated by Django 4.2.5 on 2023-10-02 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_product_productcategory_productpackage_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name_plural': 'Product Categories'},
        ),
        migrations.AlterField(
            model_name='term',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
