from django.urls import path

from . import views

app_name = 'predict'
urlpatterns = [
    path('', views.index, name='index'),
    path('season/', views.seasons, name='seasons'),
    path('dynamic/', views.dynamics, name='dynamics'),
    path('demand/', views.profile_demand, name='demands')
]
