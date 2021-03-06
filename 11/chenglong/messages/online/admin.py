from django.contrib import admin

# Register your models here.
from .models import Message2




class Message2Admin(admin.ModelAdmin):
    list_display = ('username', 'title','content','publish_date')
    search_fields = ('username', 'title','content', 'publish_date')
    list_filter = ('username','publish_date')

admin.site.register(Message2, Message2Admin)