from django.contrib import admin
from .models import CarModel, Car, Service, ServicePrice, Order

class CarADmin(admin.ModelAdmin):
    list_display = ('client', 'plate_nr', 'car_model', 'vin_number')
    list_filter = ('client', 'car_model')
    search_fields = ('client', 'plate_nr', 'vin_number')

admin.site.register(CarModel)
admin.site.register(Car, CarADmin)
admin.site.register(Service)
admin.site.register(ServicePrice)
admin.site.register(Order)
# OrderList
# admin.site.register(OrderList)