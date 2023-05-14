from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.title


"""
    >> python3 manage.py shell
    >> from blog.models import Post
    >> from django.contrib.auth.models import User
    ...
    ...
    ...
    >> user.post_set.all()
    >> user.post_set.create(titile='Blog 3', content='Third Post Content!')

"""