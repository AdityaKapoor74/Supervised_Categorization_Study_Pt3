from django.urls import path
from .import views

urlpatterns = [
    path('set<int:num>/', views.register, name='register_type3'),
    path('contact/', views.contact, name='contact_type3'),
    path('about/', views.about, name='about_type3'),
    path("terms/", views.terms, name='terms_type3'),
    path("registered/", views.register_type3_done, name='register_type3_done'),
    path("training_phase_start/", views.training_phase_start_type3, name='training_phase_start_type3'),
    path("observe_and_learn/", views.observe_and_learn_type3, name='observe_and_learn_type3'),
    path("observe_and_learn_instructions/", views.observe_and_learn_instructions_type3, name='observe_and_learn_instructions_type3'),
    path("observe_and_learn_display_stimuli/", views.observe_and_learn_display_stimuli_type3, name='observe_and_learn_display_stimuli_type3'),
    path("fixation_screen_observe/", views.fixation_screen_observe_type3, name='fixation_screen_type3'),
    path("fixation_screen_classify/", views.fixation_screen_classify_type3, name='fixation_screen_classify_type3'),
    path("classify_and_learn_instructions/", views.classify_and_learn_instructions_type3, name='classify_and_learn_instructions_type3'),
    path("classify_and_learn_display_stimuli/", views.classify_and_learn_display_stimuli_type3,name='classify_and_learn_display_stimuli_type3'),
    path("classify_result/", views.classify_result_type3, name='classify_result_type3'),
    path("classify_performance/", views.classify_performance_type3, name='classify_performance_type3'),
    path("test_phase/", views.test_phase_type3, name='test_phase_type3'),
    path("test_block/", views.test_block_type3, name='test_block_type3'),
    path("test_block_samples/", views.test_block_display_stimuli_type3, name='test_block_display_stimuli_type3'),
    # path("fixature_screen_test/", views.fixature_screen_test_type3, name='fixature_screen_test_type3'),
    path("common_features_test_phase/", views.common_features_test_phase_type3, name='common_features_test_phase_type3'),
    path("common_features_test_phase_block/", views.common_features_test_phase_block_type3, name='common_features_test_phase_block_type3'),
    path("common_features_test_samples/", views.common_features_test_block_display_stimuli_type3, name='common_features_test_block_display_stimuli_type3'),
    path("description/", views.save_responses_description, name='save_responses_description_type3'),

]