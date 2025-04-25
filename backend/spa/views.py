from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.conf import settings
import stripe
from .models import Subscriber, ContactMessage, Service, Employee, CustomerProfile, Booking, Product, Order, Paystub, Availability, Special
from .serializers import (
    SubscriberSerializer, ContactMessageSerializer, ServiceSerializer, EmployeeSerializer,
    CustomerProfileSerializer, BookingSerializer, ProductSerializer, OrderSerializer,
    PaystubSerializer, AvailabilitySerializer, SpecialSerializer
)

stripe.api_key = settings.STRIPE_SECRET_KEY

class SubscriberCreateView(generics.CreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        send_mail(
            subject=f"New Contact Message from {instance.name}",
            message=f"Email: {instance.email}\nMessage: {instance.message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
        )

class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class CustomerProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return CustomerProfile.objects.get(user=self.request.user)

class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderCreateView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            items = serializer.validated_data['items']
            customer = serializer.validated_data['customer']
            try:
                line_items = [
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': item['name'],
                            },
                            'unit_amount': int(item['price'] * 100),
                        },
                        'quantity': item['quantity'],
                    }
                    for item in items
                ]
                session = stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    line_items=line_items,
                    mode='payment',
                    success_url='https://spakling.onrender.com/shop',
                    cancel_url='https://spakling.onrender.com/shop',
                    customer_email=customer.user.email,
                )
                order = Order.objects.create(
                    customer=customer,
                    stripe_session_id=session.id,
                    items=items
                )
                return Response({'session_id': session.id}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaystubListView(generics.ListAPIView):
    queryset = Paystub.objects.all()
    serializer_class = PaystubSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        employee = Employee.objects.get(user=self.request.user)
        return Paystub.objects.filter(employee=employee)

class AvailabilityCreateView(generics.CreateAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        employee = Employee.objects.get(user=self.request.user)
        serializer.save(employee=employee)

class SpecialListView(generics.ListAPIView):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer
