from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('materials/', views.materials, name='materials'),
    path('addnote/', views.addnote, name='addnote'),
    path('myclass/', views.myclass, name='myclass'),
    path('profile/', views.profile, name='profile'),

    path('class/8/', views.class_eight, name='class_eight'),
    path('class/9/', views.class_nine, name='class_nine'),
    path('class/10/', views.class_ten, name='class_ten'),
    path('class/11/', views.class_eleven, name='class_eleven'),
    path('class/12/', views.class_twelve, name='class_twelve'),

    path('class/8/system', views.subject_list, {'grade': 8, 'group': 'system'}, name='eight_system'),
    path('class/8/system', views.subject_list, {'grade': 8, 'group': 'networks'}, name='eight_networks'),
    path('class/8/system', views.subject_list, {'grade': 8, 'group': 'system'}, name='eight_ai'),
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