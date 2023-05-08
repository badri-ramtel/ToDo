from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.home, name='main-home'),
    # path('login/', views.login, name='main-login'),
    path('add/', views.add, name='main-add'),
    path('edit/<int:id>', views.edit, name='main-edit'),
    path('delete/<int:id>', views.delete, name='main-delete')
]