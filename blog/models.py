from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.text[:100] + '...'
    
    def cool_date(self):
        return self.pub_date.strftime('%b %e %Y')
    
