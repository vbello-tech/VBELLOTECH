from django.db import models
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    body = models.TextField()
    post_image = models.ImageField(blank=False, upload_to="Blog/")
    publish_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

class Project(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    project_name = models.CharField(max_length=250)
    project_description = models.TextField()
    project_image = models.ImageField(upload_to="portfolio/")
    project_url = models.URLField(blank=True, null=True)
    github_url = models.URLField()
    published_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.project_name


class Comments(models.Model):
    post = models.ForeignKey('Blog', related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=300, default="")
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)



