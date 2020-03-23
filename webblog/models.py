from django.db import models
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
 
    def summary(self):
        return self.body[:300]
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')
    def __str__(self):
        return self.title