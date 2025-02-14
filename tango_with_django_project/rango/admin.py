from django.contrib import admin

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

from rango.models import Category, Page
admin.site.register(Category)
admin.site.register(Page, PageAdmin)