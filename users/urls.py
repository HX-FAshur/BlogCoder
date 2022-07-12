from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ProfilePageView, CreateProfilePageView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register',UserRegisterView.as_view(),name='register'),
    path('edit_profile',UserEditView.as_view(),name='update-profile'),
    path('change_success',views.change_success,name='change-success'),
    path('<int:pk>/profile/',ProfilePageView.as_view(),name="profile-page"),
    path('create_profile/',CreateProfilePageView.as_view(),name="create_profile"),
]