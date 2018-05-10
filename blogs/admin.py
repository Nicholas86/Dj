from django.contrib import admin

from blogs.models import Category, Tag, Blog
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order_num', 'create_date')
    list_filter = ('name',)
    ordering = ('id',)

admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order_num', 'create_date')
    list_filter = ('name',)
    ordering = ('id',)

admin.site.register(Tag, TagAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'create_date')
    list_filter = ('title', )
    ordering = ('id', )

admin.site.register(Blog, BlogAdmin)


