from django import forms
from .models import Invoice
		
class InvoiceForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['name', 'phone_number', 'invoice_date','invoice_number',
				'line_one', 'line_one_quantity', 'line_one_unit_price',
				'total', 'invoice_type', 'paid'
				]


	def clean_invoice_number(self):
		invoice_number = self.cleaned_data.get('invoice_number')
		if not invoice_number:
			raise forms.ValidationError('This field is required')
		return invoice_number

	def clean_name(self):
		name = self.cleaned_data.get('name')
		if not name:
			raise forms.ValidationError('This field is required')
		return name

class InvoiceSearchForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['invoice_number', 'name']

class InvoiceUpdateForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields =  ['name', 'phone_number', 'invoice_date','invoice_number',
				'line_one', 'line_one_quantity', 'line_one_unit_price',
				'total', 'invoice_type', 'paid'
				]
		def clean_invoice_number(self):
			invoice_number = self.cleaned_data.get('invoice_number')
			if not invoice_number:
				raise forms.ValidationError('This field is required')
			return invoice_number

		def clean_name(self):
			name = self.cleaned_data.get('name')
			if not name:
				raise forms.ValidationError('This field is required')
			return name