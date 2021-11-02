from django.urls import path

from . import views

app_name = "badge"
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('announcements/', views.announcements, name='announcements'),
    path('claim/', views.claim, name='claim'),
    path('verify/<str:code>/', views.view_badge, name='view_badge'),
    path('verify/', views.verify, name='verify'),
    path('search/<str:name>/', views.view_guilder, name='view_guilder'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
]