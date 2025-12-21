from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name='home'),
    path("another/<str:pk>/",views.another,name='another'), # if we change the first but the second remain same no effect will occur
    path("create-room/",views.create_room,name='create-room'),
    path("update-room/<str:pk>",views.update_room,name='update-room'),
]