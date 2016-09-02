from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    signup_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.signup_date = timezone.now()
        self.save()

