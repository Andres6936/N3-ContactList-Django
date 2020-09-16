from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, {'pagename': ''}, name='home'),
    path('add', views.add, name='add'),
    path('view', views.index, {'pagename': 'view'}, name='view'),
]
