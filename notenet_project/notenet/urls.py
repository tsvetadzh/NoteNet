from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('materials/', views.materials, name='materials'),
    path('addnote/', views.addnote, name='addnote'),
    path('myclass/', views.myclass, name='myclass'),
    path('profile/', views.profile, name='profile'),
]