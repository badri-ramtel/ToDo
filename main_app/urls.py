from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.home, name='main-home'),
    # path('', views.listing, name='main-listing'),
    path('add/', views.add, name='main-add'),
    path('edit/<int:id>', views.edit, name='main-edit'),
    path('delete/<int:id>', views.delete, name='main-delete'),
    path('complete/<int:id>', views.complete, name='main-complete'),
    path('404/', views.not_found, name='404notfound')
]