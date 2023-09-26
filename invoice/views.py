from django.shortcuts import render
from .forms import InvoiceForm


# Create your views here.
def home(request):
	title = 'Welcome: This is the Home Page'
	context = {
	"title": title,
	}
	return render(request, "home.html",context)

def add_invoice(request):
	form = InvoiceForm(request.POST or None)
	if form.is_valid():
		form.save()
	context = {
		"form": form,
		"title": "New Invoice",
	}
	return render(request, "entry.html", context)