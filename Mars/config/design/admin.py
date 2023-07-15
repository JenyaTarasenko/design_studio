from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ['author', 'description', 'category']


class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'slug']


admin.site.register(models.Category, MPTTModelAdmin)#подключаем вложенность MPTT
admin.site.register(models.DescriptionPost, DescriptionAdmin)
admin.site.register(models.Post, PostAdmin)




