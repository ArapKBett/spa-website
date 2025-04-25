from django.urls import path
from .views import (
    SubscriberCreateView, ContactMessageCreateView, ServiceListView, EmployeeListView,
    BookingCreateView, ProductListView, OrderCreateView, PaystubListView,
    AvailabilityCreateView, SpecialListView
)

urlpatterns = [
    path('subscribers/', SubscriberCreateView.as_view(), name='subscriber-create'),
    path('contact/', ContactMessageCreateView.as_view(), name='contact-create'),
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('bookings/', BookingCreateView.as_view(), name='booking-create'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('orders/', OrderCreateView.as_view(), name='order-create'),
    path('paystubs/', PaystubListView.as_view(), name='paystub-list'),
    path('availability/', AvailabilityCreateView.as_view(), name='availability-create'),
    path('specials/', SpecialListView.as_view(), name='special-list'),
]
