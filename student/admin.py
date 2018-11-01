from django.contrib import admin
from student.models import Students
from student.models import Marks
from student.models import Depart

# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
	list_display = ('USN', 'Name','Department','Email', 'Phone')
	search_fields = ['USN', 'Name','Email','Phone','Department']


class MarksAdmin(admin.ModelAdmin):
	list_display = ('USN', 'MAT', 'CHE', 'PCD','CED','ELN', 'CIV')
	search_fields = ['USN__USN']


class DepartAdmin(admin.ModelAdmin):
	list_display = ('DCode','DName')


admin.site.register(Students,StudentsAdmin)
admin.site.register(Marks,MarksAdmin)
admin.site.register(Depart,DepartAdmin)
admin.site.site_header = 'MarkX Admin Panel'