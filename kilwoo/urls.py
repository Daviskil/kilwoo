from django.urls import path
from . import views

urlpatterns = [
    path('',     views.e_introduction, name='e_introduction'),
    path('introduction/edit/<int:pk>/', views.introduction_edit, name='e_introduction_edit'),
    path('teams/<int:pk>/', views.e_teams, name='e_teams'),
    path('subcategory/<int:pk>/', views.e_subcategory, name='e_subcategory'),
    path('services/<int:pk>/', views.e_services, name='e_services'),
]