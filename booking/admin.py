from django.contrib import admin

# Register your models here.

from booking.models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'coming_date', 'leaving_date', 'email_address', 'therapy')
    list_filter = ('therapy',)
    date_hierarchy = 'coming_date'
    ordering = ('coming_date',)
    search_fields = ('last_name', 'first_name', 'email_address')

    fieldsets = (
        ('Clients', {
            'classes': ['collapse',],
            'fields': ('last_name', 'first_name', 'email_address')
        }),
        ('Infos', {
           'description': 'Informations complémentaires sur la réservation',
           'fields': ('coming_date', 'leaving_date', 'therapy')
        }),
    )

admin.site.register(Booking, BookingAdmin)
