from django.db import models
from django.utils import timezone

class Post(models.Model): 
    title = models.CharField(max_length=20)
    plan = models.TextField() 
    date = models.DateTimeField(default=timezone.now)  
    
    def __str__(self):
        return f"{self.title} vaqti:{self.date}"

