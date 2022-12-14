# Generated by Django 4.1.1 on 2022-12-14 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AndroidConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collapse_key', models.CharField(max_length=200)),
                ('ttl', models.CharField(max_length=200)),
                ('restricted_package_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AndroidFCMOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analytics_label', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=200, unique=True)),
                ('Type', models.CharField(choices=[('FCM', 'FCM'), ('APN', 'APN')], default='FCM', max_length=50)),
                ('device', models.CharField(choices=[('ios', 'IOS'), ('android', 'Android'), ('Windows', 'Windows')], default='android', max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, unique=True)),
                ('service', models.CharField(blank=True, choices=[('SendGrid', 'SendGrid'), ('MailChimp', 'MailChimp')], max_length=50, null=True)),
                ('subject', models.CharField(max_length=80)),
                ('text', models.TextField()),
                ('bulk', models.BooleanField(default=False)),
                ('template', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FCMOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analytics_label', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FCMPushNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('FCM', 'FCM')], default='FCM', max_length=50, null=True, unique=True)),
                ('data', models.JSONField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Condition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.condition')),
                ('android', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.androidconfig')),
                ('fcm_options', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.fcmoptions')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('language', models.CharField(choices=[('en', 'English'), ('fa', 'Persian'), ('es', 'Spanish'), ('zh-Hans', 'Chinese'), ('fr', 'French'), ('af', 'Afrikaans'), ('sq', 'Albanian'), ('ar', 'Arabic'), ('de', 'German'), ('iw', 'Hebrew'), ('hi', 'Hindi'), ('it', 'Italian'), ('ja', 'Japanese'), ('kn', 'Kannada'), ('ko', 'Korean'), ('la', 'Latin'), ('pt', 'Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sg', 'Sangro'), ('th', 'Thai'), ('tr', 'Turkish'), ('uk', 'Ukrainian')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LightSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.JSONField()),
                ('light_on_duration', models.CharField(max_length=200)),
                ('light_off_duration', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Time_To_Send',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, null=True)),
                ('minute', models.CharField(max_length=200, null=True)),
                ('hour', models.CharField(max_length=200, null=True)),
                ('day_of_week', models.CharField(max_length=200, null=True)),
                ('day_of_month', models.CharField(max_length=200, null=True)),
                ('month_of_year', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='WebpushFCMOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WebpushNotificationAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('icon', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WebpushNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=120)),
                ('direction', models.CharField(choices=[('auto', 'Auto'), ('rtl', 'rtl'), ('ltr', 'ltr')], max_length=50)),
                ('require_interaction', models.BooleanField()),
                ('renotify', models.BooleanField()),
                ('silent', models.BooleanField()),
                ('tag', models.CharField(max_length=80)),
                ('timestamp_millis', models.DateField(auto_now=True)),
                ('custom_data', models.JSONField()),
                ('actions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.webpushnotificationaction')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.language')),
            ],
        ),
        migrations.CreateModel(
            name='WebpushConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fcm_options', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.webpushfcmoptions')),
                ('webpush_notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.webpushnotification')),
            ],
        ),
        migrations.CreateModel(
            name='SMSTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, unique=True)),
                ('service', models.CharField(blank=True, choices=[('Twilio', 'Twilio'), ('FarazSMS', 'FarazSMS')], max_length=50, null=True)),
                ('template', models.BooleanField(default=False)),
                ('text', models.TextField()),
                ('bulk', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.time_to_send')),
            ],
        ),
        migrations.CreateModel(
            name='PushNoticationTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headers', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('topic', models.CharField(blank=True, max_length=50, null=True)),
                ('alert', models.CharField(blank=True, max_length=50, null=True)),
                ('sound', models.CharField(blank=True, max_length=50, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('badge', models.URLField(blank=True, null=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('template', models.BooleanField(default=False)),
                ('text', models.TextField()),
                ('bulk', models.BooleanField(default=False)),
                ('data', models.JSONField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.fcmpushnotification')),
                ('time', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.time_to_send')),
            ],
        ),
        migrations.CreateModel(
            name='MultiNotify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notify_name', models.CharField(max_length=80, null=True, unique=True)),
                ('triggertype', models.CharField(blank=True, choices=[('event_type', 'Event_type'), ('schedule', 'Schedule')], max_length=25, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('email_template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.emailtemplate')),
                ('push_notification_template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.pushnoticationtemplate')),
                ('sms_template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.smstemplate')),
                ('time_to_send', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.time_to_send')),
            ],
        ),
        migrations.CreateModel(
            name='LogNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('successfull', 'message sent successfully'), ('scheduled', 'message scheduled successfully '), ('canceld', 'message canceled'), ('failed', 'massage failed')], max_length=15)),
                ('receiver_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('receiver_phone_number', models.CharField(blank=True, max_length=30, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('time_to_send', models.DateTimeField(blank=True, null=True)),
                ('multinotify', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.multinotify')),
            ],
        ),
        migrations.AddField(
            model_name='fcmpushnotification',
            name='time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.time_to_send'),
        ),
        migrations.AddField(
            model_name='fcmpushnotification',
            name='token',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.devicetoken'),
        ),
        migrations.AddField(
            model_name='fcmpushnotification',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.topic'),
        ),
        migrations.AddField(
            model_name='fcmpushnotification',
            name='webpush',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.webpushconfig'),
        ),
        migrations.AddField(
            model_name='emailtemplate',
            name='time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.time_to_send'),
        ),
        migrations.CreateModel(
            name='AndroidNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=120)),
                ('color', models.CharField(max_length=80)),
                ('sound', models.CharField(max_length=80)),
                ('tag', models.CharField(max_length=80)),
                ('click_action', models.CharField(max_length=200)),
                ('body_loc_key', models.CharField(max_length=200)),
                ('body_loc_args', models.JSONField()),
                ('title_loc_key', models.CharField(max_length=120)),
                ('title_loc_args', models.JSONField()),
                ('channel_id', models.CharField(max_length=200)),
                ('ticker', models.CharField(max_length=200)),
                ('sticky', models.BooleanField()),
                ('event_time', models.DateTimeField()),
                ('local_only', models.BooleanField()),
                ('notification_priority', models.CharField(choices=[('default', 'Default'), ('min', 'Min'), ('low', 'Low'), ('high', 'High'), ('max', 'Max'), ('normal', 'Normal')], max_length=50)),
                ('vibrate_timings_millis', models.JSONField()),
                ('default_vibrate_timings', models.BooleanField()),
                ('default_light_settings', models.BooleanField()),
                ('default_sound', models.BooleanField()),
                ('visibility', models.CharField(choices=[('private', 'Private'), ('public', 'Public'), ('secret', 'Secret')], max_length=50)),
                ('notification_count', models.IntegerField()),
                ('light_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.lightsettings')),
            ],
        ),
        migrations.AddField(
            model_name='androidconfig',
            name='android_notification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.androidnotification'),
        ),
        migrations.AddField(
            model_name='androidconfig',
            name='fcm_options',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.androidfcmoptions'),
        ),
    ]
