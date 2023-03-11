from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager


def get_upload_path(instance, filename):
    return "user_avatar/user_{0}/{1}".format(instance.email, filename)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=160)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    avatar = models.ImageField(
        upload_to=get_upload_path,
        verbose_name='User photo',
        default='user_avatar/default.png',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        super().save()
        image = Image.open(self.avatar.path)
        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.avatar.path)

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.avatar.url))
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.email
