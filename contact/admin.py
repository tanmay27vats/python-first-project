from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'created')

    # Remove "Add Contact Us Requests" button from right side of the page.
    def has_add_permission(self, request):
        return False

    # Remove delete action
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Contact, ContactAdmin)