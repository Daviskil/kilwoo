from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



#KILWOO
class Introduction(models.Model):
    text = RichTextField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    location = RichTextField(blank=True)


#PRODUCTS
class Team(models.Model):
    #team number
    title = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

class Subcategory(models.Model):
    name = models.CharField(max_length=30)
    companyimage = models.ImageField(null=True, blank=True, upload_to="images/")
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    caption = RichTextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)



#SERVICES
class Services(models.Model):

    #service name
    title = models.CharField(max_length=50)

    heading = models.TextField(max_length=50)
    caption = RichTextField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
