from django.db import models

from core.validators import gmail_validation

class Contact(models.Model):
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        max_length=100,
        blank=True,
        null=True,
        validators=[gmail_validation],
    )
    content = models.TextField()
    attachment = models.FileField(
        upload_to="media/",
        blank=True,
        null=True,
    )