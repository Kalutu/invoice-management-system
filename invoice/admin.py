from django.contrib import admin
from .models import Invoice
from .forms import InvoiceForm

# Register your models here.

class InvoiceAdmin(admin.ModelAdmin):
   list_display = ['name', 'invoice_number', 'invoice_date']
   form = InvoiceForm
   list_filter = ['name']
   search_fields = ['name', 'invoice_number']

admin.site.register(Invoice, InvoiceAdmin)