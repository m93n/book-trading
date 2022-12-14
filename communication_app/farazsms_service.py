from booktrading import settings
from ippanel import Client as FarazClient
from ippanel import Error

from .base_service_client import BaseServiceClient

class FarazSMS(BaseServiceClient):
    def __init__(self, template_data , reciver_data):
        super().__init__(template_data , reciver_data)    
        
    def create(self):
       
        self.client = FarazClient(settings.FARAZ_API_KEY)
        self.originator=settings.FARAZ_NUMBER


    def send_with_service(self):

        for item in range(len(self.to_receivers)) : 
            try:
                reciver = self.to_receivers[item]
                if self.template == True :content = self.content[item] 
                else : content= self.content

                print('---------------')
                print(reciver)
                print(content)
                print('---------------')

                message =  self.client.send(originator = self.originator, recipients=self.receiver , message=self.content)
                response = f"message send successfully, {message.sid}"

                print('---------------')
                print(response)
                print('---------------')
            except Error as e:
                response = f"Error handled => code: {e.code}"
            
        return response