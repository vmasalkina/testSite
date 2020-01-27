from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm, AdminPasswordChangeForm
from django.contrib.auth.models import User
from django.template.response import TemplateResponse
from django.views.decorators.http import require_GET, require_POST
from server.models import Data

@login_required
def statistics(request):
    user = request.user
    d = Data.objects.filter(user=user)
    data = {i.timestamp.timestamp(): i.value for i in d}
    #data[i['timestamp'].strftime('%d.%m.%Y %H:%M')]
    return JsonResponse(data)

def is_superuser(user):
    return user.is_superuser

@require_GET
@login_required
@user_passes_test(is_superuser, login_url='statistics')
def users(request):
    users = User.objects.all()
    return TemplateResponse(request, 'users.html', {'users': users})

@login_required
@user_passes_test(is_superuser, login_url='statistics')
def create_user(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return TemplateResponse(request, 'create_user.html', {'form': form})
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User created successfully.')
        else:
            return TemplateResponse(request, 'create_user.html', {'form': form})

@login_required
@user_passes_test(is_superuser, login_url='statistics')
def user_password_change(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'GET':
        form = AdminPasswordChangeForm(user)
        return TemplateResponse(request, 'user_password_change.html', {'form': form, 'user_id': user_id})
    elif request.method == 'POST':
        form = AdminPasswordChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Password changed successfully.')
        else:
            return TemplateResponse(request, 'user_password_change.html', {'form': form, 'user_id': user_id})

@login_required
@user_passes_test(is_superuser, login_url='statistics')
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/server/users/')

