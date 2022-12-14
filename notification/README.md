# Notification

>**Notification** is an django application that handeled both eventtrigger message and schedule message.
>Type of message in this app are Email, SMS & especially Push Notification.
>**Notification** worked with adaptor app (that handled Email & SMS)so for use this app, needs install adaptor app.

<!-- [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)


![](https://www.logistec.com/wp-content/uploads/2017/12/placeholder.png) -->

[python]: https://www.python.org/


## Requirements  (Prerequisites)
Tools and packages required to successfully install this project.
* [Python 3.8](https://www.python.org/)
* [RabbitMQ](https://www.rabbitmq.com/)
* [django_user_agents](https://pypi.org/project/django-user-agents/)

## Installation
$ pip install <!--Notification-->

$ pip install<!--adaptor-->

$ pip install requirements.txt

    # set environment variables
        -celery settings like borker url, ...
        -mailchimp, sendgrid, twillio, farazsms settings

    # Configure settings.py
        INSTALLED_APPS = (
            # Other apps...
            'django_celery_beat',
            'rest_framework',
            'django_user_agents',
        )

        MIDDLEWARE_CLASSES = (
            # other middlewares...
            'django_user_agents.middleware.UserAgentMiddleware',
        )
    # Run Redis broker if use it
        
    # Run celery worker

        $ celery -A <app> worker --loglevel=info

    # Run celery beat for schedule notification

        $ celery -A <app> beat -l info

    # Run celery worker with this command if task received but not executed

        $ celery -A <app> worker --loglevel=info -P solo
 
## Screenshots
<!-- Use this space to give a little demo of your project. Attach important screenshots if applicable. This section is optional and might not be applicable in some cases.

![Screenshots of projects](https://dradisframework.com/images/pro/screenshots/screenshot-62_small.png)

![Screenshots of the project](http://securityroots.com/blog/wp-content/uploads/2013/12/snowcrash-01.png) -->

## Features

* Used Bootstrap to make it Scheduling & High availability and horizontal scaling.
* Used RabbitMQ because RabbitMQ has been designed as a dedicated message-broker & used rabbitmq to make app Flexible Routing.
* Used FireBase to Treat data as streams to build highly scalable applications.

## Usage example

```python
# For Schedule Notifications:
Insert new Multinotify in db & **Notification** will send it auto at their times

import Notify

# For Event Trigger Notification:
app_instance = Notify.EventTrigger(notify_name='Welcome', token='*-registeration token-', 
                                email='example@example.com', phone_number='012345678')
app_instance.trigger() # send push notification to token & email message to email & sms to phone_number eventually returns responses

```

## Tech Stack / Built With
1. [django](https://www.djangoproject.com/) - The Django framework
2. [celery](https://docs.celeryproject.org/en/stable/#) - The Celery system
3. [sendgrid](https://docs.sendgrid.com/for-developers/sending-email) - The Sendgrid service
4. [mailchimp](https://mailchimp.com/developer/transactional/guides/quick-start/) - The Mailchimp service
6. [mandrillapp](https://mandrillapp.com/docs/?_ga=1.34114145.1141874178.1422518109) - The mandrillapp via Mailchimp
7. [twillio](https://www.twilio.com/docs/sms) - The Twillio service
8. [farazsms](https://sms.farazsms.com/) - The Farazsms service
9. [firebase](https://firebase.google.com/) - The FCM service
10. [redis](https://riptutorial.com/redis/example/29962/installing-and-running-redis-server-on-windows) - Redis install and run

## Credits

* [REST Resource: projects.messages](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages)
* [firebase_admin.messaging module](https://firebase.google.com/docs/reference/admin/python/firebase_admin.messaging)
* [Installing and running Redis Server on Windows](https://riptutorial.com/redis/example/29962/installing-and-running-redis-server-on-windows)

