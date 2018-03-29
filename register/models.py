from django.db import models
from multiselectfield import MultiSelectField

availability = (
    ('1', 'Sunday'),
    ('2', 'Monday'),
    ('3', 'Tuesday'),
    ('4', 'Wednesday'),
    ('5', 'Thursday'),
    ('6', 'Friday'),
    ('7', 'Saturday'),
)

satisfaction = (
    ('1', 'Bad'),
    ('2', 'Neutral'),
    ('3', 'Good'),
)


# Create your models here.
class Company(models.Model):
    social_name = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    cnpj = models.CharField(max_length=14)
    found_date = models.DateField()

    def __str__(self):
        return (self.name)