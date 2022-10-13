from django.db import models
from common.models import *
# Create your models here.
class Blog(TSFieldsIndexed):

    title= models.CharField(max_length=500,null=True,blank=False)
    video_url = models.CharField(max_length=500, null=True, blank=True)

    description = models.TextField(max_length=50000,blank=True, null=True)

    image=models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title