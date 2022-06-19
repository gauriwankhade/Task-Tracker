from django.db import models
from Utils.choice_list import *
from django.utils import timezone
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


class CustomUser(AbstractUser):
    email = models.EmailField(null=False, blank=False)
    role = models.CharField(choices=UserRole.CHOICES, max_length=255)

    def __str__(self):
        return self.email + ' role - ' + self.role

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


class Team(models.Model):
    name = models.CharField(max_length=255)
    leader = models.ForeignKey(CustomUser ,on_delete=models.CASCADE,
            limit_choices_to={'role': UserRole.TEAM_LEADER})
    

    def __str__(self):
        return self.name 



class Task(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(choices=TaskStatus.CHOICES, max_length=255)
    started_at = models.DateTimeField(default=timezone.now)
    completed_at = models.DateTimeField(blank=True, null=True)
    assigned_to = models.ForeignKey(Team, on_delete=models.CASCADE)


    def __str__(self):
        return self.name 



class TeamToMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    member = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                     limit_choices_to={'role': UserRole.TEAM_MEMBER})


    def __str__(self):
        return self.member.email + ' member of team - ' + self.team.name


class TaskAssignedToMember(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    member = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                     limit_choices_to={'role': UserRole.TEAM_MEMBER})

    def __str__(self):
        return self.task.name + ' assigned to - ' + self.member.email








