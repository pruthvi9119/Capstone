from django.urls import path, include
from django.contrib import admin
from .views import home, geo, inspectionpolicy,zipcode,allrestaurants,restaurantname,restauranttype,streetaddress,inspectionscore,powerbidashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),  # Root URL to display CSV data
    path('', home, name='home'),
    path('geo/', geo, name='geo'),
    path('inspectionpolicy/', inspectionpolicy, name='inspectionpolicy'),
    path('zipcode/', zipcode, name='zipcode'),
    path('allrestaurants/',allrestaurants, name='allrestaurants'),
    path('restaurantname/', restaurantname, name='restaurantname'),
    path('restauranttype/', restauranttype, name='restauranttype'),
    path('streetaddress/', streetaddress, name='streetaddress'),
    path('inspectionscore/', inspectionscore, name='inspectionscore'),
    path('powerbi/', powerbidashboard, name='powerbidashboard'),
 
]

