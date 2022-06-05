from django.contrib.auth.models import User

def unique_username(name):
    return User.objects.filter(username=name).exists()
