from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class standard(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class department(models.Model):
    department_id = models.CharField(max_length=100)
