from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.home,name='home'),
    path('register/',views.register,name='register'),
    path('',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
    path('author_list/',views.author_list,name="list_author"),
    path('author_create/',views.author_create,name="author_create"),
    path('author_delete/<int:pk>',views.author_delete,name="author_delete"),
    path('author_update/<int:pk>',views.author_update,name="author_update"),
    path('book_list/',views.book_list,name="book_list"),
    path('add_student',views.add_student,name="add_student"),
    path('student_list/',views.student_list,name="student_list"),
    path('add_course',views.add_course,name="add_course"),
    path('course_list/',views.course_list,name="course_list"),
    path('send_message/',views.send_message,name="send_message")
]
