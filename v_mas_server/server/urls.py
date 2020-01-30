from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from server.views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create_user/', create_user, name='create_user'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('statistics/', statistics, name='statistics'),
    path('users/', users, name='users'),
    path('user_password_change/<int:user_id>/', user_password_change, name='user_password_change'),
]
