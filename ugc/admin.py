from django.contrib import admin
from .models import UGCPost, Location, Coordinates


# Register your models here.


@admin.register(UGCPost)
class UGCPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'updated_at']
    search_fields = ['title', 'user__username']


admin.site.register(Coordinates)
admin.site.register(Location)
