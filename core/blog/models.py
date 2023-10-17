from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
  

# getting user model object
User = get_user_model()


# model posts
class Post(models.Model):
    '''
    this is a class to define posts for blog app
    '''

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    image = models.ImageField(upload_to='blog/',  null=False, blank=False)
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
# model category    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


