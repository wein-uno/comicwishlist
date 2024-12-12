from django.contrib import admin
from .models import Comic

# now make my admin like we did on dogapi add the searchable field
@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'value', 'grade')
    search_fields = ('title')
