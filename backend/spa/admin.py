from django.contrib import admin
from .models import Subscriber, ContactMessage, Special, Employee, Service, Booking, Product, Order, CustomerProfile, Paystub

@admin.register(Special)
class SpecialAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'active']
    list_filter = ['active']
    search_fields = ['title', 'description']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'availability']
    search_fields = ['user__username', 'role']

admin.site.register(Subscriber)
admin.site.register(ContactMessage)
admin.site.register(Service)
admin.site.register(Booking)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(CustomerProfile)
admin.site.register(Paystub)
