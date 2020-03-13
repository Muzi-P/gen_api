from django.db import models

# Create your models here.


class Inflow(models.Model):
    Created = models.DateTimeField(auto_now_add=True)
    Day_of_Input = models.DateField(primary_key=True)
    GS_2 = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    GS_15 = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    Ferreira = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    Luphohlo_Daily_Level = models.DecimalField(
        max_digits=20, decimal_places=3, default=0)
    Mkinkomo_Reservoir_Daily_Level = models.DecimalField(
        max_digits=20, decimal_places=3, default=0)


class Meta:
    ordering = ['Day_of_Input']
