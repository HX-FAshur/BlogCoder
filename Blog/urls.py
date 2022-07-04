from django.urls import path
from .views import AddPostView, HomeView, ArticleDetailView, UpdatePostView,DeletePostView

urlpatterns = [
    #path('',views.home, name='home'),
    path('', HomeView.as_view(),name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'), 
    path('post', AddPostView.as_view(),name='add_post'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name='update'),
    path('article/edit/<int:pk>/delete',DeletePostView.as_view(),name='delete'),
]