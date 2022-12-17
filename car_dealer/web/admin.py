from django.contrib import admin
from django.contrib.auth.models import User

from .models import Listing, Feedback, ContactForm


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', "username", 'email', 'is_staff', 'is_superuser', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('first_name', 'last_name','email')
    ordering = ('-date_joined',)

    fieldsets = (
        (
            'Personal Info',
            {
                'fields': ('first_name', 'last_name', 'email', 'username', 'password'),
            }
        ),
        ('Permissions',
         {'fields': ('is_staff', 'is_superuser'),
          }
         ),
    )

    def full_name(self,obj):
        return f'{obj.first_name} {obj.last_name}'


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "brand", "model",'year', 'price')
    list_filter = ('brand','year')
    ordering = ('-date_created',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("full_name", "rating", "comment")
    ordering = ('-date',)


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("email", "phone_number", "message", 'submission_date')
    ordering = ('-submission_date',)

