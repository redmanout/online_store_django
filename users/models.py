from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager


def get_upload_path(instance, filename):
    return "user_avatar/user_{id}/{file}".format(id=instance.email, file=filename)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    avatar = models.ImageField(
        upload_to=get_upload_path,
        verbose_name='User photo',
        default='default.png',
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

    def __str__(self):
        return self.email
