
from django.http import HttpResponse
from django.contrib.auth.models import User

def home(request):
    user = User.objects.create_user(username='qodestackr', password='swiftanalytics')
    user.save()
    return HttpResponse('Do not hit me again...')


def check_users(request):
    user = User.objects.get(username='qodestackr')

    print(user.username)
    print(user.password)

    return HttpResponse('Lol, fetched this MF::', user.username)