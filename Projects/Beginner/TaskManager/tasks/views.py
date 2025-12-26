from django.shortcuts import render
from .models import Tasks
from django.urls import reverse_lazy
""" We will create the views of our Different Pages in the Tasks App"""

from django.views.generic import CreateView,UpdateView,DeleteView,DetailView,ListView

"""
We will use context_objects names in our list and detail view for easy naming in 
html files of the object_list datatype.
"""
class TaskView(ListView):
    model=Tasks
    template_name='task.html'
    context_object_name='tasks'

class TaskDetailView(DetailView):
    model=Tasks
    template_name='task_detail.html'
    context_object_name='task'

class TaskCreateView(CreateView):
    model=Tasks
    fields='__all__'
    success_url=reverse_lazy('task')
    template_name='task_create.html'

"""By default after the edit dajngo automatically redirects to the page of the 
get_absolute_url in our models file.
"""
class TaskEditView(UpdateView):
    model=Tasks
    fields=['title','description','status','due_date',]
    template_name='task_edit.html'

class TaskDeleteView(DeleteView):
    model=Tasks
    success_url=reverse_lazy('task')
    template_name='task_delete.html'
