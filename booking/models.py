from django.db import models

# Create your models here.

class Booking(models.Model):
    last_name = models.CharField(max_length=42)
    first_name = models.CharField(max_length=42)
    coming_date = models.DateField(help_text='Date de début du séjour')
    leaving_date = models.DateField(help_text='Date de fin du séjour')
    email_address = models.EmailField()
    therapy = models.BooleanField(verbose_name='Allez vous en cure ?', blank=True)

    def __str__(self):
        return self.last_name
