from .base_service_client import BaseServiceClient
from firebase_admin import messaging
class FCMPushNotification(BaseServiceClient): 
    def __init__(self,push_notification_template , subject , content  , tokens ,   to_recivers , template):
        subject = subject 
        content= content 
        tokens = tokens 
        template = template 
        to_recivers = to_recivers 

        FCMPushNotification = push_notification_template.service
        FCMOption =FCMPushNotification.fcm_options
        self.web_push_notification =FCMPushNotification.webpush
        self.andorid_push_notification =FCMPushNotification.android 

        self.headers = push_notification_template.headers 
        self.title = push_notification_template.title
        self.topic = push_notification_template.topic 
        self.alert = push_notification_template.alert
        self.sound = push_notification_template.sound
        self.badge = push_notification_template.badge
        self.image = push_notification_template.image
        self.tempalate = push_notification_template.template
        self.text = push_notification_template.text
        self.body = push_notification_template.body
        self.bulk = push_notification_template.bulk
        self.dataObject = push_notification_template.data
        self.data = push_notification_template.data 
        self.analytics_label =FCMOption.analytics_label
        self.condition =FCMPushNotification.Condition
        self.token=FCMPushNotification.token

        if self.web_push_notification:
            self.action = self.web_push_notification.webpush_notification.actions.action
            self.action_title = self.web_push_notification.webpush_notification.actions.title
            self.action_icon = self.web_push_notification.webpush_notification.actions.icon
            self.direction = self.web_push_notification.webpush_notification.direction
            self.lang = self.web_push_notification.webpush_notification.language
            self.require_interaction = self.web_push_notification.webpush_notification.require_interaction
            self.renotify = self.web_push_notification.webpush_notification.renotify
            self.silent = self.web_push_notification.webpush_notification.silent
            self.web_tag = self.web_push_notification.webpush_notification.tag
            self.timestamp_millis = self.web_push_notification.webpush_notification.timestamp_millis
            self.custom_data = self.web_push_notification.webpush_notification.custom_data
            self.web_link = self.web_push_notification.fcm_options.link

            
        if self.andorid_push_notification:
            self.collapse_key = self.andorid_push_notification.collapse_key
            self.ttl = self.andorid_push_notification.ttl
            self.restricted_package_name = self.andorid_push_notification.restricted_package_name
            self.android_icon = self.andorid_push_notification.android_notification.icon
            self.sound_file = self.sound
            self.android_tag = self.andorid_push_notification.android_notification.tag
            self.ticker = self.andorid_push_notification.android_notification.ticker
            self.sticky = self.andorid_push_notification.android_notification.sticky
            self.event_timestamp = self.andorid_push_notification.android_notification.event_time
            self.local_only = self.andorid_push_notification.android_notification.local_only
            self.notify_priority = self.andorid_push_notification.android_notification.notification_priority
            self.vibrate_timings_millis = self.andorid_push_notification.android_notification.vibrate_timings_millis
            self.default_vibrate_timings = self.andorid_push_notification.android_notification.default_vibrate_timings
            self.default_sound = self.andorid_push_notification.android_notification.default_sound
            self.color = self.andorid_push_notification.android_notification.light_settings.color
            self.light_on_duration_millis = self.andorid_push_notification.android_notification.light_settings.light_on_duration
            self.light_off_duration_millis = self.andorid_push_notification.android_notification.light_settings.light_off_duration
            self.default_light_settings = self.andorid_push_notification.android_notification.default_light_settings
            self.visibility = self.andorid_push_notification.android_notification.visibility
            self.notification_count = self.andorid_push_notification.android_notification.notification_count
            self.analytics_label_android = self.andorid_push_notification.fcm_options.analytics_label
            self.click_action = self.andorid_push_notification.android_notification.click_action
            self.body_loc_key = self.andorid_push_notification.android_notification.body_loc_key
            self.body_loc_args = self.andorid_push_notification.android_notification.body_loc_args
            self.title_loc_key = self.andorid_push_notification.android_notification.title_loc_key
            self.title_loc_args = self.andorid_push_notification.android_notification.title_loc_args
            self.channel_id = self.andorid_push_notification.android_notification.channel_id

            
    def create(self):
        if self.web_push_notification :
            WebPushConfig = messaging.WebpushConfig(
                    headers=self.headers,
                    notification=messaging.WebpushNotification(title=self.title, body=self.body,
                                        actions=messaging.WebpushNotificationAction(action=self.action, title=self.action_title, icon=self.action_icon),
                                        badge=self.badge, data=self.data, direction=self.direction, image=self.image, language=self.lang, require_interaction=self.require_interaction, 
                                        renotify=self.renotify, silent=self.silent, tag=self.web_tag, timestamp_millis=self.timestamp_millis, custom_data=self.custom_data
                                        ),
                    fcm_options=messaging.WebpushFCMOptions(link=self.web_link))

        if self.andorid_push_notification : 
            AndroidPushConfig = messaging.AndroidConfig(
                collapse_key=self.collapse_key,  ttl=self.ttl, restricted_package_name=self.restricted_package_name,
                notification=messaging.AndroidNotification(title=self.title, body=self.body, icon=self.android_icon, sound=self.sound_file, tag=self.android_tag, image=self.image,
                                            ticker=self.ticker, sticky=self.sticky, event_timestamp=self.event_timestamp, local_only=self.local_only, priority=self.notify_priority,
                                            vibrate_timings_millis=self.vibrate_timings_millis, default_vibrate_timings=self.default_vibrate_timings, default_sound=self.default_sound,
                                            light_settings=messaging.LightSettings(color=self.color, light_on_duration_millis=self.light_on_duration_millis,
                                                                                light_off_duration_millis=self.light_off_duration_millis),
                                            default_light_settings=self.default_light_settings, visibility=self.visibility, notification_count=self.notification_count,
                                            click_action=self.click_action, body_loc_key=self.body_loc_key, body_loc_args=self.body_loc_args, title_loc_key=self.title_loc_key,
                                            title_loc_args=self.title_loc_args, channel_id=self.channel_id
                                    ),
                fcm_options=messaging.AndroidFCMOptions(analytics_label=self.analytics_label_android))

        notification = messaging.Notification(title=self.title, body=self.body, image=self.image)
        fcm_options =messaging.FCMOptions(analytics_label=self.analytics_label)

        self.maessage = messaging.Message(
                notification=notification,
                webpush=WebPushConfig if self.web_push_notification else None,
                android=AndroidPushConfig if self.andorid_push_notification else None,
                data=self.dataObject,
                fcm_options=fcm_options,
                token=self.token.token,
                # topic=topic.topic,
                # condition=condition.condition
            )
    def send(self):
        """
        Call send_multicast method of firebase_admin.message and returns response
        """
        response = messaging.send(message=self.maessage)
        print(response)
        return response
