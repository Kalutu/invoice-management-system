from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['name', 'phone_number', 'invoice_date','invoice_number',
				'line_one', 'line_one_quantity', 'line_one_unit_price',
				'total', 'invoice_type', 'paid'
				]
		
class InvoiceSearchForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['invoice_number', 'name']