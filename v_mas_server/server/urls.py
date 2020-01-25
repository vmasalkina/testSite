from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from server.views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html', success_url='statistics'), name='password_change'),
    path('create_user/', create_user, name='create_user'),
    path('statistics/', statistics, name='statistics'),
    path('users/', users, name='users'),
#    path(r'^(?P<user_id>\d{,5})/changepassword/$', changepassword, name='changepassword'),
#    #GET
#    path(r'^(?P<user_id>\d{,5})/article_list/$', article_list),
#    path(r'^(?P<user_id>\d{,5})/article_by_days/(?P<article_id>\d{,5})/(?P<year>\d{4})/(?P<month>\d{1,2})/$', article_by_days),
#    path(r'^(?P<user_id>\d{,5})/article_by_months/(?P<article_id>\d{,5})/(?P<year>\d{4})/$', article_by_months),
#    path(r'^(?P<user_id>\d{,5})/day/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', day_by_articles),
#    path(r'^(?P<user_id>\d{,5})/month_by_articles/(?P<year>\d{4})/(?P<month>\d{1,2})/$', month_by_articles),
#    path(r'^(?P<user_id>\d{,5})/month_by_days/(?P<year>\d{4})/(?P<month>\d{1,2})/$', month_by_days),
#    path(r'^(?P<user_id>\d{,5})/year_by_articles/(?P<year>\d{4})/$', year_by_articles),
#    path(r'^(?P<user_id>\d{,5})/year_by_months/(?P<year>\d{4})/$', year_by_months),
#    path(r'^(?P<user_id>\d{,5})/detail/(?P<article_id>\d{,5})/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', detail_article),
#    #POST
#    path(r'^(?P<user_id>\d{,5})/create_expense/$', create_expense),
#    path(r'^(?P<user_id>\d{,5})/update_expense/$', update_expense),
#    path(r'^(?P<user_id>\d{,5})/delete_expense/$', delete_expense),
#    path(r'^(?P<user_id>\d{,5})/create_article/$', create_article),
#    path(r'^(?P<user_id>\d{,5})/update_article/$', update_article),
#    path(r'^(?P<user_id>\d{,5})/delete_article/$', delete_article),
]
