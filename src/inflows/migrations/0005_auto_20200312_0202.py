# Generated by Django 3.0.4 on 2020-03-12 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inflows', '0004_auto_20200312_0140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inflow',
            name='id',
        ),
        migrations.AlterField(
            model_name='inflow',
            name='Day_of_Input',
            field=models.DateField(primary_key=True, serialize=False),
        ),
    ]
