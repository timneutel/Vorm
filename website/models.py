from django.db import models
from django.contrib import admin

# Create your models here.
class Design(models.Model):
    title = models.CharField(max_length = 30)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to = "designs")
    def __unicode__(self): return self.title

admin.site.register(Design)