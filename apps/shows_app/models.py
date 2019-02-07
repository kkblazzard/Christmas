from django.db import models


# Create your models here.
class shows(models.Model):
    title= models.CharField(max_length=45)
    network = models.CharField(max_length=15)
    air_date = models.DateField(null=True)
    time=models.TimeField(null=True)
    desc= models.CharField(max_length=250)
    
    image=models.URLField(max_length=1250)
    video=models.URLField(max_length=1250)
    theme=models.CharField(max_length=45)
    rate=models.IntegerField(default=0)
    number_of_votes=models.IntegerField(default=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    # rating = models.ManyToManyField(show, related_name="users")
