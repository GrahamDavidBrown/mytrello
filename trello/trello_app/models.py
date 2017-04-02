from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    name_first = models.CharField(max_length=20)
    name_last = models.CharField(max_length=20)


class Board(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    users = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    child = models.CharField(max_length=20, default='lists')


class List(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    boards = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, blank=True)
    child = models.CharField(max_length=20, default='cards')


class Card(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    priority = models.IntegerField(null=True, blank=True)
    comment = models.CharField(max_length=250, null=True, blank=True)
    lists = models.ForeignKey(List, on_delete=models.CASCADE, null=True, blank=True)
