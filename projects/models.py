from django.db import models
from django.contrib.auth.models import User
from register.models import Company

status = (
    ('1', 'Stuck'),
    ('2', 'Working'),
    ('3', 'Done'),
)

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=80)
    status = models.CharField(max_length=7, choices=status, default=1)
    dead_line = models.DateField()
    assign = models.ForeignKey(User)
    company = models.ForeignKey(Company)
    complete_per = models.FloatField(max_length=2)

    add_date = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return (self.name)
