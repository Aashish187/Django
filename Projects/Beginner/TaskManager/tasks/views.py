from django.shortcuts import render
from .models import Tasks
from django.urls import reverse_lazy
""" We will create the views of our Different Pages in the Tasks App"""

from django.views.generic import CreateView,UpdateView,DeleteView,DetailView,ListView,TemplateView

"""
We will use context_objects names in our list and detail view for easy naming in 
html files of the object_list datatype.
"""
class HomePageView(TemplateView):
    template_name='home.html'

class TaskView(ListView):
    model=Tasks
    template_name='task.html'
    context_object_name='tasks'
    def get_queryset(self):
        return Tasks.objects.filter(owner=self.request.user)
"""This for that logged in user can only see their tasks only."""

class TaskDetailView(DetailView):
    model=Tasks
    template_name='task_detail.html'
    context_object_name='task'

class TaskCreateView(CreateView):
    model=Tasks
    fields=['title','description','status','due_date']
    success_url=reverse_lazy('task')
    template_name='task_create.html'
# In this we auto add the user into the database instance is the temp object
# stored which is edited by the owner and then return to the database filled with 
#owner as the logged in user
    def form_valid(self, form):
        form.instance.owner=self.request.user
        return super().form_valid(form)

"""By default after the edit django automatically redirects to the page of the 
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
