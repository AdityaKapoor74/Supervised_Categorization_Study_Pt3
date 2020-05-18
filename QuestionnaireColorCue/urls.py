from django.urls import path
from .import views

urlpatterns = [
    path('', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path("terms/", views.terms, name='terms'),
    path("registered/", views.register_type2_done, name='register_type2_done'),
    path("set_number/", views.set_number_register_type2, name='set_number_register_type2'),
    path("training_phase_start/", views.training_phase_start_type2, name='training_phase_start_type2'),
]