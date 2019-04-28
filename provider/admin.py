from django.contrib import admin

from .models import Provider, Service


admin.site.register(Provider)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'created']
	prepopulated_fields = {'slug': ['title',]}
	search_fields = ['title', 'overview', 'body']
	list_filter = ['created', 'updated']

