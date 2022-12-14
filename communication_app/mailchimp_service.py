from mailchimp_transactional.api_client import ApiClientError

from booktrading import settings
from .base_service_client import BaseServiceClient

class MailChimp(BaseServiceClient):

    def __init__(self, template_data , reciver_data):
        super().__init__(template_data , reciver_data)        
      
    def create(self):
        Mail =[] 
        for item in range(len(self.to_receivers)) : 
            self.mail = {
                "from_email": settings.Mailchimp_EMAIL,
                "subject": self.subject,
                "text": self.content,
                "to": self.to_receivers,
                "merge_vars": self.tokens,
            }
            Mail.append(self.mail)
        self.mail = Mail

    def send(self):
      
       
        for mail in self.mail :
            try:
                self.response = self.mailchimp.messages.send({"message": mail})
                self.response = f'API called successfully: {self.response}'
                print(self.response)

            except ApiClientError as error:
                self.response = f'An exception occurred: {error.text}'
                print(self.response)
        
        
        return self.response