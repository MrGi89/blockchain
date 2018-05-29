# Generated by Django 2.0.5 on 2018-05-21 16:57

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bc_app', '0006_auto_20180521_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='bc_app.Address'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='outputs',
            field=jsonfield.fields.JSONField(),
        ),
    ]
