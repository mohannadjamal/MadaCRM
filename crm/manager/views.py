from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from manager.models import Customers, Services
from manager.serializers import CustomersSerializer, ServicesSerializer
from manager.filters import CustomersFilter
from django.db.models import Q
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# Create your views here.


class CustomersList(APIView):

    def get(self, request, format=None):
        customers = Customers.objects.all()
        query = request.GET.get('q')
        if query:
            customers = Customers.objects.filter(
                Q(firstname__icontains=query) | Q(
                    lastname__icontains=query) | Q(phone__icontains=query)
            )
        customers_serializer = CustomersSerializer(customers, many=True)
        return Response(customers_serializer.data)

    def post(self, request, format=None):
        customers_serializer = CustomersSerializer(data=request.data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return Response(customers_serializer.data, status=status.HTTP_201_CREATED)
        return Response(customers_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CustomersDetail(APIView):

#    def get_object(self, pk):
#        try:
#            return Customers.objects.get(pk=pk)
#        except Customers.DoesNotExist:
#            raise Http404

#    def get(self, request, pk, format=None):
#        customer = self.get_object(pk)
#        customer_serializer = CustomersSerializer(customer)
#        return Response(customer_serializer.data)

#    def put(self, request, pk, format=None):
#        customer = self.get_object(pk)
#        customer_serializer = CustomersSerializer(customer, data=request.data)
#        if customer_serializer.is_valid():
#            customer_serializer.save()
#            return Response(customer_serializer.data)

#    def delete(self, request, pk, format=None):
#        customer = self.get_object(pk)
#        customer.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer


class ServicesList(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ServicesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

################################################################# FUNCTION BASED VIEWS#################################################################################
# @api_view(['GET', 'POST'])
# def customers_list(request):
#    if request.method == 'GET':
#        customers = Customers.objects.all()
#        #filterset = CustomersFilter(request.GET, queryset=customers)
#        # if filterset.is_valid():
#        #    customers = filterset.qs
#        query = request.GET.get('q')
#        if query:
#            customers = Customers.objects.filter(
#                Q(firstname__icontains=query) | Q(
#                    lastname__icontains=query) | Q(phone__icontains=query)
#            )
#        customers_serializer = CustomersSerializer(customers, many=True)
#        return JsonResponse(customers_serializer.data, safe=False)
#    elif request.method == 'POST':
#        customers_data = JSONParser().parse(request)
#        customers_serializer = CustomersSerializer(data=customers_data)
#        if (customers_serializer.is_valid()):
#            customers_serializer.save()
#            return JsonResponse(customers_serializer.data, status=status.HTTP_201_CREATED)
#        return JsonResponse(customers_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def customers_detail(request, pk):

#    try:
#        customer = Customers.objects.get(pk=pk)
#    except Customers.DoesNotExist:
#        return JsonResponse({'message': 'The customer does not exist'}, status=status.HTTP_404_NOT_FOUND)

#    if request.method == 'GET':
#        customers_serializer = CustomersSerializer(customer)
#        return JsonResponse(customers_serializer.data)

#    elif request.method == 'PUT':
#        customer_data = JSONParser().parse(request)
#        customers_serializer = CustomersSerializer(
#            customer, data=customer_data)
#        if (customers_serializer.is_valid()):
#            customers_serializer.save()
#            return JsonResponse(customers_serializer.data)
#        return JsonResponse(customers_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#    elif request.method == 'DELETE':
#        customer.delete()
#        return JsonResponse({'message': 'Customer was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def services_list(request):
#    if request.method == 'GET':
#        services = Services.objects.all()
#        services_serializer = ServicesSerializer(services, many=True)
#        return JsonResponse(services_serializer.data, safe=False)

#    elif request.method == 'POST':
#        services_data = JSONParser().parse(request)
#        services_serializer = ServicesSerializer(data=services_data)
#        if (services_serializer.is_valid()):
#            services_serializer.save()
#            return JsonResponse(services_serializer.data, status=status.HTTP_201_CREATED)
#        return JsonResponse(services_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def services_detail(request, pk):

#    try:
#        services = Services.objects.get(pk=pk)
#    except Services.DoesNotExist:
#        return JsonResponse({'message': 'The service does not exist'}, status=status.HTTP_404_NOT_FOUND)

#    if request.method == 'GET':
#        services_serializer = ServicesSerializer(services)
#        return JsonResponse(services_serializer.data)

#    elif request.method == 'PUT':
#        services_data = JSONParser().parse(request)
#        services_serializer = ServicesSerializer(
#            services, data=services_data)
#        if (services_serializer.is_valid()):
#            services_serializer.save()
#            return JsonResponse(services_serializer.data)
#        return JsonResponse(services_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#    elif request.method == 'DELETE':
#        services.delete()
#        return JsonResponse({'message': 'Service was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
