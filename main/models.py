from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=10000)
    headquarters = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'


class Internship(models.Model):
    position = models.CharField(max_length=255)
    description = models.CharField(max_length=10000)
    categories = models.CharField(max_length=1000)
    city = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return f'{self.position} at {self.company.name}'


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
