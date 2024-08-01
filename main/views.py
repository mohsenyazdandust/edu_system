from django.shortcuts import redirect

from django.views.generic import CreateView, TemplateView, View, ListView, DeleteView, UpdateView

from django.contrib import messages
from django.contrib.auth import logout as auth_logout, login as auth_login
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy

from django.contrib.auth import get_user_model

# from braces.views import AnonymousRequiredMixin, LoginRequiredMixin, StaffuserRequiredMixin

from .forms import (
    CreateUserForm,
    CreateCollegeForm,
    CreateTermForm,
    CreateGroupForm,
    CreateCourseForm,
    CreateTeacherForm,
    CreateEntryForm,
    CreateTimingForm,
    CreateLocationForm,
)

from . import models

from .mixins import GetLinkInfoMixin

from django.shortcuts import render


User = get_user_model()

# CONFIGS

class LinkInfoView(View):
    def get(self, request, *args, **kwargs):
        active_term = request.GET.get('term', False)
        if active_term:
            if int(active_term) == 0:
                try:
                    del request.session['active_term']
                except:
                    pass
            else:
                request.session['active_term'] = active_term
        
        active_college = request.GET.get('college', False)
        if active_college:
            if int(active_college) == 0:
                try:
                    del request.session['active_college']
                except:
                    pass
            else:
                request.session['active_college'] = active_college
        
        return redirect(request.META.get('HTTP_REFERER'))
        

# AUTH

class LogInView(LoginView):
    redirect_authenticated_user = True
    template_name = "auth/login.html"
    
    def get_success_url(self):
        return reverse_lazy('main:dashboard') 
    

class LogOutView(View):
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return redirect(reverse_lazy("main:login"))
    

class ChangePasswordView(GetLinkInfoMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "auth/change-password.html", self.get_context_data(**kwargs))
    
    def post(self, request, *args, **kwargs):
        password1 = request.POST.get("password1", False)
        password2 = request.POST.get("password2", False)
        
        if (password1 and password1 == password2):
            request.user.set_password(password1)
            request.user.save()
            auth_login(request, request.user)
            return redirect(reverse_lazy("main:dashboard"))
        else:
            return redirect(reverse_lazy("main:changepassword"))


# DASHBOARD

class DashboardView(GetLinkInfoMixin, TemplateView):
    template_name = "dashboard.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["classes"] = len(models.Class.objects.all())
        context["classrooms"] = len(models.Classroom.objects.all())
        context["courses"] = len(models.Course.objects.all())
        context["entries"] = len(models.Entry.objects.all())
        context["teachers"] = len(models.Teacher.objects.all())
        context["groups"] = len(models.Group.objects.all())
        
        return context


# USERS

class UserListView(GetLinkInfoMixin, ListView):
    model = User
    context_object_name = "users"
    template_name = "users/index.html"


class CreateUserView(GetLinkInfoMixin, CreateView):
    model = User
    template_name = 'users/create.html'
    form_class = CreateUserForm
    
    def get_success_url(self):
        return reverse_lazy('main:users') 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = models.Group.objects.all()
        context['colleges'] = models.College.objects.all()
        return context
    

class DeleteUserView(GetLinkInfoMixin, DeleteView):
    model = User
    
    def get_success_url(self):
        return reverse_lazy('main:users') 
    

class UpdateUserView(GetLinkInfoMixin, UpdateView):
    model = User
    template_name = "users/create.html"
    form_class = CreateUserForm
    context_object_name = "cuser"
        
    def get_success_url(self):
        return reverse_lazy('main:users') 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = models.Group.objects.all()
        context['colleges'] = models.College.objects.all()
        return context
    
# COLLEGES

class CollegeListView(GetLinkInfoMixin, ListView):
    model = models.College
    context_object_name = "colleges"
    template_name = "colleges/index.html"


class CreateCollegeView(GetLinkInfoMixin, CreateView):
    model = models.College    
    template_name = 'colleges/create.html'
    form_class = CreateCollegeForm
    
    def get_success_url(self):
        return reverse_lazy('main:colleges') 
    

class DeleteCollegeView(GetLinkInfoMixin, DeleteView):
    model = models.College
    
    def get_success_url(self):
        return reverse_lazy('main:colleges') 
    

class UpdateCollegeView(GetLinkInfoMixin, UpdateView):
    model = models.College
    template_name = "colleges/create.html"
    form_class = CreateCollegeForm
    context_object_name = "college"
        
    def get_success_url(self):
        return reverse_lazy('main:colleges') 
    

# TERMS

class TermListView(GetLinkInfoMixin, ListView):
    model = models.Term
    context_object_name = "terms"
    template_name = "terms/index.html"


class CreateTermView(GetLinkInfoMixin, CreateView):
    model = models.Term    
    template_name = 'terms/create.html'
    form_class = CreateTermForm
    
    def get_success_url(self):
        return reverse_lazy('main:terms') 
    

class DeleteTermView(GetLinkInfoMixin, DeleteView):
    model = models.Term
    
    def get_success_url(self):
        return reverse_lazy('main:terms') 
    

class UpdateTermView(GetLinkInfoMixin, UpdateView):
    model = models.Term
    template_name = "terms/create.html"
    form_class = CreateTermForm
    context_object_name = "term"
        
    def get_success_url(self):
        return reverse_lazy('main:terms') 
    

# GROUPS

class GroupListView(GetLinkInfoMixin, ListView):
    model = models.Group
    context_object_name = "groups"
    template_name = "educational-groups/index.html"


class CreateGroupView(GetLinkInfoMixin, CreateView):
    model = models.Group    
    template_name = 'educational-groups/create.html'
    form_class = CreateGroupForm
    
    def get_success_url(self):
        return reverse_lazy('main:groups') 
    

class DeleteGroupView(GetLinkInfoMixin, DeleteView):
    model = models.Group
    
    def get_success_url(self):
        return reverse_lazy('main:groups') 
    

class UpdateGroupView(GetLinkInfoMixin, UpdateView):
    model = models.Group
    template_name = "educational-groups/create.html"
    form_class = CreateGroupForm
    context_object_name = "group"
        
    def get_success_url(self):
        return reverse_lazy('main:groups') 
    

# COURSES

class CourseListView(GetLinkInfoMixin, ListView):
    model = models.Course
    context_object_name = "courses"
    template_name = "lessons/index.html"


class CreateCourseView(GetLinkInfoMixin, CreateView):
    model = models.Course    
    template_name = 'lessons/create.html'
    form_class = CreateCourseForm
    
    def get_success_url(self):
        return reverse_lazy('main:courses') 
    

class DeleteCourseView(GetLinkInfoMixin, DeleteView):
    model = models.Course
    
    def get_success_url(self):
        return reverse_lazy('main:courses') 
    

class UpdateCourseView(GetLinkInfoMixin, UpdateView):
    model = models.Course
    template_name = "lessons/create.html"
    form_class = CreateCourseForm
    context_object_name = "course"
        
    def get_success_url(self):
        return reverse_lazy('main:courses') 

# COURSES

class TeacherListView(GetLinkInfoMixin, ListView):
    model = models.Teacher
    context_object_name = "teachers"
    template_name = "professors/index.html"


class CreateTeacherView(GetLinkInfoMixin, CreateView):
    model = models.Teacher    
    template_name = 'professors/create.html'
    form_class = CreateTeacherForm
    
    def get_success_url(self):
        return reverse_lazy('main:teachers') 
    

class DeleteTeacherView(GetLinkInfoMixin, DeleteView):
    model = models.Teacher
    
    def get_success_url(self):
        return reverse_lazy('main:teachers') 
    

class UpdateTeacherView(GetLinkInfoMixin, UpdateView):
    model = models.Teacher
    template_name = "professors/create.html"
    form_class = CreateTeacherForm
    context_object_name = "teacher"
        
    def get_success_url(self):
        return reverse_lazy('main:teachers') 
    
# ENTRY

class EntryListView(GetLinkInfoMixin, ListView):
    model = models.Entry
    context_object_name = "entries"
    template_name = "entries/index.html"


class CreateEntryView(GetLinkInfoMixin, CreateView):
    model = models.Entry    
    template_name = 'entries/create.html'
    form_class = CreateEntryForm
    
    def get_success_url(self):
        return reverse_lazy('main:entries') 
    

class DeleteEntryView(GetLinkInfoMixin, DeleteView):
    model = models.Entry
    
    def get_success_url(self):
        return reverse_lazy('main:entries') 
    

class UpdateEntryView(GetLinkInfoMixin, UpdateView):
    model = models.Entry
    template_name = "entries/create.html"
    form_class = CreateEntryForm
    context_object_name = "entry"
        
    def get_success_url(self):
        return reverse_lazy('main:entries') 


# TIMING

class TimingListView(GetLinkInfoMixin, ListView):
    model = models.Timing
    context_object_name = "times"
    template_name = "time-periods/index.html"


class CreateTimingView(GetLinkInfoMixin, CreateView):
    model = models.Timing    
    template_name = 'time-periods/create.html'
    form_class = CreateTimingForm
    
    def get_success_url(self):
        return reverse_lazy('main:times') 
    

class DeleteTimingView(GetLinkInfoMixin, DeleteView):
    model = models.Timing
    
    def get_success_url(self):
        return reverse_lazy('main:times') 
    

class UpdateTimingView(GetLinkInfoMixin, UpdateView):
    model = models.Timing
    template_name = "time-periods/create.html"
    form_class = CreateTimingForm
    context_object_name = "time"
        
    def get_success_url(self):
        return reverse_lazy('main:times') 

# CLASSES

class CreateClassView(GetLinkInfoMixin, View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["times"] = models.Timing.objects.all()
        context["teachers"] = models.Teacher.objects.all()
        context["groups"] = models.Group.objects.all()
        context["courses"] = models.Course.objects.all()
        context["entries"] = models.Entry.objects.all()
        return context
    
    def get(self, request, *args, **kwargs):
        return render(request, 'classrooms/create.html', self.get_context_data(**kwargs))
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        linked_term=context['active_info']['term']
        linked_college=context['active_info']['college']
        
        for i in range(5):
            for time in context['times']:
                new_class = models.Class(
                    day=i,
                    time=time,
                    course_id=request.POST.get(f'course[{i}-{time.id}]'),
                    teacher_id=request.POST.get(f'teacher[{i}-{time.id}]'),
                    stat=request.POST.get(f'stat[{i}-{time.id}]'),
                    group_id=request.POST.get(f'group[{i}-{time.id}]'),
                    entry_id=request.POST.get(f'entry[{i}-{time.id}]'),
                )
                if linked_term:
                    new_class.linked_term = linked_term
                    
                if linked_college:
                    new_class.linked_college = linked_college

                try:
                    new_class.save()
                except:
                    pass
                
        return redirect(reverse_lazy("main:classes"))

class ClassListView(GetLinkInfoMixin, View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["times"] = models.Timing.objects.all()
        context["teachers"] = models.Teacher.objects.all()
        context["groups"] = models.Group.objects.all()
        context["courses"] = models.Course.objects.all()
        context["entries"] = models.Entry.objects.all()
        classes = models.Class.objects.all()
        if context['active_info']['term'] and context['active_info']['college']:
            context['classes'] = classes.filter(linked_term=context['active_info']['term']).filter(linked_college=context['active_info']['college'])
        else:
            context['classes'] = False

        return context
    
    def get(self, request, *args, **kwargs):
        return render(request, 'classrooms/index.html', self.get_context_data(**kwargs))
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        linked_term = context['active_info']['term']
        linked_college = context['active_info']['college']

        for i in range(5):
            for time in context['times']:
                try:
                    old_class = models.Class.objects.get(
                        day=i,
                        time=time,
                        linked_term=linked_term,
                        linked_college=linked_college,
                    )
                    old_class.course_id = request.POST.get(f'course[{i}-{time.id}]')
                    old_class.teacher_id = request.POST.get(f'teacher[{i}-{time.id}]')
                    old_class.stat = request.POST.get(f'stat[{i}-{time.id}]')
                    old_class.group_id = request.POST.get(f'group[{i}-{time.id}]')
                    old_class.entry_id = request.POST.get(f'entry[{i}-{time.id}]')
                    old_class.save()
                except:
                    pass
                
        return redirect(reverse_lazy('main:classes'))
    

class DeleteClassView(GetLinkInfoMixin, DeleteView):
    model = models.Class
    
    def get_success_url(self):
        return reverse_lazy('main:classes') 
    

# LOCATION

class LocationListView(GetLinkInfoMixin, ListView):
    model = models.Location
    context_object_name = "locations"
    template_name = "locations/index.html"


class CreateLocationView(GetLinkInfoMixin, CreateView):
    model = models.Location    
    template_name = 'locations/create.html'
    form_class = CreateLocationForm
    
    def get_success_url(self):
        return reverse_lazy('main:locations') 
    

class DeleteLocationView(GetLinkInfoMixin, DeleteView):
    model = models.Location
    
    def get_success_url(self):
        return reverse_lazy('main:locations') 
    

class UpdateLocationView(GetLinkInfoMixin, UpdateView):
    model = models.Location
    template_name = "locations/create.html"
    form_class = CreateLocationForm
    context_object_name = "location"
        
    def get_success_url(self):
        return reverse_lazy('main:locations') 


class DetermineClassLocationView(GetLinkInfoMixin, View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["times"] = models.Timing.objects.all()
        context["teachers"] = models.Teacher.objects.all()
        context["groups"] = models.Group.objects.all()
        context["courses"] = models.Course.objects.all()
        context["entries"] = models.Entry.objects.all()
        classes = models.Class.objects.all()
        if context['active_info']['term'] and context['active_info']['college']:
            context['classes'] = classes.filter(linked_term=context['active_info']['term']).filter(linked_college=context['active_info']['college'])
        else:
            context['classes'] = False
        context['locations'] = models.Location.objects.all()
        return context
    
    def get(self, request, *args, **kwargs):
        return render(request, 'locations/determine.html', self.get_context_data(**kwargs))
    
    def post(self, request, *args, **kwargs):
        for class_str in request.POST.keys():
            try:
                class_id = class_str.split("-")[-1]
                class_id = int(class_id)
                the_class = models.Class.objects.get(id=class_id)
                
                location_id = request.POST.get(class_str)
                if location_id == '':
                    the_class.location = None
                else:
                    the_class.location_id = int(location_id)
                the_class.save()
            except:
                pass
        return redirect(reverse_lazy('main:determine_location'))
        
