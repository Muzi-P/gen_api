# Generated by Django 3.0.4 on 2020-03-12 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inflows', '0006_auto_20200312_0256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inflow',
            name='Ferreira',
        ),
        migrations.RemoveField(
            model_name='inflow',
            name='GS_15',
        ),
        migrations.RemoveField(
            model_name='inflow',
            name='GS_2',
        ),
        migrations.RemoveField(
            model_name='inflow',
            name='Luphohlo_Daily_Level',
        ),
        migrations.RemoveField(
            model_name='inflow',
            name='Mkinkomo_Reservor_Daily_Level',
        ),
    ]