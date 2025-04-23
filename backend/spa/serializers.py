from rest_framework import serializers
from .models import Subscriber, ContactMessage, Booking, Product, Order, CustomerProfile, Paystub, Employee

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['email']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['customer', 'employee', 'service', 'start_time', 'end_time']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock', 'image']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'products', 'total', 'pickup_time']

class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = ['points', 'referral_code']

class PaystubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paystub
        fields = ['date', 'amount']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['availability']
