from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('capacity_chart/', views.capacity_chart, name='capacity_chart'),
    path('stat1/', views.stat1, name = 'stat1'),
    path('stat2/', views.stat2, name = 'stat2'),
    path('stat3/', views.stat3, name = 'stat3'),
    path('agregacija/', views.agregacija, name = 'agregacija'),
]

