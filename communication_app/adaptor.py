
from . import sendgrid_service , twilio_service , farazsms_service , mailchimp_service , FCM_servic

class Dispatcher:

    def __init__(self, push_notification_template = None ,file_or_dict="", service="", subject="None", to_receivers=[], content="",
                 content_path="", data_path="",
                 bulk=False, template={}, tokens={}):
        self.push_notification_template = push_notification_template
        self.subject = subject
        self.content = content
        self.file_or_dict =file_or_dict
        self.service_provider = service
        self.bulk = bulk
        self.template = template 
        self.to_receivers = to_receivers
        self.content_path = content_path
        self.data_path =data_path
        self.tokens = tokens
        services = {
            'SendGrid': sendgrid_service.sendGrid,
            'MailChimp': mailchimp_service.MailChimp,
            'Twilio': twilio_service.Twilio, 
            'FarazSMS': farazsms_service.FarazSMS,
            'FCM' : FCM_servic.FCMPushNotification
        }
        self.service_provider_client = services.get(self.service_provider)

    def send(self):
        if self.push_notification_template : 
            service_provider_client = self.service_provider_client(self.push_notification_template , self.subject , self.content,self.tokens , self.to_receivers , self.template)
        else:
            service_provider_client = self.service_provider_client( self.subject , self.content,self.tokens , self.to_receivers , self.template)

        if self.template  : 
                service_provider_client.dynamic_data_substitution()
        service_provider_client.create()
        try:
            service_provider_client.send() 
                    
        except Exception as e:
            print(e)
        

    

            
