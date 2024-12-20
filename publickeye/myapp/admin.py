from django.contrib import admin
from .models import CrimeReport
from .models import Comment
admin.site.register(Comment)
admin.site.register(CrimeReport)
from django.contrib import admin
from .models import Officer
@admin.register(Officer)
class OfficerAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email', 'phone', 'specialization', 'created_at')
    search_fields = ('username', 'name', 'email')
    ordering = ('created_at',)
    list_filter = ('specialization',)


from .models import MostWanted

@admin.register(MostWanted)
class MostWantedAdmin(admin.ModelAdmin):
    list_display = ('name', 'crime_type', 'reward', 'created_at')  # Fields to display in the list view
    search_fields = ('name', 'crime_type')  # Fields to search by
    list_filter = ('crime_type',)  # Add filters for crime types

from .models import Feedback  # Import the Feedback model

# Register the Feedback model with the admin site
admin.site.register(Feedback)