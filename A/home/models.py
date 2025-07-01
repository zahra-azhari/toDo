from django.db import models
class Todo(models.Model):
    title=models.CharField(max_length=300)
    body=models.TextField()
    craeted=models.DateTimeField()

