from asyncio import Task

from django.db import models

# Create your models here.
class Trek(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.DateTimeField(null=True, blank=True)

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.status_display()} - {self.get_priority_display()}"

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()  

    
    attachments = models.FileField(upload_to='comment_attachments/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Comment by {self.author.username} on {self.task.title}"

