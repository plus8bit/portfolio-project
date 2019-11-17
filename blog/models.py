from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
