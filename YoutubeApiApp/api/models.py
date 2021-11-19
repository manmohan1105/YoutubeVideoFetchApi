from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=100)

class Videos(models.Model):
    title = models.CharField(null=True,blank=True,max_length=500)                               # Title Of the Video
    description = models.CharField(null=True, blank=True, max_length=6000)                      # Description Of the Video
    publishingDateTime = models.DateTimeField()                                                 # Publish date/time Of the Video
    thumbnailsUrls = models.URLField()                                                          # URL Of the Thumbnail
    channelTitle = models.CharField(null=True,blank=True,max_length=500)                        # Title/Name Of the Channel