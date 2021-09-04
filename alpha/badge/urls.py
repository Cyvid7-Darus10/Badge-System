from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('claim', views.claim, name='claim'),
    path('verify/<str:code>', views.view_badge, name='verify'),
    path('verify/', views.verify, name='verify')
]