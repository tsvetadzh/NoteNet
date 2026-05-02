from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('', views.materials, name='materials'),
    path('', views.addnote, name='addnote'),
    path('', views.myclass, name='myclass'),
    path('', views.profile, name='profile'),
]