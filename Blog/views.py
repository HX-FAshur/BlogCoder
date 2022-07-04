from pdb import post_mortem
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .forms import PostForm
from .models import Post
# Create your views here.

def home(request):
    return render(request,'home.html',{})

class HomeView(ListView):
    model=Post
    template_name='home.html'
    ordering= ['-pub_date']

class ArticleDetailView(DetailView):
    model=Post
    template_name='article_details.html'

class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='add_post.html'
    #fields='__all__'

class UpdatePostView(UpdateView):
    model = Post
    template_name='edit_post.html'
    fields=['title','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url= reverse_lazy('home')