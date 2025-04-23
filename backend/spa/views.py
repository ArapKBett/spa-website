from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
import stripe
from django.conf import settings
from .models import Subscriber, ContactMessage, Booking, Product, Order, CustomerProfile, Paystub, Employee
from .serializers import (
    SubscriberSerializer, ContactSerializer, BookingSerializer, ProductSerializer,
    CustomerProfileSerializer, PaystubSerializer, EmployeeSerializer
)

stripe.api_key = settings.STRIPE_SECRET_KEY

class SubscribeView(APIView):
    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
                'Welcome to Our Spa!',
                'Thank you for subscribing to our newsletter.',
                'from@spa.com',
                [serializer.validated_data['email']],
                fail_silently=False,
            )
            return Response({'message': 'Subscribed successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
                'New Contact Message',
                f"From: {serializer.validated_data['name']}\nEmail: {serializer.validated_data['email']}\nMessage: {serializer.validated_data['message']}",
                'from@spa.com',
                ['admin@spa.com'],
            )
            return Response({'message': 'Message sent'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        bookings = Booking.objects.filter(customer=request.user)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(customer=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class CreateCheckoutSessionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        order_id = request.data.get('order_id')
        order = Order.objects.get(id=order_id, customer=request.user)
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': item.product.name},
                    'unit_amount': int(item.product.price * 100),
                },
                'quantity': item.quantity,
            } for item in order.orderitem_set.all ],
            mode='payment',
            success_url='http://localhost:5173/success',
            cancel_url='http://localhost:5173/cancel',
        )
        return Response({'sessionId': session.id})

class ReferralView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        code = request.data.get('referral_code')
        try:
            referrer = CustomerProfile.objects.get(referral_code=code)
            profile = CustomerProfile.objects.get(user=request.user)
            profile.referred_by = referrer
            profile.save()
            return Response({'message': 'Referral applied'})
        except CustomerProfile.DoesNotExist:
            return Response({'error': 'Invalid code'}, status=status.HTTP_400_BAD_REQUEST)

class PaystubView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employee = Employee.objects.get(user=request.user)
        paystubs = Paystub.objects.filter(employee=employee)
        serializer = PaystubSerializer(paystubs, many=True)
        return Response(serializer.data)

class AvailabilityView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        employee = Employee.objects.get(user=request.user)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Availability updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
