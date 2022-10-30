from django.urls import path, include
from . import views
urlpatterns = [
    path('index/', views.index, name="index"),
    path('policy/', views.policy, name="policy"),
]