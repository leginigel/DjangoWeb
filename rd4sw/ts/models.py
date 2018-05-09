from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.IntegerField
    num = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    nick = models.CharField(max_length=100, blank=True)
    dept = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    email  = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
	
    def __str__ (self):
	
        return self.name