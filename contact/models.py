from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=42)
    name = models.CharField(max_length=42)
    subject = models.CharField(max_length=100)
    email_address = models.EmailField()
    message = models.TextField(null=True)

    def __str__(self):
        return self.name + ', ' + self.subject
