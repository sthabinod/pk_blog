from django.contrib import admin
from .models import BlogTable

@admin.register(BlogTable)
class AdminBlog(admin.ModelAdmin):
    pass