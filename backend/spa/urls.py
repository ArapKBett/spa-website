from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from spa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/subscribe/', views.SubscribeView.as_view(), name='subscribe'),
    path('api/contact/', views.ContactView.as_view(), name='contact'),
    path('api/bookings/', views.BookingView.as_view(), name='bookings'),
    path('api/products/', views.ProductView.as_view(), name='products'),
    path('api/checkout/', views.CreateCheckoutSessionView.as_view(), name='checkout'),
    path('api/referral/', views.ReferralView.as_view(), name='referral'),
    path('api/paystubs/', views.PaystubView.as_view(), name='paystubs'),
    path('api/availability/', views.AvailabilityView.as_view(), name='availability'),
]
