class NotificationTemplate:
  
    def __init__(self,push_notification_template):
        """
        Create firebase_admin.message parameters & instance of that
        """
        title = push_notification_template.title
        body = push_notification_template.body
        image = push_notification_template.image
        dataObject = push_notification_template.data
        analytics_label = push_notification_template.fcm_options
        topic = push_notification_template.topic
        condition = push_notification_template.Condition
        token=push_notification_template.token

        web = push_notification_template.webpush
        if web:
            headers = web.headers
            web_title = web.webpush_notification.title
            web_body = web.webpush_notification.body
            web_icon = web.webpush_notification.icon
            action = web.webpush_notification.actions.action
            action_title = web.webpush_notification.actions.title
            action_icon = web.webpush_notification.actions.icon
            badge = web.webpush_notification.badge
            web_data = web.webpush_notification.data
            direction = web.webpush_notification.direction
            web_image = web.webpush_notification.image
            lang = web.webpush_notification.language
            require_interaction = web.webpush_notification.require_interaction
            renotify = web.webpush_notification.renotify
            silent = web.webpush_notification.silent
            web_tag = web.webpush_notification.web_tag
            timestamp_millis = web.webpush_notification.timestamp_millis
            custom_data = web.webpush_notification.custom_data
            web_link = web.fcm_options.link

            webpush = messaging.WebpushConfig(
                headers=headers,
                notification=messaging.WebpushNotification(title=web_title, body=web_body, icon=web_icon,
                                    actions=messaging.WebpushNotificationAction(action=action, title=action_title, icon=action_icon),
                                    badge=badge, data=web_data, direction=direction, image=web_image, language=lang, require_interaction=require_interaction, 
                                    renotify=renotify, silent=silent, tag=web_tag, timestamp_millis=timestamp_millis, custom_data=custom_data
                                    ),
                fcm_options=messaging.WebpushFCMOptions(link=web_link)
            )


        android = push_notification_template.android
        if android:
            collapse_key = android.collapse_key
            priority = android.priority
            ttl = android.ttl
            restricted_package_name = android.restricted_package_name
            android_data = android.data
            android_title = android.android_notification.title
            android_body = android.android_notification.body
            android_icon = android.android_notification.icon
            sound_file = android.android_notification.sound
            android_tag = android.android_notification.tag
            android_image = android.android_notification.image
            ticker = android.android_notification.ticker
            sticky = android.android_notification.sticky
            event_timestamp = android.android_notification.event_time
            local_only = android.android_notification.local_only
            notify_priority = android.android_notification.notification_priority
            vibrate_timings_millis = android.android_notification.vibrate_timings_millis
            default_vibrate_timings = android.android_notification.default_vibrate_timings
            default_sound = android.android_notification.default_sound
            color = android.android_notification.light_settings.color
            light_on_duration_millis = android.android_notification.light_settings.light_on_duration_millis
            light_off_duration_millis = android.android_notification.light_settings.light_off_duration_millis
            default_light_settings = android.android_notification.default_light_settings
            visibility = android.android_notification.visibility
            notification_count = android.android_notification.notification_count
            analytics_label_android = android.android_notification.fcm_options.analytics_label
            click_action = android.android_notification.click_action
            body_loc_key = android.android_notification.body_loc_key
            body_loc_args = android.android_notification.body_loc_args
            title_loc_key = android.android_notification.title_loc_key
            title_loc_args = android.android_notification.title_loc_args
            channel_id = android.android_notification.channel_id
            androidpush = messaging.AndroidConfig(
                collapse_key=collapse_key, priority=priority, ttl=ttl, restricted_package_name=restricted_package_name,
                notification=messaging.AndroidNotification(title=android_title, body=android_body, icon=android_icon, sound=sound_file, tag=android_tag, image=android_image,
                                            ticker=ticker, sticky=sticky, event_timestamp=event_timestamp, local_only=local_only, priority=notify_priority,
                                            vibrate_timings_millis=vibrate_timings_millis, default_vibrate_timings=default_vibrate_timings, default_sound=default_sound,
                                            light_settings=messaging.LightSettings(color=color, light_on_duration_millis=light_on_duration_millis,
                                                                                light_off_duration_millis=light_off_duration_millis),
                                            default_light_settings=default_light_settings, visibility=visibility, notification_count=notification_count,
                                            click_action=click_action, body_loc_key=body_loc_key, body_loc_args=body_loc_args, title_loc_key=title_loc_key,
                                            title_loc_args=title_loc_args, channel_id=channel_id
                                    ),
                fcm_options=messaging.AndroidFCMOptions(analytics_label=analytics_label_android)
            )

        notification = messaging.Notification(title=title, body=body, image=image)
        fcm_options = messaging.FCMOptions(analytics_label=analytics_label)
        
 
        self.maessage = messaging.Message(
            notification=notification,
            webpush=webpush if web else None,
            android=androidpush if android else None,
            data=dataObject,
            fcm_options=fcm_options,
            token=token.token,
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
