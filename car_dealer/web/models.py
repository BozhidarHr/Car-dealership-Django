from datetime import timezone

from django.contrib.auth.models import User
from django.db import models

#create validations


class Feedback(models.Model):
    RATING_CHOICES = (
        ("VS", 'Very satisfied'),
        ('S','Satisfied'),
        ("NS",'Neither satisfied nor dissatisfied'),
        ("U",'Unsatisfied'),
        ("VU",'Very unsatisfied') ,
    )
    full_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    rating = models.CharField(max_length=2, choices = RATING_CHOICES, blank=False, null= False)
    comment = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, null=True)


class ContactForm(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.IntegerField()
    message = models.TextField(max_length=500)
    submission_date = models.DateTimeField(auto_now_add=True, null=True)



class Listing(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    engine = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='media/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f'{self.brand} {self.model}'

    def delete(self, using=None, keep_parents=False):
        self.image.delete()
        super().delete()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    comment = models.TextField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.comment


class ReportListing(models.Model):
    PROBLEM_CHOICES = (
        ("P", 'Incorrect price'),
        ('C', 'Incorrect characteristics'),
        ('F', 'Fake listing'),
        ('O', 'Other'),
    )
    problem = models.CharField(max_length=1, choices=PROBLEM_CHOICES, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True)
    description = models.CharField(max_length=200)
    full_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=60, blank=True)
