from django.contrib import admin
from .models import Principal, Notice, Program, Department, Gallery
from .models import HeroSlide
admin.site.register(Principal)
admin.site.register(Notice)
admin.site.register(Program)
admin.site.register(Department)
admin.site.register(Gallery)
admin.site.register(HeroSlide)
from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
    )

    list_filter = (
        "created_at",
    )