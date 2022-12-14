from notification.Notify import Dispatcher

class NotificationTemplates : 
    def __init__(self , notification_template =None , receivers =[] , tokens=[]   ):
        self.notification_template = notification_template
        print(notification_template.service)
        self.service = notification_template.service
        self.text_content = notification_template.text
        self.bulk = notification_template.bulk
        self.template = notification_template.template
        self.receivers = receivers
        self.tokens = tokens
        self.type = 'dict'

    def send(self):
        
        dispatcher =Dispatcher( None ,'dict', self.service, self.subject,
        self.receivers, self.text_content   , '', '', bulk=self.bulk,
        template=self.template,tokens=self.tokens)
        response = dispatcher.send()
        return response
        
            