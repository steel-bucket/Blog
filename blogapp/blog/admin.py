from django.contrib import admin
from . import models


@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'slug', 'status', 'author')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Category)
