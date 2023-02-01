from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from fileUpload.models import FilesModel


class FileUploadAdmin(admin.ModelAdmin):
    # fieldsets = (
    #                 (None, {'fields': ('username', 'password')}),
    #                 (_('Personal info'), {'fields': ('email', 'first_name', 'last_name')}),
    #                 (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'roles',)}),
    #                 (_('Important dates'), {'fields': ('date_joined',)}),
    #
    #             )

    list_display = ('id', 'name', 'file')
    list_display_links = ('id', 'name', 'file')
    search_fields = ('name', )


admin.site.register(FilesModel, FileUploadAdmin)
