from django.contrib import admin

from blogs.models import Category, Tag, Blog
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order_num', 'create_date')
    list_filter = ('name', 'id', 'create_date')
    ordering = ('id',)

admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order_num', 'create_date')
    list_filter = ('name', 'id', 'create_date')
    ordering = ('id',)

admin.site.register(Tag, TagAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'category', 'display_tag_name', 'create_date')
    list_filter = ('title', 'id', 'create_date')
    ordering = ('id', )

admin.site.register(Blog, BlogAdmin)


