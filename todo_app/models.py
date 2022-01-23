from django.db import models
from django.contrib.auth.models import User

class TODO(models.Model):
    status_choices = [
    ('DONE', 'TUGATILDI'),
    ('DOING', 'BAJARILMOQDA'),
    ]
    name = models.CharField(max_length=50)
    process = models.CharField(max_length=15 , choices=status_choices)
    date = models.DateTimeField(auto_now_add=True)
    user  = models.ForeignKey(User  , on_delete= models.CASCADE)