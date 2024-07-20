from django.db import models

class Project(models.Model):
    """
    Model representing a project.
    """
    title = models.CharField(max_length=150)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title

class Skill(models.Model):
    """
    Model representing a skill.
    """
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)  # e.g., Beginner, Intermediate, Advanced
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    """
    Model representing a contact submission.
    """
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.name
