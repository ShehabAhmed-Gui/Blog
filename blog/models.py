from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateField()
    content = models.TextField(max_length=3000)
    publicher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
