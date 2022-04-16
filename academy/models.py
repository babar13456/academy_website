from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Add_teacher(models.Model):
	select_img = models.ImageField(upload_to='teacher_images', null=True, blank = True)
	teacher_name=models.CharField(max_length=120)
	teacher_skill=models.CharField(max_length=120)
	teacher_desc=models.TextField()
	twitter=models.CharField(max_length=2000, null=True, blank=True)
	facebook=models.CharField(max_length=2000, null=True, blank=True)
	instagram=models.CharField(max_length=2000, null=True, blank=True)

	def __str__(self):
		return self.teacher_name


class Add_course(models.Model):
	category_list = (
		('Web Development', 'Web Development'),
		('Digital Marketting', 'Digital Marketing'),
		('Word Press', 'Word Press'),
		('Amazon', 'Amazon'),
		('Programming', 'Programming'),
		('Diploma', 'Diploma'),
		('Short Course', 'Short Course'),
		)
	select_img = models.ImageField(upload_to='courses_images', null=True, blank=True)
	select_category = models.CharField(max_length=20, choices=category_list)
	price = models.IntegerField(null=True, blank=True)
	course_name = models.CharField(max_length=120)
	course_desc=models.TextField()
	select_teacher=models.ForeignKey(Add_teacher, on_delete=models.CASCADE)
	seats = models.IntegerField(default=40, null=True, blank=True)
	start = models.TimeField(null=True, blank=True)
	end = models.TimeField(null=True, blank=True)

	def snippet(self):
		return self.course_desc[:150] + "..."

	def __str__(self):
		return self.course_name


class Apply_course(models.Model):
	gender = (
		('Male', 'Male'),
		('Female', 'Female'),
		('Other', 'Other')
	)
	domicile = (
		('Mohmand', 'Mohmand'),
		('Peshawar', 'Peshawar'),
		('Charsadda', 'Charsadda'),
	)
	qualification = (
		('Matriculation', 'Matriculation'),
		('FSC', 'FSC'),
		('Bachelor', 'Bachelor'),
		('Master', 'Master'),
	)
	select_user = models.ForeignKey(User, on_delete=models.CASCADE)
	father_name = models.CharField(max_length=40, null=True, blank=True)
	birth_date = models.DateField()
	select_img = models.ImageField(upload_to='media/profile')
	select_gender = models.CharField(max_length=10, choices=gender)
	select_domicile = models.CharField(max_length=10, choices=domicile)
	mobile_no = models.IntegerField(null=True, blank=True)
	cnic = models.IntegerField(null=True, blank=True)
	guardian_no = models.IntegerField(null=True, blank=True)
	select_qualification = models.CharField(max_length=20, choices=qualification)
	select_course = models.ForeignKey(Add_course, on_delete=models.CASCADE)
	date = models.DateField(auto_now_add=True)
	matric_dmc = models.FileField(upload_to='media/documents', null=True, blank=True)
	fsc_dmc = models.FileField(upload_to='media/documents', null=True, blank=True)
	cnic_front = models.ImageField(upload_to='media/documents', null=True, blank=True)
	cnic_back = models.ImageField(upload_to='media/documents', null=True, blank=True)
	Address = models.TextField()

	def __str__(self):
		return self.select_user.first_name
