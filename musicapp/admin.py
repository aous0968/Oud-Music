from django.contrib import admin

from .models import Track

class TrackAdmin(admin.ModelAdmin):
    # list_display = ("name")
    # prepopulated_fields = {"slug": ("name",)}
    pass

admin.site.register(Track , TrackAdmin)