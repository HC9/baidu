from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Register your models here.
def _active_user_staff(modeladmin, request, queryset):
    # 将选中的用户的权限统一更改为 staff
    for user in queryset:
        user.is_staff = True
        user.save()


_active_user_staff.short_description = "一键激活用户"


class MyUserAdmin(UserAdmin):
    actions = [_active_user_staff]


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
