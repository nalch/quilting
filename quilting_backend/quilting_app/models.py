from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    about = models.TextField()


class UuidModel(models.Model):
    uuid = models.CharField(max_length=64, default=uuid4, primary_key=True)

    def __str__(self):
        return self.uuid

    class Meta:
        abstract = True


class Tutorial(UuidModel):
    title = models.CharField(max_length=255)
    short_link = models.CharField(max_length=64)
    thumbnail = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class TutorialStep(UuidModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tutorial = models.ForeignKey(
        Tutorial,
        related_name='steps',
        on_delete=models.CASCADE)


class TutorialImage(models.Model):
    tutorial = models.ForeignKey(
        Tutorial,
        related_name='images',
        on_delete=models.CASCADE)
    image = models.ImageField()


class TutorialStepImage(models.Model):
    tutorial_step = models.ForeignKey(
        TutorialStep,
        related_name='images',
        on_delete=models.CASCADE)
    image = models.ImageField()
