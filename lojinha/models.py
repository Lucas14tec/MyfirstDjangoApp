
from django.conf import settings
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



class Post(models.Model):
    author         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title          = models.TextField(max_length=100)
    resume         = RichTextField()
    text           = RichTextUploadingField()
    created_date   = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title