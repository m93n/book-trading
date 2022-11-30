from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings

import os
from twilio.rest import Client

import kavenegar

UserModel = get_user_model()

class PasswordResetForm(forms.Form):
    mobile_number = forms.CharField(label='mobile number', max_length=11,
                                   validators=[RegexValidator(regex=r'09(\d{9})$')])

    def send_sms(self, mobile_number, reset_link):
        # # try:
        # #     api = kavenegar.KavenegarAPI(settings.KAVENEGAR_APIKEY)
        # #     message = f'برای بازیابی رمز عبور روی لینک زیر کلیک کنید \n {reset_link}'
        # #     params = {
        # #         'sender': 'booktrader',
        # #         'receptor': mobile_number,
        # #         'message': message,
        # #     }
        # #     response = api.sms_send(params)
        # #     print(response)
        # # except kavenegar.APIException as e:
        # #     print(e)
        # # except kavenegar.HTTPException as e:
        # #     print(e)
        # account_sid = settings.TWILIO_ACCOUNT_SID
        # auth_token = settings.TWILIO_AUTH_TOKEN
        # client = Client(account_sid, auth_token)

        # message = client.messages.create(
        #                     body=f'برای بازیابی رمز عبور روی لینک زیر کلیک کنید \n {reset_link}',
        #                     from_='+989100697362',
        #                     to=f'+98{mobile_number[1:]}'
        #                 )

        # print(message.sid)
        pass

    def get_users(self, mobile_number):
        return UserModel.objects.get(mobile_number=mobile_number)

    def save(self, domain_override=None,
             use_https=False, token_generator=default_token_generator,
             request=None):
        """
        Generate a one-use only link for resetting password and send it to the
        user.
        """
        mobile_number = self.cleaned_data["mobile_number"]
        if not domain_override:
            current_site = get_current_site(request)
            domain = current_site.domain
        else:
            domain = domain_override
        user = self.get_users(mobile_number)
        user_mobile_number = user.mobile_number  # type: ignore
        protocol = 'https' if use_https else 'http'
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)
        reset_link = protocol + '://' + domain + reverse('account:password_reset_confirm',
                                                         args=[uid, token])
                                                         
        self.send_sms(user_mobile_number, reset_link)