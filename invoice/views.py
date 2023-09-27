from django.shortcuts import render, redirect
from .forms import *
from .models import Invoice
from django.contrib import messages
# For Report Lab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
# End for report lab
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	title = 'Invoice Management System'
	context = {
	"title": title,
	}
	return render(request, "home.html",context)

@login_required
def add_invoice(request):
	form = InvoiceForm(request.POST or None)
	total_invoices = Invoice.objects.count()
	queryset = Invoice.objects.order_by('-invoice_date')[:6]
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully Saved')
		return redirect('list')
	context = {
		"form": form,
		"title": "New Invoice",
		"total_invoices": total_invoices,
		"queryset": queryset,
	}
	return render(request, "entry.html", context)

def list_invoice(request):
	title = 'List of Invoices'
	queryset = Invoice.objects.all()
	form = InvoiceSearchForm(request.POST or None)
	context = {
		"title": title,
		"queryset": queryset,
		"form": form,
	}
	if request.method == 'POST':
		queryset = Invoice.objects.filter(
											invoice_number__icontains=form['invoice_number'].value(),
											name__icontains=form['name'].value()
										)
		context = {
			"form": form,
			"title": title,
			"queryset": queryset,
		}

		if form['generate_invoice'].value() == True:
			instance = queryset
			data_file = instance
			num_of_invoices = len(queryset)
			message = str(num_of_invoices) + " invoices successfully generated."
			messages.success(request, message)

			def import_data(data_file):
				invoice_data = data_file
				for row in invoice_data:
					invoice_type = row.invoice_type
					invoice_number = row.invoice_number
					invoice_date = row.invoice_date
					name = row.name
					phone_number = row.phone_number

					item = row.item
					quantity = row.quantity
					unit_price = row.unit_price
					total_price = row.total_price

					pdf_file_name = str(invoice_number) + '_' + str(name) + '.pdf'
					generate_invoice(str(name), str(invoice_number), 
					str(item), str(quantity), str(unit_price), 
					str(total_price), str(phone_number), str(invoice_date),
					str(invoice_type), pdf_file_name)

			def generate_invoice(name, invoice_number, 
				item, quantity, unit_price, total_price,
				phone_number, invoice_date, invoice_type, pdf_file_name):
				c = canvas.Canvas(pdf_file_name)

			# image of seal
				logo = 'logoarb.png'
				c.drawImage(logo, 50, 700, width=500, height=120)

				c.setFont('Helvetica', 12, leading=None)
				c.drawCentredString(400, 660, str(invoice_type) + ':')
				c.setFont('Helvetica', 12, leading=None)
				invoice_number_string = str('0000' + invoice_number)
				c.drawCentredString(490, 660, invoice_number_string)


				c.setFont('Helvetica', 12, leading=None)
				c.drawCentredString(409, 640, "Date:")
				c.setFont('Helvetica', 12, leading=None)
				c.drawCentredString(492, 641, invoice_date)


				c.setFont('Helvetica', 12, leading=None)
				c.drawCentredString(397, 620, "Amount:")
				c.setFont('Helvetica-Bold', 12, leading=None)
				c.drawCentredString(484, 622, 'Ksh.'+total_price)


				c.setFont('Helvetica', 12, leading=None)
				c.drawCentredString(80, 660, "To:")
				c.setFont('Helvetica', 12, leading=None)
				c.drawCentredString(150, 660, name)

				c.setFont('Helvetica', 12, leading=None)
				c.drawCentredString(98, 640, "Phone #:")
				c.setFont('Helvetica', 12, leading=None)
				c.drawCentredString(150, 640, phone_number)     

				c.setFont('Helvetica-Bold', 14, leading=None)
				c.drawCentredString(310, 580, str(invoice_type))
				c.drawCentredString(110, 560, "Particulars:")
				c.drawCentredString(295, 510, "__________________________________________________________")
				c.drawCentredString(295, 480, "__________________________________________________________")
				c.drawCentredString(295, 450, "__________________________________________________________")
				c.drawCentredString(295, 420, "__________________________________________________________")
				c.drawCentredString(295, 390, "__________________________________________________________")
				c.drawCentredString(295, 360, "__________________________________________________________")
				c.drawCentredString(295, 330, "__________________________________________________________")
				c.drawCentredString(295, 300, "__________________________________________________________")
				c.drawCentredString(295, 270, "__________________________________________________________")
				c.drawCentredString(295, 240, "__________________________________________________________")
				c.drawCentredString(295, 210, "__________________________________________________________")

				c.setFont('Helvetica-Bold', 12, leading=None)
				c.drawCentredString(110, 520, 'ITEMS')     
				c.drawCentredString(220, 520, 'QUANTITY')     
				c.drawCentredString(330, 520, 'UNIT PRICE')     
				c.drawCentredString(450, 520, 'LINE TOTAL')  


				c.setFont('Helvetica', 12, leading=None)
				c.drawCentredString(110, 490, item)     
				c.drawCentredString(220, 490, quantity)     
				c.drawCentredString(330, 490, unit_price)          
				# TOTAL
				c.setFont('Helvetica-Bold', 20, leading=None)
				c.drawCentredString(400, 140, "TOTAL:")
				c.setFont('Helvetica-Bold', 20, leading=None)
				c.drawCentredString(484, 140, 'Ksh.'+total_price) 


				# SIGN
				c.setFont('Helvetica-Bold', 12, leading=None)
				c.drawCentredString(150, 140, "Signed:__________________")
				c.setFont('Helvetica-Bold', 12, leading=None)
				c.drawCentredString(170, 120, 'Manager') 


				c.showPage()
				print('writing')
				c.save()

				import_data(data_file)
	return render(request, "list.html", context)

@login_required
def update_invoice(request, pk):
	queryset = Invoice.objects.get(id=pk)
	form = InvoiceUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = InvoiceUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			messages.success(request, 'Successfully Updated')
			return redirect('list')

	context = {
		'form':form
	}
	return render(request, 'entry.html', context)

@login_required
def delete_invoice(request, pk):
	queryset = Invoice.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request, 'Successfully Deleted')
		return redirect('/list')
	return render(request, 'delete.html')
