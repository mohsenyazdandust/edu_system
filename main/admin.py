from django.contrib import admin

from .models import CUser, Class, PandA, Course, Teacher

admin.site.register(CUser)
admin.site.register(Class)
admin.site.register(PandA)
admin.site.register(Course)
admin.site.register(Teacher)
