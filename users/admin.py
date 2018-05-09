from django.contrib import admin

from users.models import Account
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'username', 'telephone', 'register_source', 'register_time')
    list_filter = ('user',)

admin.site.register(Account, AccountAdmin)