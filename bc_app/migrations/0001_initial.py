# Generated by Django 2.0.5 on 2018-05-21 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.IntegerField()),
                ('hash160', models.CharField(max_length=128)),
                ('final_balance', models.IntegerField()),
                ('n_tx', models.IntegerField()),
                ('total_received', models.IntegerField()),
                ('total_spend', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_height', models.IntegerField()),
                ('double_spend', models.BooleanField()),
                ('hash', models.CharField(max_length=128)),
                ('relayed_by', models.CharField(max_length=128)),
                ('size', models.IntegerField()),
                ('time', models.IntegerField()),
                ('tx_index', models.IntegerField()),
                ('version', models.SmallIntegerField()),
                ('inputs', models.TextField()),
                ('outputs', models.TextField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='bc_app.Address')),
            ],
        ),
    ]
