from django.contrib import admin
from api.models import UserModel

class UserAdmin(admin.ModelAdmin):
    fields=('id', 'name')

admin.site.register(UserModel, UserAdmin)