from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=11)
    balance = models.FloatField()

    def __str__(self):
        return self.username


class Destinations(models.Model):
    destination_id = models.BigAutoField(primary_key=True)
    destination_name = models.CharField(max_length=20)
    description = models.TextField()
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.destination_name


class Review(models.Model):
    review_id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=20)
    rating = models.IntegerField(max_length=2)
    comment = models.TextField
    date_posted = models.DateField

    def __str__(self):
        return self.review_id
