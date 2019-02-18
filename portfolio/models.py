from django.db import models

# pillow django-imagekit
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Portfolio(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'images/')

    # Thumbnail 
    image_thumbnail = ImageSpecField(source = 'image', processors = [ResizeToFill(100, 100)], format='JPEG')

    description = models.CharField(max_length = 300)

    def __str__(self):
        return self.title