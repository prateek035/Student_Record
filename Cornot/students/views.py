

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator


from .models import School, Book, Student

def student_list(request):
	students = Student.objects.all()

	paginator = Paginator(students, 4)
	
	page = request.GET.get('page')

	students = paginator.get_page(page)


	return render(request, "students/student_list.html", 
		         {'students':students})


def student_detail(request, sid):
	student = Student.objects.get(sid = sid)
	return render(request, 'students/detail.html',
		{'student':student})
	

def search(request): 
	query = request.GET.get('q')
	print('coming')
	print(query)
	if query != None:
		request.session['query'] = query


	students = Student.objects.filter(Q(fname__contains = request.session['query'])| 
		                              Q(lname__contains = request.session['query']))
	
	paginator = Paginator(students, 4)
	page = request.GET.get('page')
	students = paginator.get_page(page)

	return render(request, 'students/student_list.html', 
		   {'students':students})
