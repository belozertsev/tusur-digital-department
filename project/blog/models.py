from django.db import models

class User(models.Model):
    username = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=30)

class Post(models.Model):
    username = models.CharField(max_length=30)
    creator = models.CharField(max_length=30)
    header = models.CharField(max_length=50)
    text = models.CharField(max_length=300)
    
class Right(models.Model):
    class Meta:
        unique_together = (('username', 'applicant'),)
        
    username = models.CharField(max_length=30)
    applicant = models.CharField(max_length=30)
    get_right = models.BooleanField()
    post_right = models.BooleanField()
    put_right = models.BooleanField()
    delete_right = models.BooleanField()
