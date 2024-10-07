from django.urls import path
from . import views

app_name = 'authentication'
urlpatterns = [
    path('reg/', views.RegistrationView.as_view(), name='reg'),
    path('log/', views.LoginView.as_view(), name='log'),
    path('me/', views.get_username, name='me')
]
