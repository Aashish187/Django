from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from .models import Articles
from django.urls import reverse_lazy
# Create your views here.
class ArticleListView(ListView):
    model=Articles
    template_name='article_list.html'


class ArticleUpdateView(UpdateView):
    model=Articles
    template_name='article_edit.html'
    fields=['title','body']

class ArticleDeleteView(DeleteView):
    model=Articles
    template_name='article_delete.html'
    success_url=reverse_lazy('article_list')

