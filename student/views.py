from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q, F, Sum
from .models import Students, Marks

# Create your views here.

def results(request):
	if request.method=='POST':
		srch = request.POST['srh']

		if srch:
			match = Students.objects.filter(Q(USN__iexact=srch))
			matchm = Marks.objects.filter(Q(USN__USN__iexact=srch))
			

			if match and matchm:
				total = Marks.objects.filter(Q(USN__USN__iexact=srch)).annotate(totalMarks=Sum(F('MAT')+ F('CHE')+F('PCD')+F('CED')+F('ELN')+F('CIV')))
				for i in total:
					tot = i.totalMarks
					per = i.totalMarks / 600.00 * 100
					per = (round(per,2))

				return render(request,'results.html',{'sr':match, 'mr':matchm,'tr':total,'per':per,'tot':tot})
			else:
				messages.error(request,'No result found')
		else:
			return HttpResponseRedirect(reverse('results'))

	return render(request, 'results.html')

def about(request):
	return render(request,'about.html')


