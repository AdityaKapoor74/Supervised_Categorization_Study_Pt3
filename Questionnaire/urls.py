from django.urls import path
from .import views

urlpatterns = [
    path('', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path("terms/", views.terms, name='terms'),
    path("registered/", views.register_type1_done, name='register_type1_done'),
    path("set_number/", views.set_number_register_type1, name='set_number_register_type1'),
    path("training_phase_start/", views.training_phase_start_type1, name='training_phase_start_type1'),
    path("observe_and_learn/", views.observe_and_learn_type1, name='observe_and_learn_type1'),
    path("observe_and_learn_instructions/", views.observe_and_learn_instructions_type1, name='observe_and_learn_instructions_type1'),
    path("observe_and_learn_display_stimuli/", views.observe_and_learn_display_stimuli_type1, name='observe_and_learn_display_stimuli_type1'),
    path("fixation_screen/", views.fixation_screen_type1, name='fixation_screen_type1'),
    path("classify_and_learn_instructions/", views.classify_and_learn_instructions_type1, name='classify_and_learn_instructions_type1'),
    path("classify_and_learn_display_stimuli/", views.classify_and_learn_display_stimuli_type1,name='classify_and_learn_display_stimuli_type1'),
    path("classify_result/", views.classify_result_type1, name='classify_result_type1'),
    path("classify_performance/", views.classify_performance_type1, name='classify_performance_type1'),

]