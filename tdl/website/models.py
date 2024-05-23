from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDoItem(models.Model):
    user = models.ForeignKey(User,null=True, on_delete= models.SET_NULL)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete', 'due_date']
    
    