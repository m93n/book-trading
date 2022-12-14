######## define receivers

import json
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from notification.models import MultiNotify, Email, SMS, Notification
from django_celery_beat.models import CrontabSchedule, PeriodicTask, PeriodicTasks
#to be fixed 


@receiver(pre_save, sender=MultiNotify)
def handle_new_notify(sender, instance, **kwargs):
    if instance.id is None:
        notify_name = instance.notify_name
        print("Ok")
        if instance.triggertype == "schedule":
            PeriodicTask.objects.all().update(last_run_at=None)
            for task in PeriodicTask.objects.all():
                PeriodicTasks.changed(task)
            if instance.email != None:
                time = instance.email.time
                schedule, _ = CrontabSchedule.objects.get_or_create(
                        minute=time.minute,
                        hour=time.hour,
                        day_of_week=time.day_of_week,
                        day_of_month=time.day_of_month,
                        month_of_year=time.month_of_year,
                    )
                new_periodtask = PeriodicTask.objects.create(name=f'{instance.email.name}_email', task='Notification.tasks.check_scheduled_notify', crontab=schedule, args=json.dumps([f'{notify_name}']))

            if instance.sms != None:
                time = instance.sms.time
                schedule, _ = CrontabSchedule.objects.get_or_create(
                        minute=time.minute,
                        hour=time.hour,
                        day_of_week=time.day_of_week,
                        day_of_month=time.day_of_month,
                        month_of_year=time.month_of_year,
                    )
                new_periodtask = PeriodicTask.objects.create(name=f'{instance.sms.name}_sms', task='Notification.tasks.check_scheduled_notify', crontab=schedule, args=json.dumps([f'{notify_name}']),)
            
            if instance.notification != None:
                time = instance.notification.time
                schedule, _ = CrontabSchedule.objects.get_or_create(
                        minute=time.minute,
                        hour=time.hour,
                        day_of_week=time.day_of_week,
                        day_of_month=time.day_of_month,
                        month_of_year=time.month_of_year,
                    )
                PeriodicTask.objects.create(name=f'{instance.notification.name}_notify', task='Notification.tasks.check_scheduled_notify', crontab=schedule, args=json.dumps([f'{notify_name}']))


@receiver(pre_delete, sender=MultiNotify)
def handle_delete_email(sender, **kwargs):
    multinotify = kwargs['instance']
    if multinotify.email != None:
        q = PeriodicTask.objects.get(name=f'{multinotify.email.name}_email')
        q.delete()
    if multinotify.sms != None:
        q = PeriodicTask.objects.get(name=f'{multinotify.sms.name}_sms')
        q.delete()
    if multinotify.notification != None:
        q = PeriodicTask.objects.get(name=f'{multinotify.notification.name}_notify')
        q.delete()


@receiver(pre_save, sender=SMS)
def handle_change_sms(sender, instance, **kwargs):
    if instance.id is not None:
        previous = SMS.objects.get(id=instance.id)
        if previous.time != instance.time:
            print('sms Notify was changed')
            time = instance.time
            schedule, _ = CrontabSchedule.objects.get_or_create(
                        minute=time.minute,
                        hour=time.hour,
                        day_of_week=time.day_of_week,
                        day_of_month=time.day_of_month,
                        month_of_year=time.month_of_year,
                    )
            try:
                q = PeriodicTask.objects.get(name=f'{instance.name}_sms')
                q.crontab = schedule
                q.save()
            except:
                pass

@receiver(pre_save, sender=Email)
def handle_change_email(sender, instance, **kwargs):
    if instance.id is not None:
        previous = Email.objects.get(id=instance.id)
        if previous.time != instance.time:
            print('email Notify was changed')
            time = instance.time
            schedule, _ = CrontabSchedule.objects.get_or_create(
                        minute=time.minute,
                        hour=time.hour,
                        day_of_week=time.day_of_week,
                        day_of_month=time.day_of_month,
                        month_of_year=time.month_of_year,
                    )
            try:
                q = PeriodicTask.objects.get(name=f'{instance.name}_email')
                q.crontab = schedule
                q.save()
            except:
                pass

@receiver(pre_save, sender=Notification)
def handle_change_notification(sender, instance, **kwargs):
    if instance.id is not None:
        previous = Notification.objects.get(id=instance.id)
        if previous.time != instance.time:
            print('notification Notify was changed')
            time = instance.time
            schedule, _ = CrontabSchedule.objects.get_or_create(
                        minute=time.minute,
                        hour=time.hour,
                        day_of_week=time.day_of_week,
                        day_of_month=time.day_of_month,
                        month_of_year=time.month_of_year,
                    )
            try:
                q = PeriodicTask.objects.get(name=f'{instance.name}_notify')
                q.crontab = schedule
                q.save()
            except:
                pass


