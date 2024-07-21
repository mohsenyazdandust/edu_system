from django.urls import path

from . views import *


urlpatterns = [
    # AUTH
    path('login/', LogInView.as_view(), name="login"),
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
]
