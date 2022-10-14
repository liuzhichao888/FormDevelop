from django.contrib import admin

from .models import Comment
from FormalDevelop.custorm_site import custom_site
from FormalDevelop.base_admin import BaseOwnerAdmin

@admin.register(Comment, site=custom_site)
class ComentAdmin(admin.ModelAdmin):
    list_filter = ('target', 'nickname', 'content', 'website', 'created_time')

