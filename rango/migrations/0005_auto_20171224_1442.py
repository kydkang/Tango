# Generated by Django 2.0 on 2017-12-24 07:42

from django.db import migrations, models
import rango.models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20171224_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0, validators=[rango.models.validate_number]),
        ),
    ]
