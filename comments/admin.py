from django.contrib import admin

from comments.models import Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'content_type', 'create_date')
    list_filter = ('content',)
    ordering = ('id',)

admin.site.register(Comment, CommentAdmin)