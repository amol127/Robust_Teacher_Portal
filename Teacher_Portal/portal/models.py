from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    marks = models.PositiveIntegerField()

    class Meta:
        unique_together = ('name', 'subject')

    def __str__(self):
        return f"{self.name} - {self.subject}: {self.marks}"
