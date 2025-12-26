from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

"""
We create Tasks model in which we want choices in the status attribute.
so we give a (value,label) tuple for it in the Charfield.
"""
class Tasks(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    CHOICES=[
        ("PENDING",'Pending'),
        ('DONE','Done'),
        ('NOT_DONE','Not Done'),
    ]
    status=models.CharField(max_length=20,choices=CHOICES,default='PENDING')
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    due_date=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.title[:20]
    """Get absolute is very useful. for the detail page if we ever 
    change the url it automatically changes all the urls for it and we can use 
    name.get_absolute_url in templates for easy url access
    """
    def get_absolute_url(self):
        return reverse('task_detail',args=[str(self.id)])