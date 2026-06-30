from django.contrib import admin
from .models import AdmissionApplication


def generate_merit_positions(modeladmin, request, queryset):
    programs = queryset.values_list("program", flat=True).distinct()

    for program in programs:
        applications = AdmissionApplication.objects.filter(
            program=program,
            status="Approved"
        ).order_by("-merit_percentage")

        position = 1
        for app in applications:
            app.merit_position = position
            app.save()
            position += 1


generate_merit_positions.short_description = "Generate Merit Positions"


@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
        "program_type",
        "program",
        "merit_percentage",
        "merit_position",
        "status",
        "is_merit_published",
        "applied_at",
    )

    list_filter = (
        "program_type",
        "program",
        "status",
    )

    search_fields = (
        "full_name",
        "father_name",
        "cnic",
        "email",
    )

    list_editable = (
        "status",
        "is_merit_published",
    )

    actions = (
        generate_merit_positions,
    )