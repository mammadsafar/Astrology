from re import T
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from accounts.models.profile import Profile
from pathlib import Path

from django.db.models.signals import post_save
from django.dispatch import receiver

BASE_DIR = Path(__file__).resolve().parent.parent

from django.db import models
from django.utils.text import slugify


class Card(models.Model):
    STATUS_CHOICES = (
        ('False', 'در انتظار پرداخت'),
        ('True', 'پرداخت شده'),
    )

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)

    page_title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)

    image = models.ImageField(upload_to='image/', null=True, blank=True)
    logo = models.ImageField(upload_to='logo/', null=True, blank=True)

    status = models.CharField(verbose_name='وضعیت', choices=STATUS_CHOICES, max_length=9, default='True')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/{self.slug}/"

    def __str__(self):
        return self.first_name + ' ' + self.last_name


# @receiver(post_save, sender=Card)
# def save_profile(sender, instance, created, **kwargs):
#     if created:
#         Card.objects.create(user=instance)


class SocialMedia(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    icon = models.ImageField(upload_to='SocialMedia/', null=True, blank=True)
    link = models.CharField(max_length=500)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.link


class Button(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    text = models.CharField(max_length=9)
    link = models.CharField(max_length=500)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.link
