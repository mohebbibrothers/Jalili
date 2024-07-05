from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    national_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    car_name = models.CharField(max_length=100)
    car_color = models.CharField(max_length=50)
    car_tag = models.CharField(max_length=10)
    areas = models.ManyToManyField('Area', related_name='providers')

    def __str__(self):
        return f'name: {self.name} national code: {self.national_code} phone number: {self.phone_number} car name: {self.car_name} car color: {self.car_color} car tag: {self.car_tag}'
    
class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name