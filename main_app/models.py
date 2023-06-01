from django.db import models
from django.urls import reverse

BASE = (
    ('F', 'First'),
    ('S', 'Second'),
    ('T', 'Third'),
    ('F', 'Home Run'),
)

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

class Hit(models.Model):
    date = models.DateField('date of hit')
    base = models.CharField(
        max_length = 1,
        choices=BASE,
        default=BASE[0][0]
    )
    
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.get_base_display()} on {self.date}"