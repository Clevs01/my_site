from django.urls import path
from . import views
# from blog import urls

urlpatterns = [
    path('', views.index, name='site-home'),
    path('resources/', views.resources, name='resources'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('about_tuts/', views.about_tuts, name='about_tuts'),
    path('thanks/', views.thanks, name='thanks'),
    path('exercises/', views.exercises, name='exercises'),
]
