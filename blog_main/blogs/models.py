from django.db import models
from django.contrib.auth import get_user_model  

User = get_user_model()

STATUS_CHOICES = (
        (0, 'Draft'),
        (1, 'Published')
    )

# Create your models here.

class Category(models.Model):
    Category_name = models.CharField(max_length=100 ,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
    
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.Category_name
    

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True,blank=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='blog_images/')
    short_desciption = models.CharField(max_length=500)
    blog_body = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title