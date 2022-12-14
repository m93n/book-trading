from firebase_admin import messaging
class WebPushNotificationCreation: 

    def WebPushNotification(self) : 
        self.web_push_notification_actions= messaging.WebpushNotificationAction(action=self.action, title=self.action_title, icon=self.action_icon) 
        self.web_push_config_notification = messaging.WebpushNotification(title=self.web_title, body=self.web_body, icon=self.web_icon,
                                    actions=self.web_push_notification_actions,badge=self.badge, data=self.web_data, direction=self.direction, image=self.web_image, language=self.lang, require_interaction=self.require_interaction, 
                                    renotify=self.renotify, silent=self.silent, timestamp_millis=self.timestamp_millis, custom_data=self.custom_data)

    def WebPushNotificationFCMoption(self): 
        self.web_link = self.web_push_notification.fcm_options.link
        self.fcm_options=messaging.WebpushFCMOptions(link=self.web_link)


    def WebPushConfig(self) : 
        self.web_push_config = messaging.WebpushConfig( headers=self.headers , 
                                                        notification = self.web_push_config_notification ,
                                                        fcm_options = self.fcm_options) 
        return self.web_push_config 
               

#----------------------------------------


class AndroidPushNotification : 
    def __init__(self , android_push_ontification):
        self.android_push_ontification = android_push_ontification
        self.collapse_key = android_push_ontification.collapse_key
        self.priority = android_push_ontification.priority
        self.ttl = android_push_ontification.ttl
        self.restricted_package_name = android_push_ontification.restricted_package_name
        self.android_data = android_push_ontification.data
        self.android_title = android_push_ontification.android_notification.title
        self.android_body = android_push_ontification.android_notification.body
        self.android_icon = android_push_ontification.android_notification.icon
        self.sound_file = android_push_ontification.android_notification.sound
        self.android_tag = android_push_ontification.android_notification.tag
        self.android_image = android_push_ontification.android_notification.image
        self.ticker = android_push_ontification.android_notification.ticker
        self.sticky = android_push_ontification.android_notification.sticky
        self.event_timestamp = android_push_ontification.android_notification.event_time
        self.local_only = android_push_ontification.android_notification.local_only
        self.notify_priority = android_push_ontification.android_notification.notification_priority
        self.vibrate_timings_millis = android_push_ontification.android_notification.vibrate_timings_millis
        self.default_vibrate_timings = android_push_ontification.android_notification.default_vibrate_timings
        self.default_sound = android_push_ontification.android_notification.default_sound
        self.default_light_settings = android_push_ontification.android_notification.default_light_settings
        self.visibility = android_push_ontification.android_notification.visibility
        self.notification_count = android_push_ontification.android_notification.notification_count
        self.click_action = android_push_ontification.android_notification.click_action
        self.body_loc_key = android_push_ontification.android_notification.body_loc_key
        self.body_loc_args = android_push_ontification.android_notification.body_loc_args
        self.title_loc_key = android_push_ontification.android_notification.title_loc_key
        self.title_loc_args = android_push_ontification.android_notification.title_loc_args
        self.channel_id = android_push_ontification.android_notification.channel_id
        self.color = self.android_push_ontification.android_notification.light_settings.color  
        self.light_on_duration_millis = self.android_push_ontification.android_notification.light_settings.light_on_duration 
        self.light_off_duration_millis = self.android_push_ontification.android_notification.light_settings.light_off_duration
    def AndroidWebPushNotification(self) : 
      
        self.light_settings=messaging.LightSettings(color=self.color, light_on_duration_millis=self.light_on_duration_millis , light_off_duration_millis=self.light_off_duration_millis),
        self.notification=messaging.AndroidNotification(title=self.android_title, body=self.android_body, icon=self.android_icon, sound=self.sound_file, tag=self.android_tag, image=self.android_image,
                                        ticker=self.ticker, sticky=self.sticky, event_timestamp=self.event_timestamp, local_only=self.local_only, priority=self.notify_priority,
                                        vibrate_timings_millis=self.vibrate_timings_millis, default_vibrate_timings=self.default_vibrate_timings, default_sound=self.default_sound,
                                        light_settings=self.light_settings,
                                        default_light_settings=self.default_light_settings, visibility=self.visibility, notification_count=self.notification_count,
                                        click_action=self.click_action, body_loc_key=self.body_loc_key, body_loc_args=self.body_loc_args, title_loc_key=self.title_loc_key,
                                        title_loc_args=self.title_loc_args, channel_id=self.channel_id)


    def AndroidPushNotificationFCMoption(self) : 
        analytics_label_android = self.android_push_ontification.fcm_options.analytics_label                       
        self.fcm_options=messaging.AndroidFCMOptions(analytics_label=analytics_label_android)

    def AndroidPushNotificationConfig(self) : 

        self.android_push_notification_config = messaging.AndroidConfig(  collapse_key=self.collapse_key, priority=self.priority, ttl=self.ttl, restricted_package_name=self.restricted_package_name,
                                                notification =self.notification , fcm_options = self.fcm_options )
        
        return self.android_push_notification_config