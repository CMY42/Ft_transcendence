from django.db import models

class Player(models.Model):
    alias = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)  # Hashed password

    def __str__(self):
        return self.alias
