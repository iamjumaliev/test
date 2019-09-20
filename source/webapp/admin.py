from django.contrib import admin
from webapp.models import Plan


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'status']
    list_filter = ['status']
    list_display_links = ['pk',]
    search_fields = ['descriptions']
    fields = ['description', 'deadline', 'status']


admin.site.register(Plan, ArticleAdmin)
