from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register',UserRegisterView.as_view(),name='register'),
    path('edit_profile',UserEditView.as_view(),name='update-profile'),
    path('change_success',views.change_success,name='change-success'),
]