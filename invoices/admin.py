from django.contrib import admin
from .models import Invoice, SType, Service
# Register your models here.

class ServiceInline(admin.StackedInline):
    model = Service

class InvoiceAdmin(admin.ModelAdmin):
    inlines = [
        ServiceInline,
    ]
    list_display = ('customer', 'total_amount', 'created_on')
    


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(SType)