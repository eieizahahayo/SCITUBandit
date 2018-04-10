from django.contrib import admin
from .models import form,document


class formAdmin(admin.ModelAdmin):
	list_display=[f.name for f in form._meta.fields]


class documentAdmin(admin.ModelAdmin):
	list_display=[f.name for f in document._meta.fields]

admin.site.register(form,formAdmin)
admin.site.register(document,documentAdmin)
