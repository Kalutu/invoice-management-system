from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['name', 'phone_number', 'invoice_date',
				'line_one', 'line_one_quantity', 'line_one_unit_price', 'line_one_total_price',
				'line_two', 'line_two_quantity', 'line_two_unit_price', 'line_two_total_price',
				'line_three', 'line_three_quantity', 'line_three_unit_price', 'line_three_total_price',
				'line_four', 'line_four_quantity', 'line_four_unit_price', 'line_four_total_price',
				'line_five', 'line_five_quantity', 'line_five_unit_price', 'line_five_total_price', 
				'total', 'paid', 'invoice_type'
				]
