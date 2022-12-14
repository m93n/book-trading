from __future__ import unicode_literals, absolute_import

from celery import shared_task
from notification import Notify
from notification.models import EmailTemplate,SMSTemplate

@shared_task
def check_scheduled_notify(notification_template_id,reviever,token,reviever_type):

    if reviever_type == 'email':
        email_template=EmailTemplate.objects.get(id=notification_template_id)
        email_response=Notify.EmailTemplate(
                    notification_template = email_template ,
                    receivers = reviever,
                    tokens=token)
        email_response.send()
    else:
        sms_template=SMSTemplate.objects.get(id=notification_template_id)
        sms_response=Notify.SmsTemplate(
                    notification_template = sms_template,
                    receivers = reviever,
                    tokens = token)
        sms_response.send()
