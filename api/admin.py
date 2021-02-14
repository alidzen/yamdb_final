
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'username', 'role', 'is_admin', 'is_active')
    list_filter = ('role', 'is_active', )

    fieldsets = (
        (
            None,
            {'fields': ('email', 'password', 'username', 'role')}
        ),
        (
            'Access',
            {'fields': ('is_active',)}
        ),
        (
            'Credentials',
            {'fields': ('first_name', 'last_name', 'bio')}
        ),
    )

    add_fieldsets = (
        (
            None,
            {'fields': ('email', 'password', 'username', 'role')}
        ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
