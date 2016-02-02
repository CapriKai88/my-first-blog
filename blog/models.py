from django.db import models
from django.utils import timezone

# Create your models here.
# All lines starting with from or imprt menas that it is taken from other files.
# Class Post.. - defines our model (it's an object).
# Class = defining an object
# Post = name of our model
# models.Model = Post is a django model so django knows it should be saved in Database.

# Then define the properties title, text etc,i.e is it a number, date, relation to another object like user.
# models.Charfield = define text with limited number of characters
# models.TextField = defines long text w/out limit
# models.ForeignKey = links to another model

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
#  def publish(self) = def is function/method publish is the name of the method
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
