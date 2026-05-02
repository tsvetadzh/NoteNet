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

    path('class/8/system/', views.eight_system, name='eight_system'),
    path('class/8/ai/', views.eight_ai, name='eight_ai'),
    path('class/8/networks/', views.eight_networks, name='eight_networks'),

    path('class/9/system/', views.nine_system, name='nine_system'),
    path('class/9/networks/', views.nine_networks, name='nine_networks'),

    path('class/10/system/', views.ten_system, name='ten_system'),
    path('class/10/networks/', views.ten_networks, name='ten_networks'),

    path('class/11/system/', views.eleven_system, name='eleven_system'),
    path('class/11/networks/', views.eleven_networks, name='eleven_networks'),

    path('class/12/system/', views.twelve_system, name='twelve_system'),
    path('class/12/networks/', views.twelve_networks, name='twelve_networks'),

    path('class/9/networkssubj/', views.nine_networkssubj, name='nine_networkssubj'),
    path('class/9/electrotechnics/', views.nine_electrotechnics, name='nine_electrotechnics'),
    path('class/9/literature/', views.nine_literature, name='nine_literature'),
    path('class/9/chemistry/', views.nine_chemistry, name='nine_chemistry'),
    path('class/9/geography/', views.nine_geography, name='nine_geography'),
    path('class/9/scripts/', views.nine_scripts, name='nine_scripts'),
    path('class/9/history/', views.nine_history, name='nine_history'),
    path('class/9/programming/', views.nine_programming, name='nine_programming'),
    path('class/9/zbut/', views.nine_zbut, name='nine_zbut'),
    path('class/9/gradivni/', views.nine_gradivni, name='nine_gradivni'),
    path('class/9/physycs/', views.nine_physycs, name='nine_physycs'),
    path('class/9/phylosophy/', views.nine_phylosophy, name='nine_phylosophy'),
    path('class/9/russian/', views.nine_russian, name='nine_russian'),
    path('class/9/maths/', views.nine_maths, name='nine_maths'),
    path('class/9/english/', views.nine_english, name='nine_english'),
    path('class/9/biology/', views.nine_biology, name='nine_biology'),
    path('class/9/it/', views.nine_it, name='nine_it'),
    path('class/9/enterprenuering/', views.nine_enterprenuering, name='nine_enterprenuering'),
]