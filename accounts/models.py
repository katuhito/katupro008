from django.db import models
from django.contrib.auth.models import AbstractUser
# from matplotlib.image import thumbnail
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

class CustomUser(AbstractUser):
    desctiption = models.TextField(verbose_name='プロフィール', null=True, blank=True)
    photo = models.ImageField(verbose_name='写真', blank=True, null=True, upload_to='images/')
    thumbnail = ImageSpecField(source='photo', processors=[ResizeToFill(256, 256)], format='JPEG', options={'quality': 60})

    class Meta:
        verbose_name_plural = 'CustomUser'
        

