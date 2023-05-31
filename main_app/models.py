from django.db import models
from django.urls import reverse

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    jersey_number = models.IntegerField()
    age = models.IntegerField()
    
    
def __str__(self):
    return f'{self.name} ({self.id})'

def get_absolute_url(self):
    return reverse('detail', kwargs={'player_id': self.id})