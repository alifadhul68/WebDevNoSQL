from django.db import models

class Hotel(models.Model):
    title = models.CharField(max_length=200, verbose_name='Hotel Name')
    description = models.TextField(null=True)
    city = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title