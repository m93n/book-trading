from booktrading import settings

from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client as TwilioClient
from .base_service_client import BaseServiceClient

class Twilio(BaseServiceClient):
   
    def create(self):
        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        self.notify_service_sid = ''
        self.client = TwilioClient(account_sid, auth_token)

    def send(self):
        print('SMS' )
        for item in range(len(self.to_receivers)) : 
            try:
                reciver = self.to_receivers[item]
                if self.template == True :content = self.content[item] 
                else : content= self.content

                print('---------------')
                print(reciver)
                print(content)
                print('---------------')

                message = self.client.messages.create(to=reciver,from_=settings.TWILIO_NUMBER,body=content)
                response = f"message send successfully, {message.sid}"

                print('---------------')
                print(response)
                print('---------------')
            except TwilioRestException as e:
                
                response = f" Error {e.code}"
                print('---------------')
                print(response)
                print('---------------')

        return response

       
            
