from django.db import models

# Create your models here.

class Mobile(models.Model):

    
    BrandName = models.CharField(max_length=222,unique=True)
    Model = models.CharField(max_length=222,blank=True,null=True)
    Color = models.CharField(max_length=222,blank=True,null=True)
    JANCode = models.CharField(max_length=222,unique=True)
    Image = models.ImageField(upload_to='media/post_image',blank=True)

    def __str__(self):
        return self.BrandName