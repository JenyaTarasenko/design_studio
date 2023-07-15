from django.urls import reverse

from django.contrib.auth.models import User

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey




class Category(MPTTModel):#библиотека вложенности категорий
    """категории работ и описание"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey('self', related_name='children', on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.name#указывает в perent name


    class MPTTMeta:
        order_insertion_by = ['name']




#class Tag(models.Model):
#    """модель тэгов"""
#    name = models.CharField(max_length=100)
#    slug = models.SlugField(max_length=100)

#    def __str__(self):
#        return self.name





class DescriptionPost(models.Model):
    author = models.ForeignKey(User, related_name='text', on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='articles/')
    category = models.ForeignKey(Category, related_name='text', on_delete=models.SET_NULL, null=True)
    price = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, default=None, blank=True, null=True)


    def __str__(self):
        return self.description


    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"slug": self.category.slug})






class Post(models.Model):
    author = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, default=None, null=True)
    create_at = models.DateTimeField(null=True)
    category = models.ForeignKey(Category, related_name='post', on_delete=models.SET_NULL, null=True)




    def __str__(self):
        return self.title

    #def get_absolute_url(self):
    #    return reverse('design/list_details.html', kwargs={'slug': self.slug})

    def get_absolute_url(self):
        return reverse('list_details', kwargs={"slug": self.category.slug})





