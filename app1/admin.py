from django.contrib import admin
from app1.models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','sno','sname','marks']
admin.site.register(Student,StudentAdmin)


