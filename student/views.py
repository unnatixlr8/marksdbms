from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages
from django.db.models import Q, F, Sum
from .models import Students, Marks
from django.core.serializers import serialize

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

				return render(request,'results.html',{'sr':match, 'mr':matchm, 'per':per,'tot':tot})
			else:
				messages.error(request,'No result found')
		else:
			return HttpResponseRedirect(reverse('results'))

	return render(request, 'results.html')

def about(request):
	return render(request,'about.html')


def printJSON(request):
	if request.method=='GET':
		json_data = request.GET['json_data']
		if json_data:
			print(json_data)
			query1 = Students.objects.filter(Q(USN__iexact=json_data))
			query2 = Marks.objects.filter(Q(USN__USN__iexact=json_data))
			json_student = serialize('json', query1)
			json_student = json_student + serialize('json',query2)

			print(json_student)
			response = JsonResponse(json_student,safe=False,content_type='application/json')
			response['Content-Disposition'] = 'attachment; filename=%s.json' %json_data
	return response


