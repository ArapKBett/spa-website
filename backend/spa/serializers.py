from rest_framework import serializers
from .models import Subscriber, ContactMessage, Service, Employee, Booking, Product, Order, Paystub, Availability, Special
from django.contrib.auth.models import User

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['email']

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'price', 'duration']

class EmployeeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Employee
        fields = ['id', 'user', 'bio']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['service', 'employee', 'customer_email', 'start_time', 'end_time']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer_email', 'items']

class PaystubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paystub
        fields = ['date', 'amount']

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ['day', 'time_range']

class SpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Special
        fields = ['title', 'description', 'image']
