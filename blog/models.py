from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.urls import reverse

class Blog(models.Model):

    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=now)
    body = models.TextField()
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def get_absolute_url(self):
        return reverse('detail', kwargs={'blog_id': self.pk})
