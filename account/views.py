from django.conf import settings
from django.contrib.auth import authenticate, login
from django.shortcuts import render

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
        

