from django.shortcuts import render
from django.contrib.auth.models import User, auth
from .models import UserProfile


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        avatar = request.POST['avatar']

        if password == password1:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'Note': 'Please Enter Another User Name'})
            elif User.objects.filter(email=email).exists():
                return render(request, 'register.html', {'Note': 'Please Enter Another Email'})

            else:

                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                avatar = UserProfile.objects.create(user=user, avatar=avatar)
                user.save()
                avatar.save()

                print('usr registered ')
                return render(request, 'index.html')
        else:
            return render(request, 'register.html', {'Note': 'password dont match'})

    else:

        return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        print(username)

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'note': 'Enter Valid Credentials'})

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'index.html')


def profile(request):
    if request.user.is_authenticated:
        data = request.user
        data_ava = UserProfile.objects.filter(user=data)
        return render(request, 'profile.html', {'data': data_ava, 'data1': data})
    else:
        return render(request, 'login.html')
