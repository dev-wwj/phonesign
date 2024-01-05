from django.urls import path
from .views import PhoneLoginView, UserProfileView

urlpatterns = [
    path('phone-login/', PhoneLoginView.as_view(), name='phone-login'),
    path('user-profile/', UserProfileView.as_view(), name='user-profile'),
    # Add other URLs as needed
]