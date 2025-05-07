from django.contrib import admin
from blog.models import Blog,Author
from .models import Student, Course, Enrollment

admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Course)