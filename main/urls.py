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
    path('terms/', TermListView.as_view(), name="terms"),
    path('terms/add/', CreateTermView.as_view(), name="add_term"),
    path('terms/delete/<int:pk>/', DeleteTermView.as_view(), name="delete_term"),
    path('terms/update/<int:pk>/', UpdateTermView.as_view(), name="update_term"),
    # GROUPS
    path('groups/', GroupListView.as_view(), name="groups"),
    path('groups/add/', CreateGroupView.as_view(), name="add_group"),
    path('groups/delete/<int:pk>/', DeleteGroupView.as_view(), name="delete_group"),
    path('groups/update/<int:pk>/', UpdateGroupView.as_view(), name="update_group"),
    # COURSES
    path('courses/', CourseListView.as_view(), name="courses"),
    path('courses/add/', CreateCourseView.as_view(), name="add_course"),
    path('courses/delete/<int:pk>/', DeleteCourseView.as_view(), name="delete_course"),
    path('courses/update/<int:pk>/', UpdateCourseView.as_view(), name="update_course"),
    # TEACHERS
    path('teachers/', TeacherListView.as_view(), name="teachers"),
    path('teachers/add/', CreateTeacherView.as_view(), name="add_teacher"),
    path('teachers/delete/<int:pk>/', DeleteTeacherView.as_view(), name="delete_teacher"),
    path('teachers/update/<int:pk>/', UpdateTeacherView.as_view(), name="update_teacher"),
    # ENTRIES
    path('entries/', EntryListView.as_view(), name="entries"),
    path('entries/add/', CreateEntryView.as_view(), name="add_entry"),
    path('entries/delete/<int:pk>/', DeleteEntryView.as_view(), name="delete_entry"),
    path('entries/update/<int:pk>/', UpdateEntryView.as_view(), name="update_entry"),
    # TIMING
    path('times/', TimingListView.as_view(), name="times"),
    path('times/add/', CreateTimingView.as_view(), name="add_time"),
    path('times/delete/<int:pk>/', DeleteTimingView.as_view(), name="delete_time"),
    path('times/update/<int:pk>/', UpdateTimingView.as_view(), name="update_time"),
    # CLASSES
    path('classes/', ClassListView.as_view(), name="classes"),
    path('classes/add/', CreateClassView.as_view(), name="add_class"),
    path('classes/delete/<int:pk>/', DeleteClassView.as_view(), name="delete_class"),
    # TIMING
    path('locations/', LocationListView.as_view(), name="locations"),
    path('locations/add/', CreateLocationView.as_view(), name="add_location"),
    path('locations/delete/<int:pk>/', DeleteLocationView.as_view(), name="delete_location"),
    path('locations/update/<int:pk>/', UpdateLocationView.as_view(), name="update_location"),
    path('locations/determine/', DetermineClassLocationView.as_view(), name="determine_location"),
    # SCHEDULE
    path('location/', ScheduleListView.as_view(), name="schedule"),
    # PandA
    path('presence/', SubmitPandAView.as_view(), name="p_and_a"),
    path('presence/log/', PandAListView.as_view(), name="logs_p_and_a"),
    
]
