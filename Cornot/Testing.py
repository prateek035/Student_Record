# from students.models import Student, Book, School


name = open('../../Problem-Statement/dummy_data.csv')
for n in name:
	list_ = n.split(",")
	print(type(list_[0]))
	book = Book.objects.create(title=list[6])
	school = School.objects.create(sname=list[5])
	student = Student.objects.create(sid=int(list[0]), fname=list[1], lname=list[2], email=list[3], gender=list[4], school=school)
	student.add(book)
	student.save()