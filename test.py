inflow = Inflow(Day_of_Input='2009-01-01',GS_2 = 17.06,GS_15=15.04,Ferreira=3.25,Luphohlo_Daily_Level=1011.08, Mkinkomo_Reservor_Daily_Level=589.5)


from inflows.models import Inflow
from inflows.serializers import InflowSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

serializer = InflowSerializer(inflow)
serializer.data

inflow.save()


echo '{"Day_of_Input":"2009-01-02","GS_2":"2.200","GS_15":"1.400","Ferreira":"3.250","Luphohlo_Daily_Level":"1.080","Mkinkomo_Reservor_Daily_Level":"5.500"}' | http http://127.0.0.1:8000/inflows/









































# from inflows.models import Inflow
# from inflows.serializers import InflowSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class InflowList(APIView):
#     """
#     List all inflows, or create a new inflow.
#     """

#     def get(self, request, format=None):
#         inflows = Inflow.objects.all()
#         serializer = InflowSerializer(inflows, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = InflowSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get_object(self, pk):
#         try:
#             return Inflow.objects.get(pk=pk)
#         except Inflow.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         inflow = self.get_object(pk)
#         serializer = InflowSerializer(inflow)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         inflow = self.get_object(pk)
#         serializer = InflowSerializer(inflow, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         inflow = self.get_object(pk)
#         inflow.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # Create your views here.


# @api_view(['GET', 'POST'])
# def inflow_list(request, format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         inflows = Inflow.objects.all()
#         serializer = InflowSerializer(inflows, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = InflowSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def inflow_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a inflow.
#     """
#     try:
#         inflow = Inflow.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = InflowSerializer(inflow)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = InflowSerializer(inflow, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         inflow.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
