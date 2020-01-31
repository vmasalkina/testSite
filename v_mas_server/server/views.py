import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm, AdminPasswordChangeForm
from django.contrib.auth.models import User
from django.core import exceptions
from django.template.response import TemplateResponse
from django.views.decorators.http import require_GET, require_POST
from server.models import Data
from server.forms import RangeForm

@login_required
def statistics(request):
    user = request.user
    if request.method == 'GET':
        end = datetime.datetime.now()
        start = end - datetime.timedelta(days=1)
        form = RangeForm(initial={'start': start, 'end': end, 'step': '5'})
    elif request.method == 'POST':
        form = RangeForm(request.POST)
        if form.is_valid():
            end = form.cleaned_data['end']
            start = form.cleaned_data['start']
        else:
            return TemplateResponse(request, 'statistics.html', {'data': {}, 'user': user, 'form': form})
    d = Data.objects.filter(user=user, timestamp__range=(start, end))
    data = {i.timestamp.timestamp(): i.value for i in d}
    #data[i['timestamp'].strftime('%d.%m.%Y %H:%M')]
    return TemplateResponse(request, 'statistics.html', {'data': data, 'user': user, 'form': form})
    #return JsonResponse(data)

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
#            form.add_error(None, exceptions.ValidationError('Incorrect login or password.'))
            form.save()
            return HttpResponseRedirect('/server/users/')
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
            return HttpResponseRedirect('/server/users/')
        else:
            return TemplateResponse(request, 'user_password_change.html', {'form': form, 'user_id': user_id})

@login_required
@user_passes_test(is_superuser, login_url='statistics')
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/server/users/')

