from django.db import models
from hotels.models import Hotel

class Review(models.Model):
    rating_choices = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name='hotels')
    publish_date = models.DateTimeField('Date Published')
    user = models.CharField(max_length=100)
    comment = models.CharField(max_length=1000)
    rating = models.IntegerField(choices=rating_choices)
