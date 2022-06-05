from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from .utils import unique_username


def user_add(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password']:
            if unique_username(request.POST['username']):
                context = {
                    'error': 'данный польззователь уже существует'
                }
                return render(request, 'user_form.html', context)
            else:
                user = User.objects.create(username=request.POST['username'], password=request.POST.get('password'))
                user.set_password(request.POST.get('password'))
                if request.POST['email']:
                    user.email = request.POST['email']
                if request.POST['first_name']:
                    user.first_name = request.POST['first_name']
                if request.POST['last_name']:
                    user.last_name = request.POST['last_name']
                user.save()
                context = {
                    'text': 'пользователь успешно создан'
                }
                return render(request, 'user_form.html', context)
    return render(request, 'user_form.html')
