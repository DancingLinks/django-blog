from django.contrib import admin
from .models import Comment, Page

admin.site.register(Comment)
admin.site.register(Page)