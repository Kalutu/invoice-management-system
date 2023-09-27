from django.db import models

# Create your models here.
class Invoice(models.Model):
	comments = models.TextField(max_length=3000, default='', blank=True, null=True)
	invoice_number = models.IntegerField(blank=True, null=True)
	invoice_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
	name = models.CharField('Customer Name', max_length=120, default='', blank=True, null=True)
	
	item = models.CharField('Item', max_length=120, default='', blank=True, null=True)
	quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
	unit_price = models.IntegerField('Unit Price (Ksh)', default=0, blank=True, null=True)
	total_price = models.IntegerField('Total (Ksh)', default=0, blank=True, null=True)

	phone_number = models.CharField(max_length=120, default='', blank=True, null=True)
	balance = models.IntegerField(default='0', blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)
	paid = models.BooleanField(default=False)
	invoice_type_choice = (
			('Receipt', 'Receipt'),
			('Proforma Invoice', 'Proforma Invoice'),
			('Invoice', 'Invoice'),
		)
	invoice_type = models.CharField(max_length=50, default='', blank=True, null=True, choices=invoice_type_choice)

	def __str__(self):
		return self.name