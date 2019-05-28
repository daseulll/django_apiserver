from django.conf import settings
from django.db import models

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                related_name='sample5_post_set') # user.sample5_post_set.all()
                                # sample_3 의 Post.author와 reverse가 겹치므로 변경
    message = models.CharField(max_length=140)
    ip = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    