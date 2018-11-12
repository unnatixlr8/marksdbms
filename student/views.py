from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages
from django.db.models import Q, F, Sum
from .models import Students, Marks
from django.core.serializers import serialize
from django.core import serializers
from django.conf import settings
import json, urllib.request, urllib.parse, ssl
from django.core.serializers.json import DjangoJSONEncoder

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
			#print(json_data)
			query1 = Students.objects.filter(Q(USN__iexact=json_data)).values('USN','Name','Department','Email','Phone')
			query2 = Marks.objects.filter(Q(USN__USN__iexact=json_data)).values('MAT','CHE','PCD','CED','ELN','CIV')
			#json_student = serialize('json', query1)
			#json_student = json_student + serialize('json',query2)
			json_student = json.dumps(list(query1), cls=DjangoJSONEncoder)
			json_student = json_student + json.dumps(list(query2), cls=DjangoJSONEncoder)
			#print(json_student)
			response = JsonResponse(json_student,safe=False,content_type='application/json')
			response['Content-Disposition'] = 'attachment; filename=%s.json' %json_data
	return response


def sendSMS(request):
	if request.method=='POST':
		phone = request.POST['phone']
		json_data = request.POST['json_data']
		if phone and json_data:
			print("'"+phone+"'")
			#print(json_data)
			#print("'"+settings.TEXTLOCAL_API+"'")
			marks = Marks.objects.filter(Q(USN__USN__iexact=json_data)).values('USN','MAT','CHE','PCD','CED','ELN','CIV')
			#marks = serialize('json', marks) "'" + term + "'"
			#marks = serializers.serialize('json', marks, fields=('USN','MAT','CHE','PCD','ELN','CIV'))
			marks = json.dumps(list(marks), cls=DjangoJSONEncoder)
			marksStr = json.loads(marks)
			print(marks)
			marksData = str("USN: " + str(marksStr[0]['USN']) + "\nMAT: " + str(marksStr[0]['MAT'])+ "\nCHE: "+ str(marksStr[0]['CHE'])+"\nPCD: "+ str(marksStr[0]['PCD'])+ "\nCED: "+ str(marksStr[0]['CED'])+ "\nELN: "+ str(marksStr[0]['ELN'])+ "\nCIV: "+ str(marksStr[0]['CIV']))
			print(marksData)
			#resp = actualSendSMS('2AQn1u6DJg4-ampt4ZBau1xgve3MOYe4Vb6zRpzMx1','8873333559','hello unnati','TXTLCL')
			resp = actualSendSMS(settings.TEXTLOCAL_API,"'"+phone+"'",marksData,'TXTLCL')
			print (resp)
			json_print = json.loads(resp.decode())
	#return HttpResponse(status=204)
	#return render(request,'results.html',{'smsResp': json_print})
	return JsonResponse(json_print,safe=False,content_type='application/json')


def actualSendSMS(apikey, numbers, message, sender):
	data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers, 'message' : message, 'sender': sender})
	data = data.encode('utf-8')
	context = ssl._create_unverified_context()
	request = urllib.request.Request("https://api.textlocal.in/send/?")
	f = urllib.request.urlopen(request, data, context=context)
	fr = f.read()
	return (fr)
