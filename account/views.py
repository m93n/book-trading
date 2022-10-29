from django.conf import settings
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib import messages

from account.models import Account


# using custom User model that sets at settings
User_Model = settings.AUTH_USER_MODEL


def login_view(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # check if user athenticated with above attributes
        user = authenticate(request, email=email, password=password)
    
        if user is not None:
            login(request, user)

            return render(request, 'account/success.html')
    
    return render(request, 'account/sign-in.html')

def signup_view(request):

    if request.method == 'POST':
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'password and confiramtion password not match!!!')
        
        else:
            user = Account.objects.create_user(email=email, mobile_number=mobile_number, username=username, password=password)
        
            return render(request, 'account/success.html', context={'user': user})

    return render(request, 'account/sign-up.html')




        

