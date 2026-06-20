from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class EventUserModel(AbstractUser):
    full_name = models.CharField(max_length = 255, null = True, blank = True)
    phone_number = models.CharField(max_length = 15, null = True, blank = True)
    
    def __str__(self):
        return f"{self.username}---{self.phone_number}"

class EventModel(models.Model):
    EVENT_TYPE = [
        ('Conference' , 'Conference'),
        ('Concert' , 'Concert'),
        ('Wedding' , 'Wedding'),
        ('Graduation' , 'Graduation'),
        ('Birthday' , 'Birthday')
    ]
    EVENT_STATUS = [
        ('Not_Started' , 'Not Started'),
        ('In_Progress' , 'In Progress'),
        ('Completed' , 'Completed')
    ]
    event_title = models.CharField(max_length = 255, null = True)
    event_type = models.CharField(max_length = 50, choices = EVENT_TYPE, null = True)
    event_description = models.TextField(null = True)
    event_date = models.DateField(null = True)
    event_status = models.CharField(max_length = 50, choices=EVENT_STATUS, null = True)
    event_location = models.CharField(max_length = 100, null = True)
    event_image = models.ImageField(upload_to='media/photos', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.event_title}---{self.event_type}"
