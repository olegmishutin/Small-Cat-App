from django.urls import path
from .views import RegistrationView, LoginView

app_name = 'authentication'
urlpatterns = [
    path('reg/', RegistrationView.as_view(), name='reg'),
    path('log/', LoginView.as_view(), name='log')
]
