from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

from .models import Post
# Create your views here.

def test(request):
    return HttpResponse("<h1> TEST VIEW - OK </h1>")

class BlogListView(ListView):
    model = Post

class BlogDetailView(DetailView):
    model = Post

class BlogCreateView(CreateView):
    model = Post
    template_name = "blog/post_create.html"
    fields = ["title", "author","body"]

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_update.html"
    fields = ["title","body"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("post_list")