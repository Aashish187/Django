from django.urls import path
from .views import ArticleListView,ArticleUpdateView,ArticleDeleteView
urlpatterns=[
    path('',ArticleListView.as_view(),name='article_list'),
    path('<int:pk>/edit/',ArticleUpdateView.as_view(),name='article_edit'),
    path('<int:pk>/delete/',ArticleDeleteView.as_view(),name='article_delete'),
]