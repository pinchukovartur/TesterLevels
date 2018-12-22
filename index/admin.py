"""
The script edit admin panel

created by: Pinchukov Artur
date: 13.10.17
"""

# frameworks
from django.contrib import admin
# project models
from .models import TestSecretKey, LevelFile


class TestSecretKeyAdmin(admin.ModelAdmin):
    """
    The class edit view admin panel for TestSecretKey model
    """
    # hides the field
    exclude = ('status', 'secret_key', 'key_pub_date', 'key_active_date')
    # adds a small sort by date
    date_hierarchy = 'key_pub_date'
    # create filter for manyToMany relation field
    filter_horizontal = ("levels",)
    # add full info about entity
    list_display = ("title", "secret_key", "lifetime", "status", "key_pub_date", "key_active_date")


class LevelFileAdmin(admin.ModelAdmin):
    """
    The class edit view admin panel for LevelFile model
    """
    # hides the field
    exclude = ('level_pub_date',)
    # adds a small sort by date
    date_hierarchy = 'level_pub_date'
    # create filter for manyToMany relation field
    filter_horizontal = ("keys",)
    # add full info about entity
    list_display = ("level_name", "level_file", "level_pub_date")

# register edit classes on admin panel
admin.site.register(TestSecretKey, TestSecretKeyAdmin)
admin.site.register(LevelFile, LevelFileAdmin)
