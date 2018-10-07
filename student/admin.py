from django.contrib import admin
from student.models import Students
from student.models import Marks

# Register your models here.
admin.site.register(Students)
admin.site.register(Marks)