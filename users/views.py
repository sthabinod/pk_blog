from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_user(request):
    if request.method == 'POST':
        # Getting from post request
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        # Checking if the user exists in database
        if User.objects.filter(username=username).exists():
            user = authenticate(username=username,password=password)
            # Checking if user is active or not
            if user is None:
                print("Hereeee")

                messages.error(request, "User not found!")
                return redirect('login')
            else:
                # Calling login function and redirect to home page
                login(request,user)
                return redirect('show_blog')
        else:
            messages.error(request, 'Username or password does not matched!')
    else:
        print("This is not POST method")
    return render(request, 'login.html')


login_required(login_url='login')
def logout_user(request):
    try:
        logout(request)
        return redirect('login')
    except Exception:
        messages.error(request,"Something went wrong while logging out! Please try again and contact admin.")
