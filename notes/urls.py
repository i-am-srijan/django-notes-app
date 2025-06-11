from django.urls import path
from . import views
from .views import dashboard, add_post, edit_post

from django.contrib.auth import views as auth_views
from notes.forms import CustomLoginForm  # Make sure 'notes' is your app nam

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_note, name='create_note'),
    path('edit/<int:note_id>/', views.edit_note, name='edit_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('note/<int:note_id>/', views.view_note, name='view_note'),
    path('dashboard/', dashboard, name='dashboard'),
    path('post/new/', add_post, name='add_post'),
    path('post/<int:pk>/edit/', edit_post, name='edit_post'),


     path('accounts/login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=CustomLoginForm  # Use your custom form here
    ), name='login'),
]
