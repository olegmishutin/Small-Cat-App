from django.urls import path
from . import views

app_name = 'authentication'
urlpatterns = [
    path('reg/', views.RegistrationView.as_view(), name='reg'),
    path('log/', views.login_view, name='log'),
    path('me/', views.get_username_view, name='me')
]
