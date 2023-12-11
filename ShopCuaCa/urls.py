from django.urls import path
from ShopCuaCa import views

urlpatterns = [
    path('', views.home, name='home'),
]
