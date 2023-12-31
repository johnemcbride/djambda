# Generated by Django 4.2.5 on 2023-10-04 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_productcategory_options_alter_term_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('forename', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('siblings', models.BooleanField()),
                ('profile', models.CharField(choices=[('SIBLING', 'Sibling'), ('UNDER30', 'Under30'), ('FULL', 'Full')], max_length=200)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('PREFERNOTSAY', 'Prefernotsay'), ('OTHER', 'Other')], max_length=200)),
                ('ethnicity', models.CharField(max_length=200)),
                ('payment_holiday', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='productpackage',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='polls.productcategory'),
        ),
    ]
