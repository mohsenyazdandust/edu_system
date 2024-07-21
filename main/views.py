import datetime

from django.db.models import Sum
from django.shortcuts import redirect

from django.views.generic import CreateView, TemplateView, View, ListView, DeleteView, UpdateView

from django.contrib import messages
from django.contrib.auth import logout as auth_logout, login as auth_login
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

# from braces.views import AnonymousRequiredMixin, LoginRequiredMixin, StaffuserRequiredMixin

# from hub.models import Download, Source

from .forms import CreateUserForm
from . import models



from django.shortcuts import render
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


User = get_user_model()

class LogInView(LoginView):
    redirect_authenticated_user = True
    template_name = "auth/login.html"
    
    def get_success_url(self):
        return reverse_lazy('main:dashboard') 
    

class LogOutView(View):
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return redirect(reverse_lazy("main:login"))
    

class ChangePasswordView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "auth/change-password.html")
    
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

class DashboardView(TemplateView):
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
    


class UserListView(ListView):
    model = User
    context_object_name = "users"
    template_name = "users/index.html"


class CreateUserView(CreateView):
    model = User    
    template_name = 'users/create.html'
    form_class = CreateUserForm
    
    def get_success_url(self):
        return reverse_lazy('main:users') 
    

class DeleteUserView(DeleteView):
    model = User
    
    def get_success_url(self):
        return reverse_lazy('main:users') 
    

class UpdateUserView(UpdateView):
    model = User
    template_name = "users/create.html"
    form_class = CreateUserForm
    context_object_name = "cuser"
        
    def get_success_url(self):
        return reverse_lazy('main:users') 
    
    
    