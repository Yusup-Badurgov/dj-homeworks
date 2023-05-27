from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)