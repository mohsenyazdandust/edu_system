from django.db import models

from django_jalali.db import models as jmodels


from django.contrib.auth.models import AbstractUser


class Linker(models.Model):
    linked_term = models.ForeignKey('main.Term', on_delete=models.SET_NULL, null=True, blank=True)
    linked_college = models.ForeignKey('main.College', on_delete=models.SET_NULL, null=True, blank=True)

    
    class Meta:
        abstract = True


class CUser(AbstractUser):
    access_level = models.IntegerField(default=0)
    cgroup = models.ForeignKey('main.Group', on_delete=models.SET_NULL, null=True, blank=True)
    college = models.ForeignKey('main.College', on_delete=models.SET_NULL, null=True, blank=True)

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    
    
class College(models.Model):
    title = models.CharField(max_length=100)
    

class Term(models.Model):
    title = models.CharField(max_length=100)


class Group(models.Model):
    title = models.CharField(max_length=100)
    short = models.CharField(max_length=10)
    
    
class Classroom(models.Model):
    number = models.CharField(max_length=10)
    

class Class(Linker):
    time = models.ForeignKey('main.Timing', on_delete=models.SET_NULL, null=True, blank=True)
    day = models.IntegerField(default=0)
    course = models.ForeignKey('main.Course', on_delete=models.SET_NULL, null=True, blank=True)
    teacher = models.ForeignKey('main.Teacher', on_delete=models.SET_NULL, null=True, blank=True)
    stat = models.IntegerField(default=0)
    group = models.ForeignKey('main.Group', on_delete=models.SET_NULL, null=True, blank=True)
    entry = models.ForeignKey('main.Entry', on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey('main.Location', on_delete=models.SET_NULL, null=True, blank=True)

class Entry(models.Model):
    title = models.CharField(max_length=100)
    

class Timing(models.Model):
    title = models.CharField(max_length=100)
    

class Location(models.Model):
    title = models.CharField(max_length=100)
    
    
class PandA(models.Model):
    theclass = models.ForeignKey('main.Class', on_delete=models.SET_NULL, null=True, blank=True)
    date = jmodels.jDateField()
    stat = models.IntegerField(default=0)