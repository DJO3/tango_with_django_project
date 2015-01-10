from django.contrib import admin
from rango.models import Category, Page

# Alters Admin Page view to show three columns
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)