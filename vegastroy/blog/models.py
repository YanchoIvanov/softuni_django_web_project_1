from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/')

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.email} on {self.post.title}"
