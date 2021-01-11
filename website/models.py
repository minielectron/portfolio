from django.db import models

class Project(models.Model):
    """
    Represents a project model in home page.
    """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    action_url = models.URLField(blank=True) 
    image = models.ImageField( upload_to="website/images", max_length=None)

    def __str__(self):
        return self.title