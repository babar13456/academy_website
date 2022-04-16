from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('courses/', views.courses, name='courses'),
    path('teacher/', views.teacher, name='teacher'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('single_course/<str:pk>/', views.single_course, name='single_course'),
    path('register_save/', views.register_save, name="register_save"),
    path('sign_in_access/', views.sign_in_access, name='sign_in_access'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('course_apply/', views.course_apply, name='course_apply'),
    path('view_courses/', views.view_courses, name='view_courses'),

    path('single_course_apply/<str:pk>/', views.single_course_apply, name='single_course_apply'),
]
