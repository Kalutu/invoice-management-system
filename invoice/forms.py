from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['name', 'phone_number', 'invoice_date',
				'line_one', 'line_one_quantity', 'line_one_unit_price', 'line_one_total_price',
				'total', 'invoice_type', 'paid'
				]