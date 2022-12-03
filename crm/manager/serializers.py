from rest_framework import serializers
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
        Customers.objects.get(id=instance.id).update(**validated_data)
        for data in services_data:
            service, created = Services.objects.get_or_create(**data)
            customer.services.add(service)
        return instance
