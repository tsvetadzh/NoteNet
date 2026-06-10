from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('materials/', views.materials, name='materials'),
    path('addnote/', views.addnote, name='addnote'),
    path('myclass/', views.myclass, name='myclass'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path('setup-profile/', views.setup_profile, name='setup_profile'),
    path('simulate-grade-advancement/', views.simulate_grade_advancement, name='simulate_grade_advancement'),
    path('class/<int:grade>/<str:subject>/upload/', views.upload_material, name='upload_material'),

    path('class/<int:grade>/', views.class_grade, name='class_grade'),

    path('class/8/system/', views.subject_list, {'grade': 8, 'group': 'system'}, name='eight_system'),
    path('class/8/networks/', views.subject_list, {'grade': 8, 'group': 'networks'}, name='eight_networks'),
    path('class/9/system/', views.subject_list, {'grade': 9, 'group': 'system'}, name='nine_system'),
    path('class/9/networks/', views.subject_list, {'grade': 9, 'group': 'networks'}, name='nine_networks'),
    path('class/10/system/', views.subject_list, {'grade': 10, 'group': 'system'}, name='ten_system'),
    path('class/10/networks/', views.subject_list, {'grade': 10, 'group': 'networks'}, name='ten_networks'),
    path('class/11/system/', views.subject_list, {'grade': 11, 'group': 'system'}, name='eleven_system'),
    path('class/11/networks/', views.subject_list, {'grade': 11, 'group': 'networks'}, name='eleven_networks'),
    path('class/12/system/', views.subject_list, {'grade': 12, 'group': 'system'}, name='twelve_system'),
    path('class/12/networks/', views.subject_list, {'grade': 12, 'group': 'networks'}, name='twelve_networks'),

    path('class/<int:grade>/<str:subject>/', views.discipline, name='discipline'),
]