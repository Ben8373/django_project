
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


