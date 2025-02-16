from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.mail import EmailMessage 
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from core.models import UserProfile


def register(request):
    if request.method == 'POST':
            uname = request.POST.get('username')
            email = request.POST.get('email')
            first_name = request.POST.get('f_name')
            last_name = request.POST.get('l_name')
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')

            # Check if username or email already exists
            if UserProfile.objects.filter(username=uname).exists():
                messages.error(request, "Username already exists!")
                return redirect('register')
            elif UserProfile.objects.filter(email=email).exists():
                messages.error(request, "Email already exists!")
                return redirect('register')
            elif pass1 != pass2:
                messages.error(request, "Your password and confirm password are not the same!")
                return redirect('register')

            # Validate password strength
            try:
                validate_password(pass1)  # This will raise a ValidationError if the password is weak
            except ValidationError as e:
                # Add error messages for weak password
                for error in e:
                    messages.error(request, error)
                return redirect('register')

            # Create new user
            my_user = UserProfile(username=uname, email=email, first_name=first_name, last_name=last_name)
            my_user.set_password(pass1)  # Use set_password() to properly hash the password
            my_user.save()
            messages.success(request, "Your request has been accepted successfylly Please wait for admin canfirmation to login!")
            return redirect('login')
    else:
        return render(request, 'core/signup.html')

        

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        # Check if user exists
        if user is None:
            messages.error(request, "Invalid UserName or Password.")
            return redirect('login')
        else:
            auth.login(request, user)
            return redirect('home')
    else:
        return render(request, 'core/login.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Username or Password.")
            return redirect('login')
        
        # Login the user
        auth.login(request, user)

        # Redirect staff to admin, others to home
        if user.is_staff:
            return redirect('/admin/')
        else:
            return redirect('home')

    return render(request, 'core/login.html')




# Logout view
def logout(request):
    auth.logout(request)
    return redirect('home')


def home(request):
    user = request.user if request.user.is_authenticated else None
    context = {
            'user': user,
        }
    return render(request, 'core/home.html',context)
    

