from django.contrib import admin
from .models import Post, Hashtag, PostAction, PostHashTag

# Register your models here.

@admin.register(Post, Hashtag, PostAction, PostHashTag)
class PostAdmin(admin.ModelAdmin):
    pass