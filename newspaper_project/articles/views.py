from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView,UpdateView,DeleteView,DetailView
from .models import Articles
from django.urls import reverse_lazy
# Create your views here.
class ArticleListView(LoginRequiredMixin,ListView):
    model=Articles
    template_name='article_list.html'
    login_url='login'

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model=Articles
    template_name='article_detail.html'
    login_url='login'

class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model=Articles
    template_name='article_edit.html'
    fields=['title','body']
    login_url='login'

class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model=Articles
    template_name='article_delete.html'
    success_url=reverse_lazy('article_list')
    login_url='login'

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model=Articles
    template_name='article_create.html'
    fields=['title','body']
    login_url='login'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
