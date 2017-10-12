from django.contrib import admin
from app01 import models
# Register your models here.

class NewsInfoAdmin(admin.ModelAdmin):
    list_display = ('title','favor_count','reply_count')

admin.site.register(models.UserType)
admin.site.register(models.Admin)
admin.site.register(models.Chat)
admin.site.register(models.NewsType)
admin.site.register(models.News,NewsInfoAdmin)
admin.site.register(models.Reply)