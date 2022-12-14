from booktrading import settings

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
from sendgrid.helpers.mail import Mail,To
from .base_service_client import BaseServiceClient

class sendGrid(BaseServiceClient):

    def create(self):
        mail = [] 
        print(' Mail ')

        for item in range(len(self.to_receivers)) : 
            to_receiver = self.to_receivers[item]
            if self.template == True :  content = self.content[item]
            else : content = self.content
            self.mail = Mail(from_email = settings.SENDGRID_EMAIL , to_emails = to_receiver , subject = self.subject , html_content = Content("text/plain", content))
            mail.append(self.mail)

            print('---------------')
            print(self.mail)
            print('---------------')
            
        self.mail = mail 
        return self.mail

    def send(self):
        SendGridClient = SendGridAPIClient(settings.SENDGRID_API_KEY)
        print(' Error  ')
        for item in self.mail : 
            try:
                response = SendGridClient.send(item)

            except Exception as e:
                print('---------------')
                print(e.to_dict)
                print('---------------')
                response = e.to_dict
        return response
