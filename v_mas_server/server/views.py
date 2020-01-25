from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.template.response import TemplateResponse
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

@login_required
@user_passes_test(is_superuser, login_url='statistics')
def users(request):

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
