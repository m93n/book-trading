from django.db import models
from django.conf import settings

User_Model = settings.AUTH_USER_MODEL



class MultiNotify(models.Model):
    TRIGGER_CHOICE = [
        ('event_type', 'Event_type'),
        ('schedule', 'Schedule'),
    ]

    notify_name = models.CharField(max_length=80, null=True, unique=True)
    triggertype = models.CharField(max_length=25, choices=TRIGGER_CHOICE, null=True, blank=True)
    email_template = models.ForeignKey('EmailTemplate', on_delete=models.CASCADE, null=True, blank=True)
    sms_template = models.ForeignKey('SMSTemplate', on_delete=models.CASCADE, null=True, blank=True)
    push_notification_template = models.ForeignKey('PushNoticationTemplate', on_delete=models.CASCADE, null=True, blank=True)
    time_to_send = models.ForeignKey('Time_To_Send', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.notify_name

class LogNotification(models.Model):
    STATUS_CHOICES=[
        ('successfull','message sent successfully'),
        ('scheduled','message scheduled successfully '),
        ('canceld','message canceled'),
        ('failed','massage failed')
    ]
    status=models.CharField(max_length=15,choices=STATUS_CHOICES)
    multinotify=models.ForeignKey(MultiNotify, on_delete=models.CASCADE)
    receiver_email=models.EmailField(null=True,blank=True)
    receiver_phone_number=models.CharField( max_length= 30 ,null=True,blank=True)
    #bundle_id=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    time_to_send=models.DateTimeField(null=True,blank=True)
        
    def __str__(self):
        return self.status



    
#change to EmailTemplate 
class EmailTemplate(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True)
    SERVICE_CHOICE = [
        ('SendGrid', 'SendGrid'),
        ('MailChimp', 'MailChimp'),
    ]
    service = models.CharField(max_length=50, choices=SERVICE_CHOICE, null=True, blank=True)
    subject = models.CharField(max_length=80)
    text = models.TextField()
    bulk = models.BooleanField(default=False)
    template = models.BooleanField(default=False)
    time = models.ForeignKey('Time_To_Send', blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class SMSTemplate(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True)
    SERVICE_CHOICE = [
        ('Twilio', 'Twilio'),
        ('FarazSMS', 'FarazSMS'),
    ]
    service = models.CharField(max_length=50, choices=SERVICE_CHOICE, null=True, blank=True)
    #phone_number = models.IntegerField(blank=True)
    template = models.BooleanField(default=False)

    text = models.TextField()
    bulk = models.BooleanField(default=False)
    time = models.ForeignKey('Time_To_Send', blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class PushNoticationTemplate(models.Model) : 
    
    headers = models.CharField(max_length=50, blank=True, null=True) 
    title = models.CharField(max_length=50, blank=True, null=True) 
    topic  = models.CharField(max_length=50, blank=True, null=True) 
    alert   = models.CharField(max_length=50, blank=True, null=True) 
    sound   = models.CharField(max_length=50, blank=True, null=True)
    body = models.TextField(blank=True , null= True) 
    badge = models.URLField(blank= True , null= True)
    image = models.URLField(null=True, blank=True)
    service = models.ForeignKey("FCMPushNotification" , null = True , blank=True ,on_delete=models.CASCADE)
    template = models.BooleanField(default=False)
    text = models.TextField()
    bulk = models.BooleanField(default=False)
    data = models.JSONField(null=True, blank=True)
    time = models.ForeignKey('Time_To_Send', blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)

   
class FCMPushNotification(models.Model):
    name_choices = [
        ('FCM' , 'FCM') , 
    ]
    name = models.CharField(max_length=50, choices=name_choices , default='FCM',  unique=True, null=True)
    webpush = models.ForeignKey('WebpushConfig', blank=True, null=True, on_delete=models.CASCADE)
    android = models.ForeignKey('AndroidConfig', blank=True, null=True, on_delete=models.CASCADE)
    data = models.JSONField(null=True, blank=True)
    fcm_options = models.ForeignKey('FCMOptions', on_delete=models.CASCADE, null=True, blank=True)
    token = models.ForeignKey('DeviceToken', on_delete=models.CASCADE, null=True, blank=True)
    topic = models.ForeignKey('Topic', null=True, blank=True, on_delete=models.CASCADE)
    Condition = models.ForeignKey('Condition', null=True, blank=True, on_delete=models.CASCADE)
    time = models.ForeignKey('Time_To_Send', blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name  
    
     

class FCMOptions(models.Model):
    analytics_label = models.CharField(max_length=200)

class WebpushConfig(models.Model):

    webpush_notification = models.ForeignKey('WebpushNotification', on_delete=models.CASCADE)
    fcm_options = models.ForeignKey('WebpushFCMOptions', on_delete=models.CASCADE, null=True, blank=True)

class WebpushFCMOptions(models.Model):
    link = models.CharField(max_length=200)

class WebpushNotification(models.Model):
    DIR_CHOICE = [
        ('auto', 'Auto'),
        ('rtl', 'rtl'),
        ('ltr', 'ltr'),
    ]


    icon = models.CharField(max_length=120)
    actions = models.ForeignKey('WebpushNotificationAction', on_delete=models.CASCADE, null=True, blank=True)
    direction = models.CharField(max_length=50, choices=DIR_CHOICE)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    require_interaction = models.BooleanField()
    renotify = models.BooleanField()
    silent = models.BooleanField()
    tag = models.CharField(max_length=80)
    timestamp_millis = models.DateField(auto_now=True)
    custom_data = models.JSONField()

class WebpushNotificationAction(models.Model):
    action = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)

#change to DeviceToken
class DeviceToken(models.Model):
    SERVICE_TYPE = [
        ('FCM','FCM'),
        ('APN','APN')
    ]

    DEVICE_CHOICES = [
        ('ios', 'IOS'),
        ('android','Android'),
        ('Windows' , 'Windows') , #Added By Kiarash Izadpanah 
    ]
    creator = models.ForeignKey(User_Model, on_delete=models.CASCADE, null=True)
    token = models.CharField(max_length=200, unique=True)
    Type = models.CharField(max_length=50, choices=SERVICE_TYPE, default='FCM')
    device = models.CharField(max_length=50, choices=DEVICE_CHOICES, default='android')
    created = models.DateTimeField(auto_now_add=True, null=True)


    class Meta:
        ordering = ["-created"]
    
    def __str__(self):
        return self.token

class Topic(models.Model):
    topic = models.CharField(max_length=120)

    def __str__(self):
        return self.topic

class Condition(models.Model):
    condition = models.CharField(max_length=120)

    def __str__(self):
        return self.condition

class Time_To_Send(models.Model):
    name = models.CharField(max_length=80, null=True)
    minute=models.CharField(max_length=200, null=True) 
    hour=models.CharField(max_length=200, null=True)
    day_of_week=models.CharField(max_length=200, null=True)
    day_of_month=models.CharField(max_length=200, null=True)
    month_of_year=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50)

    LANGUAGE_CHOICE = [
        ('en', 'English'),
        ('fa', 'Persian'),
        ('es', 'Spanish'),
        ('zh-Hans', 'Chinese'),
        ('fr', 'French'),
        ('af', 'Afrikaans'),
        ('sq', 'Albanian'),
        ('ar', 'Arabic'),
        ('de', 'German'),
        ('iw', 'Hebrew'),
        ('hi', 'Hindi'),
        ('it', 'Italian'),
        ('ja', 'Japanese'),
        ('kn', 'Kannada'),
        ('ko', 'Korean'),
        ('la', 'Latin'),
        ('pt', 'Portuguese'),
        ('ro', 'Romanian'),
        ('ru', 'Russian'),
        ('sg', 'Sangro'),
        ('th', 'Thai'),
        ('tr', 'Turkish'),
        ('uk', 'Ukrainian'),
    ]

    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICE)

    def __str__(self):
        return self.language

class AndroidConfig(models.Model):
    PRIORITY_CHOICE = [
        ('normal', 'Normal'),
        ('high', 'High'),
    ]
    collapse_key = models.CharField(max_length=200)
    ttl = models.CharField(max_length=200)
    restricted_package_name = models.CharField(max_length=200)
    android_notification = models.ForeignKey('AndroidNotification', on_delete=models.CASCADE)
    fcm_options = models.ForeignKey('AndroidFCMOptions', on_delete=models.CASCADE, null=True, blank=True)

class AndroidNotification(models.Model):
    PRIORITY_CHOICE = [
        ('default', 'Default'),
        ('min', 'Min'),
        ('low', 'Low'),
        ('high', 'High'),
        ('max', 'Max'),
        ('normal', 'Normal'),
    ]
    VISIBILITY_CHOICE = [
        ('private', 'Private'),
        ('public', 'Public'),
        ('secret', 'Secret'),
    ]

    icon = models.CharField(max_length=120)
    color = models.CharField(max_length=80)
    sound = models.CharField(max_length=80)
    tag = models.CharField(max_length=80)
    click_action = models.CharField(max_length=200)
    body_loc_key = models.CharField(max_length=200)
    body_loc_args  = models.JSONField()
    title_loc_key = models.CharField(max_length=120)
    title_loc_args = models.JSONField()
    channel_id = models.CharField(max_length=200)
    ticker = models.CharField(max_length=200)
    sticky = models.BooleanField()
    event_time = models.DateTimeField()
    local_only = models.BooleanField()
    notification_priority = models.CharField(max_length=50, choices=PRIORITY_CHOICE)

    vibrate_timings_millis = models.JSONField()
    default_vibrate_timings = models.BooleanField()
    default_light_settings = models.BooleanField()
    default_sound = models.BooleanField()
    light_settings = models.ForeignKey('LightSettings', on_delete=models.CASCADE)
    visibility = models.CharField(max_length=50, choices=VISIBILITY_CHOICE)
    notification_count = models.IntegerField()

class AndroidFCMOptions(models.Model):
    analytics_label = models.CharField(max_length=200)

class LightSettings(models.Model):
    color = models.JSONField()
    light_on_duration = models.CharField(max_length=200)
    light_off_duration = models.CharField(max_length=200)
