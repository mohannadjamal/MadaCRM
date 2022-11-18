from django.urls import path
from manager import views

urlpatterns = [
    #path('customers/', views.customers_list),
    #path('customers/<int:pk>', views.customers_detail),
    #path('services/', views.services_list),
    #path('services/<int:pk>', views.services_detail),
    path('customers/', views.CustomersList.as_view()),
    path('customers/<int:pk>/', views.CustomersDetail.as_view()),
    path('services/', views.ServicesList.as_view()),
    path('services/<int:pk>', views.ServicesDetail.as_view()),
]
