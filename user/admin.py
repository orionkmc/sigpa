from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from user.models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    verbose_name_plural = 'Configuracion'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
