from com_adaptor.adaptor import Dispatcher
from notification import models as notmodels 
from notification.MultiNotifyTemplates import NotificationTemplates 
import datetime
import pytz
from django.utils import timezone
import datetime
from .tasks import check_scheduled_notify

class EmailTemplate(NotificationTemplates):
    def __init__(self, notification_template=None, receivers=[], tokens=[]):
        self.subject = notification_template.subject     
        super().__init__(notification_template=notification_template, receivers=receivers, tokens=tokens)

class SmsTemplate(NotificationTemplates):
    def __init__(self, notification_template=None, receivers=[], tokens=[]):
        self.subject = None
        super().__init__(notification_template=notification_template, receivers=receivers, tokens=tokens)


class PushNotificationTemplate(NotificationTemplates) : 
    def __init__(self, notification_template=None, receivers=[], tokens=[]):
        self.subject = None
        super().__init__(notification_template=notification_template, receivers=receivers, tokens=tokens)

    def send(self) : 
        dispatcher =Dispatcher( self.notification_template ,'dict', self.service.name, self.subject,
        self.receivers, self.text_content   , '', '', bulk=self.bulk,
        template=None,tokens=self.tokens)
        response = dispatcher.send()
        return response




class EventTrigger:
    def __init__(self,multinotification,time_to_send ,receiver_emails=None
    ,receiver_phone_numbers=None,receiver_users=None,template_data=[],**kwargs):
        if isinstance(time_to_send,datetime.datetime):
            if time_to_send.hour:
                self.time_to_send=time_to_send
            else:
                corect_format="y-m-d h-m-s"
                raise Exception("Time is not valid, please enter hour",corect_format)
        else:
            raise Exception("Invalid time")

        self.multinotify = multinotification
        self.receiver_emails=receiver_emails
        self.receiver_phone_numbers=receiver_phone_numbers
        self.tokens =template_data
        self.email_template = self.multinotify.email_template
        self.sms_template = self.multinotify.sms_template
        self.push_notification_template=self.multinotify.push_notification_template

        
    def add_receiver_to_lognotify(self,get_receiver,schedule):
        if isinstance(get_receiver, list):
            for receiver in get_receiver:
                log=notmodels.LogNotification(multinotify=self.multinotify)
                if get_receiver == self.receiver_emails: 
                    log.receiver_email = receiver
                else: 
                    log.receiver_phone_number = receiver    
                if schedule: 
                    log.status='scheduled'
                else:
                    log.status='successfull'
                log.save()
        else:
            return "get_receiver argument must be a list"


    #return true if time is grater than now otherwise return false
    def check_time_to_send(self,get_time):
        utc=pytz.utc
        get_time=get_time.replace(tzinfo=utc)
        if get_time > timezone.now():
            return True
        else:
            return False

    def trigger(self):
      
        if self.check_time_to_send(self.time_to_send)==False:
            schedule=False
        else:
            schedule=True
        if schedule == False:
            if self.email_template and self.receiver_emails:
                email_response =EmailTemplate(
                    notification_template = self.email_template ,
                    receivers = self.receiver_emails,
                    tokens=self.tokens)
                email_response.send()   
                self.add_receiver_to_lognotify(self.receiver_emails,schedule)
            if self.push_notification_template : 
                push_notification_template = PushNotificationTemplate(notification_template= self.push_notification_template , receivers= [] , tokens= [] )
                push_notification_template.send() 
            if self.sms_template and self.receiver_phone_numbers:
                sms_response = SmsTemplate(
                    notification_template = self.sms_template,
                    receivers = self.receiver_phone_numbers,
                    tokens = self.tokens)
                sms_response.send() 
                self.add_receiver_to_lognotify(self.receiver_phone_numbers,schedule)
        else:
            if self.email_template and self.receiver_emails:
                email_template_id=self.email_template.id
                receiver_type='email'
                check_scheduled_notify.apply_async(
                    (email_template_id,
                    self.receiver_emails,
                    self.tokens,receiver_type),eta=self.time_to_send)
                self.add_receiver_to_lognotify(self.receiver_emails,schedule)

            if self.sms_template and self.receiver_phone_numbers:
                sms_template_id=self.sms_template.id
                receiver_type='sms'
                check_scheduled_notify.apply_async(
                (sms_template_id,
                self.receiver_phone_numbers,
                self.tokens,receiver_type),eta=self.time_to_send)
                self.add_receiver_to_lognotify(self.receiver_phone_numbers,schedule)

     

