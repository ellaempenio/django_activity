from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('indexss/', views.indexss, name="indexss"),  
]