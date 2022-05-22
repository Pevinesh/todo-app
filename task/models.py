from turtle import title
from django.db import models

# Create your models here.
class Schedule(models.Model):
    title=models.CharField(max_length=100)
    complete=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title