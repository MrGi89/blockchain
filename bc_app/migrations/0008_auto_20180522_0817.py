# Generated by Django 2.0.5 on 2018-05-22 08:17

import django.contrib.postgres.fields
from django.db import migrations, models
from django.contrib.postgres.operations import HStoreExtension


class Migration(migrations.Migration):

    dependencies = [
        ('bc_app', '0007_auto_20180521_1657'),
    ]

    operations = [
        HStoreExtension(),
        migrations.AlterField(
            model_name='transaction',
            name='inputs',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None),
        ),
    ]
