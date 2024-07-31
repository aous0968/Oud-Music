from django.db import models
import os
from django.utils.text import slugify

def get_upload_path(instance, filename):
    return os.path.join(
      "uploads/tracks/" , "track_"+instance.name+"/" , filename )

class Track(models.Model):
    name = models.CharField( max_length=255)
    track_img = models.ImageField(upload_to=get_upload_path, height_field=None, width_field=None, max_length=None)
    track = models.FileField(upload_to=get_upload_path, max_length=100)
    downloads = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    times_played = models.IntegerField(default=0)
    createdAt = models.DateField(auto_now=False, auto_now_add=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
      if not self.slug:
          self.slug = slugify(self.name)
      super().save(*args, **kwargs)
