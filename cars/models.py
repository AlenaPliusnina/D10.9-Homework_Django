from django.db import models


class Car(models.Model):
    company = models.CharField(max_length=100)
    model = models.CharField(max_length=20)
    year = models.IntegerField()

    MECHANICS = 1
    AUTOMATIC = 2
    ROBOT = 3
    TRANSMISSION = [
        (MECHANICS, 'механика'),
        (AUTOMATIC, 'автомат'),
        (ROBOT, 'робот'),
    ]
    transmission = models.SmallIntegerField(choices=TRANSMISSION, default=MECHANICS)

    color = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/cars', blank=True)
