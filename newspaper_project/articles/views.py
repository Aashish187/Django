from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from .models import Articles
# Create your views here.
class ArticleListView(ListView):
    model=Articles
    template_name='article_list.html'


class ArticleUpdateView(UpdateView):
    model=Articles
    template_name='article_edit.html'
    fields=['title','body']