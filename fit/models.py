from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
    name = models.CharField(max_length=20)
    xp = models.IntegerField(default=0)
    hp = models.IntegerField(default=100)
    max_hp = models.IntegerField(default=100)
    strength = models.IntegerField(default=5)
    endurance = models.IntegerField(default=5)
    dexterity = models.IntegerField(default=5)
    willpower = models.IntegerField(default=5)
    

