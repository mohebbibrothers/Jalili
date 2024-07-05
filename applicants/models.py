from django.db import models
from location_field.models.plain import PlainLocationField

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    national_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    TYPE_CHOICES = [
        ('1', 'استفاده از صندوق سیار'),
        ('2', 'استفاده از خدمات حمل و نقل مردمی'),
    ]

    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='1')
    location = PlainLocationField(based_fields=['Tehran'], zoom=7)


    def __str__(self):
        return f'name: {self.name} national code: {self.national_code} phone number: {self.phone_number} type: {self.type}'