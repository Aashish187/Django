from django.contrib import admin
from .models import Articles,Comments
# Register your models here.
class CommentInline(admin.StackedInline): #will display the comment objects in short
    model=Comments  # which model to use

class ArticleAdmin(admin.ModelAdmin): # to customize the articles admin page
    inlines=[CommentInline,] #     show the commentinline

admin.site.register(Articles,ArticleAdmin) 
admin.site.register(Comments) 
