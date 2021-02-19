from django.db import models

# Create your models here.


from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Article_Type(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=False, max_length=20)
    description = models.CharField(max_length=255)
    createAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['createAt']


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=False, max_length=20)
    typeID = models.ForeignKey(Article_Type, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    isShow = models.BooleanField(default=True)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now_add=True)
    createBy = models.CharField(default="quulio", blank=False, max_length=30)
    updateBy = models.CharField(default="quulio", blank=False, max_length=30)
    isRecommend = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['createAt']


class Article_Image(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=15, blank=False, default="not set")
    articleID = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="urls")
    topic = models.BooleanField(default=False)
    detail = models.BooleanField(default=False)
    detailTopic = models.BooleanField(default=False)
    url = models.CharField(max_length=255)
    isShow = models.BooleanField(default=True)
    createAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

    class Meta:
        ordering = ['createAt']


class Article_Content(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=15, blank=False, default="not set")
    articleID = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    isShow = models.BooleanField(default=True)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['createAt']
