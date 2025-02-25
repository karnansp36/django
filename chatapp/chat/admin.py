from django.contrib import admin
from .models import Group, ImagePost
# Register your models here.

class GroupAdmin(admin.ModelAdmin):
    list_display = ("group_name", "description","timestamp")


admin.site.register(Group, GroupAdmin)

admin.site.register(ImagePost)