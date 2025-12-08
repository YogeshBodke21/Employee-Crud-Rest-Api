from celery import shared_task
from django.core.mail import send_mail
from EMP_MGM import settings
from django.core.mail import send_mail, EmailMultiAlternatives

@shared_task
def send_html_mail_task(email, html_content):
     msg = EmailMultiAlternatives(
     "Django MauliAlternative Mail",
     "Welcome to Django based Application.",
     settings.EMAIL_HOST_USER,
     [email],
     headers={"List-Unsubscribe": email},
     )
     msg.attach_alternative(html_content, "text/html")
     msg.send()
     return "done"
