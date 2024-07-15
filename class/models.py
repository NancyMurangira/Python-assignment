from django.db import models

class Class():
    class_name=models.CharField(max_length=20)
    class_code=models.CharField(max_length=20)
    assistant_trainer_inchar =models.CharField(max_length=20)
    room_number = models.SmallIntegerField
    no_of_tables = models.CharField(max_length=20)
    class_rep = models.CharField(max_length = 20)
    no_of_seats = models.SmallIntegerField
    max_students = models.SmallIntegerField
    current_students= models.SmallIntegerField
    no_of_groups= models.SmallIntegerField

def __str__(self):
    f"{self.max_students} {self.class_rep}"

