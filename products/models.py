from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
    icon = models.ImageField(upload_to='images/')
    image = models.ImageField(upload_to='images/')
    body =  models.TextField()
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %#d %Y')


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
