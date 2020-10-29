from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse

from .models import Post


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail-view.html'


class CreatePostView(CreateView):
    model = Post
    template_name = 'add-post.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
