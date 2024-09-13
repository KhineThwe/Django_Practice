from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home,name='home'),
    path('author_list/',views.author_list,name="list_author"),
    path('author_create/',views.author_create,name="author_create"),
    path('author_delete/<int:id>',views.author_delete,name="author_delete"),
    path('author_update/<int:id>',views.author_update,name="author_update"),
    path('book_list/',views.book_list,name="book_list"),
    path('student_list/',views.student_list,name="student_list"),
    path('course_list/',views.course_list,name="course_list")
]
