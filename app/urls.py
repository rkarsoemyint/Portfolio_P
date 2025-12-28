from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    
    path('contact/', views.contact, name='contact'),

    path('cv/', views.cv_detail, name='cv_detail'),

    path('about/', views.about, name='about'),
]
