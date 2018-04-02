from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

# Create your models here.
class Company(models.Model):
    social_name = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    found_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Companies'
        ordering = ('name',)


    def __str__(self):
        return (self.name)

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    project = models.ManyToManyField(Project)

    def __str__(self):
        return (str(self.user))

    def invite(self, invite_profile):
        invite = Invite(inviter=self, invited=invite_profile)
        invite.save()


class Invite(models.Model):
    inviter = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING ,related_name='made_invites')
    invited = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING ,related_name='received_invites')