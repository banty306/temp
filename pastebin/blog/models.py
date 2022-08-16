from django.db import models
from django.db import models
from django.utils import timezone

# Create your models here.
class BlogData(models.Model):
    key              = models.CharField(max_length=32)
    title			 = models.CharField(max_length=255,null=True,blank=True)
    description		 = models.TextField()
    author	         = models.CharField(max_length=10,null=True,blank=True)
    views		     = models.IntegerField(default=0)
    created_at       = models.DateTimeField(default=timezone.now)
    updated_at       = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'BlogData'