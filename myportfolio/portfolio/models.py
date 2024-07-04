from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length= 150)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField
    
    def __str__(self):
        return self.name