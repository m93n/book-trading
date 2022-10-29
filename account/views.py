import re
from django.db import IntegrityError
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
            try:
                user = Account.objects.create_user(email=email, mobile_number=mobile_number, username=username, password=password)
                
                return render(request, 'account/success.html', context={'user': user})

            except IntegrityError as e:
                if 'Duplicate entry' in str(e):
                    #find key error of IntegrityError for return that message
                    error_message = e.args[1]
                    key_index = error_message.find('key') + 4 # find index of key string and plus 4 for start from key value like mobile_number
                    key = error_message[key_index:].replace("'", '').replace("_", ' ')
                    
                    error_message = error_message.replace("'" + f"{key}" + "'", '') # remove key from message for blow procces
                    
                    value_of_field = re.search('Duplicate entry(.*) for key ', error_message).group(1) #value of field that is couse for user exist error

                    messages.error(request, message=f"user with {value_of_field} {key} is exist")
        
            

    return render(request, 'account/sign-up.html')




        

