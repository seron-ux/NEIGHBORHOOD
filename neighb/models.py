from django.db import models

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=50)
    location= models.CharField(max_length=60)
    admin = models.ForeignKey("Profile",on_delete=models.CASCADE, related_name = 'hood')
    description = models.TextField( default = '')
    hood_logo = models.ImageField( upload_to='images/', blank ='true',default='')
    emergency_contact=models.CharField(max_length=100,null=True, blank=True)
    occupants_count = models.IntegerField(null  = True ,blank = True)
