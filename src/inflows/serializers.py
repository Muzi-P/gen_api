from rest_framework import serializers
from inflows.models import Inflow



class InflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inflow
        fields = ['Day_of_Input', 'GS_2', 'GS_15', 'Ferreira', 'Luphohlo_Daily_Level', 'Mkinkomo_Reservor_Daily_Level']


























        
# class InflowSerializer(serializers.Serializer):
#     Day_of_Input = serializers.CharField()
#     GS_2 = serializers.DecimalField(max_digits=20, decimal_places=3)
#     GS_15 = serializers.DecimalField(max_digits=20, decimal_places=3)
#     Ferreira = serializers.DecimalField(max_digits=20, decimal_places=3)
#     Luphohlo_Daily_Level = serializers.DecimalField(
#         max_digits=20, decimal_places=3)
#     Mkinkomo_Reservor_Daily_Level = serializers.DecimalField(
#         max_digits=20, decimal_places=3)


# def create(self, validated_data):
#     """
#     Create and return a new `Inflow` instance, given the validated data.
#     """
#     return Inflow.objects.create(**validated_data)

# def update(self, instance, validated_data):
#     """
#     Update and return an existing `Inflow` instance, given the validated data.
#     """
#     instance.Day_of_Input = validated_data.get('Day_of_Input', instance.Day_of_Input)
#     instance.GS_2 = validated_data.get('GS_2', instance.GS_2)
#     instance.GS_15 = validated_data.get('GS_15', instance.GS_15)
#     instance.Ferreira = validated_data.get('Ferreira', instance.Ferreira)
#     instance.Luphohlo_Daily_Level = validated_data.get('Luphohlo_Daily_Level', instance.Luphohlo_Daily_Level)
#     instance.Mkinkomo_Reservor_Daily_Level = validated_data.get('Mkinkomo_Reservor_Daily_Level', instance.Mkinkomo_Reservor_Daily_Level)
    
#     instance.save()
#     return instance  
