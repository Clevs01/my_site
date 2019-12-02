from datetime import datetime as t
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
TITLE = (
    ('M', 'Mr'),
    ('Ms', 'Mrs'),
    ('Dr', 'Doctor')
)


class AboutMe(models.Model):
    name = models.CharField(max_length=64, verbose_name='My full names')
    picture = models.ImageField()
    hobbies = RichTextField()
    bio = RichTextField()
    description = RichTextUploadingField()

    def __str__(self):
        return f'This is about {self.name}'


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    country = models.CharField(max_length=64, blank=True)
    address = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=2, choices=TITLE)
    recieved_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message "{self.message}" from {self.title} {self.name} received at {t.utcnow()}.'


class Learning(models.Model):
    """
    docstring for . Learning model. This model takes care of all learning
    resources.
    """
    provider = models.CharField(max_length=200)
    title = models.CharField(max_length=250)
    img = models.ImageField(upload_to='course_pic')
    course_url = models.CharField(max_length=250, default=None)
    description = RichTextUploadingField()

    def __str__(self):
        return self.title
