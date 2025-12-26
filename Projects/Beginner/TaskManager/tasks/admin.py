from django.contrib import admin
from .models import Tasks
# Register your models here.
"""We will register our Tasks model to the admin"""
admin.site.register(Tasks)
