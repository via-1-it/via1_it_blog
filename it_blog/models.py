from django.db import models
from datetime import datetime

# Create your models here.

class it_blog(models.Model):
    title = models.Charfield(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank = True)
