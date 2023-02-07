from django.db import models


class Imgs(models.Model):
    id= models.AutoField(primary_key=True)
    desc = models.CharField(max_length=50,null=True,blank=True)
    title=models.CharField(max_length=100)
    image=models.ImageField(null=True, blank=True,default='/placeholder.png')

    def __str__(self):
        return self.title