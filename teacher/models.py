from django.db import models

class Class():
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email =models.CharField(max_length=20)
    phone_number = models.SmallIntegerField
    department = models.CharField(max_length=20)
    country = models.CharField(max_length = 20)
    gender = models.CharField(max_length=20)
    picture = models.ImageField
    current_students= models.SmallIntegerField
    bio= models.CharField(max_length=20)

def __str__(self):
    f"{self.bio} {self.gender}"

