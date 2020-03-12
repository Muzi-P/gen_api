from inflows.models import Inflow
from inflows.serializers import InflowSerializer
from rest_framework import generics


class InflowList(generics.ListCreateAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer


class InflowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer
