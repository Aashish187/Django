from django.urls import path
from . views import TaskView,TaskDetailView,TaskCreateView,TaskDeleteView,TaskEditView,HomePageView

"""
path() is for the destination: it connects a URL directly to a specific View (page) to display content.
include() is for organization: it groups URLs together and 
forwards the user to another urls.py file (usually inside a specific App) to handle the rest of the path.
"""
"""Always end the trail by slash becasue django looks for it by default and will 
help prevent errors while deployment.
"""
urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
    path('task/',TaskView.as_view(),name='task'),
    path('task/new/',TaskCreateView.as_view(),name='task_create'),
    path('task/<int:pk>/',TaskDetailView.as_view(),name='task_detail'),
    path('task/<int:pk>/edit/',TaskEditView.as_view(),name='task_edit'),
    path('task/<int:pk>/delete/',TaskDeleteView.as_view(),name='task_delete'),
]