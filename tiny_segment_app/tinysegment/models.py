from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(blank=False, null=False, unique=True)
    name = models.CharField(max_length=128, unique=False)
    username = models.CharField(max_length=128, unique=False)
    about = models.TextField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if self.username is None:
            self.username = (self.first_name[0] + self.last_name.replace(' ', '')).lower()
        super().save(*args, **kwargs)


class CodeComponent(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    source_event = models.CharField(max_length=255)
    source_div_id = models.CharField(max_length=255)
    html_code = models.TextField()
    code_placement = models.CharField(max_length=20, choices=[('replace', 'Replace Parent Div\'s InnerHTML'), ('bottom', 'Place at Bottom of Parent Div'), ('top', 'Place at Top of Parent Div')])
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Paused', 'Paused')])

    def __str__(self):
        return self.name


class SegmentObjects(models.Model):
    anonymous_user_id = models.CharField(max_length=255, null=True, blank=True)
    user_id = models.CharField(max_length=255, null=True, blank=True)
    message_id = models.CharField(max_length=255, null=True, blank=True)

    page_path = models.CharField(max_length=255, null=True, blank=True)
    page_title = models.CharField(max_length=255, null=True, blank=True)

    source_element_id = models.CharField(max_length=255, null=True, blank=True)
    event_name = models.CharField(max_length=255, null=True, blank=True)
    event_type = models.CharField(max_length=255, null=True, blank=True)

    received_at = models.DateTimeField()
    def __str__(self):
        return self.anonymous_user_id
