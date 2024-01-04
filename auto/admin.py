from django.contrib import admin

# Register your models here.
from .models import *

class AutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'marka', 'gos_number', 'time_create', 'photo', 'is_published', 'post') # весь список полей
    list_display_links = ('id', 'marka') # список полей, по которым формируются ссылки
    search_fields = ('marka', 'gos_number') # список полей, по которым возможен поиск
    list_editable = ('is_published',) # список редактируемых полей
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("marka",)}
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Auto, AutoAdmin)
admin.site.register(Category, CategoryAdmin)


