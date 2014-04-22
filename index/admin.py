from django.contrib import admin
from index.models import Visit



class VisitAdmin(admin.ModelAdmin):
    fields = ['ip_address', 'visit_time']
    list_display = ('ip_address', 'visit_time')


admin.site.register(Visit, VisitAdmin)
