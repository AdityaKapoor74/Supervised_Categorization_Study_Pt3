from django.urls import path
from .import views

urlpatterns = [
    path('', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path("terms/", views.terms, name='terms'),
    path("registered/", views.register_type1_done, name='register_type1_done'),
    path("set_number/", views.set_number_register_type1, name='set_number_register_type1'),
]