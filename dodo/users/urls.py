from django.urls import path, include
from .views import myprofile, RegistrationView, LoginView

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', myprofile, name='my_profile'),
            # path('profile/<int:pk>', otherprofile, name='other_profile')
]