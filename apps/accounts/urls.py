from django.urls import path, include
from . import views
from .views import SingUp
urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('signup/',SingUp.as_view(), name='signup'),
    ]