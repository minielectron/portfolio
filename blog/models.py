from django.db import models

# Create your models here.
class Blog(models.Model):
    """
    Represents a project model in home page.
    """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    date = models.DateField()
    
    def __str__(self):
        return self.title