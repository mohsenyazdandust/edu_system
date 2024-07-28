from django.urls import path

from .views import *


urlpatterns = [
    # CONFIGS
    path('link/', LinkInfoView.as_view(), name='link_info'),
    # AUTH
    path('', LogInView.as_view(), name="login"),
    path('logout/', LogOutView.as_view(), name="logout"),
    path('changepassword/', ChangePasswordView.as_view(), name="changepassword"),
    # DASHBOARD
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    # USERS
    path('users/', UserListView.as_view(), name="users"),
    path('users/add/', CreateUserView.as_view(), name="add_user"),
    path('users/delete/<int:pk>/', DeleteUserView.as_view(), name="delete_user"),
    path('users/update/<int:pk>/', UpdateUserView.as_view(), name="update_user"),
    # COLLEGES
    path('colleges/', CollegeListView.as_view(), name="colleges"),
    path('colleges/add/', CreateCollegeView.as_view(), name="add_college"),
    path('colleges/delete/<int:pk>/', DeleteCollegeView.as_view(), name="delete_college"),
    path('colleges/update/<int:pk>/', UpdateCollegeView.as_view(), name="update_college"),
    # TERMS
    path('terms/', CollegeTermView.as_view(), name="terms"),
    path('terms/add/', CreateTermView.as_view(), name="add_term"),
    path('terms/delete/<int:pk>/', DeleteTermView.as_view(), name="delete_term"),
    path('terms/update/<int:pk>/', UpdateTermView.as_view(), name="update_term"),
    # GROUPS
    path('groups/', CollegeGroupView.as_view(), name="groups"),
    path('groups/add/', CreateGroupView.as_view(), name="add_group"),
    path('groups/delete/<int:pk>/', DeleteGroupView.as_view(), name="delete_group"),
    path('groups/update/<int:pk>/', UpdateGroupView.as_view(), name="update_group"),
    # COURSES
    path('courses/', CollegeCourseView.as_view(), name="courses"),
    path('courses/add/', CreateCourseView.as_view(), name="add_course"),
    path('courses/delete/<int:pk>/', DeleteCourseView.as_view(), name="delete_course"),
    path('courses/update/<int:pk>/', UpdateCourseView.as_view(), name="update_course"),
    # TEACHERS
    path('teachers/', CollegeTeacherView.as_view(), name="teachers"),
    path('teachers/add/', CreateTeacherView.as_view(), name="add_teacher"),
    path('teachers/delete/<int:pk>/', DeleteTeacherView.as_view(), name="delete_teacher"),
    path('teachers/update/<int:pk>/', UpdateTeacherView.as_view(), name="update_teacher"),
]
