from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Add_course, Add_teacher, Apply_course
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import ApplyForm

# Create your views here.

def index_page(request):
	all_users = User.objects.count()
	all_teachers = Add_teacher.objects.all()[:3]
	all_courses = Add_course.objects.all()[:3]
	for i in all_courses:
		print("Teacher :", i.select_teacher.select_img)
	courses_count = Add_course.objects.count()
	teachers_count = Add_teacher.objects.count()
	print(teachers_count)
	context = {'all_teachers': all_teachers, 'all_courses': all_courses, 
				'courses_count': courses_count, 'teachers_count': teachers_count, 
					'all_users': all_users}
	return render(request, "academy/index.html", context)

def courses(request):
	all_courses = Add_course.objects.all()
	context = {'all_courses': all_courses}
	return render(request, "academy/courses.html", context)

def single_course(request, pk):
	get_id = Add_course.objects.get(id=pk)
	context = {'get_id': get_id}
	return render(request, 'academy/course-details.html', context)

def teacher(request):
	all_teachers = Add_teacher.objects.all()
	context = {'all_teachers': all_teachers}
	return render(request, 'academy/teachers.html', context)

def contact(request):
	return render(request, 'academy/contact.html')


# ==========================================================================
# ============================ Register Users ==============================
# ==========================================================================

def register(request):
	return render(request, 'academy/register.html')

def register_save(request):
	context = {}
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		if password1 == password2:
			if User.objects.filter(username=username).exists():
				messages.error(request, 'Username Already Taken Try Another One')
				context['first_name'] = first_name
				context['last_name'] = last_name
				context['username'] = username
				context['email'] = email
				print(context)
				return render(request, 'academy/register.html', context)
			elif User.objects.filter(email=email).exists():
				messages.error(request, "Email Already Exists")
				context['first_name'] = first_name
				context['last_name'] = last_name
				context['username'] = username
				context['email'] = email
				return render(request, 'academy/register.html', context)
			else:
				usr = User.objects.create_user(username, email, password1)
				usr.first_name = first_name
				usr.last_name = last_name
				usr.username = username
				usr.email = email
				usr.password1 = password1
				usr.save()
				messages.success(request, "User Created Successfully")
				return redirect('/sign_in/')
		else:
			messages.error(request, "Password didn't Match")
			context['first_name'] = first_name
			context['last_name'] = last_name
			context['username'] = username
			context['email'] = email
			return render(request, 'academy/register.html', context)
	return redirect(request, 'academy/register.html', context)


def sign_in(request):
	return render(request, 'academy/sign_in.html')

def sign_in_access(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			if user.is_superuser:
				return redirect('/admin/')
			else:
				return redirect('/user_dashboard/')
		else:
			return HttpResponse("Not a Valid User")
	return HttpResponse("Access Function Called...")

def user_dashboard(request):
	return render(request, 'academy/user_dashboard.html')

def view_courses(request):
	data = Apply_course.objects.filter(select_user__id=request.user.id)
	context = {'data': data}
	return render(request, 'academy/view_courses.html', context)

def single_course_apply(request, pk):
	single = Apply_course.objects.get(id=pk)
	data = Apply_course.objects.filter(select_user__id=request.user.id)
	context = {'data': data, 'single': single}
	for i in data:
		print(i.select_img)
	return render(request, 'academy/single_course.html')

def course_apply(request):
	form = ApplyForm()
	context = {'form': form}
	ch = Apply_course.objects.filter(select_user__id=request.user.id)
	if len(ch) > 0:
		data = Apply_course.objects.filter(select_user__id=request.user.id)
		context['data'] = data
	data = Apply_course.objects.filter(select_user__id=request.user.id)
	if request.method == 'POST':
		form = ApplyForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.save(commit=False)
			login_user = User.objects.get(username=request.user.username)
			data.select_user = login_user
			data.save()
			messages.success(request, "Your Application submitted Successfully...")
			return redirect('/user_dashboard/')
		else:
			return HttpResponse("Something Wrong in your Form")
	return render(request, 'academy/course_apply.html', context)

def logout_user(request):
	auth.logout(request)
	return redirect('/sign_in/')