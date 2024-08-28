from django.db import models

class Teacher(models.Model): 
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]

    name = models.CharField(max_length=15, verbose_name="Teacher Name")
    email = models.EmailField(verbose_name="Email")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Gender")
    age = models.IntegerField(verbose_name="Age")

    class Meta:
        abstract = True


class Employee(Teacher):  
    salary = models.DecimalField(max_digits=10, decimal_places=2)


class Topper(Teacher):
    marks = models.IntegerField()


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Person(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    age = models.IntegerField()


class Human(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
