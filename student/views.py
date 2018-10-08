from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from .models import Students, Marks

# Create your views here.

def results(request):
	if request.method=='POST':
		srch = request.POST['srh']

		if srch:
			match = Students.objects.filter(Q(USN__icontains=srch))
			#matchm = Marks.objects.filter(Q(USN__icontains=srch))
			if match:
				return render(request,'results.html',{'sr':match})
			else:
				messages.error(request,'no result found')
		else:
			return HttpResponseRedirect(reverse('results'))

	return render(request, 'results.html')


