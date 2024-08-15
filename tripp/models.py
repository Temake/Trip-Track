from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator

# Create your models here.
user = get_user_model()
class Trip(models.Model):
    city  = models.CharField(max_length=20)
    country =models.CharField( max_length=2)
    start_date=models.DateField(null=True, blank=True)
    end_date=models.DateField(null=True, blank=True)
    owner = models.ForeignKey(user,  on_delete=models.CASCADE, related_name='trips')

    def __str__(self):
        return self.city
    
class Note(models.Model):
    Excursions = (
        ('event', 'Event'),
        ('dining', 'Dining'),
        ('experience', 'Experience'),
        ('general', 'General'),
    )
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='notes')
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=Excursions)
    img = models.ImageField(upload_to='notes', null=True, blank=True)
    rating = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5)])

    def __str__(self):
        return f'{self.name} in {self.trip.city}'
    