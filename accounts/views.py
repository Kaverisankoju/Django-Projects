# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from .models import User


# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         role = request.POST['role']

#         User.objects.create_user(
#             username=username,
#             password=password,
#             role=role
#         )

#         return redirect('login')

#     return render(request, 'accounts/register.html')


# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(username=username, password=password)

#         if user:
#             login(request, user)
#             return redirect('job_list')

#     return render(request, 'accounts/login.html')



# def user_logout(request):
#     logout(request)
#     return redirect('login')


# # Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User


def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        # USERNAME EXISTS

        if User.objects.filter(username=username).exists():

            return render(
                request,
                'accounts/register.html',
                {
                    'error':
                    'Username already exists'
                }
            )

        # PASSWORD LENGTH

        if len(password) < 6:

            return render(
                request,
                'accounts/register.html',
                {
                    'error':
                    'Password must be at least 6 characters'
                }
            )

        User.objects.create_user(
            username=username,
            password=password,
            role=role
        )

        return redirect('login')

    return render(request, 'accounts/register.html')

def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect('home')

        else:

            return render(
                request,
                'accounts/login.html',
                {
                    'error':
                    'Invalid username or password'
                }
            )

    return render(request, 'accounts/login.html')


def user_logout(request):

    logout(request)

    return redirect('login')
