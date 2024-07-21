from django.urls import path

from . views import *


urlpatterns = [
    path('login/', LogInView.as_view(), name="login"),
    path('logout/', LogOutView.as_view(), name="logout"),
    path('changepassword/', ChangePasswordView.as_view(), name="changepassword"),
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    path('users/', UserListView.as_view(), name="users"),
    path('users/add/', CreateUserView.as_view(), name="add_user"),
    path('users/delete/<int:pk>/', DeleteUserView.as_view(), name="delete_user"),
    path('users/update/<int:pk>/', UpdateUserView.as_view(), name="update_user"),
]
