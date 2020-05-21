from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

# Canonical URLs for models
from django.urls import reverse

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Drfat'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    #CharField, which translates into a VARCHAR column in the SQL database.
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    #slug is a short label that contains only letters, numbers, underscores, or hyphens. slug field to build
    #SEO-friendly URLs. Django will prevent multiple posts from having the same slug for a given date.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_poasts')
    #A foreign key defines a many-to-one relationship. Django will create a foreign key in the database using
    #the primary key of the related model. The on_delete parameter specifies the behavior to adopt when the
    #refernced object is deleted. This is not specific to Django; it is an SQL standard. Using CASCADE, it
    #specifies that when the referenced model is deleted, the database will also delete its related model.
    body = models.TextField()
    #TextField, which translates into a TEXT column in the SQL database.
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    #auto_now_add, the date will be saved automatically when creating an object.
    updated = models.DateTimeField(auto_now=True)
    #auto_now, the date will be updated automatically when saving an object
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='draft')
    #choices parameter, the value of this field can only be set to one of the given choices.
    #All Django field types :  https://docs.djangoproject.com/en/2.0/ref/modles/fields/
    #primary_key attribute
    #DJango create a primary key automatically for each model, the default primary key is an id column, which
    #consists of an integer that in increamented automatically.
    #By using primary_key attribute on one of modle fields, that column corresponds to the id field that is
    #automatically added to your models.

    class Meta:
        ordering = ('-publish',)
    #The Meta class inside the model contains metadata. Django sort results in the publish fiend in descending
    #order by default when users query the database. Using the negative prefix. posts published recently will
    #apper first
    #   db_table = 'model_name'
    #Django generates the tables names by combining the app name and the lowercase name of the model.
    #Specify the tables name with using the db_table attribute.

    def __str__(self):
        return self.title
    #The __strt__() method is the default human-readable representation of the object.
    #**NOTE**Python 2.x __unicode__() method is obsolete, in Python 3, all strings are natively consdiered Unicode.

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.publish.year,
                                                self.publish.month,
                                                self.publish.day,
                                                self.slug])
    ##reverse() method that aloows you to build URLs by their name and passing optional parameters.