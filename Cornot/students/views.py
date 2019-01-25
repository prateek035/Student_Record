

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render




from .models import School, Book, Student

def student_list(request):
	students = Student.objects.all()

	return render(request, "students/student_list.html", 
		         {'students':students})


def student_detail(request, sid):
	student = Student.objects.get(sid = sid)
	return render(request, 'students/detail.html',
		{'student':student})
	

def search(request):
	template = 'students/student_list.html'
	query = request.GET.get('q')


	try:
		students = Student.objects.filter(Q(sid= int(query)))
		return render(request, template, {'students':students})
	except:
		pass

	students = Student.objects.filter(Q(fname__contains = query))

	return render(request, template, {'students':students})
