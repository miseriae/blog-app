from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField(max_length=420)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
