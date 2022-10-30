from django.conf import settings
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.views import PasswordContextMixin
from django.views.generic import FormView
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.tokens import default_token_generator

from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy

from django.urls import reverse_lazy

from account.forms import PasswordResetForm
from account.models import Account


# using custom User model that sets at settings
UserModel = settings.AUTH_USER_MODEL


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
            messages.error(request, 'password and confiramtion password does not match !!!')
        
        if Account.objects.filter(email=email):
            messages.error(request, f'user with {email} email is exist !!!')
        
        if Account.objects.filter(username=username):
            messages.error(request, f'user with {username} username is exist !!!')
            
        if Account.objects.filter(mobile_number=mobile_number):
            messages.error(request, f'user with {mobile_number} mobile_number is exist !!!')

        else:
            user = Account.objects.create_user(email=email, mobile_number=mobile_number, username=username, password=password)
            return render(request, 'account/success.html', context={'user': user})
        
    return render(request, 'account/sign-up.html')

class PasswordResetView(PasswordContextMixin, FormView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('account:password_reset_done')
    template_name = 'account/password-reset.html'
    token_generator = default_token_generator
    title = gettext_lazy('Password reset')

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        mobile_number = form.cleaned_data['mobile_number']
        try:
            opts = {
                'use_https': self.request.is_secure(),
                'token_generator': self.token_generator,
                'request': self.request,
            }
            form.save(**opts)
        except UserModel.DoesNotExist:
            form.add_error(None, 'mobile number not found !')
            return self.form_invalid(form)
        return super().form_valid(form)




        

