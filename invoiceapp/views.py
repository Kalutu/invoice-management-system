from django.shortcuts import render

def home(request):
	title = 'Invoice Management System'
	context = {
	"title": title,
	}
	return render(request, "home.html",context)