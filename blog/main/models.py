from django.db import models
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from PIL import Image

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=200)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.category
    
    def get_absolute_url(self):
        return f"/category/{self.slug}"
    
    @property
    def get_post_count(self):
        return self.post_set.all().count()

    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=200, null=True, blank=True)
    body = RichTextField()
    snippet = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    # thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)
    featured = models.BooleanField(default=False)


    class Meta:
        get_latest_by = 'time_stamp'

    def get_absolute_url(self):
        return f"/post/{self.slug}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)  # Call the real save() method

    def __str__(self):
        return self.title

    @property
    def get_comment_count(self):
        return self.comment_set.all().count()
    
    @property
    def get_view_count(self):
        return self.view_set.all().count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    reply = models.ForeignKey('Comment', null=True,
                              related_name='replies', on_delete=models.CASCADE)
    email = models.EmailField()
    text = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    @property
    def is_reply(self):
        return True if self.reply else False

    def __str__(self):
        return f"{self.name}-{self.id}-{self.is_reply}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    message = models.TextField()

    def __str__(self):
        return f"message from {self.name}"


class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=200)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}...--{self.author}"
    
    class Meta:
        get_latest_by = 'time_stamp'


class View(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
