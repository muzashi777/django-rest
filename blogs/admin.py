from django.contrib import admin

# Register your models here.
from .models import Article, Article_Type, Article_Image, Article_Content

admin.site.register(Article)
admin.site.register(Article_Type)
admin.site.register(Article_Image)
admin.site.register(Article_Content)
