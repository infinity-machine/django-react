from django.contrib import admin
from api.models import UserModel

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserModel, UserAdmin)