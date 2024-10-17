from django.db import models

class Post(models.Model):
    # Default behavior - Django creates primary keys automatically
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="Olona")  # New signature field
    date = models.DateTimeField()

    def __str__(self):
        return self.title
