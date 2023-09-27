from django.shortcuts import render, redirect
from .forms import *
from .models import Invoice
from django.contrib import messages

# Create your views here.
def home(request):
	title = 'Welcome: This is the Home Page'
	context = {
	"title": title,
	}
	return render(request, "home.html",context)

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
	return render(request, "list.html", context)

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

def delete_invoice(request, pk):
	queryset = Invoice.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request, 'Successfully Deleted')
		return redirect('/list')
	return render(request, 'delete.html')
