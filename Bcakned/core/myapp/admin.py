from django.contrib import admin

# Register your models here.
from .models import Post,Comment,CustomUser

admin.site.register(CustomUser)

admin.site.register(Post)
admin.site.register(Comment)
