from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
	name = "Unnati Gupta"
	numbers = [1,5,6]
	args = {"Name": name, "Numbers":numbers}
	return render(request, 'accounts/login.html',args)