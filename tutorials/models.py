from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.

# image manipulation with pilow.
# image = ContentFile(b64decode(part.get_payload()))
#       im = Image.open(image)
#       tempfile = im.rotate(270)
#       tempfile_io =StringIO.StringIO()
#       tempfile.save(tempfile_io, format='JPEG')# image_file = InMemoryUploadedFile(tempfile_io, #None, 'rotate.jpg','image/jpeg',tempfile_io.len, None)
#       img = Photo(user=user)
#       img.img.save('rotate.jpg', image_file)
#       img.save()

# Creating the tables for the User
'''
class AppUser(models.Model):
    """docstring for AppUser."""
    PERMISSIONS = (
        (0, False),
        (1, True),
    )
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=120)
    password = models.CharField(max_length=60)
    is_admin = models.BooleanField(default=False, choices=PERMISSIONS)
    is_author = models.BooleanField(default=False, choices=PERMISSIONS)

    def __str__(self):
        return str(self.name)
'''


class Post(models.Model):
    STATUS = (
        (0, "Draft"),
        (1, "Publish")
    )
    CHOICES = (
        ('Java', 'Java'),
        ('JavaScript', 'JavaScript'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('Python', 'Python'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    lang = models.CharField(max_length=10, choices=CHOICES)
    title = models.CharField(max_length=200, verbose_name='Post Title')
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='tutorials_pics')
    body = RichTextUploadingField()
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return f'{self.title} from {self.author}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100, blank=True)
    comment = models.TextField(max_length=3000)
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    # parent = models.ForeignKey('self', null=True, blank=True, related_name='\
    # replies')

    class Meta:
        ordering = ('-created_time',)

    def __str__(self):
        return f'Comment by {self.name} at {self.created_time}'
