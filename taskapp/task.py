from celery import shared_task
from django.core.mail import EmailMessage
from django.conf import settings


@shared_task
def send_mail_task(email_recipient, subject, body):
    email = EmailMessage(
    subject,
    body,
    settings.EMAIL_HOST_USER,
    email_recipient)
    email.send()

