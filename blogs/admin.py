from django.contrib import admin

from blogs.models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'create_date')
    list_filter = ('title', )
    ordering = ('id', )

admin.site.register(Blog, BlogAdmin)


