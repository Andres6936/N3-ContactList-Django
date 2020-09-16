from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, {'pagename': 'home'}, name='home'),
    path('add', views.add, name='add'),
    path('home', views.index, {'pagename': 'home'}, name='home'),
    path('view', views.index, {'pagename': 'view'}, name='view'),
]
