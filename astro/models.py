from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=20,default='')
    Second_Name = models.CharField(max_length=20,default='')
    bio =models.TextField(blank=True)
    code = models.CharField(max_length=8,blank=True)
    # recommended_by = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True,related_name='ref_by')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
    city = models.CharField(max_length=200,default='city')
    Phone_Number = models.CharField(max_length=10,null=True)
    Role = models.CharField(max_length=10,null=True)
    # Category = models.CharField(max_length=100, choices=Catogories , default='STUDENT')
    image = models.ImageField(default='deafault.jpeg', upload_to='profile_pics')
    # is_pro = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}-{self.code}"