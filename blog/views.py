# Import django defaults for basic CRUD operations
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Import all the classes you will need for all pages
from .models import Blog
# The reverse tool
from django.urls import reverse_lazy


# At a minimum each class needs a path to the HTML file and the model to use
class blogCreateView(CreateView):
    template_name = 'blog-create.html'
    model = Blog
    fields = ['title', 'author', 'body']


class blogListView(ListView):
    template_name = 'blog-read-list.html'
    model = Blog
    fields = ['title']


class blogDetailView(DetailView):
    template_name = 'blog-read-detail.html'
    model = Blog
    fields = ['title', 'author', 'body']


class blogUpdateView(UpdateView):
    template_name = 'blog-update.html'
    model = Blog
    fields = ['title', 'body']


class blogDeleteView(DeleteView):
    template_name = 'blog-delete.html'
    model = Blog
    success_url = reverse_lazy('blog_read_list')
