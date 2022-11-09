import django_filters
from manager.models import Customers


class CustomersFilter(django_filters.FilterSet):
    firstname = django_filters.CharFilter(lookup_expr='icontains')
    lastname = django_filters.CharFilter(lookup_expr='icontains')
    phone = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Customers
        fields = '__all__'
