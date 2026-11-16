from django.contrib import admin
from .models import Customer, Medicine


class MedicineInline(admin.TabularInline):
    model = Medicine
    extra = 1


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "phone")
    search_fields = ("name", "phone")
    inlines = [MedicineInline]


admin.site.register(Medicine)
