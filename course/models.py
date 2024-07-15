from django.db import models

class Class():
    course_name=models.CharField(max_length=20)
    course_code=models.CharField(max_length=20)
    description =models.CharField(max_length=20)
    max_capacity = models.SmallIntegerField
    department = models.CharField(max_length=20)
    trainer = models.CharField(max_length = 20)
    pass_grade = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    assistnat_trainer= models.SmallIntegerField
    tools= models.CharField(max_length=20)

def __str__(self):
    f"{self.pass_grade} {self.duration}"

