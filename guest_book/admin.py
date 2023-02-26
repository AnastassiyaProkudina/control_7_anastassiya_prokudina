from django.contrib import admin

from guest_book.models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "text",
        "status",
        "created_at",
        "updated_at",
        "is_deleted",
        "deleted_at",
    )
    list_filter = ("name",)
    fields = ("name", "email", "text")


admin.site.register(GuestBook, GuestBookAdmin)
