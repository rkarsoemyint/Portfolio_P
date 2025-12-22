from django.urls import path
from . import views

urlpatterns = [
    # Home Page (Search နဲ့ Filter ပါ ပါဝင်သည်)
    path('', views.index, name='index'),
    
    # Project Detail Page (ID အလိုက်သွားမည်)
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    
    # Contact Page
    path('contact/', views.contact, name='contact'),

    path('cv/', views.cv_detail, name='cv_detail'),

    path('about/', views.about, name='about'),
]