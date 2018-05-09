from django.contrib import admin
from likes.models import Like

# Register your models here.
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'content_type', 'create_date')
    list_filter = ('status',)
    ordering = ('id',)

admin.site.register(Like, LikeAdmin)