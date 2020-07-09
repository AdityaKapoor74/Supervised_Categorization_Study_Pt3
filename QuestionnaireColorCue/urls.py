from django.urls import path
from .import views

urlpatterns = [
    path('set<int:num>/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path("terms/", views.terms, name='terms'),
    path("registered/", views.register_type2_done, name='register_type2_done'),
    path("training_phase_start/", views.training_phase_start_type2, name='training_phase_start_type2'),
    path("observe_and_learn/", views.observe_and_learn_type2, name='observe_and_learn_type2'),
    path("observe_and_learn_instructions/", views.observe_and_learn_instructions_type2, name='observe_and_learn_instructions_type2'),
    path("observe_and_learn_display_stimuli/", views.observe_and_learn_display_stimuli_type2, name='observe_and_learn_display_stimuli_type2'),
    path("fixation_screen/", views.fixation_screen_type2, name='fixation_screen_type2'),
    path("classify_and_learn_instructions/", views.classify_and_learn_instructions_type2, name='classify_and_learn_instructions_type2'),
    path("classify_and_learn_display_stimuli/", views.classify_and_learn_display_stimuli_type2,name='classify_and_learn_display_stimuli_type2'),
    path("classify_result/", views.classify_result_type2, name='classify_result_type2'),
    path("classify_performance/", views.classify_performance_type2, name='classify_performance_type2'),
    path("test_phase/", views.test_phase_type2, name='test_phase_type2'),
    path("test_block/", views.test_block_type2, name='test_block_type2'),
    path("test_block_samples/", views.test_block_display_stimuli_type2, name='test_block_display_stimuli_type2'),
    path("common_features_test_phase/", views.common_features_test_phase_type2, name='common_features_test_phase_type2'),
    path("common_features_test_phase_block/", views.common_features_test_phase_block_type2, name='common_features_test_phase_block_type2'),
    path("common_features_test_samples/", views.common_features_test_block_display_stimuli_type2, name='common_features_test_block_display_stimuli_type2'),
    path("description/", views.save_responses_description, name='save_responses_description'),

]