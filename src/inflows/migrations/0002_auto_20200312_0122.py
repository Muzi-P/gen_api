# Generated by Django 3.0.4 on 2020-03-12 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inflows', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inflow',
            old_name='Created',
            new_name='created',
        ),
    ]
