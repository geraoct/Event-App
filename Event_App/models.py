from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    title= models.CharField(max_length=200)
    description = models.TextField()
    category_choices = [
        ('Wedding', 'Wedding'),
        ('Birthday', 'Birthday'),
        ('Graduation', 'Graduation'),
        ('Other', 'Other'),

    ]
    category = models.CharField(max_length=50, choices=category_choices,default='Other')
    date = models.DateField()
    time= models.TimeField()
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE , related_name='organized_events')
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)


    def __str__(self):
        return self.event_name
