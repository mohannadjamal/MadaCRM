from rest_framework import serializers
from django.shortcuts import get_object_or_404
from manager.models import Customers, Services


class ServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = '__all__'


class CustomersSerializer(serializers.ModelSerializer):
    services = ServicesSerializer(many=True)

    class Meta:
        model = Customers
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        services_data = validated_data.pop('services')
        customers = Customers.objects.create(**validated_data)
        for data in services_data:
            service, created = Services.objects.get_or_create(**data)
            customers.services.add(service)
        return customers

    def update(self, instance, validated_data):
        services_data = validated_data.pop('services')
        print(validated_data)
        first_name = validated_data.pop('firstname')
        last_name= validated_data.pop('lastname')
        phone = validated_data.pop('phone')
        instance.firstname = first_name
        instance.lastname = last_name
        instance.phone = phone
        instance.services.clear()
        for data in services_data:
            service, created = Services.objects.get_or_create(**data)
            #customer.services.add(service)
            instance.services.add(service)
        instance.save(update_fields=['firstname', 'lastname', 'phone'])
        return instance
